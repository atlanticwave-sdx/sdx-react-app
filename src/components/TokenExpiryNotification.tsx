import { useEffect, useState } from "react";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { Button } from "@/components/ui/button";
import { X, RefreshCw, AlertTriangle } from "lucide-react";
import { TokenStorage } from "@/lib/token-storage";
import { TokenData, Provider } from "@/lib/types";
import { useTokenRefresh } from "@/hooks/useTokenRefresh";

interface TokenExpiryNotificationProps {
  warningMinutes?: number;
  className?: string;
}

export function TokenExpiryNotification({
  warningMinutes = 10,
  className = "",
}: TokenExpiryNotificationProps) {
  const [expiringTokens, setExpiringTokens] = useState<
    Array<{ provider: Provider; token: TokenData; timeLeft: string }>
  >([]);
  const [dismissed, setDismissed] = useState<Set<string>>(new Set());

  const { manualRefresh, refreshStatus } = useTokenRefresh();

  useEffect(() => {
    const checkTokens = () => {
      const providers: Provider[] = ["cilogon", "orcid"];
      const expiring: Array<{
        provider: Provider;
        token: TokenData;
        timeLeft: string;
      }> = [];

      providers.forEach((provider) => {
        const token = TokenStorage.getToken(provider);
        if (token && TokenStorage.isTokenValid(token)) {
          const isNearExpiry = TokenStorage.isTokenNearExpiry(
            token,
            warningMinutes
          );
          const dismissKey = `${provider}-${token.issued_at}`;

          if (isNearExpiry && !dismissed.has(dismissKey)) {
            expiring.push({
              provider,
              token,
              timeLeft: TokenStorage.formatTimeUntilExpiry(token),
            });
          }
        }
      });

      setExpiringTokens(expiring);
    };

    // Check immediately and then every 30 seconds
    checkTokens();
    const interval = setInterval(checkTokens, 30000);
    return () => clearInterval(interval);
  }, [warningMinutes, dismissed]);

  const handleDismiss = (provider: Provider, issuedAt: number) => {
    const dismissKey = `${provider}-${issuedAt}`;
    setDismissed((prev) => new Set([...prev, dismissKey]));
  };

  const handleRefresh = async (provider: Provider) => {
    const token = expiringTokens.find((t) => t.provider === provider)?.token;
    if (token && TokenStorage.canRefreshToken(token)) {
      try {
        await manualRefresh(provider);
        // Remove from expiring tokens on successful refresh
        setExpiringTokens((prev) =>
          prev.filter((t) => t.provider !== provider)
        );
      } catch (error) {
        console.error(`Failed to refresh ${provider} token:`, error);
      }
    }
  };

  if (expiringTokens.length === 0) {
    return null;
  }

  return (
    <div className={`space-y-3 ${className}`}>
      {expiringTokens.map(({ provider, token, timeLeft }) => (
        <Alert
          key={`${provider}-${token.issued_at}`}
          className="border-2 border-[rgb(50,135,200)]/40 dark:border-[rgb(100,180,255)]/50 bg-gradient-to-br from-[rgb(236,244,250)] to-[rgb(248,251,255)] dark:from-blue-500/10 dark:to-blue-500/5 shadow-lg backdrop-blur-sm"
        >
          <AlertTriangle className="h-5 w-5 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]" />
          <AlertDescription className="flex items-center justify-between gap-4">
            <div className="flex items-center gap-3 flex-wrap">
              <span className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-medium text-sm">
                <strong className="font-bold text-base text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                  {provider.toUpperCase()}
                </strong>{" "}
                token expires in{" "}
                <span className="font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                  {timeLeft}
                </span>
              </span>
              {TokenStorage.canRefreshToken(token) && (
                <span className="text-sm text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] font-medium">
                  Auto-refresh enabled
                </span>
              )}
            </div>
            <div className="flex items-center gap-2 flex-shrink-0">
              {TokenStorage.canRefreshToken(token) && (
                <Button
                  size="sm"
                  variant="outline"
                  onClick={() => handleRefresh(provider)}
                  disabled={refreshStatus?.isRefreshing}
                  className="h-7 px-3 text-xs font-medium border-[rgb(50,135,200)] dark:border-[rgb(100,180,255)] text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(64,143,204)] dark:hover:border-[rgb(120,200,255)] transition-all shadow-sm hover:shadow-md disabled:opacity-50"
                >
                  {refreshStatus?.isRefreshing ? (
                    <RefreshCw className="h-3.5 w-3.5 animate-spin" />
                  ) : (
                    <>
                      <RefreshCw className="h-3.5 w-3.5 mr-1.5" />
                      Refresh Now
                    </>
                  )}
                </Button>
              )}
              <Button
                size="sm"
                variant="ghost"
                onClick={() => handleDismiss(provider, token.issued_at)}
                className="h-7 w-7 p-0 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:text-[rgb(64,143,204)] dark:hover:text-[rgb(120,200,255)] transition-all rounded-md"
              >
                <X className="h-4 w-4" />
              </Button>
            </div>
          </AlertDescription>
        </Alert>
      ))}
    </div>
  );
}
