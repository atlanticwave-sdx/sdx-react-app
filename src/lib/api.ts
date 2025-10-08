import { config } from "@/lib/config";
import { TopologyResponse, ApiError } from "@/lib/types";
import { TokenStorage } from "@/lib/token-storage";

/**
 * API service for SDX topology and other endpoints
 */
export class ApiService {
  private static getAuthToken(): string | null {
    // Try to get id_token from either ORCID or CILogon
    const orcidToken = TokenStorage.getToken("orcid");
    const cilogonToken = TokenStorage.getToken("cilogon");
    
    // Prefer the most recent valid token
    const tokens = [orcidToken, cilogonToken].filter(token => 
      token && TokenStorage.isTokenValid(token)
    );
    
    if (tokens.length === 0) {
      console.warn('No valid tokens found for API authentication');
      return null;
    }
    
    // Sort by issued_at to get the most recent
    const mostRecentToken = tokens.sort((a, b) => b!.issued_at - a!.issued_at)[0];
    
    // Return id_token for Bearer authentication
    if (mostRecentToken?.id_token) {
      console.log('Using id_token for API authentication from provider:', mostRecentToken.provider);
      return mostRecentToken.id_token;
    }
    
    console.warn('No id_token found in valid tokens');
    return null;
  }

  private static async makeAuthenticatedRequest<T>(
    endpoint: string, 
    options: RequestInit = {}
  ): Promise<T> {
    const token = this.getAuthToken();
    
    // Temporarily disable authentication requirement for testing
    // if (!token) {
    //   throw new Error('No authentication token available. Please login first.');
    // }

    const url = `${config.api.baseUrl}${endpoint}`;
    
    const headers: HeadersInit = {
      'Content-Type': 'application/json',
      ...(token && { 'Authorization': `Bearer ${token}` }), // Only add auth if token exists
      ...options.headers,
    };

    console.log(`Making API request to: ${url}`);
    console.log('Request headers:', headers);
    console.log('Request options:', options);
    
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          ...(token && { 'Authorization': `Bearer ${token}` }),
        },
      });

      console.log(`API response status: ${response.status}`);
      console.log(`API response headers:`, Object.fromEntries(response.headers.entries()));

      if (!response.ok) {
        let errorMessage = `HTTP ${response.status}: ${response.statusText}`;
        
        try {
          // Read response body only once
          const responseText = await response.text();
          console.log('Error response text:', responseText);
          
          // Try to parse as JSON
          const errorData = JSON.parse(responseText) as ApiError;
          errorMessage = errorData.message || errorData.error || errorMessage;
          console.log('Error response data:', errorData);
        } catch (parseError) {
          console.log('Could not parse error response as JSON:', parseError);
          // errorMessage already contains the response text or default message
        }
        
        throw new Error(errorMessage);
      }

      const data = await response.json();
      console.log('API response received successfully, data length:', JSON.stringify(data).length);
      return data as T;
      
    } catch (error) {
      console.error('API request failed with error:', error);
      if (error instanceof TypeError) {
        console.error('This might be a CORS or network connectivity issue');
      }
      throw error;
    }
  }

  /**
   * Fetch network topology data
   */
  static async getTopology(): Promise<TopologyResponse> {
    const backendResponse = await this.makeAuthenticatedRequest<{
      success: boolean;
      data: TopologyResponse;
      timestamp: string;
    }>(config.api.endpoints.topology);
    
    // Extract the topology data from the backend response wrapper
    return backendResponse.data;
  }

  /**
   * Check if user has valid authentication for API calls
   */
  static hasValidAuth(): boolean {
    return this.getAuthToken() !== null;
  }

  /**
   * Get the current authentication provider
   */
  static getAuthProvider(): string | null {
    const orcidToken = TokenStorage.getToken("orcid");
    const cilogonToken = TokenStorage.getToken("cilogon");
    
    const tokens = [
      { token: orcidToken, provider: 'orcid' },
      { token: cilogonToken, provider: 'cilogon' }
    ].filter(({ token }) => token && TokenStorage.isTokenValid(token));
    
    if (tokens.length === 0) return null;
    
    // Return the most recent provider
    const mostRecent = tokens.sort((a, b) => 
      b.token!.issued_at - a.token!.issued_at
    )[0];
    
    return mostRecent.provider;
  }
}