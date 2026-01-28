//  backend/server.js

const path = require("path");
require("dotenv").config({ path: path.join(__dirname, ".env") });

const nodemailer = require("nodemailer");
const crypto = require("crypto");
const rateLimit = require("express-rate-limit");
const express = require("express");
const cors = require("cors");
const fetch = require("node-fetch");

const app = express();
const PORT = process.env.PORT || 3004;
const isProduction = process.env.NODE_ENV === "production";

// Enable CORS for frontend
app.use(
  cors({
    origin: process.env.CORS_ORIGINS
      ? process.env.CORS_ORIGINS.split(",")
      : [
          "http://127.0.0.1:5002",
          "http://localhost:5002",
          "http://127.0.0.1:5000",
          "http://localhost:5000",
          "http://127.0.0.1:5173",
          "http://localhost:5173",
        ],
    credentials: true,
  })
);

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ORCID OAuth configuration
const ORCID_CONFIG = {
  clientId: process.env.ORCID_CLIENT_ID || "APP-6U5WZH9AC4EYDVAD",
  clientSecret:
    process.env.ORCID_CLIENT_SECRET || "c839f6ee-8991-4b4e-9ae3-aab528adc22c",
  tokenUrl: process.env.ORCID_TOKEN_URL || "https://orcid.org/oauth/token",
};

// CILogon OAuth configuration
const CILOGON_CONFIG = {
  clientId: 'cilogon:/client_id/49ffba66ee294f1a9530301d2a281c74',
  clientSecret: 'pKdqDGRvbmQOdRgA2e-Ceh05xyFNN9sIYtGZs3s4Ym6iygdyX-qKynS4cyMS1VGZmCqGsp9fEFMwEh4HS4PbIQ',
  tokenUrl: 'https://cilogon.org/oauth2/token'
};

// SDX API configuration
const SDX_API_CONFIG = {
  baseUrl: "https://sdxapi.atlanticwave-sdx.ai/production",
  endpoints: {
    topology: "/topology",
  },
};

// =============================================================================
// OAuth ENDPOINTS
// =============================================================================

app.post("/oauth/exchange", async (req, res) => {
  try {
    if (!isProduction) {
      console.log("OAuth exchange request:", {
        provider: req.body.provider,
        hasCode: !!req.body.code,
        hasRedirectUri: !!req.body.redirect_uri,
        hasCodeVerifier: !!req.body.code_verifier,
      });
    }

    const { provider, code, state, redirect_uri, code_verifier } = req.body;

    if (!provider || !code) {
      return res.status(400).json({
        error: "Missing required parameters: provider and code",
      });
    }
    if (provider !== "orcid" && provider !== "cilogon") {
      return res.status(400).json({
        error: "Only ORCID and CILogon providers are supported",
      });
    }

    let response;
    let providerName;

    if (provider === "orcid") {
      // Prepare token exchange request for ORCID
      const params = new URLSearchParams({
        client_id: ORCID_CONFIG.clientId,
        client_secret: ORCID_CONFIG.clientSecret,
        grant_type: "authorization_code",
        redirect_uri: redirect_uri,
        code: code,
      });

      if (!isProduction) {
        console.log("Making request to ORCID token endpoint...");
        console.log("Request params:", params.toString());
      }

      // Exchange code for token with ORCID
      response = await fetch(ORCID_CONFIG.tokenUrl, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: params.toString(),
      });

      providerName = "ORCID";
    } else if (provider === "cilogon") {
      // CILogon requires PKCE flow - check for code_verifier
      if (!code_verifier) {
        return res.status(400).json({
          error: "Missing code_verifier for CILogon PKCE flow",
        });
      }

      // Prepare token exchange request for CILogon with PKCE
      const params = new URLSearchParams({
        client_id: CILOGON_CONFIG.clientId,
        client_secret: CILOGON_CONFIG.clientSecret,
        grant_type: "authorization_code",
        redirect_uri: redirect_uri,
        code: code,
        code_verifier: code_verifier, // Required for PKCE
      });

      if (!isProduction) {
        console.log("Making request to CILogon token endpoint...");
        console.log("Request params:", params.toString());
      }

      // Exchange code for token with CILogon
      response = await fetch(CILOGON_CONFIG.tokenUrl, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: params.toString(),
      });

      providerName = "CILogon";
    }

    const responseText = await response.text();

    if (!isProduction) {
      console.log(`${providerName} response status:`, response.status);
      console.log(`${providerName} response body:`, responseText);
    }

    if (!response.ok) {
      console.error(`${providerName} token exchange failed:`, response.status);
      return res.status(response.status).json({
        error: `${providerName} token exchange failed`,
        status: response.status,
        ...(!isProduction && { details: responseText }),
      });
    }


    let tokenData;
    try {
      tokenData = JSON.parse(responseText);
    } catch (parseError) {
      return res.status(500).json({
        error: `Invalid JSON response from ${providerName}`,
        ...(!isProduction && { details: responseText }),
      });
    }

    if (!isProduction) {
      console.log(`${providerName} token exchange successful`);
    }

    // Return the token data to frontend
    res.json({
      success: true,
      provider: provider,
      tokenData: tokenData,
      exchangedAt: new Date().toISOString(),
    });
  } catch (error) {
    console.error(
      "OAuth exchange error:",
      isProduction ? error.message : error
    );
    res.status(500).json({
      error: "Internal server error during token exchange",
      ...(!isProduction && { message: error.message }),
    });
  }
});

// =============================================================================
// reCAPTCHA verification endpoint
// =============================================================================

app.post("/api/verify-recaptcha", async (req, res) => {
  try {
    const { recaptchaToken, action } = req.body;

    if (!isProduction) {
      console.log("=== reCAPTCHA Verification ===");
      console.log(
        "Token received:",
        recaptchaToken ? "YES (length: " + recaptchaToken.length + ")" : "NO"
      );
      console.log("Action:", action);
    }

    if (!recaptchaToken) {
      return res.status(400).json({
        success: false,
        error: "Missing reCAPTCHA token",
      });
    }

    if (!process.env.RECAPTCHA_SECRET) {
      console.error("❌ RECAPTCHA_SECRET is not set in environment variables!");
      return res.status(500).json({
        success: false,
        error: "Server configuration error - secret key not configured",
      });
    }

    const verifyUrl = "https://www.google.com/recaptcha/api/siteverify";
    const params = new URLSearchParams({
      secret: process.env.RECAPTCHA_SECRET,
      response: recaptchaToken,
    });

    if (!isProduction) {
      console.log("Sending verification to Google...");
    }

    const response = await fetch(verifyUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: params.toString(),
    });

    const data = await response.json();
    
    if (!isProduction) {
      console.log("Google response:", JSON.stringify(data, null, 2));
    }

    if (!data.success) {
      console.error("❌ Verification failed:", data["error-codes"]);
      return res.json({
        success: false,
        error: "reCAPTCHA verification failed",
        errorCodes: data["error-codes"],
        score: 0,
      });
    }

    if (data.action && data.action !== action) {
      console.warn("⚠️ Action mismatch:", data.action, "vs", action);
      return res.status(400).json({
        success: false,
        error: "Action mismatch",
        score: data.score,
      });
    }

    if (!isProduction) {
      console.log("✅ Verification successful! Score:", data.score);
    }

    res.json({
      success: data.success,
      score: data.score,
      action: data.action,
      timestamp: data.challenge_ts,
      hostname: data.hostname,
    });
  } catch (error) {
    console.error("❌ reCAPTCHA verification error:", error.message);
    res.status(500).json({
      success: false,
      error: "Internal server error during reCAPTCHA verification",
      ...(!isProduction && { message: error.message }),
    });
  }
});

// =============================================================================
// EMAIL VERIFICATION
// =============================================================================

const verificationStore = new Map();
const VERIF_HMAC_KEY = process.env.VERIF_HMAC_KEY || "dev-secret-key";

function hashCode(email, code) {
  return crypto
    .createHmac("sha256", VERIF_HMAC_KEY)
    .update(`${email}:${code}`)
    .digest("hex");
}

function genCode() {
  return Math.floor(100000 + Math.random() * 900000).toString();
}

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: Number(process.env.SMTP_PORT) || 587,
  secure: false,
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS,
  },
  family: 4,
  tls: {
    rejectUnauthorized: true,
  },
  connectionTimeout: 10000,
  greetingTimeout: 10000,
  socketTimeout: 10000,
  debug: !isProduction,
  logger: !isProduction,
});

const sendLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 6,
  message: { error: "Too many requests, please try again later." },
});

const verifyLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  message: { error: "Too many verification attempts, try again later." },
});

// Test endpoint (development only)
if (!isProduction) {
  app.get("/api/test-email", async (req, res) => {
    const testEmail = req.query.email || process.env.SMTP_EMAIL;

    console.log("🧪 Testing email to:", testEmail);
    console.log("📧 SMTP Config:", {
      host: process.env.SMTP_HOST,
      port: process.env.SMTP_PORT,
      user: process.env.SMTP_USER,
      from: process.env.SMTP_EMAIL,
    });

    try {
      const info = await transporter.sendMail({
        from: process.env.SMTP_EMAIL,
        to: testEmail,
        subject: "SDX Email Verification Test",
        text: "This is a test email. If you receive this, SMTP is working correctly!",
        html: "<p>This is a <strong>test email</strong>. If you receive this, SMTP is working correctly!</p>",
      });

      console.log("✅ Email sent successfully:", info.messageId);

      res.json({
        success: true,
        message: "Test email sent successfully",
        messageId: info.messageId,
        response: info.response,
      });
    } catch (error) {
      console.error("❌ Test email failed:", error);
      res.status(500).json({
        error: error.message,
        code: error.code,
        command: error.command,
      });
    }
  });
}

app.post("/api/send-verification", sendLimiter, async (req, res) => {
  try {
    let { email } = req.body;
    if (!email) return res.status(400).json({ error: "Missing email" });

    email = String(email).trim().toLowerCase();

    const existing = verificationStore.get(email);
    if (existing && Date.now() < (existing.sentAt || 0) + 60 * 1000) {
      return res.status(429).json({ error: "Try again later" });
    }

    const code = genCode();
    const hash = hashCode(email, code);
    const ttlMs = 10 * 60 * 1000;
    const expiresAt = Date.now() + ttlMs;

    verificationStore.set(email, {
      hash,
      expiresAt,
      attempts: 0,
      sentAt: Date.now(),
    });

    const mailOptions = {
      from: process.env.SMTP_EMAIL,
      to: email,
      subject: "Your verification code",
      text: `Your verification code is ${code}. It expires in 10 minutes.`,
      html: `<p>Your verification code is <strong>${code}</strong>.</p><p>This code expires in 10 minutes.</p>`,
    };

    await transporter.sendMail(mailOptions);

    if (!isProduction) {
      console.log(
        `Sent verification code to ${email} (expires at ${new Date(
          expiresAt
        ).toISOString()})`
      );
    }

    res.json({ success: true, message: "Verification code sent", expiresAt });
  } catch (err) {
    console.error("send-verification error:", err.message);
    res.status(500).json({ error: "Failed to send verification" });
  }
});

app.post("/api/verify-code", verifyLimiter, (req, res) => {
  try {
    let { email, code } = req.body;
    if (!email || !code)
      return res.status(400).json({ error: "Missing email or code" });

    email = String(email).trim().toLowerCase();
    code = String(code).trim();

    if (!/^\d{6}$/.test(code)) {
      return res.status(400).json({ error: "Invalid code or email" });
    }

    const stored = verificationStore.get(email);
    if (!stored) {
      return res.status(400).json({ error: "Invalid code or email" });
    }

    if (Date.now() > stored.expiresAt) {
      verificationStore.delete(email);
      return res.status(400).json({ error: "Invalid code or email" });
    }

    stored.attempts = (stored.attempts || 0) + 1;
    if (stored.attempts > 10) {
      verificationStore.delete(email);
      return res.status(429).json({ error: "Too many attempts" });
    }
    verificationStore.set(email, stored);

    const incomingHash = hashCode(email, code);
    const storedHash = stored.hash;

    if (incomingHash.length !== storedHash.length) {
      return res.status(400).json({ error: "Invalid code or email" });
    }

    const ok = crypto.timingSafeEqual(
      Buffer.from(incomingHash),
      Buffer.from(storedHash)
    );

    if (ok) {
      verificationStore.delete(email);
      return res.json({ success: true, message: "Email verified" });
    } else {
      return res.status(400).json({ error: "Invalid code or email" });
    }
  } catch (err) {
    console.error("verify-code error:", err.message);
    res.status(500).json({ error: "Verification failed" });
  }
});

// =============================================================================
// SDX API ENDPOINTS
// =============================================================================

const validateToken = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (authHeader && authHeader.startsWith("Bearer ")) {
    const token = authHeader.substring(7);
    req.token = token;
    if (!isProduction) {
      console.log("Request authenticated with token:", token.substring(0, 20) + "...");
    }
  } else {
    if (!isProduction) {
      console.log("Request without authentication token");
    }
  }
  next();
};

// Topology endpoint
app.get("/api/topology", validateToken, async (req, res) => {
  try {
    const topologyUrl = `${SDX_API_CONFIG.baseUrl}${SDX_API_CONFIG.endpoints.topology}`;

    if (!isProduction) {
      console.log("Topology request received");
      console.log("Fetching topology from:", topologyUrl);
    }

    const response = await fetch(topologyUrl, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        ...(req.token && { Authorization: `Bearer ${req.token}` }),
      },
    });

    if (!isProduction) {
      console.log("Topology API response status:", response.status);
    }

    if (!response.ok) {
      console.error("Topology API error:", response.status, response.statusText);
      return res.status(response.status).json({
        error: "Failed to fetch topology data",
        status: response.status,
        ...(!isProduction && { details: response.statusText }),
      });
    }

    const topologyData = await response.json();

    if (!isProduction) {
      console.log(
        "Topology data received, nodes:",
        topologyData.nodes?.length,
        "links:",
        topologyData.links?.length
      );
    }

    res.json({
      success: true,
      data: topologyData,
      timestamp: new Date().toISOString(),
    });
  } catch (error) {
    console.error("Topology endpoint error:", error.message);
    res.status(500).json({
      error: "Internal server error while fetching topology",
      ...(!isProduction && { message: error.message }),
    });
  }
});

// L2VPN delete endpoint
app.delete("/api/l2vpn/1.0/:serviceId", validateToken, async (req, res) => {
  try {
    const { serviceId } = req.params;
    const l2vpnUrl = `${SDX_API_CONFIG.baseUrl}/l2vpn/1.0/${serviceId}`;

    if (!isProduction) {
      console.log("L2VPN delete request received");
      console.log("Deleting L2VPN:", serviceId);
      console.log("DELETE URL:", l2vpnUrl);
    }

    const response = await fetch(l2vpnUrl, {
      method: "DELETE",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        ...(req.token && { Authorization: `Bearer ${req.token}` }),
      },
    });

    if (!isProduction) {
      console.log("SDX L2VPN DELETE response status:", response.status);
    }

    const responseText = await response.text();
    let responseData;

    try {
      responseData = responseText ? JSON.parse(responseText) : { success: true };
    } catch (parseError) {
      console.error("Failed to parse L2VPN delete response:", responseText);
      responseData = { message: responseText || "Deleted successfully" };
    }

    if (!response.ok) {
      console.error("L2VPN delete failed:", response.status, responseData);
      return res.status(response.status).json({
        error: "Failed to delete L2VPN",
        status: response.status,
        ...responseData,
      });
    }

    if (!isProduction) {
      console.log("L2VPN deleted successfully:", responseData);
    }

    res.status(response.status).json(responseData);
  } catch (error) {
    console.error("L2VPN delete endpoint error:", error.message);
    res.status(500).json({
      error: "Internal server error while deleting L2VPN",
      ...(!isProduction && { message: error.message }),
    });
  }
});

// L2VPN update endpoint
app.patch("/api/l2vpn/1.0/:serviceId", validateToken, async (req, res) => {
  try {
    const { serviceId } = req.params;
    const l2vpnUrl = `${SDX_API_CONFIG.baseUrl}/l2vpn/1.0/${serviceId}`;

    if (!isProduction) {
      console.log("L2VPN update request received");
      console.log("Updating L2VPN:", serviceId);
      console.log("Request body:", JSON.stringify(req.body, null, 2));
      console.log("PATCH URL:", l2vpnUrl);
    }

    const response = await fetch(l2vpnUrl, {
      method: "PATCH",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        ...(req.token && { Authorization: `Bearer ${req.token}` }),
      },
      body: JSON.stringify(req.body),
    });

    if (!isProduction) {
      console.log("SDX L2VPN PATCH response status:", response.status);
    }

    const responseText = await response.text();
    let responseData;

    try {
      responseData = JSON.parse(responseText);
    } catch (parseError) {
      console.error("Failed to parse L2VPN update response:", responseText);
      return res.status(response.status).json({
        error: "Invalid response from SDX API",
        ...(!isProduction && { details: responseText }),
      });
    }

    if (!response.ok) {
      console.error("L2VPN update failed:", response.status, responseData);
      return res.status(response.status).json({
        error: "Failed to update L2VPN",
        status: response.status,
        ...responseData,
      });
    }

    if (!isProduction) {
      console.log("L2VPN updated successfully:", responseData);
    }

    res.status(response.status).json(responseData);
  } catch (error) {
    console.error("L2VPN update endpoint error:", error.message);
    res.status(500).json({
      error: "Internal server error while updating L2VPN",
      ...(!isProduction && { message: error.message }),
    });
  }
});

// L2VPN list endpoint
app.get("/api/l2vpn/1.0", validateToken, async (req, res) => {
  try {
    const l2vpnUrl = `${SDX_API_CONFIG.baseUrl}/l2vpn/1.0`;

    if (!isProduction) {
      console.log("L2VPN list request received");
      console.log("Fetching from:", l2vpnUrl);
    }

    // Forward request to SDX API
    const response = await fetch(l2vpnUrl, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        ...(req.token && { Authorization: `Bearer ${req.token}` }),
      },
    });

    if (!isProduction) {
      console.log("SDX L2VPN API response status:", response.status);
    }

    const responseText = await response.text();
    let responseData;

    try {
      responseData = JSON.parse(responseText);
    } catch (parseError) {
      console.error("Failed to parse L2VPN response:", responseText);
      return res.status(response.status).json({
        error: "Invalid response from SDX API",
        ...(!isProduction && { details: responseText }),
      });
    }

    if (!response.ok) {
      console.error("L2VPN list fetch failed:", response.status, responseData);
      return res.status(response.status).json({
        error: "Failed to fetch L2VPNs",
        status: response.status,
        ...responseData,
      });
    }

    if (!isProduction) {
      console.log("L2VPNs fetched successfully:", responseData);
    }

    res.status(response.status).json(responseData);
  } catch (error) {
    console.error("L2VPN list endpoint error:", error.message);
    res.status(500).json({
      error: "Internal server error while fetching L2VPNs",
      ...(!isProduction && { message: error.message }),
    });
  }
});

// L2VPN creation endpoint
app.post("/api/l2vpn/1.0", validateToken, async (req, res) => {
  try {
    const l2vpnUrl = `${SDX_API_CONFIG.baseUrl}/l2vpn/1.0`;

    if (!isProduction) {
      console.log("L2VPN creation request received");
      console.log("Request body:", JSON.stringify(req.body, null, 2));
      console.log("Posting to:", l2vpnUrl);
    }

    // Validate required fields
    const { name, endpoints, ownership } = req.body;
    if (!name || !endpoints || !ownership) {
      return res.status(400).json({
        error: "Missing required fields: name, endpoints, or ownership",
      });
    }

    if (!Array.isArray(endpoints) || endpoints.length < 2) {
      return res.status(400).json({
        error: "At least 2 endpoints are required",
      });
    }

    // Validate endpoints structure
    for (const ep of endpoints) {
      if (!ep.port_id || !ep.vlan) {
        return res.status(400).json({
          error: "Each endpoint must have port_id and vlan",
        });
      }
    }

    // Forward request to SDX API
    const response = await fetch(l2vpnUrl, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        ...(req.token && { Authorization: `Bearer ${req.token}` }),
      },
      body: JSON.stringify(req.body),
    });

    if (!isProduction) {
      console.log("SDX L2VPN API response status:", response.status);
    }

    const responseText = await response.text();
    let responseData;

    try {
      responseData = JSON.parse(responseText);
    } catch (parseError) {
      console.error("Failed to parse L2VPN response:", responseText);
      return res.status(response.status).json({
        error: "Invalid response from SDX API",
        ...(!isProduction && { details: responseText }),
      });
    }

    if (!response.ok) {
      console.error("L2VPN creation failed:", response.status, responseData);
      return res.status(response.status).json({
        error: "Failed to create L2VPN",
        status: response.status,
        ...responseData,
      });
    }

    if (!isProduction) {
      console.log("L2VPN created successfully:", responseData);
    }

    res.status(response.status).json(responseData);
  } catch (error) {
    console.error("L2VPN endpoint error:", error.message);
    res.status(500).json({
      error: "Internal server error while creating L2VPN",
      ...(!isProduction && { message: error.message }),
    });
  }
});

// General SDX API proxy endpoint
app.all("/api/sdx/*", validateToken, async (req, res) => {
  try {
    const sdxPath = req.path.replace("/api/sdx", "");
    const sdxUrl = `${SDX_API_CONFIG.baseUrl}${sdxPath}`;

    if (!isProduction) {
      console.log(`Proxying ${req.method} request to:`, sdxUrl);
    }

    const response = await fetch(sdxUrl, {
      method: req.method,
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        ...(req.token && { Authorization: `Bearer ${req.token}` }),
      },
      ...(req.method !== "GET" &&
        req.method !== "HEAD" && { body: JSON.stringify(req.body) }),
    });

    if (!isProduction) {
      console.log(`SDX API response status: ${response.status}`);
    }

    const responseData = await response.json();
    res.status(response.status).json(responseData);
  } catch (error) {
    console.error("SDX API proxy error:", error.message);
    res.status(500).json({
      error: "Internal server error while proxying SDX API request",
      ...(!isProduction && { message: error.message }),
    });
  }
});

// =============================================================================
// UTILITY ENDPOINTS
// =============================================================================

app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV || "development",
  });
});

app.get("/", (req, res) => {
  res.json({
    message: "SDX OAuth Backend Server",
    version: "1.0.0",
    environment: process.env.NODE_ENV || "development",
    endpoints: {
      "POST /oauth/exchange": "Exchange OAuth authorization code for tokens (ORCID & CILogon)",
      "POST /api/verify-recaptcha": "Verify reCAPTCHA token",
      "POST /api/send-verification": "Send email verification code",
      "POST /api/verify-code": "Verify email code",
      "GET /api/topology": "Get network topology",
      "GET /api/l2vpn/1.0": "List L2VPN connections",
      "POST /api/l2vpn/1.0": "Create L2VPN connection",
      "PATCH /api/l2vpn/1.0/:serviceId": "Update L2VPN connection",
      "DELETE /api/l2vpn/1.0/:serviceId": "Delete L2VPN connection",
      "GET /health": "Health check",
      ...(!isProduction && {
        "GET /api/test-email": "Test email sending (dev only)",
      }),
    },
  });
});

// =============================================================================
// STARTUP
// =============================================================================

if (!isProduction) {
  console.log("SMTP config:", {
    host: process.env.SMTP_HOST,
    port: process.env.SMTP_PORT,
    userSet: !!process.env.SMTP_USER,
    from: process.env.SMTP_EMAIL,
  });
}

transporter
  .verify()
  .then(() => console.log("✅ SMTP transporter ready"))
  .catch((err) =>
    console.error("❌ SMTP transporter verification failed:", err.message)
  );

app.listen(PORT, () => {
  console.log(
    `🚀 SDX OAuth Backend Server running on http://localhost:${PORT}`
  );
  console.log(`📝 Environment: ${isProduction ? "PRODUCTION" : "DEVELOPMENT"}`);

  if (!isProduction) {
    console.log(`📝 Available endpoints:`);
    console.log(`   POST http://localhost:${PORT}/oauth/exchange`);
    console.log(`   POST http://localhost:${PORT}/api/verify-recaptcha`);
    console.log(`   POST http://localhost:${PORT}/api/send-verification`);
    console.log(`   POST http://localhost:${PORT}/api/verify-code`);
    console.log(`   GET  http://localhost:${PORT}/api/topology`);
    console.log(`   POST http://localhost:${PORT}/api/l2vpn/1.0`);
    console.log(`   GET  http://localhost:${PORT}/api/test-email`);
    console.log(`   GET  http://localhost:${PORT}/health`);
  }
});

module.exports = app;
