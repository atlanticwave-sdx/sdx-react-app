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
const PORT = process.env.PORT || 3002;
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

// SDX API configuration
const SDX_API_CONFIG = {
  baseUrl: process.env.SDX_API_BASE_URL || "http://localhost:6098",
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
      });
    }

    const { provider, code, state, redirect_uri } = req.body;

    if (!provider || !code) {
      return res.status(400).json({
        error: "Missing required parameters: provider and code",
      });
    }

    if (provider !== "orcid") {
      return res.status(400).json({
        error: "Only ORCID provider is currently supported",
      });
    }

    const params = new URLSearchParams({
      client_id: ORCID_CONFIG.clientId,
      client_secret: ORCID_CONFIG.clientSecret,
      grant_type: "authorization_code",
      redirect_uri: redirect_uri,
      code: code,
    });

    if (!isProduction) {
      console.log("Making request to ORCID token endpoint...");
    }

    const response = await fetch(ORCID_CONFIG.tokenUrl, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: params.toString(),
    });

    const responseText = await response.text();

    if (!isProduction) {
      console.log("ORCID response status:", response.status);
    }

    if (!response.ok) {
      console.error("ORCID token exchange failed:", response.status);
      return res.status(response.status).json({
        error: "ORCID token exchange failed",
        status: response.status,
        ...(!isProduction && { details: responseText }),
      });
    }

    let tokenData;
    try {
      tokenData = JSON.parse(responseText);
    } catch (parseError) {
      return res.status(500).json({
        error: "Invalid JSON response from ORCID",
      });
    }

    if (!isProduction) {
      console.log("Token exchange successful");
    }

    res.json({
      success: true,
      provider: "orcid",
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
    rejectUnauthorized: isProduction,
    ...(!isProduction && { ciphers: "SSLv3" }),
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
      console.log("Request authenticated with token");
    }
  } else {
    if (!isProduction) {
      console.log("Request without authentication token");
    }
  }
  next();
};

app.get("/api/topology", validateToken, async (req, res) => {
  try {
    const topologyUrl = `${SDX_API_CONFIG.baseUrl}${SDX_API_CONFIG.endpoints.topology}`;

    if (!isProduction) {
      console.log("Fetching topology from:", topologyUrl);
    }

    const response = await fetch(topologyUrl, {
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    });

    if (!isProduction) {
      console.log("Topology API response status:", response.status);
    }

    if (!response.ok) {
      console.error("Topology API error:", response.status);
      return res.status(response.status).json({
        error: "Failed to fetch topology data",
        status: response.status,
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
    });
  }
});

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
      "POST /oauth/exchange": "Exchange OAuth authorization code for tokens",
      "POST /api/send-verification": "Send email verification code",
      "POST /api/verify-code": "Verify email code",
      "GET /api/topology": "Get network topology",
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
    console.log(`   POST http://localhost:${PORT}/api/send-verification`);
    console.log(`   POST http://localhost:${PORT}/api/verify-code`);
    console.log(`   GET  http://localhost:${PORT}/api/topology`);
    console.log(`   GET  http://localhost:${PORT}/api/test-email`);
    console.log(`   GET  http://localhost:${PORT}/health`);
  }
});

module.exports = app;
