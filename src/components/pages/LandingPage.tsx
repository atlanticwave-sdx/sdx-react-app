import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Provider } from "@/lib/config";
import { FullSDXLogo } from "@/components/FullSDXLogo";
import { CILogonProvider } from "@/lib/providers/cilogon";

interface LandingPageProps {
  onLogin: (provider: Provider) => void;
  onNavigateToDashboard?: () => void;
}

const providerInfo = {
  cilogon: {
    name: "CILogon",
    iconPath: "src/assets/images/CILogon-icon.png",
    description: "Academic federation",
  },
  orcid: {
    name: "ORCID",
    iconPath: "src/assets/images/ORCID-ICON.png",
    description: "Researcher identifiers",
  },
} as const;

export function LandingPage({
  onLogin,
  onNavigateToDashboard,
}: LandingPageProps) {
  const handleProviderClick = async (provider: Provider) => {
    // For CILogon, directly start authentication and skip the login page
    if (provider === "cilogon") {
      try {
        await CILogonProvider.startAuthentication();
        // This will redirect the page, so no code after this will execute
      } catch (error) {
        console.error("Failed to start CILogon authentication:", error);
        // If there's an error, fall back to the login page
        onLogin(provider);
      }
    } else {
      // For other providers (e.g., ORCID), use the existing flow
      onLogin(provider);
    }
  };

  return (
    <div className="min-h-screen bg-white p-3 pt-8">
      {/* Dashboard button in top right */}
      {onNavigateToDashboard && (
        <div className="fixed top-4 right-4 z-40">
          <Button
            variant="outline"
            onClick={onNavigateToDashboard}
            className="border-[rgb(120,176,219)] text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
          >
            📊 Dashboard
          </Button>
        </div>
      )}

      <div className="max-w-2xl mx-auto space-y-8">
        {/* Header */}
        <FullSDXLogo />

        {/* Provider Selection */}
        <Card className="bg-white border-[rgb(200,200,200)] shadow-lg">
          <CardHeader
            className="text-center border-b"
            style={{ paddingTop: "10px", paddingBottom: "10px" }}
          >
            <CardTitle className="text-2xl font-semibold text-[rgb(50,135,200)]">
              Select an Identity Provider
            </CardTitle>
          </CardHeader>
          <CardContent style={{ paddingTop: "10px", paddingBottom: "50px" }}>
            <div className="w-full max-w-md mx-auto">
              {Object.entries(providerInfo).map(([key, info], index) => {
                const provider = key as Provider;
                const isLastButton =
                  index === Object.entries(providerInfo).length - 1;

                return (
                  <Button
                    key={provider}
                    variant="outline"
                    className="w-full justify-start p-6 h-auto transition-all duration-200 rounded-lg bg-white hover:bg-[rgb(245,245,245)] !border-[rgb(200,200,200)] hover:!border-[rgb(180,180,180)] hover:shadow-md active:scale-[0.98]"
                    style={{ marginBottom: isLastButton ? "0" : "10px" }}
                    onClick={() => handleProviderClick(provider)}
                  >
                    <div className="flex items-center gap-4 w-full">
                      <div className="flex-shrink-0">
                        <img
                          src={info.iconPath}
                          alt={`${info.name} icon`}
                          className="w-10 h-10 object-cover rounded"
                          style={{
                            minWidth: "40px",
                            minHeight: "40px",
                            maxWidth: "40px",
                            maxHeight: "40px",
                          }}
                        />
                      </div>
                      <div className="text-left flex-1">
                        <div className="font-semibold text-lg text-[rgb(50,135,200)]">
                          {info.name}
                        </div>
                        <div className="text-sm text-[rgb(50,135,200)]">
                          {info.description}
                        </div>
                      </div>
                    </div>
                  </Button>
                );
              })}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
