import { TokenData, TokenClaims } from "@/lib/types";

const TOKEN_KEYS = {
  cilogon: "auth.cilogon",
  orcid: "auth.orcid"
} as const;

export class TokenStorage {
  static getToken(provider: keyof typeof TOKEN_KEYS): TokenData | null {
    try {
      const key = TOKEN_KEYS[provider];
      const stored = localStorage.getItem(key);
      if (!stored) return null;
      return JSON.parse(stored);
    } catch (error) {
      return null;
    }
  }

  static setToken(provider: keyof typeof TOKEN_KEYS, token: TokenData): void {
    const key = TOKEN_KEYS[provider];
    console.log(`TokenStorage.setToken(${provider}):`, { key, token });
    localStorage.setItem(key, JSON.stringify(token));
    console.log(`TokenStorage.setToken(${provider}) completed`);
  }

  static removeToken(provider: keyof typeof TOKEN_KEYS): void {
    localStorage.removeItem(TOKEN_KEYS[provider]);
  }

  static clearAllTokens(): void {
    Object.values(TOKEN_KEYS).forEach(key => {
      localStorage.removeItem(key);
    });
  }

  static isTokenValid(token: TokenData | null): boolean {
    console.log('TokenStorage.isTokenValid called with:', token);
    
    if (!token) {
      console.log('Token is null/undefined');
      return false;
    }
    
    if (!token.issued_at || !token.expires_in) {
      console.log('Token missing issued_at or expires_in:', { issued_at: token.issued_at, expires_in: token.expires_in });
      return false;
    }
    
    if (!token.access_token && !token.id_token) {
      console.log('Token missing both access_token and id_token');
      return false;
    }
    
    const now = Math.floor(Date.now() / 1000);
    const expiresAt = token.issued_at + token.expires_in;
    const isValid = expiresAt > now;
    
    console.log('Token validation:', {
      now,
      issued_at: token.issued_at,
      expires_in: token.expires_in,
      expiresAt,
      timeLeft: expiresAt - now,
      isValid
    });
    
    return isValid;
  }

  static getTokenExpiryDate(token: TokenData): Date {
    return new Date((token.issued_at + token.expires_in) * 1000);
  }

  static getTimeUntilExpiry(token: TokenData): number {
    const now = Math.floor(Date.now() / 1000);
    const expiresAt = token.issued_at + token.expires_in;
    return Math.max(0, expiresAt - now);
  }

  static isTokenNearExpiry(token: TokenData, warningMinutes: number = 5): boolean {
    const timeUntilExpiry = this.getTimeUntilExpiry(token);
    return timeUntilExpiry <= (warningMinutes * 60) && timeUntilExpiry > 0;
  }

  static canRefreshToken(token: TokenData): boolean {
    return !!token.refresh_token;
  }

  static formatTimeUntilExpiry(token: TokenData): string {
    const seconds = this.getTimeUntilExpiry(token);
    if (seconds <= 0) return 'Expired';
    
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;
    
    if (hours > 0) {
      return `${hours}h ${minutes}m`;
    } else if (minutes > 0) {
      return `${minutes}m ${remainingSeconds}s`;
    } else {
      return `${remainingSeconds}s`;
    }
  }
}

export function decodeJWT(token: string): any {
  try {
    const parts = token.split('.');
    if (parts.length !== 3) return null;
    
    const payload = parts[1];
    const decoded = atob(payload.replace(/-/g, '+').replace(/_/g, '/'));
    return JSON.parse(decoded);
  } catch {
    return null;
  }
}

/**
 * Check if email validation can be skipped based on JWT claims
 */
export function canSkipEmailValidation(token: TokenData): { canSkip: boolean; email?: string; eppn?: string } {
  if (!token.id_token) {
    return { canSkip: false };
  }
  
  const claims = decodeJWT(token.id_token);
  if (!claims) {
    return { canSkip: false };
  }
  
  const email = claims.email || claims.mail;
  const eppn = claims.eppn;
  
  console.log('JWT Claims check:', { email, eppn, claims });
  
  // Can skip if both eppn and email are present
  if (eppn && email) {
    return { canSkip: true, email, eppn };
  }
  
  return { canSkip: false, email, eppn };
}

/**
 * Calculate ownership hash from JWT sub field
 * PHP equivalent:
 * $sub = $response_arr['sub'];
 * $subExtract = str_replace('http://cilogon.org', '', $sub);
 * $subExtract = preg_replace('/server[A-Z]/', 'serverX', $subExtract);
 * $hashedString = hash('sha256', $subExtract);
 * $base64Encoded = base64_encode($hashedString);
 * $trimmedOutput = substr($base64Encoded, 0, 16);
 */
export async function calculateOwnership(sub: string): Promise<string> {
  // Remove 'http://cilogon.org' from sub
  let subExtract = sub.replace('http://cilogon.org', '');

  // Replace serverA, serverB, etc. with serverX
  subExtract = subExtract.replace(/server[A-Z]/g, 'serverX');

  // Hash with SHA-256
  const encoder = new TextEncoder();
  const data = encoder.encode(subExtract);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);

  // Convert hash to hex string
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashedString = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

  // Base64 encode the hex hash
  const base64Encoded = btoa(hashedString);

  // Get first 16 characters
  const trimmedOutput = base64Encoded.substring(0, 16);

  return trimmedOutput;
}