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
import { Provider, config } from "@/lib/config";
import { DeviceFlowState } from "@/lib/types";
import { TokenStorage } from "@/lib/token-storage";
import { CILogonProvider } from "@/lib/providers/cilogon";
import { ORCIDProvider } from "@/lib/providers/orcid";
import { FullSDXLogo } from "@/components/FullSDXLogo";
import { CheckCircle, XCircle, Clock } from "@phosphor-icons/react";

interface LoginPageProps {
  provider: Provider;
  onComplete: () => void;
  onBack: () => void;
}

export function LoginPage({ provider, onComplete, onBack }: LoginPageProps) {
  const [deviceFlow, setDeviceFlow] = useState<DeviceFlowState>({
    status: "idle",
  });
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // Debug: Log provider information
    console.log("LoginPage initialized for provider:", provider);
  }, [provider]);

  const startCILogonFlow = async () => {
    console.log("Starting CILogon authentication...");
    setIsLoading(true);
    setDeviceFlow({ status: "pending" });

    try {
      // Use same window authentication instead of popup
      // This will redirect the browser to CILogon, so no code after this will execute
      await CILogonProvider.startAuthentication();
    } catch (error: any) {
      console.error("CILogon authentication failed:", error);
      const errorMessage =
        error instanceof Error ? error.message : "Authentication failed";

      toast.error(`❌ ${errorMessage}`);
      setDeviceFlow({
        status: "error",
        error: errorMessage,
      });
      setIsLoading(false);
    }
  };

  const startORCIDFlow = async () => {
    console.log("Starting ORCID authentication...");
    setIsLoading(true);

    try {
      const token = await ORCIDProvider.startAuthenticationPopup();
      console.log("ORCID authentication successful:", token);

      toast.success("ORCID authentication successful!");
      setDeviceFlow({ status: "success", token });

      // Complete the login process
      setTimeout(() => {
        onComplete();
      }, 1000);
    } catch (error: any) {
      console.error("ORCID authentication failed:", error);
      const errorMessage =
        error instanceof Error ? error.message : "Authentication failed";
      toast.error(errorMessage);
      setDeviceFlow({
        status: "error",
        error: errorMessage,
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container mx-auto px-6 py-16 max-w-3xl bg-[rgb(255,255,255)] min-h-screen">
      {/* Header */}
      <FullSDXLogo />

      <Button
        variant="ghost"
        onClick={onBack}
        className="mb-8 -ml-2 text-base text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
      >
        ← Back to selection
      </Button>

      <Card className="shadow-lg border-2 border-[rgb(120,176,219)] bg-[rgb(255,255,255)]">
        <CardHeader className="pb-8 text-center">
          <CardTitle className="text-2xl text-[rgb(64,143,204)] text-center">
            Authenticate with {provider.toUpperCase()}
          </CardTitle>
          <CardDescription className="text-lg mt-2 text-[rgb(50,135,200)] text-center">
            Complete the authentication flow to obtain your token
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-10 pt-0">
          {provider === "cilogon" && (
            <>
              {deviceFlow.status === "idle" && (
                <div className="space-y-6">
                  <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
                    <AlertDescription className="text-base text-[rgb(64,143,204)]">
                      <strong>CILogon Authentication:</strong> Click the button
                      below to authenticate with CILogon. You will be redirected
                      to CILogon's login page and then back to this application.
                    </AlertDescription>
                  </Alert>

                  {/* URL Information Display */}
                  <Alert className="border-2 border-[rgb(50,135,200)] bg-white">
                    <AlertDescription className="text-sm text-[rgb(64,143,204)]">
                      <div className="space-y-2">
                        <p>
                          <strong>Debug Information:</strong>
                        </p>
                        <div className="space-y-1 font-mono text-xs break-all">
                          <div>
                            <span className="font-bold text-[rgb(50,135,200)]">
                              Client ID:
                            </span>
                            <br />
                            <span className="text-[rgb(64,143,204)]">
                              {config.cilogon.clientId}
                            </span>
                          </div>
                          <div>
                            <span className="font-bold text-[rgb(50,135,200)]">
                              Registered Redirect URI:
                            </span>
                            <br />
                            <span className="text-[rgb(64,143,204)]">
                              {config.cilogon.redirectUri}
                            </span>
                          </div>
                          <div>
                            <span className="font-bold text-[rgb(50,135,200)]">
                              Current Window Location:
                            </span>
                            <br />
                            <span className="text-[rgb(64,143,204)]">
                              {typeof window !== "undefined"
                                ? window.location.origin +
                                  window.location.pathname
                                : "N/A"}
                            </span>
                          </div>
                          <div>
                            <span className="font-bold text-[rgb(50,135,200)]">
                              Scope:
                            </span>
                            <br />
                            <span className="text-[rgb(64,143,204)]">
                              {config.cilogon.scope}
                            </span>
                          </div>
                          <div className="mt-2 p-2 bg-[rgb(236,244,250)] rounded">
                            <span className="font-bold text-[rgb(50,135,200)]">
                              Callback Status:
                            </span>
                            <br />
                            <span className="text-[rgb(64,143,204)]">
                              ✓ Callback file exists at both
                              /auth/callback/cilogon/ and
                              /multi-provider-authe/auth/callback/cilogon/
                            </span>
                          </div>
                        </div>
                      </div>
                    </AlertDescription>
                  </Alert>

                  <Button
                    onClick={startCILogonFlow}
                    disabled={isLoading}
                    size="lg"
                    className="w-full py-4 text-lg font-semibold bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)]"
                  >
                    {isLoading
                      ? "Opening Authentication..."
                      : "Login with CILogon"}
                  </Button>
                </div>
              )}
              {deviceFlow.status === "pending" && (
                <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
                  <Clock className="h-5 w-5 text-[rgb(50,135,200)]" />
                  <AlertDescription className="text-base ml-2 text-[rgb(64,143,204)]">
                    <strong>Redirecting to CILogon...</strong> You will be
                    redirected momentarily.
                  </AlertDescription>
                </Alert>
              )}

              {deviceFlow.status === "success" && (
                <Alert className="border-2 border-green-200 bg-green-50">
                  <CheckCircle className="h-5 w-5 text-green-600" />
                  <AlertDescription className="text-base ml-2 text-green-800">
                    ✅ Authentication successful! Redirecting to your token
                    page...
                  </AlertDescription>
                </Alert>
              )}

              {deviceFlow.status === "error" && (
                <div className="space-y-4">
                  <Alert variant="destructive">
                    <XCircle className="h-5 w-5" />
                    <AlertDescription>{deviceFlow.error}</AlertDescription>
                  </Alert>

                  <div className="space-y-4">
                    <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
                      <AlertDescription className="text-sm text-[rgb(64,143,204)]">
                        <p>
                          <strong>Troubleshooting Tips:</strong>
                        </p>
                        <ul className="list-disc ml-4 mt-2 space-y-1">
                          <li>Ensure you have a valid CILogon account</li>
                          <li>
                            Try using a different browser or incognito mode
                          </li>
                          <li>Clear your browser cache and cookies</li>
                          <li>
                            Disable browser extensions that might interfere
                          </li>
                        </ul>
                      </AlertDescription>
                    </Alert>

                    <Button
                      onClick={() => {
                        setDeviceFlow({ status: "idle" });
                        setIsLoading(false);
                      }}
                      variant="default"
                      size="lg"
                      className="w-full bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)]"
                    >
                      Try Again
                    </Button>
                  </div>
                </div>
              )}
            </>
          )}

          {provider === "orcid" && (
            <>
              {deviceFlow.status === "idle" && (
                <div className="space-y-6">
                  <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
                    <AlertDescription className="text-base text-[rgb(64,143,204)]">
                      <strong>
                        ORCID strives to enable transparent and trustworthy
                        connections between researchers, their contributions,
                        and their affiliations by providing a unique, persistent
                        identifier for individuals to use as they engage in
                        research, scholarship, and innovation activities.
                      </strong>
                      <br />
                      <br />
                      We do this by providing three interrelated services:
                      <ul className="list-disc ml-4 mt-2">
                        <li>
                          The ORCID iD: a unique, persistent identifier free of
                          charge to researchers
                        </li>
                        <li>An ORCID record connected to the ORCID iD, and</li>
                        <li>
                          A set of Application Programming Interfaces (APIs), as
                          well as the services and support of communities of
                          practice that enable interoperability between an ORCID
                          record and member organizations so researchers can
                          choose to allow connection of their iD with their
                          affiliations and contributions
                        </li>
                      </ul>
                    </AlertDescription>
                  </Alert>

                  <Button
                    onClick={startORCIDFlow}
                    disabled={isLoading}
                    size="lg"
                    className="w-full py-4 text-lg font-semibold bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)]"
                  >
                    {isLoading
                      ? "Opening Authentication..."
                      : "Login with ORCID"}
                  </Button>
                </div>
              )}

              {deviceFlow.status === "success" && (
                <Alert className="border-2 border-green-200 bg-green-50">
                  <CheckCircle className="h-5 w-5 text-green-600" />
                  <AlertDescription className="text-base ml-2 text-green-800">
                    ✅ Authentication successful! Redirecting to your token
                    page...
                  </AlertDescription>
                </Alert>
              )}

              {deviceFlow.status === "error" && (
                <div className="space-y-4">
                  <Alert variant="destructive">
                    <XCircle className="h-5 w-5" />
                    <AlertDescription>{deviceFlow.error}</AlertDescription>
                  </Alert>

                  <div className="space-y-4">
                    <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
                      <AlertDescription className="text-sm text-[rgb(64,143,204)]">
                        <p>
                          <strong>Troubleshooting Tips:</strong>
                        </p>
                        <ul className="list-disc ml-4 mt-2 space-y-1">
                          <li>Ensure you have a valid ORCID account</li>
                          <li>
                            Try using a different browser or incognito mode
                          </li>
                          <li>
                            Check if your browser is blocking pop-ups or
                            redirects
                          </li>
                          <li>Clear your browser cache and cookies</li>
                          <li>
                            Disable browser extensions that might interfere
                          </li>
                        </ul>
                      </AlertDescription>
                    </Alert>

                    <Button
                      onClick={() => {
                        setDeviceFlow({ status: "idle" });
                        setIsLoading(false);
                      }}
                      variant="default"
                      size="lg"
                      className="w-full bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)]"
                    >
                      Try Again
                    </Button>
                  </div>
                </div>
              )}
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
