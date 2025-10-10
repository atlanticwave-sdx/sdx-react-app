import { useState, useEffect } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { toast } from "sonner";
import { config } from "@/lib/config";
import { SessionManager } from "@/lib/session";
import {
  TokenStorage,
  decodeJWT,
  canSkipEmailValidation,
} from "@/lib/token-storage";
import { FullSDXLogo } from "@/components/FullSDXLogo";

interface ORCIDCallbackPageProps {
  onBack: () => void;
  onNavigateToDashboard?: () => void;
  onNavigateToEmailValidation?: (email?: string) => void;
}

export function ORCIDCallbackPage({
  onBack,
  onNavigateToDashboard,
  onNavigateToEmailValidation,
}: ORCIDCallbackPageProps) {
  const [status, setStatus] = useState<"processing" | "success" | "error">(
    "processing"
  );
  const [code, setCode] = useState<string | null>(null);
  const [state, setState] = useState<string | null>(null);
  const [tokenResponse, setTokenResponse] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const [useCorsProxy, setUseCorsProxy] = useState(false);
  const [useBackend, setUseBackend] = useState(true); // Default to backend

  useEffect(() => {
    handleCallback();
  }, []);

  const handleCallback = async () => {
    try {
      // Extract parameters from URL
      const urlParams = new URLSearchParams(window.location.search);
      const authCode = urlParams.get("code");
      const authState = urlParams.get("state");
      const authError = urlParams.get("error");

      setCode(authCode);
      setState(authState);

      console.log("ORCID Callback - URL Params:", {
        code: authCode,
        state: authState,
        error: authError,
        fullUrl: window.location.href,
      });

      if (authError) {
        throw new Error(`ORCID OAuth error: ${authError}`);
      }

      if (!authCode || !authState) {
        throw new Error("Missing authorization code or state parameter");
      }

      // Get state from sessionStorage for validation
      const storedState = sessionStorage.getItem("orcid_state");

      console.log("ORCID Callback - Session Storage:", {
        storedState,
        stateMatch: storedState === authState,
      });

      if (storedState !== authState) {
        throw new Error("State parameter mismatch - possible CSRF attack");
      }

      // Exchange code for token using client_secret flow
      await exchangeCodeForToken(authCode, authState);
    } catch (err) {
      console.error("ORCID callback error:", err);
      setError(err instanceof Error ? err.message : "Unknown error");
      setStatus("error");
    }
  };

  const exchangeCodeForToken = async (authCode: string, authState: string) => {
    try {
      if (useBackend) {
        console.log("Using backend server for token exchange...");
        await exchangeViaBackend(authCode, authState);
      } else {
        console.log("Using direct browser request for token exchange...");
        await exchangeViaBrowser(authCode, authState);
      }
    } catch (err) {
      console.error("Token exchange error:", err);
      throw err;
    }
  };

  const exchangeViaBackend = async (authCode: string, authState: string) => {
    const backendUrl = "http://localhost:3002/oauth/exchange";

    console.log("Making request to backend:", backendUrl);

    const requestBody = {
      provider: "orcid",
      code: authCode,
      state: authState,
      redirect_uri: config.orcid.redirectUri,
    };

    console.log("Backend request body:", requestBody);

    const response = await fetch(backendUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(requestBody),
    });

    console.log("Backend response status:", response.status);

    const responseText = await response.text();
    console.log("Backend response body:", responseText);

    if (!response.ok) {
      throw new Error(
        `Backend token exchange failed: ${response.status} ${response.statusText}\nResponse: ${responseText}`
      );
    }

    const result = JSON.parse(responseText);
    console.log("Backend response parsed:", result);

    if (result.success && result.tokenData) {
      setTokenResponse(result.tokenData);
      setStatus("success");

      // Store the token data first
      const tokenData = {
        ...result.tokenData,
        issued_at: Math.floor(Date.now() / 1000), // Add current timestamp
        provider: "orcid" as const, // Ensure provider is set
      };

      console.log("Raw token data from backend:", result.tokenData);
      console.log("Token data to store:", tokenData);

      // Decode JWT id_token if present
      if (tokenData.id_token) {
        const decodedIdToken = decodeJWT(tokenData.id_token);
        console.log("Decoded ID Token:", decodedIdToken);
      }

      TokenStorage.setToken("orcid", tokenData);

      // Verify the token was stored correctly
      const storedToken = TokenStorage.getToken("orcid");
      console.log("Stored token verification:", storedToken);
      console.log(
        "Is stored token valid?",
        TokenStorage.isTokenValid(storedToken)
      );

      // Check if email validation can be skipped
      const emailCheck = canSkipEmailValidation(tokenData);
      console.log("Email validation check:", emailCheck);

      // Create session for the authenticated user
      SessionManager.createSession("orcid");

      // Verify session was created correctly
      const session = SessionManager.getSession();
      console.log("Session created:", session);
      console.log(
        "Is authenticated after session creation?",
        SessionManager.isAuthenticated()
      );

      if (emailCheck.canSkip) {
        // Skip email validation - go directly to dashboard
        toast.success(
          `🎉 ORCID authentication successful! Email verified: ${emailCheck.email}`
        );
        setTimeout(() => {
          if (onNavigateToDashboard) {
            onNavigateToDashboard();
          }
        }, 2000);
      } else {
        // Need email validation
        toast.success(
          "🎉 ORCID authentication successful! Please verify your email."
        );
        setTimeout(() => {
          if (onNavigateToEmailValidation) {
            onNavigateToEmailValidation(emailCheck.email);
          }
        }, 2000);
      }
    } else {
      throw new Error("Backend returned invalid response format");
    }

    // Clean up session storage
    sessionStorage.removeItem("orcid_state");
  };

  const exchangeViaBrowser = async (authCode: string, _authState: string) => {
    console.log("Starting browser-based token exchange...");
    console.log("ORCID Token URL:", config.orcid.tokenUrl);

    // Prepare token exchange request matching the curl command exactly
    const params = new URLSearchParams({
      client_id: config.orcid.clientId,
      client_secret: (config.orcid as any).clientSecret, // TypeScript workaround
      grant_type: "authorization_code",
      redirect_uri: config.orcid.redirectUri,
      code: authCode,
    });

    console.log("Token exchange request params:", params.toString());

    // Choose URL based on proxy setting
    const directUrl = config.orcid.tokenUrl;
    const proxyUrl = `https://cors-anywhere.herokuapp.com/${config.orcid.tokenUrl}`;
    const requestUrl = useCorsProxy ? proxyUrl : directUrl;

    console.log(
      `Using ${useCorsProxy ? "CORS proxy" : "direct"} request to:`,
      requestUrl
    );

    let response: Response;
    response = await fetch(requestUrl, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        ...(useCorsProxy && { "X-Requested-With": "XMLHttpRequest" }),
      },
      body: params.toString(),
    });

    console.log("Token response status:", response.status);
    console.log(
      "Token response headers:",
      Object.fromEntries(response.headers.entries())
    );

    const responseText = await response.text();
    console.log("Token response body (raw):", responseText);

    if (!response.ok) {
      throw new Error(
        `Token exchange failed: ${response.status} ${response.statusText}\nResponse: ${responseText}`
      );
    }

    let parsedResponse: any;
    try {
      parsedResponse = JSON.parse(responseText);
    } catch (parseError) {
      throw new Error(`Invalid JSON response: ${responseText}`);
    }

    console.log("Token response (parsed):", parsedResponse);
    setTokenResponse(parsedResponse);
    setStatus("success");

    // Clean up session storage
    sessionStorage.removeItem("orcid_state");

    toast.success("ORCID token exchange successful!");
  };

  const formatJSON = (obj: any) => {
    return JSON.stringify(obj, null, 2);
  };

  return (
    <div className="container mx-auto px-6 py-16 max-w-4xl bg-[rgb(255,255,255)] min-h-screen">
      {/* Header */}
      <FullSDXLogo />

      <Button
        variant="ghost"
        onClick={onBack}
        className="mb-8 -ml-2 text-base text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
      >
        ← Back to application
      </Button>

      <Card className="shadow-lg border-2 border-[rgb(120,176,219)] bg-[rgb(255,255,255)]">
        <CardHeader className="pb-8">
          <CardTitle className="text-2xl text-[rgb(64,143,204)]">
            ORCID OAuth Callback
          </CardTitle>
          <CardDescription className="text-lg mt-2 text-[rgb(50,135,200)]">
            Processing ORCID authentication response
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* URL Parameters Section */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold text-[rgb(64,143,204)]">
              URL Parameters
            </h3>
            <div className="bg-[rgb(236,244,250)] p-4 rounded-lg border border-[rgb(120,176,219)]">
              <div className="space-y-2 font-mono text-sm">
                <div>
                  <span className="font-bold text-[rgb(50,135,200)]">
                    Full URL:
                  </span>
                  <div className="text-[rgb(64,143,204)] break-all">
                    {window.location.href}
                  </div>
                </div>
                <div>
                  <span className="font-bold text-[rgb(50,135,200)]">
                    Authorization Code:
                  </span>
                  <div className="text-[rgb(64,143,204)]">
                    {code || "Not found"}
                  </div>
                </div>
                <div>
                  <span className="font-bold text-[rgb(50,135,200)]">
                    State:
                  </span>
                  <div className="text-[rgb(64,143,204)]">
                    {state || "Not found"}
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Status Section */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold text-[rgb(64,143,204)]">
              Processing Status
            </h3>

            {status === "processing" && (
              <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
                <AlertDescription className="text-base text-[rgb(64,143,204)]">
                  🔄 Processing ORCID callback and exchanging authorization code
                  for tokens...
                </AlertDescription>
              </Alert>
            )}

            {status === "success" && (
              <div className="space-y-4">
                <Alert className="border-2 border-green-200 bg-green-50">
                  <AlertDescription className="text-base text-green-800">
                    ✅ Token exchange successful! Authentication complete.
                  </AlertDescription>
                </Alert>

                {onNavigateToDashboard && (
                  <div className="text-center">
                    <Button
                      onClick={onNavigateToDashboard}
                      className="bg-green-600 hover:bg-green-700 text-white px-8 py-3 text-lg font-semibold"
                      size="lg"
                    >
                      🚀 Continue to Dashboard
                    </Button>
                    <p className="text-sm text-green-600 mt-2">
                      You will be automatically redirected in 3 seconds...
                    </p>
                  </div>
                )}
              </div>
            )}

            {status === "error" && (
              <div className="space-y-4">
                <Alert variant="destructive">
                  <AlertDescription>❌ Error: {error}</AlertDescription>
                </Alert>

                {error?.includes("CORS") ||
                error?.includes("Failed to fetch") ? (
                  <div className="space-y-3">
                    <Alert className="border-2 border-blue-200 bg-blue-50">
                      <AlertDescription className="text-blue-800">
                        💡 <strong>CORS Error Fix Options:</strong>
                        <br />
                        1. Try the CORS proxy button below
                        <br />
                        2. Disable CORS in Chrome:{" "}
                        <code className="bg-blue-100 px-1 rounded">
                          --disable-web-security
                        </code>
                        <br />
                        3. Use a backend server for token exchange (recommended)
                      </AlertDescription>
                    </Alert>

                    <div className="flex gap-3 flex-wrap">
                      <Button
                        onClick={() => {
                          setUseBackend(!useBackend);
                          setStatus("processing");
                          setError(null);
                          handleCallback();
                        }}
                        variant="outline"
                        className="border-purple-500 text-purple-600 hover:bg-purple-50"
                      >
                        {useBackend
                          ? "🌐 Try Browser Request"
                          : "🖥️ Try Backend Server"}
                      </Button>

                      {!useBackend && (
                        <Button
                          onClick={() => {
                            setUseCorsProxy(!useCorsProxy);
                            setStatus("processing");
                            setError(null);
                            handleCallback();
                          }}
                          variant="outline"
                          className="border-blue-500 text-blue-600 hover:bg-blue-50"
                        >
                          {useCorsProxy
                            ? "🔗 Try Direct Request"
                            : "🔗 Try CORS Proxy"}
                        </Button>
                      )}

                      <Button
                        onClick={() => {
                          setStatus("processing");
                          setError(null);
                          handleCallback();
                        }}
                        variant="outline"
                        className="border-green-500 text-green-600 hover:bg-green-50"
                      >
                        🔄 Retry
                      </Button>
                    </div>
                  </div>
                ) : null}
              </div>
            )}
          </div>

          {/* Authorization Code Section */}
          {code && (
            <div className="space-y-4">
              <h3 className="text-lg font-semibold text-[rgb(64,143,204)]">
                Authorization Code (Ready for Server-Side Exchange)
              </h3>
              <div className="bg-blue-50 border border-blue-200 p-4 rounded-lg">
                <div className="space-y-2">
                  <div>
                    <span className="font-bold text-blue-800">Code:</span>
                    <div className="font-mono text-sm text-blue-900 bg-white p-2 rounded border mt-1 break-all">
                      {code}
                    </div>
                  </div>
                  <div>
                    <span className="font-bold text-blue-800">State:</span>
                    <div className="font-mono text-sm text-blue-900 bg-white p-2 rounded border mt-1 break-all">
                      {state}
                    </div>
                  </div>
                  <div className="mt-3 p-3 bg-blue-100 rounded text-sm text-blue-800">
                    💡{" "}
                    <strong>
                      This authorization code can be used by your backend server
                      to exchange for tokens.
                    </strong>
                    <br />
                    The browser-based token exchange fails due to CORS policy,
                    but the code is valid.
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Token Response Section */}
          {tokenResponse && (
            <div className="space-y-4">
              <h3 className="text-lg font-semibold text-[rgb(64,143,204)]">
                ORCID Token Response
              </h3>
              <div className="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto">
                <pre className="text-sm whitespace-pre-wrap">
                  {formatJSON(tokenResponse)}
                </pre>
              </div>
            </div>
          )}

          {/* Configuration Info */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold text-[rgb(64,143,204)]">
              Configuration Used
            </h3>
            <div className="bg-[rgb(236,244,250)] p-4 rounded-lg border border-[rgb(120,176,219)]">
              <div className="space-y-2 font-mono text-sm">
                <div>
                  <span className="font-bold text-[rgb(50,135,200)]">
                    Client ID:
                  </span>
                  <div className="text-[rgb(64,143,204)]">
                    {config.orcid.clientId}
                  </div>
                </div>
                <div>
                  <span className="font-bold text-[rgb(50,135,200)]">
                    Redirect URI:
                  </span>
                  <div className="text-[rgb(64,143,204)]">
                    {config.orcid.redirectUri}
                  </div>
                </div>
                <div>
                  <span className="font-bold text-[rgb(50,135,200)]">
                    Token URL:
                  </span>
                  <div className="text-[rgb(64,143,204)]">
                    {config.orcid.tokenUrl}
                  </div>
                </div>
                <div>
                  <span className="font-bold text-[rgb(50,135,200)]">
                    Scope:
                  </span>
                  <div className="text-[rgb(64,143,204)]">
                    {config.orcid.scope}
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Actions */}
          <div className="pt-6 border-t border-[rgb(120,176,219)]">
            <Button
              onClick={onBack}
              className="w-full py-3 text-lg font-semibold bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)]"
              size="lg"
            >
              Continue to Application
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
