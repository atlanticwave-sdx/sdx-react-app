import { TokenStorage } from "@/lib/token-storage";
import { Provider, config } from "@/lib/config";

export interface UserSession {
  isAuthenticated: boolean;
  provider?: Provider;
  authenticatedAt?: number;
  lastActivity?: number;
  emailVerified?: boolean;
  verifiedEmail?: string;
}

export class SessionManager {
  private static SESSION_KEY = "sdx_user_session";
  private static SESSION_TIMEOUT = 24 * 60 * 60 * 1000; // 24 hours

  /**
   * Check if user has a valid session
   */
  static isAuthenticated(): boolean {
    console.log("SessionManager.isAuthenticated() called");
    const session = this.getSession();
    console.log("Current session:", session);

    if (!session.isAuthenticated) {
      console.log("Session not authenticated");
      return false;
    }

    // Check if session has expired
    if (this.isSessionExpired()) {
      console.log("Session expired, clearing...");
      this.clearSession();
      return false;
    }

    // Check if user has valid tokens
    const hasTokens = this.hasValidTokens();
    console.log("Has valid tokens:", hasTokens);

    if (!hasTokens) {
      console.log("No valid tokens found, clearing session...");
      this.clearSession();
      return false;
    }

    console.log("Authentication check passed");
    return true;
  }

  /**
   * Check if user has verified their email
   */
  static isEmailVerified(): boolean {
    console.log("SessionManager.isEmailVerified() called");
    const session = this.getSession();
    console.log("Email verification status:", session.emailVerified);
    return session.emailVerified === true;
  }

  /**
   * Mark email as verified
   */
  static setEmailVerified(email: string): void {
    const session = this.getSession();
    session.emailVerified = true;
    session.verifiedEmail = email;
    localStorage.setItem(this.SESSION_KEY, JSON.stringify(session));
    console.log("Email verified and stored:", email);
  }

  /**
   * Get verified email address
   */
  static getVerifiedEmail(): string | null {
    const session = this.getSession();
    return session.verifiedEmail || null;
  }

  /**
   * Clear email verification status
   */
  static clearEmailVerification(): void {
    const session = this.getSession();
    if (session.isAuthenticated) {
      session.emailVerified = false;
      session.verifiedEmail = undefined;
      localStorage.setItem(this.SESSION_KEY, JSON.stringify(session));
      console.log("Email verification cleared");
    }
  }

  /**
   * Check if user is fully authenticated (OAuth + Email)
   */
  static isFullyAuthenticated(): boolean {
    return this.isAuthenticated() && this.isEmailVerified();
  }

  /**
   * Get current session
   */
  static getSession(): UserSession {
    try {
      const stored = localStorage.getItem(this.SESSION_KEY);
      if (!stored) {
        return { isAuthenticated: false };
      }
      return JSON.parse(stored);
    } catch (error) {
      console.error("Error reading session:", error);
      return { isAuthenticated: false };
    }
  }

  /**
   * Create a new session after successful authentication
   */
  static createSession(provider: Provider): void {
    const session: UserSession = {
      isAuthenticated: true,
      provider,
      authenticatedAt: Date.now(),
      lastActivity: Date.now(),
    };

    localStorage.setItem(this.SESSION_KEY, JSON.stringify(session));
    console.log("Session created for provider:", provider);
  }

  /**
   * Update last activity timestamp
   */
  static updateActivity(): void {
    const session = this.getSession();
    if (session.isAuthenticated) {
      session.lastActivity = Date.now();
      localStorage.setItem(this.SESSION_KEY, JSON.stringify(session));
    }
  }

  /**
   * Clear session and all tokens
   */
  static clearSession(): void {
    localStorage.removeItem(this.SESSION_KEY);
    TokenStorage.clearAllTokens();
    sessionStorage.removeItem("email_verified");
    sessionStorage.removeItem("verified_email");
    console.log("Session cleared");
  }

  /**
   * Logout with provider-specific cleanup
   */
  static logout(): void {
    const session = this.getSession();
    const provider = session.provider;

    // Clear local session and tokens first
    this.clearSession();

    // Handle provider-specific logout
    if (provider === "orcid") {
      // For ORCID, we'll make a request to their logout endpoint and then redirect
      const logoutUrl = config.orcid.logoutUrl;
      const postLogoutRedirect = config.orcid.postLogoutRedirectUri;

      console.log("Destroying ORCID session and redirecting to homepage");

      // Make a request to ORCID logout endpoint in the background
      fetch(logoutUrl, {
        method: "GET",
        credentials: "include",
        mode: "no-cors",
      })
        .catch(() => {
          // Ignore any errors from the logout request
          console.log(
            "ORCID logout request completed (may have CORS error, but that's expected)"
          );
        })
        .finally(() => {
          // Always redirect to homepage regardless of logout request result
          window.location.href = postLogoutRedirect;
        });
    } else if (provider === "cilogon") {
      // CILogon logout - could be implemented later if needed
      console.log("CILogon logout - local session cleared");
      // Redirect to homepage for non-ORCID providers
      window.location.href = config.orcid.postLogoutRedirectUri;
    } else {
      // Default case - redirect to homepage
      window.location.href = config.orcid.postLogoutRedirectUri;
    }
  }

  /**
   * Check if session has expired
   */
  private static isSessionExpired(): boolean {
    const session = this.getSession();
    if (!session.lastActivity) return true;

    const timeSinceActivity = Date.now() - session.lastActivity;
    return timeSinceActivity > this.SESSION_TIMEOUT;
  }

  /**
   * Check if user has any valid tokens
   */
  private static hasValidTokens(): boolean {
    const cilogon = TokenStorage.getToken("cilogon");
    const orcid = TokenStorage.getToken("orcid");

    console.log("Token check - CILogon:", cilogon ? "exists" : "missing");
    console.log("Token check - ORCID:", orcid ? "exists" : "missing");

    const hasValidCilogon = cilogon && TokenStorage.isTokenValid(cilogon);
    const hasValidOrcid = orcid && TokenStorage.isTokenValid(orcid);

    console.log("Valid tokens - CILogon:", hasValidCilogon);
    console.log("Valid tokens - ORCID:", hasValidOrcid);

    return !!(hasValidCilogon || hasValidOrcid);
  }

  /**
   * Get the authenticated provider
   */
  static getAuthenticatedProvider(): Provider | null {
    const session = this.getSession();
    if (!session.isAuthenticated) return null;

    // If session doesn't have provider info, try to determine from tokens
    if (!session.provider) {
      const cilogon = TokenStorage.getToken("cilogon");
      const orcid = TokenStorage.getToken("orcid");

      if (cilogon && TokenStorage.isTokenValid(cilogon)) return "cilogon";
      if (orcid && TokenStorage.isTokenValid(orcid)) return "orcid";
    }

    return session.provider || null;
  }

  /**
   * Get session duration in minutes
   */
  static getSessionDuration(): number {
    const session = this.getSession();
    if (!session.authenticatedAt) return 0;

    return Math.floor((Date.now() - session.authenticatedAt) / (1000 * 60));
  }
}
