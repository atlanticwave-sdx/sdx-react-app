import { config } from "@/lib/config";
import { TokenData, TokenResponse } from "@/lib/types";
import { TokenStorage } from "@/lib/token-storage";
import { authenticateWithPopup } from "@/lib/auth-popup";

function generateCodeVerifier(): string {
  const array = new Uint8Array(32);
  crypto.getRandomValues(array);
  return btoa(String.fromCharCode(...array))
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
}

async function generateCodeChallenge(verifier: string): Promise<string> {
  const encoder = new TextEncoder();
  const data = encoder.encode(verifier);
  const hash = await crypto.subtle.digest('SHA-256', data);
  return btoa(String.fromCharCode(...new Uint8Array(hash)))
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
}

export class ORCIDProvider {
  // Generate auth URL for ORCID OAuth flow
  async getAuthUrl(): Promise<string> {
    const state = crypto.randomUUID();

    // Store state for validation (no PKCE needed with client_secret flow)
    sessionStorage.setItem('orcid_state', state);

    const params = new URLSearchParams({
      response_type: 'code',
      client_id: config.orcid.clientId,
      redirect_uri: config.orcid.redirectUri,
      scope: config.orcid.scope,
      state,
    });

    return `${config.orcid.authUrl}?${params}`;
  }

  async startAuthenticationPopup(): Promise<TokenData> {
    const authUrl = await this.getAuthUrl();
    
    console.log('Opening ORCID authentication window...');
    
    // Open the actual ORCID OAuth URL in a new window
    const popup = window.open(
      authUrl,
      'orcid_auth',
      'width=900,height=700,scrollbars=yes,resizable=yes,status=yes,location=yes,toolbar=yes,menubar=yes'
    );

    if (!popup) {
      throw new Error('Popup blocked. Please allow popups for this site and try again.');
    }

    // Focus the popup window
    popup.focus();

    // Return a promise that resolves when authentication completes
    return new Promise((resolve, reject) => {
      // Listen for messages from the popup
      const messageHandler = (event: MessageEvent) => {
        // Be more permissive with origins for authentication flow
        console.log('Received ORCID message from origin:', event.origin, 'with data:', event.data);
        
        if (event.data?.type === 'ORCID_AUTH_SUCCESS') {
          window.removeEventListener('message', messageHandler);
          clearInterval(checkClosed);
          popup.close();
          
          const { code, state } = event.data;
          this.exchangeCodeForToken(code, state)
            .then(resolve)
            .catch(reject);
        } else if (event.data?.type === 'ORCID_AUTH_ERROR') {
          window.removeEventListener('message', messageHandler);
          clearInterval(checkClosed);
          popup.close();
          reject(new Error(event.data.error || 'Authentication failed'));
        }
      };
      
      window.addEventListener('message', messageHandler);
      
      // Check if popup is closed every second
      const checkClosed = setInterval(() => {
        if (popup.closed) {
          clearInterval(checkClosed);
          window.removeEventListener('message', messageHandler);
          reject(new Error('Authentication window was closed before completion'));
        }
      }, 1000);

      // Timeout after 10 minutes
      setTimeout(() => {
        clearInterval(checkClosed);
        window.removeEventListener('message', messageHandler);
        if (!popup.closed) {
          popup.close();
        }
        reject(new Error('Authentication timeout. Please try again.'));
      }, 600000);
    });
  }

  async exchangeCodeForToken(code: string, state: string): Promise<TokenData> {
    console.log('ORCID exchangeCodeForToken called with:', { code, state });
    
    const storedState = sessionStorage.getItem('orcid_state');
    const codeVerifier = sessionStorage.getItem('orcid_code_verifier');
    
    console.log('ORCID stored values:', { storedState, codeVerifier: !!codeVerifier });

    if (!storedState || storedState !== state) {
      console.error('ORCID state mismatch:', { storedState, receivedState: state });
      throw new Error('Invalid state parameter');
    }

    if (!codeVerifier) {
      console.error('ORCID code verifier not found in sessionStorage');
      throw new Error('Code verifier not found');
    }

    // Clean up session storage
    sessionStorage.removeItem('orcid_state');
    sessionStorage.removeItem('orcid_code_verifier');

    // Prepare token exchange request
    const params = new URLSearchParams({
      grant_type: 'authorization_code',
      code: code,
      client_id: config.orcid.clientId,
      redirect_uri: config.orcid.redirectUri,
      code_verifier: codeVerifier,
    });

    try {
      console.log('ORCID making token request to:', config.orcid.tokenUrl);
      console.log('ORCID request params:', params.toString());
      
      const response = await fetch(config.orcid.tokenUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: params.toString(),
      });

      console.log('ORCID token response status:', response.status);

      if (!response.ok) {
        const errorText = await response.text();
        console.error('ORCID token exchange error response:', errorText);
        throw new Error(`Token exchange failed: ${response.status} ${response.statusText}`);
      }

      const tokenResponse = await response.json();
      console.log('ORCID token response:', tokenResponse);
      
      // ORCID doesn't provide id_token, so we create a minimal JWT-like structure
      // using the access_token if it's a JWT, or create a basic token
      let idToken = tokenResponse.id_token;
      if (!idToken && tokenResponse.access_token) {
        // Check if access_token is a JWT (has 3 parts separated by dots)
        if (tokenResponse.access_token.split('.').length === 3) {
          idToken = tokenResponse.access_token;
        } else {
          // Create a minimal JWT-like token for ORCID
          const header = btoa(JSON.stringify({ alg: "none", typ: "JWT" }));
          const payload = btoa(JSON.stringify({
            iss: "https://orcid.org",
            sub: "orcid-user",
            aud: config.orcid.clientId,
            exp: Math.floor(Date.now() / 1000) + (tokenResponse.expires_in || 3600),
            iat: Math.floor(Date.now() / 1000),
            access_token: tokenResponse.access_token
          }));
          idToken = `${header}.${payload}.`;
        }
      }

      const tokenData: TokenData = {
        id_token: idToken,
        refresh_token: tokenResponse.refresh_token,
        expires_in: tokenResponse.expires_in || 3600,
        issued_at: Math.floor(Date.now() / 1000),
        provider: 'orcid',
      };

      TokenStorage.setToken('orcid', tokenData);
      return tokenData;
    } catch (error) {
      console.error('ORCID token exchange error:', error);
      throw new Error(`Failed to exchange code for token: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  }

  // Static methods for backward compatibility and easier usage
  static initiateLogin = async (): Promise<string> => {
    const provider = new ORCIDProvider();
    return provider.getAuthUrl();
  }

  static handleCallback = async (code: string, state: string): Promise<TokenData> => {
    const provider = new ORCIDProvider();
    return provider.exchangeCodeForToken(code, state);
  }

  static async startAuthenticationPopup(): Promise<TokenData> {
    const provider = new ORCIDProvider();
    return provider.startAuthenticationPopup();
  }
}