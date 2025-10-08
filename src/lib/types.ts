export type Provider = "cilogon" | "orcid";

export interface TokenData {
  id_token?: string;
  access_token?: string;
  refresh_token?: string;
  expires_in: number;
  issued_at: number;
  provider?: Provider;
  token_type?: string;
  scope?: string;
}

export interface TokenClaims {
  sub?: string;
  iss?: string;
  exp?: number;
  email?: string;
  name?: string;
  [key: string]: any;
}

export interface DeviceFlowResponse {
  device_code: string;
  user_code: string;
  verification_uri: string;
  verification_uri_complete?: string;
  expires_in: number;
  interval: number;
}

export interface TokenResponse {
  access_token?: string;
  id_token?: string;
  refresh_token?: string;
  expires_in?: number;
  token_type?: string;
  scope?: string;
}

export interface BackendPayload {
  provider: Provider;
  id_token: string;
  refresh_token?: string;
  expires_in: number;
  issued_at: number;
  token_format: "jwt";
  claims_hint: TokenClaims;
}

export type AuthState = {
  selectedProvider?: Provider;
  tokens: Partial<Record<Provider, TokenData>>;
};

export type DeviceFlowState = {
  status: "idle" | "requesting" | "polling" | "pending" | "success" | "complete" | "error" | "window_closed";
  deviceCode?: string;
  userCode?: string;
  verificationUri?: string;
  verificationUriComplete?: string;
  expiresAt?: number;
  interval?: number;
  error?: string;
  token?: TokenData;
  message?: string;
};

// Topology API types
export interface TopologyNode {
  id: string;
  name: string;
  type?: string;
  location?: {
    latitude?: number;
    longitude?: number;
    address?: string;
    iso3166_2_lvl4?: string; // Added for PHP compatibility
  };
  ports?: any[]; // Ports are directly on the node, not in properties
  private_attributes?: any[];
  short_name?: string;
  properties?: {
    status?: string;
    connections?: number;
    [key: string]: any;
  };
}

export interface TopologyLink {
  id: string;
  name?: string;
  ports?: string[]; // Ports are directly on the link, not in properties
  bandwidth?: number;
  latency?: number;
  availability?: number;
  packet_loss?: number;
  residual_bandwidth?: number;
  state?: string;
  status?: string;
  timestamp?: string;
  private_attributes?: string;
  short_name?: string;
  measurement_period?: string;
  // Legacy fields for compatibility
  source?: string;
  target?: string;
  type?: string;
  properties?: {
    [key: string]: any;
  };
}

export interface TopologyResponse {
  nodes: TopologyNode[];
  links: TopologyLink[];
  metadata?: {
    version?: string;
    timestamp?: string;
    description?: string;
  };
}

export interface ApiError {
  error: string;
  message?: string;
  details?: any;
}