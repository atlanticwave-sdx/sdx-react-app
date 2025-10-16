import { useState, useEffect } from "react";
import { useKV } from "@github/spark/hooks";
import { Toaster } from "@/components/ui/sonner";
import { toast } from "sonner";
import { LandingPage } from "@/components/pages/LandingPage";
import { LoginPage } from "@/components/pages/LoginPage";
import { EmailValidationPage } from "@/components/pages/EmailValidationPage";
import { TokenPage } from "@/components/pages/TokenPage";
import { Dashboard } from "@/components/pages/Dashboard";
import { ORCIDCallbackPage } from "@/components/pages/ORCIDCallbackPage";
import { CILogonCallbackPage } from "@/components/pages/CILogonCallbackPage";
import { TokenExpiryNotification } from "@/components/TokenExpiryNotification";
import { config } from "@/lib/config";
import { Provider } from "@/lib/config";
import { TokenStorage } from "@/lib/token-storage";
import { useTokenRefresh } from "@/hooks/useTokenRefresh";
import { SessionManager } from "@/lib/session";

type Page = "landing" | "login" | "email-validation" | "token" | "dashboard" | "orcid-callback" | "cilogon-callback";

function App() {
  const [currentPage, setCurrentPage] = useState<Page>("landing");
  const [selectedProvider, setSelectedProvider] = useState<Provider | undefined>();
  const [loginProvider, setLoginProvider] = useState<Provider | undefined>();
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(() => {
    // Initialize authentication state on component mount
    return SessionManager.isAuthenticated();
  });

  // Initialize automatic token refresh system
  const tokenRefresh = useTokenRefresh({
    refreshBeforeExpiryMinutes: 5,
    checkIntervalMinutes: 1,
    showNotifications: true
  });


  // Handle URL navigation with session management
  useEffect(() => {
    const updatePageFromURL = () => {
      const path = window.location.pathname;
      const searchParams = new URLSearchParams(window.location.search);
      
      // Determine base path based on environment
      const isProduction = import.meta.env.PROD;
      const basePath = isProduction ? "/multi-provider-authe" : "";
      
      // Update session activity
      SessionManager.updateActivity();
      
      // Handle ORCID callback
      if (path === `${basePath}/auth/callback/orcid`) {
        setCurrentPage("orcid-callback");
      }
      // Handle CILogon callback
      else if (path === `${basePath}/auth/callback/cilogon`) {
        setCurrentPage("cilogon-callback");
      }
      // Handle login page
      else if (path === `${basePath}/login`) {
        const provider = searchParams.get("provider") as Provider;
        if (provider && ["cilogon", "orcid"].includes(provider)) {
          setLoginProvider(provider);
        }
        setCurrentPage("login");
      } else if (path === `${basePath}/email-validation`) {
        setCurrentPage("email-validation");
      } else if (path === `${basePath}/token`) {
        setCurrentPage("token");
      } else if (path === `${basePath}/dashboard`) {
        // Check authentication before allowing dashboard access
        console.log('Dashboard accessed, checking authentication...');
        console.log('Current localStorage session:', localStorage.getItem('sdx_user_session'));
        console.log('Available tokens:', {
          orcid: !!TokenStorage.getToken("orcid"),
          cilogon: !!TokenStorage.getToken("cilogon")
        });
        
        const isAuth = SessionManager.isAuthenticated();
        console.log('Dashboard auth check result:', isAuth);
        
        if (isAuth) {
          console.log('Dashboard authenticated, setting state');
          setIsAuthenticated(true);
          setCurrentPage("dashboard");
        } else {
          console.log('Not authenticated, redirecting to landing');
          console.log('Session state:', SessionManager.getSession());
          setIsAuthenticated(false);
          setCurrentPage("landing");
          window.history.replaceState({}, "", basePath || "/");
        }
      } else {
        // Root path - check if user is authenticated
        console.log('Root path accessed, checking authentication...');
        const isAuth = SessionManager.isAuthenticated();
        console.log('Is authenticated:', isAuth);
        
        if (isAuth) {
          // Redirect authenticated users to dashboard
          console.log('Root authenticated, redirecting to dashboard');
          setIsAuthenticated(true);
          setCurrentPage("dashboard");
          const dashboardPath = `${basePath}/dashboard`;
          if (path !== dashboardPath) {
            window.history.replaceState({}, "", dashboardPath);
          }
        } else {
          console.log('Not authenticated, showing landing page');
          setIsAuthenticated(false);
          setCurrentPage("landing");
        }
      }
    };

    updatePageFromURL();
    window.addEventListener("popstate", updatePageFromURL);
    return () => window.removeEventListener("popstate", updatePageFromURL);
  }, []);

  const navigateTo = (page: Page, provider?: Provider) => {
    // Determine base path based on environment
    const isProduction = import.meta.env.PROD;
    const basePath = isProduction ? "/multi-provider-authe" : "";
    
    let path = basePath || "/";
    
    switch (page) {
      case "login":
        path = `${basePath}/login${provider ? `?provider=${provider}` : ""}`;
        if (provider) setLoginProvider(provider);
        break;
      case "email-validation":
        path = `${basePath}/email-validation`;
        break;
      case "token":
        path = `${basePath}/token`;
        break;
      case "dashboard":
        path = `${basePath}/dashboard`;
        break;
      case "landing":
        path = basePath || "/";
        break;
    }
    
    window.history.pushState({}, "", path);
    setCurrentPage(page);
  };

  const handleLogin = (provider: Provider) => {
    setSelectedProvider(provider);
    navigateTo("login", provider);
  };

  const handleLoginComplete = () => {
    // Create session when login is completed
    if (loginProvider) {
      SessionManager.createSession(loginProvider);
      setIsAuthenticated(true); // Update authentication state
      console.log('Login completed, session created for:', loginProvider);
    }
    navigateTo("dashboard"); // Go directly to dashboard instead of token page
  };

  const handleEmailValidationComplete = () => {
    // After email validation, create session and go to dashboard
    if (loginProvider) {
      SessionManager.createSession(loginProvider);
      setIsAuthenticated(true);
    }
    navigateTo("dashboard");
  };

  const handleNavigateToEmailValidation = (email?: string) => {
    // Store the email for the validation page
    if (email) {
      sessionStorage.setItem('pre_validated_email', email);
    }
    navigateTo("email-validation");
  };

  const handleBackToLanding = () => {
    setSelectedProvider(undefined);
    setLoginProvider(undefined);
    navigateTo("landing");
  };

  const handleNavigateToDashboard = () => {
    // Check authentication before navigating to dashboard
    const isAuth = SessionManager.isAuthenticated();
    console.log('Navigate to dashboard - auth check:', isAuth);
    
    if (isAuth) {
      setIsAuthenticated(true);
      navigateTo("dashboard");
    } else {
      console.log('Not authenticated, cannot navigate to dashboard');
      setIsAuthenticated(false);
      navigateTo("landing");
    }
  };

  const handleNavigateToTokens = () => {
    navigateTo("token");
  };

  const handleLogout = () => {
    toast.success("Logging out...");
    setSelectedProvider(undefined);
    setLoginProvider(undefined);
    setIsAuthenticated(false);
    
    // Use SessionManager.logout() which handles provider-specific logout
    SessionManager.logout();
    
    // Note: For ORCID, this will redirect to ORCID logout page
    // For other providers, it will just clear local session and stay on current page
    // So we only navigate to landing if we're still on the same page (no redirect happened)
    setTimeout(() => {
      if (window.location.pathname !== '/') {
        navigateTo("landing");
      }
    }, 100);
  };


  return (
    <div className="min-h-screen" style={{ backgroundColor: 'rgb(255, 255, 255)' }}>
      <Toaster />
      
      {/* Token expiry notifications - shown on all pages */}
      <TokenExpiryNotification 
        warningMinutes={15}
        className="fixed top-4 left-4 right-4 z-50 max-w-4xl mx-auto"
      />
      
      {currentPage === "landing" && (
        <LandingPage
          selectedProvider={selectedProvider}
          onProviderSelect={setSelectedProvider}
          onLogin={handleLogin}
          onNavigateToDashboard={handleNavigateToDashboard}
        />
      )}
      
      {currentPage === "login" && loginProvider && (
        <LoginPage
          provider={loginProvider}
          onComplete={handleLoginComplete}
          onBack={handleBackToLanding}
        />
      )}
      
      {currentPage === "email-validation" && (
        <EmailValidationPage
          onComplete={handleEmailValidationComplete}
          onBack={() => navigateTo("login")}
        />
      )}
      
      {currentPage === "token" && (
        <TokenPage
          onBack={handleBackToLanding}
          onNavigateToDashboard={handleNavigateToDashboard}
        />
      )}

      {currentPage === "dashboard" && isAuthenticated && (
        <Dashboard
          onBack={handleBackToLanding}
          onNavigateToTokens={handleNavigateToTokens}
          onLogout={handleLogout}
        />
      )}

      {currentPage === "dashboard" && !isAuthenticated && (
        <LandingPage
          selectedProvider={selectedProvider}
          onProviderSelect={setSelectedProvider}
          onLogin={handleLogin}
          onNavigateToDashboard={handleNavigateToDashboard}
        />
      )}

      {currentPage === "orcid-callback" && (
        <ORCIDCallbackPage
          onBack={handleBackToLanding}
          onNavigateToDashboard={handleNavigateToDashboard}
          onNavigateToEmailValidation={handleNavigateToEmailValidation}
        />
      )}

      {currentPage === "cilogon-callback" && (
        <CILogonCallbackPage
          onBack={handleBackToLanding}
          onNavigateToDashboard={handleNavigateToDashboard}
          onNavigateToEmailValidation={handleNavigateToEmailValidation}
        />
      )}
    </div>
  );
}

export default App;