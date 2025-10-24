// Application configuration
export const config = {
  // Backend configuration
  backend: {
    port: 3004, // Centralized port configuration
    get baseUrl() {
      return `http://localhost:${config.backend.port}`;
    },
    get oauthExchangeUrl() {
      return `${config.backend.baseUrl}/oauth/exchange`;
    }
  },
  
  // Topology API configuration
  api: {
    get baseUrl() {
      return `${config.backend.baseUrl}/api`;
    },
    endpoints: {
      topology: "/topology"
    }
  },
  
  // Topology filtering configuration
  topology: {
    allowedDomains: ["ampath.net", "sax.net", "tenet.ac.za", "amlight.net"]
  },
  tokenHandoffPath: "/auth/oidc-token",
  
  // Get the current base URL dynamically
  getBaseUrl: () => {
    if (typeof window !== 'undefined') {
      return window.location.origin;
    }
    return "https://lmarinve.github.io";
  },
  
  // Get the current app path based on environment
  getAppPath: () => {
    const isProduction = process.env.NODE_ENV === 'production';
    return isProduction ? "/multi-provider-authe" : "";
  },
  
  // CILogon - Updated with correct OIDC settings
  cilogon: {
    clientId: "cilogon:/client_id/49ffba66ee294f1a9530301d2a281c74",
    clientSecret: "pKdqDGRvbmQOdRgA2e-Ceh05xyFNN9sIYtGZs3s4Ym6iygdyX-qKynS4cyMS1VGZmCqGsp9fEFMwEh4HS4PbIQ",
    scope: "openid", // Strict scopes - only openid works
    authUrl: "https://cilogon.org/authorize",
    tokenUrl: "https://cilogon.org/oauth2/token",
    jwksUrl: "https://cilogon.org/oauth2/certs",
    issuerUrl: "https://cilogon.org",
    redirectUri: "http://127.0.0.1:5000/auth/callback/cilogon",
    usePkce: false // Switch to client_secret flow instead of PKCE
  },
  
  // ORCID - Using sandbox environment for testing
  orcid: {
    clientId: "APP-6U5WZH9AC4EYDVAD", // Updated with proper ORCID client ID
    clientSecret: "c839f6ee-8991-4b4e-9ae3-aab528adc22c", // Client secret for token exchange
    issuerUrl: "https://orcid.org",
    authUrl: "https://orcid.org/oauth/authorize", 
    tokenUrl: "https://orcid.org/oauth/token",
    logoutUrl: "https://orcid.org/signout", // ORCID logout endpoint
    scope: "openid /authenticate",
    get redirectUri() {
      const baseUrl = config.getBaseUrl();
      const appPath = config.getAppPath();
      return `${baseUrl}${appPath}/auth/callback/orcid`;
    },
    get postLogoutRedirectUri() {
      const baseUrl = config.getBaseUrl();
      const appPath = config.getAppPath();
      return `${baseUrl}${appPath}/`;
    },
    usePkce: false // Switch to client_secret flow instead of PKCE
  },
  
  // Connection services (used after obtaining identity tokens)
  connections: {
    fabric: {
      cmBase: "https://cm.fabric-testbed.net",
      createPath: "/tokens/create",
      refreshPath: "/tokens/refresh",
      projectId: "1ecd9d6a-7701-40fa-b78e-b2293c9526ed",
      projectName: "AtlanticWave-SDX",
      tokenPath: "/home/fabric/.tokens.json"
    },
    meican: {
      baseUrl: "https://meican.rnp.br",
      authUrl: "https://meican.rnp.br/auth/login",
      apiUrl: "https://meican.rnp.br/api/v1"
    }
  }
} as const;

export type Provider = "cilogon" | "orcid";