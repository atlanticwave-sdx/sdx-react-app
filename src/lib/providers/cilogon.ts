import { config } from "@/lib/config";
import { TokenData, TokenResponse } from "@/lib/types";
import { TokenStorage } from "@/lib/token-storage";
import { authenticateWithPopup } from "@/lib/auth-popup";

// Pure-JS SHA-256 fallback for non-secure contexts (no crypto.subtle)
function rotr32(x: number, n: number): number {
  return (x >>> n) | (x << (32 - n));
}
function sha256Pure(data: Uint8Array): Uint8Array {
  const K = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2,
  ];
  let [h0,h1,h2,h3,h4,h5,h6,h7] = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const msgLen = data.length;
  const bitLen = msgLen * 8;
  const padded = new Uint8Array(Math.ceil((msgLen + 9) / 64) * 64);
  padded.set(data);
  padded[msgLen] = 0x80;
  const dv = new DataView(padded.buffer);
  dv.setUint32(padded.length - 4, bitLen >>> 0, false);
  dv.setUint32(padded.length - 8, Math.floor(bitLen / 0x100000000), false);
  const w = new Uint32Array(64);
  for (let c = 0; c < padded.length; c += 64) {
    const cv = new DataView(padded.buffer, c, 64);
    for (let i = 0; i < 16; i++) w[i] = cv.getUint32(i * 4, false);
    for (let i = 16; i < 64; i++) {
      const s0 = rotr32(w[i-15],7) ^ rotr32(w[i-15],18) ^ (w[i-15]>>>3);
      const s1 = rotr32(w[i-2],17) ^ rotr32(w[i-2],19) ^ (w[i-2]>>>10);
      w[i] = (w[i-16] + s0 + w[i-7] + s1) >>> 0;
    }
    let [a,b,cc,d,e,f,g,h] = [h0,h1,h2,h3,h4,h5,h6,h7];
    for (let i = 0; i < 64; i++) {
      const S1 = rotr32(e,6)^rotr32(e,11)^rotr32(e,25);
      const ch = (e&f)^(~e&g);
      const t1 = (h + S1 + ch + K[i] + w[i]) >>> 0;
      const S0 = rotr32(a,2)^rotr32(a,13)^rotr32(a,22);
      const maj = (a&b)^(a&cc)^(b&cc);
      const t2 = (S0 + maj) >>> 0;
      h=g; g=f; f=e; e=(d+t1)>>>0; d=cc; cc=b; b=a; a=(t1+t2)>>>0;
    }
    h0=(h0+a)>>>0; h1=(h1+b)>>>0; h2=(h2+cc)>>>0; h3=(h3+d)>>>0;
    h4=(h4+e)>>>0; h5=(h5+f)>>>0; h6=(h6+g)>>>0; h7=(h7+h)>>>0;
  }
  const out = new Uint8Array(32);
  const ov = new DataView(out.buffer);
  [h0,h1,h2,h3,h4,h5,h6,h7].forEach((v,i) => ov.setUint32(i*4, v, false));
  return out;
}

export class CILogonProvider {
  private generateState(): string {
    const array = new Uint8Array(32);
    crypto.getRandomValues(array);
    return btoa(String.fromCharCode(...array)).replace(/[+/=]/g, '').substring(0, 43);
  }

  private generateCodeVerifier(): string {
    const array = new Uint8Array(32);
    crypto.getRandomValues(array);
    
    // Convert to string
    let binary = '';
    for (let i = 0; i < array.length; i++) {
      binary += String.fromCharCode(array[i]);
    }
    
    // Generate base64url string with no padding - CRITICAL for PKCE S256
    const base64 = btoa(binary);
    const base64url = base64
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=/g, '') // Remove ALL padding
      .substring(0, 43); // Ensure proper length
    
    console.log('Generated code verifier (no padding):', base64url);
    return base64url;
  }

  private async generateCodeChallenge(verifier: string): Promise<string> {
    const encoder = new TextEncoder();
    const data = encoder.encode(verifier);

    let bytes: Uint8Array;
    if (crypto.subtle) {
      const digest = await crypto.subtle.digest('SHA-256', data);
      bytes = new Uint8Array(digest);
    } else {
      // Fallback for non-secure contexts (plain HTTP on non-localhost)
      bytes = sha256Pure(data);
    }

    let binary = '';
    for (let i = 0; i < bytes.byteLength; i++) {
      binary += String.fromCharCode(bytes[i]);
    }

    const base64url = btoa(binary)
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=/g, '');

    console.log('Generated code challenge (no padding):', base64url);
    return base64url;
  }

  private async getAuthUrl(state: string, codeVerifier: string): Promise<string> {
    const redirectUri = config.cilogon.redirectUri;

    const params = [
      `response_type=code`,
      `client_id=${encodeURIComponent(config.cilogon.clientId)}`,
      `redirect_uri=${encodeURIComponent(redirectUri)}`,
      `scope=${encodeURIComponent(config.cilogon.scope)}`,
      `state=${encodeURIComponent(state)}`,
    ];

    if (config.cilogon.usePkce) {
      const codeChallenge = await this.generateCodeChallenge(codeVerifier);
      params.push(`code_challenge=${encodeURIComponent(codeChallenge)}`);
      params.push(`code_challenge_method=S256`);
    }

    return `https://cilogon.org/authorize?${params.join('&')}`;
  }

  async exchangeCodeForToken(code: string, state: string, codeVerifier: string): Promise<TokenData> {
    let storedState = sessionStorage.getItem('cilogon_state');
    let storedVerifier = codeVerifier;
    
    // If sessionStorage is empty, try to recover from localStorage backup
    if (!storedState) {
      try {
        const backup = localStorage.getItem('cilogon_state_backup');
        if (backup) {
          const parsed = JSON.parse(backup);
          // Only use backup if it's less than 10 minutes old
          if (Date.now() - parsed.timestamp < 600000) {
            storedState = parsed.state;
            storedVerifier = parsed.codeVerifier;
            console.log('Recovered state from localStorage backup');
          } else {
            console.log('Backup state too old, ignoring');
          }
        }
      } catch (e) {
        console.warn('Failed to recover state from backup:', e);
      }
    }
    
    console.log('State validation:', { receivedState: state, storedState, match: state === storedState });
    
    if (!state) {
      throw new Error('Missing state parameter');
    }
    
    if (!storedState) {
      console.warn('No stored state found in sessionStorage or backup. This might be due to browser security or a new session.');
      // Don't fail completely - allow authentication to proceed if we have code and verifier
      if (!code || !storedVerifier) {
        throw new Error('Missing required authentication parameters (state, code, or verifier)');
      }
    } else if (state !== storedState) {
      console.error(`State mismatch: received "${state}", expected "${storedState}"`);
      throw new Error(`Invalid state parameter: received "${state}", expected "${storedState}"`);
    }

    // Clean up stored values after validation
    if (sessionStorage.getItem('cilogon_state')) {
      sessionStorage.removeItem('cilogon_state');
    }
    if (sessionStorage.getItem('cilogon_code_verifier')) {
      sessionStorage.removeItem('cilogon_code_verifier');
    }
    localStorage.removeItem('cilogon_state_backup');

    // Use the same redirect URI from config that was used in the authorization request
    const redirectUri = config.cilogon.redirectUri;

    const body = config.cilogon.usePkce
      ? `grant_type=authorization_code&code=${encodeURIComponent(code)}&redirect_uri=${encodeURIComponent(redirectUri)}&client_id=${encodeURIComponent(config.cilogon.clientId)}&code_verifier=${codeVerifier}`
      : `grant_type=authorization_code&code=${encodeURIComponent(code)}&redirect_uri=${encodeURIComponent(redirectUri)}&client_id=${encodeURIComponent(config.cilogon.clientId)}&client_secret=${encodeURIComponent(config.cilogon.clientSecret)}`;

    try {
      console.log('Token exchange using redirect_uri:', redirectUri);

      const response = await fetch(config.cilogon.tokenUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: body,
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error('CILogon token exchange failed:', {
          status: response.status,
          statusText: response.statusText,
          error: errorText
        });
        throw new Error(`Token exchange failed: ${response.status} ${response.statusText}. ${errorText}`);
      }

      const tokenResponse = await response.json();
      console.log('CILogon token exchange successful:', { has_id_token: !!tokenResponse.id_token, has_access_token: !!tokenResponse.access_token });
      
      const tokenData: TokenData = {
        id_token: tokenResponse.id_token || tokenResponse.access_token,
        refresh_token: tokenResponse.refresh_token,
        expires_in: tokenResponse.expires_in || 3600,
        issued_at: Math.floor(Date.now() / 1000),
        provider: "cilogon",
      };

      TokenStorage.setToken("cilogon", tokenData);
      return tokenData;
    } catch (error) {
      console.error('CILogon token exchange error:', error);
      throw new Error(`Failed to exchange code for token: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  }

  async startAuthenticationPopup(): Promise<TokenData> {
    const state = this.generateState();
    const codeVerifier = this.generateCodeVerifier();
    
    // Store both in sessionStorage and localStorage as backup
    sessionStorage.setItem('cilogon_state', state);
    sessionStorage.setItem('cilogon_code_verifier', codeVerifier);
    localStorage.setItem('cilogon_state_backup', JSON.stringify({ state, codeVerifier, timestamp: Date.now() }));
    
    const authUrl = await this.getAuthUrl(state, codeVerifier);
    
    console.log('Opening CILogon authentication window...');
    console.log('Stored state:', state);
    console.log('Stored verifier preview:', codeVerifier.substring(0, 10) + '...');
    
    // Calculate center position for popup
    const width = 800;
    const height = 600;
    const left = (window.screen.width / 2) - (width / 2);
    const top = (window.screen.height / 2) - (height / 2);
    
    // Open the actual CILogon OAuth URL in a popup window
    const popup = window.open(
      authUrl,
      'cilogon_auth',
      `width=${width},height=${height},left=${left},top=${top},scrollbars=yes,resizable=yes,status=no,location=no,toolbar=no,menubar=no`
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
        console.log('Received message from origin:', event.origin, 'with data:', event.data);
        
        if (event.data?.type === 'CILOGON_AUTH_SUCCESS') {
          window.removeEventListener('message', messageHandler);
          clearInterval(checkClosed);
          clearInterval(fallbackCheck);
          popup.close();
          
          const { code, state: returnedState } = event.data;
          let storedCodeVerifier = sessionStorage.getItem('cilogon_code_verifier');
          
          // Try to recover from backup if missing
          if (!storedCodeVerifier) {
            try {
              const backup = localStorage.getItem('cilogon_state_backup');
              if (backup) {
                const parsed = JSON.parse(backup);
                if (Date.now() - parsed.timestamp < 600000) {
                  storedCodeVerifier = parsed.codeVerifier;
                  console.log('Recovered code verifier from backup');
                }
              }
            } catch (e) {
              console.warn('Failed to recover code verifier from backup:', e);
            }
          }
          
          if (!storedCodeVerifier) {
            reject(new Error('Code verifier not found'));
            return;
          }
          
          console.log('Attempting token exchange with:', { 
            code: code?.substring(0, 10) + '...', 
            state: returnedState, 
            hasCodeVerifier: !!storedCodeVerifier 
          });
          
          this.exchangeCodeForToken(code, returnedState, storedCodeVerifier)
            .then(resolve)
            .catch((error) => {
              console.error('Token exchange failed in popup handler:', error);
              reject(error);
            });
        } else if (event.data?.type === 'CILOGON_AUTH_ERROR') {
          window.removeEventListener('message', messageHandler);
          clearInterval(checkClosed);
          clearInterval(fallbackCheck);
          popup.close();
          reject(new Error(event.data.error || 'Authentication failed'));
        }
      };
      
      window.addEventListener('message', messageHandler);
      
      // Fallback mechanism: check localStorage for auth result
      const fallbackCheck = setInterval(() => {
        try {
          const authResult = localStorage.getItem('cilogon_auth_result');
          if (authResult) {
            const result = JSON.parse(authResult);
            console.log('Found stored auth result:', result);
            // Only process recent results (within 5 minutes)
            if (Date.now() - result.timestamp < 300000) {
              localStorage.removeItem('cilogon_auth_result');
              window.removeEventListener('message', messageHandler);
              clearInterval(checkClosed);
              clearInterval(fallbackCheck);
              
              if (result.type === 'CILOGON_AUTH_SUCCESS') {
                console.log('Processing stored successful auth result');
                let storedCodeVerifier = sessionStorage.getItem('cilogon_code_verifier');
                
                // Try to recover from backup if missing
                if (!storedCodeVerifier) {
                  try {
                    const backup = localStorage.getItem('cilogon_state_backup');
                    if (backup) {
                      const parsed = JSON.parse(backup);
                      if (Date.now() - parsed.timestamp < 600000) {
                        storedCodeVerifier = parsed.codeVerifier;
                        console.log('Recovered code verifier from backup for localStorage fallback');
                      }
                    }
                  } catch (e) {
                    console.warn('Failed to recover code verifier from backup:', e);
                  }
                }
                
                if (!storedCodeVerifier) {
                  console.error('Code verifier missing from sessionStorage');
                  reject(new Error('Code verifier not found'));
                  return;
                }
                
                console.log('Attempting token exchange with stored result:', {
                  hasCode: !!result.code,
                  hasState: !!result.state,
                  hasVerifier: !!storedCodeVerifier
                });
                
                this.exchangeCodeForToken(result.code, result.state, storedCodeVerifier)
                  .then((tokenData) => {
                    console.log('Token exchange successful from localStorage fallback:', tokenData);
                    resolve(tokenData);
                  })
                  .catch((error) => {
                    console.error('Token exchange failed from localStorage fallback:', error);
                    reject(error);
                  });
              } else if (result.type === 'CILOGON_AUTH_ERROR') {
                console.log('Processing stored error auth result:', result.error);
                reject(new Error(result.error || 'Authentication failed'));
              }
            } else {
              console.log('Stored auth result is too old, ignoring');
            }
          }
        } catch (e) {
          console.error('Error checking localStorage fallback:', e);
        }
      }, 1000);
      
      // Check if popup is closed manually (user closed it)
      const checkClosed = setInterval(() => {
        if (popup.closed) {
          // Give more time to check if auth was completed before closing
          setTimeout(() => {
            try {
              const authResult = localStorage.getItem('cilogon_auth_result');
              if (authResult) {
                const result = JSON.parse(authResult);
                if (result.type === 'CILOGON_AUTH_SUCCESS' && Date.now() - result.timestamp < 300000) {
                  console.log('Found completed auth after popup closed');
                  localStorage.removeItem('cilogon_auth_result');
                  window.removeEventListener('message', messageHandler);
                  clearInterval(checkClosed);
                  clearInterval(fallbackCheck);
                  
                  const storedCodeVerifier = sessionStorage.getItem('cilogon_code_verifier');
                  if (!storedCodeVerifier) {
                    // Try backup recovery
                    try {
                      const backup = localStorage.getItem('cilogon_state_backup');
                      if (backup) {
                        const parsed = JSON.parse(backup);
                        if (Date.now() - parsed.timestamp < 600000) {
                          const recoveredVerifier = parsed.codeVerifier;
                          this.exchangeCodeForToken(result.code, result.state, recoveredVerifier)
                            .then(resolve)
                            .catch(reject);
                          return;
                        }
                      }
                    } catch (e) {
                      console.warn('Failed to recover from backup in popup closed handler:', e);
                    }
                    
                    reject(new Error('Code verifier not found'));
                    return;
                  }
                  
                  this.exchangeCodeForToken(result.code, result.state, storedCodeVerifier)
                    .then(resolve)
                    .catch(reject);
                  return;
                }
              }
              
              // If no successful auth found, it was closed manually
              clearInterval(checkClosed);
              clearInterval(fallbackCheck);
              window.removeEventListener('message', messageHandler);
              reject(new Error('Authentication window was closed. If you completed authentication, please wait a moment and use the "Continue" button below.'));
            } catch (e) {
              console.error('Error checking final auth status:', e);
              clearInterval(checkClosed);
              clearInterval(fallbackCheck);
              window.removeEventListener('message', messageHandler);
              reject(new Error('Authentication window was closed. If you completed authentication, please wait a moment and use the "Continue" button below.'));
            }
          }, 5000); // Wait 5 seconds after popup closes to check for auth
        }
      }, 1000);

      // Timeout after 10 minutes
      setTimeout(() => {
        clearInterval(checkClosed);
        clearInterval(fallbackCheck);
        window.removeEventListener('message', messageHandler);
        if (!popup.closed) {
          popup.close();
        }
        reject(new Error('Authentication timeout. Please try again.'));
      }, 600000);
    });
  }

  // Legacy methods for URL-based callback handling
  async handleCallback(): Promise<TokenData> {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');
    const state = urlParams.get('state');
    const error = urlParams.get('error');

    if (error) {
      throw new Error(`CILogon authentication error: ${error}`);
    }

    if (!code || !state) {
      throw new Error('No authorization code received from CILogon');
    }

    const storedCodeVerifier = sessionStorage.getItem('cilogon_code_verifier');
    if (!storedCodeVerifier) {
      throw new Error('Code verifier not found in session storage');
    }

    return await this.exchangeCodeForToken(code, state, storedCodeVerifier);
  }

  async startAuthentication(): Promise<void> {
    const state = this.generateState();
    const codeVerifier = this.generateCodeVerifier();
    
    sessionStorage.setItem('cilogon_state', state);
    sessionStorage.setItem('cilogon_code_verifier', codeVerifier);
    
    const authUrl = await this.getAuthUrl(state, codeVerifier);
    window.location.href = authUrl;
  }

  // Keep static methods for backward compatibility
  static async getAuthUrl(): Promise<string> {
    const provider = new CILogonProvider();
    const state = provider.generateState();
    const codeVerifier = provider.generateCodeVerifier();
    sessionStorage.setItem('cilogon_state', state);
    sessionStorage.setItem('cilogon_code_verifier', codeVerifier);
    return provider.getAuthUrl(state, codeVerifier);
  }

  static handleCallback(): Promise<TokenData> {
    const provider = new CILogonProvider();
    return provider.handleCallback();
  }

  static async startAuthentication(): Promise<void> {
    const provider = new CILogonProvider();
    return provider.startAuthentication();
  }

  static async startAuthenticationPopup(): Promise<TokenData> {
    const provider = new CILogonProvider();
    return provider.startAuthenticationPopup();
  }
}