import { useState } from "react";
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

interface LandingPageProps {
  selectedProvider?: Provider;
  onProviderSelect: (provider: Provider) => void;
  onLogin: (provider: Provider) => void;
  onNavigateToDashboard?: () => void;
}

const providerInfo = {
  cilogon: {
    name: "CILogon",
    color: "bg-[rgb(50,135,200)]",
    bgColor:
      "bg-[rgb(236,244,250)] hover:bg-[rgb(236,244,250)] border-[rgb(120,176,219)]",
    selectedBgColor: "bg-[rgb(236,244,250)] border-[rgb(64,143,204)]",
  },
  orcid: {
    name: "ORCID",
    color: "bg-[rgb(50,135,200)]",
    bgColor:
      "bg-[rgb(236,244,250)] hover:bg-[rgb(236,244,250)] border-[rgb(120,176,219)]",
    selectedBgColor: "bg-[rgb(236,244,250)] border-[rgb(64,143,204)]",
  },
} as const;

export function LandingPage({
  selectedProvider,
  onProviderSelect,
  onLogin,
  onNavigateToDashboard,
}: LandingPageProps) {
  const canContinue = selectedProvider;

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
        <Card className="bg-[rgb(236,244,250)] border-[rgb(120,176,219)] shadow-lg">
          <CardHeader className="pb-3 pt-4 px-4 bg-[rgb(50,135,200)] text-white rounded-t-lg text-center">
            <CardDescription className="text-[rgb(236,244,250)] mt-1">
              Select an Identity Provider
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-3 p-4 flex flex-col items-center justify-center">
            <div className="w-full max-w-md space-y-3 mx-auto">
              {Object.entries(providerInfo).map(([key, info]) => {
                const provider = key as Provider;
                const isSelected = selectedProvider === provider;

                return (
                  <Button
                    key={provider}
                    variant="ghost"
                    className={`w-full justify-center p-4 h-auto transition-all duration-200 border-2 rounded-xl ${
                      isSelected
                        ? `${info.selectedBgColor} shadow-lg border-opacity-100 transform scale-[1.02]`
                        : `bg-[rgb(255,255,255)] hover:bg-[rgb(236,244,250)] hover:shadow-md border-[rgb(120,176,219)] hover:border-opacity-100`
                    }`}
                    onClick={() => onProviderSelect(provider)}
                  >
                    <div className="text-center flex-1 space-y-2">
                      <div className="flex items-center justify-between">
                        <div className="flex-1">
                          <div className="font-semibold text-base text-[rgb(64,143,204)]">
                            {info.name}
                          </div>
                          <div className="text-sm text-[rgb(50,135,200)]">
                            {info.name === "ORCID"
                              ? "Researcher identifiers"
                              : info.name === "CILogon"
                              ? "Academic federation"
                              : "Identity provider"}
                          </div>
                        </div>
                      </div>
                    </div>
                  </Button>
                );
              })}
            </div>
          </CardContent>
        </Card>

        {/* Continue Button */}
        <div className="flex justify-center pt-4">
          <Button
            size="lg"
            disabled={!canContinue}
            onClick={() => canContinue && onLogin(selectedProvider)}
            className={`w-full max-w-md px-6 py-4 text-base font-semibold rounded-xl transition-all duration-200 ${
              canContinue
                ? "bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)] shadow-lg hover:shadow-xl transform hover:scale-[1.02] active:scale-[0.98]"
                : "bg-[rgb(120,176,219)] text-[rgb(255,255,255)] opacity-50 cursor-not-allowed"
            }`}
          >
            Continue with{" "}
            {selectedProvider
              ? providerInfo[selectedProvider].name
              : "Provider"}
          </Button>
        </div>
      </div>
    </div>
  );
}
