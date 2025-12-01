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

  /**
   * Create a new L2VPN connection
   */
  static async createL2VPN(requestData: any): Promise<any> {
    const token = this.getAuthToken();

    if (!token) {
      throw new Error('No authentication token available. Please login first.');
    }

    const url = `${config.api.baseUrl}/l2vpn/1.0`;

    console.log('Creating L2VPN with request:', requestData);
    console.log('POST URL:', url);

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify(requestData),
      });

      console.log(`L2VPN API response status: ${response.status}`);

      // Read response text first
      const responseText = await response.text();
      console.log('L2VPN response text:', responseText);

      let data;
      try {
        data = JSON.parse(responseText);
      } catch (parseError) {
        throw new Error(`Invalid JSON response: ${responseText}`);
      }

      // Check if response is not OK OR if the data contains an error field
      if (!response.ok || data.error || data.status === 'error') {
        const errorMessage = data.error || data.reason || data.message || `HTTP ${response.status}: ${response.statusText}`;
        console.log('Error response data:', data);

        // Throw error with full response data
        const error = new Error(errorMessage) as any;
        error.responseData = data;
        throw error;
      }

      console.log('L2VPN created successfully:', data);
      return data;

    } catch (error) {
      console.error('L2VPN creation failed with error:', error);
      if (error instanceof TypeError) {
        console.error('This might be a CORS or network connectivity issue');
      }
      throw error;
    }
  }

  /**
   * Get list of L2VPN connections
   */
  static async getL2VPNs(): Promise<any[]> {
    const token = this.getAuthToken();

    if (!token) {
      throw new Error('No authentication token available. Please login first.');
    }

    // Use the backend proxy endpoint to avoid CORS issues
    const url = `${config.api.baseUrl}/l2vpn/1.0`;

    console.log('Fetching L2VPNs from:', url);

    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      });

      console.log(`L2VPN list API response status: ${response.status}`);

      // Read response text first
      const responseText = await response.text();
      console.log('L2VPN list response text:', responseText);

      let data;
      try {
        data = JSON.parse(responseText);
      } catch (parseError) {
        throw new Error(`Invalid JSON response: ${responseText}`);
      }

      // Check if response is not OK OR if the data contains an error field
      if (!response.ok || data.error || data.status === 'error') {
        const errorMessage = data.error || data.reason || data.message || `HTTP ${response.status}: ${response.statusText}`;
        console.log('Error response data:', data);

        // Throw error with full response data
        const error = new Error(errorMessage) as any;
        error.responseData = data;
        throw error;
      }

      // Handle different response formats:
      // 1. Array response
      // 2. Object with l2vpns/data properties
      // 3. Object with UUID keys (convert to array)
      let l2vpns: any[] = [];
      
      if (Array.isArray(data)) {
        l2vpns = data;
      } else if (data.l2vpns || data.data) {
        l2vpns = data.l2vpns || data.data || [];
      } else if (typeof data === 'object' && data !== null) {
        // Convert object with UUID keys to array
        // Each value should have a service_id or use the key as id
        l2vpns = Object.entries(data).map(([key, value]: [string, any]) => ({
          ...value,
          id: value.service_id || key,
          uuid: value.service_id || key,
        }));
      }
      
      console.log(`Fetched ${l2vpns.length} L2VPNs successfully`);
      return l2vpns;

    } catch (error) {
      console.error('L2VPN list fetch failed with error:', error);
      if (error instanceof TypeError) {
        console.error('This might be a CORS or network connectivity issue');
      }
      throw error;
    }
  }
}