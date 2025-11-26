import { useState, useEffect } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { Separator } from "@/components/ui/separator";
import { toast } from "sonner";
import { TokenData, TokenClaims } from "@/lib/types";
import { TokenStorage, decodeJWT } from "@/lib/token-storage";
import { sendTokenToBackend } from "@/lib/backend";
import { TokenStatus } from "@/components/TokenStatus";
import { useTokenRefresh } from "@/hooks/useTokenRefresh";
import { SessionSelection } from "@/components/SessionSelection";
import { ORCIDProvider } from "@/lib/providers/orcid";
import { SessionManager } from "@/lib/session";
import { FullSDXLogo } from "@/components/FullSDXLogo";

interface TokenPageProps {
  onBack: () => void;
  onNavigateToDashboard?: () => void;
  modal?: boolean; // If true, hides header elements (logo, back button, view dashboard)
}

export function TokenPage({
  onBack,
  onNavigateToDashboard,
  modal = false,
}: TokenPageProps) {
  const [tokens, setTokens] = useState<{
    cilogon?: TokenData;
    orcid?: TokenData;
  }>({});
  const [selectedToken, setSelectedToken] = useState<TokenData | null>(null);
  const [claims, setClaims] = useState<TokenClaims | null>(null);
  const [isSending, setIsSending] = useState(false);
  const [showSessionSelection, setShowSessionSelection] = useState(false);

  // Initialize token refresh system
  const { refreshStatus, isTokenNearExpiry } = useTokenRefresh({
    refreshBeforeExpiryMinutes: 5,
    checkIntervalMinutes: 1,
    showNotifications: true,
  });

  const checkForORCIDAuthResult = async () => {
    try {
      console.log("TokenPage: Checking for ORCID auth result...");
      const authResult = localStorage.getItem("orcid_auth_result");
      console.log("TokenPage: Found auth result:", authResult);

      if (authResult) {
        const result = JSON.parse(authResult);
        console.log("TokenPage: Parsed auth result:", result);

        if (
          result.type === "ORCID_AUTH_SUCCESS" &&
          Date.now() - result.timestamp < 300000
        ) {
          console.log(
            "TokenPage: Valid ORCID auth result found, processing token exchange..."
          );
          localStorage.removeItem("orcid_auth_result");

          try {
            // If code verifier is included in the stored result, restore it to sessionStorage
            if (result.codeVerifier) {
              console.log(
                "TokenPage: Restoring PKCE parameters from stored auth result"
              );
              sessionStorage.setItem("orcid_state", result.state);
              sessionStorage.setItem(
                "orcid_code_verifier",
                result.codeVerifier
              );
            }

            const orcidProvider = new ORCIDProvider();
            console.log(
              "TokenPage: Starting token exchange with code:",
              result.code,
              "state:",
              result.state
            );
            const token = await orcidProvider.exchangeCodeForToken(
              result.code,
              result.state
            );
            console.log("TokenPage: ORCID token exchange successful:", token);
            toast.success("✅ ORCID authentication successful!");

            // Reload tokens to show the new ORCID token
            setTimeout(() => {
              loadTokens();
            }, 500);
          } catch (exchangeError) {
            console.error(
              "TokenPage: ORCID token exchange failed:",
              exchangeError
            );
            toast.error(
              `ORCID authentication failed: ${
                exchangeError instanceof Error
                  ? exchangeError.message
                  : "Unknown error"
              }`
            );
          }
        } else {
          console.log("TokenPage: Auth result expired or invalid type");
        }
      } else {
        console.log("TokenPage: No ORCID auth result found in localStorage");
      }
    } catch (e) {
      console.error("TokenPage: Error checking for ORCID auth result:", e);
    }
  };

  useEffect(() => {
    // Check for ORCID auth result from callback redirect
    checkForORCIDAuthResult();

    // Initial load
    loadTokens();

    // Listen for storage changes in case tokens are added from another tab/window
    const handleStorageChange = (e: StorageEvent) => {
      if (e.key && e.key.includes("auth.")) {
        console.log("Storage change detected for auth tokens, reloading");
        setTimeout(loadTokens, 100); // Small delay to ensure consistency
      }
    };

    // Listen for window focus (user returns from auth popup)
    const handleWindowFocus = () => {
      console.log("Window focused, checking for new tokens");
      loadTokens();
    };

    window.addEventListener("storage", handleStorageChange);
    window.addEventListener("focus", handleWindowFocus);

    // Also check for new tokens periodically
    const checkInterval = setInterval(() => {
      const currentTokenCount = Object.keys(tokens).length;
      const cilogon = TokenStorage.getToken("cilogon");
      const orcid = TokenStorage.getToken("orcid");
      const validCount = [cilogon, orcid].filter(
        (t) => t && TokenStorage.isTokenValid(t)
      ).length;

      if (validCount > currentTokenCount) {
        console.log("New valid token detected, reloading");
        loadTokens();
      }
    }, 2000);

    return () => {
      window.removeEventListener("storage", handleStorageChange);
      window.removeEventListener("focus", handleWindowFocus);
      clearInterval(checkInterval);
    };
  }, [tokens]);

  useEffect(() => {
    if (selectedToken) {
      const tokenClaims = decodeJWT(selectedToken.id_token);
      // If JWT decoding fails, create basic claims for display
      if (!tokenClaims) {
        setClaims({
          sub: `${selectedToken.provider}-user`,
          iss:
            selectedToken.provider === "orcid"
              ? "https://orcid.org"
              : selectedToken.provider,
          exp: selectedToken.issued_at + selectedToken.expires_in,
          iat: selectedToken.issued_at,
        });
      } else {
        setClaims(tokenClaims);
      }
    } else {
      setClaims(null);
    }
  }, [selectedToken]);

  const loadTokens = () => {
    const cilogon = TokenStorage.getToken("cilogon");
    const orcid = TokenStorage.getToken("orcid");

    const validTokens: any = {};

    if (cilogon && TokenStorage.isTokenValid(cilogon)) {
      validTokens.cilogon = cilogon;
    }

    if (orcid && TokenStorage.isTokenValid(orcid)) {
      validTokens.orcid = orcid;
    }
    setTokens(validTokens);

    // Show success message if we just got new tokens (only if not in modal mode and user is not already authenticated)
    const previousCount = Object.keys(tokens).length;
    const newCount = Object.keys(validTokens).length;
    if (
      newCount > previousCount &&
      newCount > 0 &&
      !modal &&
      !SessionManager.isAuthenticated()
    ) {
      const newProviders = Object.keys(validTokens).filter(
        (provider) => !tokens[provider as keyof typeof tokens]
      );
      if (newProviders.length > 0) {
        toast.success(
          `🎉 Successfully authenticated with ${newProviders
            .map((p) => p.toUpperCase())
            .join(", ")}!`
        );
      }
    }

    // Auto-select the most recently created valid token
    const tokensByTimestamp = Object.entries(validTokens).sort(
      ([, a], [, b]) => (b as TokenData).issued_at - (a as TokenData).issued_at
    );

    const mostRecentToken = tokensByTimestamp[0]?.[1] as TokenData | undefined;

    if (
      mostRecentToken &&
      (!selectedToken || mostRecentToken.issued_at > selectedToken.issued_at)
    ) {
      setSelectedToken(mostRecentToken);

      // Create session and redirect to dashboard if we have valid tokens (only if not in modal mode)
      if (
        Object.keys(validTokens).length > 0 &&
        !SessionManager.isAuthenticated() &&
        !modal
      ) {
        SessionManager.createSession(mostRecentToken.provider);
        toast.success(
          `🎉 Successfully authenticated with ${mostRecentToken.provider.toUpperCase()}!`
        );

        // Redirect to dashboard after a short delay
        setTimeout(() => {
          if (onNavigateToDashboard) {
            onNavigateToDashboard();
          }
        }, 2000);
      }
    }
  };

  const handleSendToBackend = async () => {
    if (!selectedToken) return;

    // Show session selection instead of directly sending to backend
    setShowSessionSelection(true);
  };

  const handleClearAllTokens = () => {
    TokenStorage.clearAllTokens();
    setTokens({});
    setSelectedToken(null);
    setClaims(null);
    setShowSessionSelection(false);
    toast.success("All tokens cleared");
  };

  const formatDate = (timestamp: number) => {
    return new Date(timestamp * 1000).toLocaleString();
  };

  const getTokenStatus = (token: TokenData) => {
    const isValid = TokenStorage.isTokenValid(token);
    const timeUntilExpiry = TokenStorage.getTimeUntilExpiry(token);
    const isNearExpiry = TokenStorage.isTokenNearExpiry(token, 15); // 15 minute warning
    const canRefresh = TokenStorage.canRefreshToken(token);

    return {
      isValid,
      expiresAt: TokenStorage.getTokenExpiryDate(token),
      timeUntilExpiry,
      isExpiringSoon: isNearExpiry,
      canRefresh,
      formattedTime: TokenStorage.formatTimeUntilExpiry(token),
    };
  };

  const availableTokens = Object.entries(tokens);

  // Show session selection if user clicked "Connect using API"
  if (showSessionSelection && selectedToken) {
    return (
      <SessionSelection
        token={selectedToken}
        onBack={() => setShowSessionSelection(false)}
      />
    );
  }

  if (availableTokens.length === 0) {
    return (
      <div
        className={`${modal ? "p-6" : "container mx-auto px-6 py-16"} ${
          modal ? "" : "max-w-3xl"
        } bg-transparent ${modal ? "" : "min-h-screen"}`}
      >
        {/* Header */}
        {!modal && <FullSDXLogo />}

        {!modal && (
          <div className="flex items-center gap-4 mb-8">
            <Button
              variant="ghost"
              onClick={onBack}
              className="-ml-2 text-base text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
            >
              ← Back to selection
            </Button>
            {onNavigateToDashboard && (
              <Button
                variant="outline"
                onClick={onNavigateToDashboard}
                className="text-base border-[rgb(120,176,219)] text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
              >
                📊 View Dashboard
              </Button>
            )}
          </div>
        )}

        <div className="space-y-6">
          <div className="space-y-2 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
            <h3 className="text-xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] mb-1">
              No Valid Tokens
            </h3>
            <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)]">
              You don't have any valid tokens. Please authenticate with a
              provider first.
            </p>
          </div>
          <Button
            onClick={onBack}
            className="w-full py-4 text-lg font-semibold bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] dark:bg-[rgb(100,180,255)] dark:hover:bg-[rgb(120,200,255)] text-white shadow-lg hover:shadow-xl transition-all duration-200 hover:scale-105 active:scale-95"
            size="lg"
          >
            Go Back to Authentication
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div
      className={`${modal ? "p-6" : "container mx-auto px-6 py-16"} ${
        modal ? "" : "max-w-6xl"
      } bg-transparent ${modal ? "" : "min-h-screen"}`}
    >
      {/* Header */}
      {!modal && <FullSDXLogo />}

      {!modal && (
        <div className="flex items-center gap-4 mb-8">
          <Button
            variant="ghost"
            onClick={onBack}
            className="-ml-2 text-base text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
          >
            ← Back to selection
          </Button>
          {onNavigateToDashboard && (
            <Button
              variant="outline"
              onClick={onNavigateToDashboard}
              className="text-base border-[rgb(120,176,219)] text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
            >
              📊 View Dashboard
            </Button>
          )}
        </div>
      )}

      <div
        className={`grid ${modal ? "lg:grid-cols-1" : "lg:grid-cols-3"} gap-8`}
      >
        {/* Token Refresh Status */}
        <div className={modal ? "col-span-1" : "lg:col-span-3"}>
          <TokenStatus
            providers={Object.keys(tokens) as any[]}
            showRefreshButtons={true}
            compact={false}
          />
        </div>

        {/* Token Selection */}
        {!modal && (
          <Card className="lg:col-span-1 shadow-lg border-2 border-[rgb(120,176,219)] bg-[rgb(255,255,255)]">
            <CardHeader className="pb-8">
              <CardTitle className="text-2xl text-[rgb(64,143,204)]">
                Available Tokens
              </CardTitle>
              <CardDescription className="text-lg mt-2 text-[rgb(50,135,200)]">
                Select a token to view details
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6 pt-0">
              {availableTokens.map(([provider, token]) => {
                const status = getTokenStatus(token);
                const isSelected = selectedToken?.provider === provider;

                return (
                  <div
                    key={provider}
                    className={`p-6 rounded-xl border-2 cursor-pointer transition-all hover:shadow-md ${
                      isSelected
                        ? "border-[rgb(50,135,200)] bg-[rgb(236,244,250)] shadow-md"
                        : "border-[rgb(120,176,219)] hover:border-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
                    }`}
                    onClick={() => setSelectedToken(token)}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-4">
                        <div>
                          <div
                            className="font-semibold text-lg"
                            style={{ color: "rgb(64, 143, 204)" }}
                          >
                            {provider.toUpperCase()}
                          </div>
                          <div
                            className="text-sm mt-1"
                            style={{ color: "rgb(50, 135, 200)" }}
                          >
                            {status.formattedTime} remaining
                          </div>
                          {status.canRefresh && (
                            <div className="text-xs text-green-600 mt-1">
                              Auto-refresh enabled
                            </div>
                          )}
                        </div>
                      </div>
                      <div className="flex items-center gap-3">
                        {status.isExpiringSoon && (
                          <Badge variant="destructive" className="text-xs">
                            {status.canRefresh ? "Refreshing" : "Expires Soon"}
                          </Badge>
                        )}
                        {status.isValid ? (
                          <span
                            style={{ color: "rgb(50, 135, 200)" }}
                            className="text-xl"
                          >
                            ✓
                          </span>
                        ) : (
                          <span className="text-destructive text-xl">✗</span>
                        )}
                      </div>
                    </div>
                  </div>
                );
              })}
            </CardContent>
          </Card>
        )}

        {/* Token Details */}
        {selectedToken && claims && (
          <div
            className={`${modal ? "col-span-1" : "lg:col-span-2"} space-y-6`}
          >
            <div className="space-y-2 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
              <h3 className="text-xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] mb-1">
                Token Details & Actions
              </h3>
              <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)]">
                Claims and metadata for {selectedToken.provider.toUpperCase()}{" "}
                token
              </p>
            </div>
            <div className="space-y-6">
              <div className="space-y-4">
                {claims.sub && (
                  <div className="flex items-start gap-4 p-5 rounded-xl bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
                    <div className="min-w-0 flex-1">
                      <div className="text-sm font-semibold mb-2 text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">
                        Subject
                      </div>
                      <div className="text-base break-all text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] font-medium">
                        {claims.sub}
                      </div>
                    </div>
                  </div>
                )}

                {claims.email && (
                  <div className="flex items-start gap-4 p-5 rounded-xl bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
                    <div className="min-w-0 flex-1">
                      <div className="text-sm font-semibold mb-2 text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">
                        Email
                      </div>
                      <div className="text-base text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] font-medium">
                        {claims.email}
                      </div>
                    </div>
                  </div>
                )}

                {claims.iss && (
                  <div className="flex items-start gap-4 p-5 rounded-xl bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
                    <div className="min-w-0 flex-1">
                      <div className="text-sm font-semibold mb-2 text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">
                        Issuer
                      </div>
                      <div className="text-base break-all text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] font-medium">
                        {claims.iss}
                      </div>
                    </div>
                  </div>
                )}
              </div>

              <Separator className="my-6 border-[rgb(200,220,240)] dark:border-blue-500/20" />

              <div className="space-y-4">
                <Button
                  onClick={handleSendToBackend}
                  disabled={!TokenStorage.isTokenValid(selectedToken)}
                  className="w-full py-4 text-lg font-semibold bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] dark:bg-[rgb(100,180,255)] dark:hover:bg-[rgb(120,200,255)] text-white shadow-lg hover:shadow-xl transition-all duration-200 disabled:opacity-50 hover:scale-105 active:scale-95"
                  size="lg"
                >
                  Connect using API
                </Button>

                {/* MEICAN and FABRIC connection buttons */}
                <div className="grid grid-cols-2 gap-4">
                  <Button
                    onClick={() =>
                      window.open("http://190.103.184.199", "_blank")
                    }
                    disabled={!TokenStorage.isTokenValid(selectedToken)}
                    className="py-3 text-base font-medium bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] dark:bg-[rgb(100,180,255)] dark:hover:bg-[rgb(120,200,255)] text-white shadow-md hover:shadow-lg transition-all duration-200 disabled:opacity-50 hover:scale-105 active:scale-95"
                  >
                    Connect using MEICAN
                  </Button>

                  <Button
                    onClick={() =>
                      window.open("https://fabric-testbed.net", "_blank")
                    }
                    disabled={!TokenStorage.isTokenValid(selectedToken)}
                    className="py-3 text-base font-medium bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] dark:bg-[rgb(100,180,255)] dark:hover:bg-[rgb(120,200,255)] text-white shadow-md hover:shadow-lg transition-all duration-200 disabled:opacity-50 hover:scale-105 active:scale-95"
                  >
                    Connect using FABRIC
                  </Button>
                </div>

                <Button
                  variant="outline"
                  onClick={handleClearAllTokens}
                  className="w-full py-3 text-base font-medium border-2 border-red-500/50 text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-500/10 hover:border-red-500 dark:hover:border-red-400 transition-all duration-200 shadow-sm hover:shadow-md hover:scale-105 active:scale-95"
                >
                  Clear All Tokens
                </Button>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Backend Configuration Info */}
      <div className={`${modal ? "mt-6" : "mt-12"} space-y-4`}>
        <div className="space-y-2 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
          <h3 className="text-xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] mb-1">
            Current Configuration
          </h3>
        </div>
        <div className="p-5 rounded-xl bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
          <div className="text-sm font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] mb-2 uppercase tracking-wide">
            Backend URL
          </div>
          <div className="text-base text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] break-all font-medium">
            https://sdxapi.atlanticwave-sdx.ai/
          </div>
        </div>
      </div>
    </div>
  );
}
