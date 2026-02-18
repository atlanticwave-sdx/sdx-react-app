// Application configuration
export const config = {
  // Backend configuration
  backend: {
    port: parseInt(import.meta.env.VITE_BACKEND_PORT),
    get baseUrl() {
      return `${import.meta.env.VITE_API_BASE}:${config.backend.port}`;
    },
    get oauthExchangeUrl() {
      return `${config.backend.baseUrl}/oauth/exchange`;
    },
  },

  // Topology API configuration
  api: {
    get baseUrl() {
      return `${config.backend.baseUrl}/api`;
    },
    endpoints: {
      topology: "/topology",
    },
  },

  // Topology filtering configuration
  topology: {
    allowedDomains: ["ampath.net", "sax.net", "tenet.ac.za", "amlight.net"],
  },
  tokenHandoffPath: "/auth/oidc-token",

  // Get the current base URL dynamically
  getBaseUrl: () => {
    if (typeof window !== "undefined") {
      return window.location.origin;
    }
    return "https://lmarinve.github.io";
  },

  // Get the current app path based on environment
  getAppPath: () => {
    const isProduction = import.meta.env.VITE_NODE_ENV === "production";
    return isProduction ? "/multi-provider-authe" : "";
  },

  // CILogon - Updated with correct OIDC settings
  cilogon: {
    clientId: import.meta.env.VITE_CILOGON_CLIENT_ID,
    clientSecret: import.meta.env.VITE_CILOGON_CLIENT_SECRET,
    scope: "openid email profile org.cilogon.userinfo", // Request user profile claims including eppn
    authUrl: "https://cilogon.org/authorize",
    tokenUrl: import.meta.env.VITE_CILOGON_TOKEN_URL,
    jwksUrl: "https://cilogon.org/oauth2/certs",
    issuerUrl: "https://cilogon.org",
    get redirectUri() {
      const baseUrl = config.getBaseUrl();
      const appPath = config.getAppPath();
      return `${baseUrl}${appPath}/auth/callback/cilogon`;
    },
    usePkce: false, // Switch to client_secret flow instead of PKCE
  },

  // ORCID - Using sandbox environment for testing
  orcid: {
    clientId: import.meta.env.VITE_ORCID_CLIENT_ID, // Updated with proper ORCID client ID
    clientSecret: import.meta.env.VITE_ORCID_CLIENT_SECRET, // Client secret for token exchange
    issuerUrl: "https://orcid.org",
    authUrl: "https://orcid.org/oauth/authorize",
    tokenUrl: import.meta.env.VITE_ORCID_TOKEN_URL, // Updated with proper ORCID token URL
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
    usePkce: false, // Switch to client_secret flow instead of PKCE
  },

  // Connection services (used after obtaining identity tokens)
  connections: {
    fabric: {
      cmBase: "https://cm.fabric-testbed.net",
      createPath: "/tokens/create",
      refreshPath: "/tokens/refresh",
      projectId: "1ecd9d6a-7701-40fa-b78e-b2293c9526ed",
      projectName: "AtlanticWave-SDX",
      tokenPath: "/home/fabric/.tokens.json",
    },
    meican: {
      baseUrl: "https://meican.rnp.br",
      authUrl: "https://meican.rnp.br/auth/login",
      apiUrl: "https://meican.rnp.br/api/v1",
    },
  },
} as const;

export type Provider = "cilogon" | "orcid";
