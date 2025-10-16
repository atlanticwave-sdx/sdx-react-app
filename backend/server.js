const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
const PORT = 3003;

// Enable CORS for frontend
app.use(cors({
  origin: ['http://127.0.0.1:5002', 'http://localhost:5002', 'http://127.0.0.1:5000', 'http://localhost:5000', 'http://127.0.0.1:5173', 'http://localhost:5173'],
  credentials: true
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ORCID OAuth configuration
const ORCID_CONFIG = {
  clientId: 'APP-6U5WZH9AC4EYDVAD',
  clientSecret: 'c839f6ee-8991-4b4e-9ae3-aab528adc22c',
  tokenUrl: 'https://orcid.org/oauth/token'
};

// CILogon OAuth configuration
const CILOGON_CONFIG = {
  clientId: 'cilogon:/client_id/49ffba66ee294f1a9530301d2a281c74',
  clientSecret: 'pKdqDGRvbmQOdRgA2e-Ceh05xyFNN9sIYtGZs3s4Ym6iygdyX-qKynS4cyMS1VGZmCqGsp9fEFMwEh4HS4PbIQ',
  tokenUrl: 'https://cilogon.org/oauth2/token'
};

// SDX API configuration
const SDX_API_CONFIG = {
  baseUrl: 'https://sdxapi.atlanticwave-sdx.ai/production',
  endpoints: {
    topology: '/topology'
  }
};

// OAuth token exchange endpoint
app.post('/oauth/exchange', async (req, res) => {
  try {
    console.log('OAuth exchange request:', req.body);
    
    const { provider, code, state, redirect_uri, code_verifier } = req.body;
    
    if (!provider || !code) {
      return res.status(400).json({
        error: 'Missing required parameters: provider and code'
      });
    }
    
    if (provider !== 'orcid' && provider !== 'cilogon') {
      return res.status(400).json({
        error: 'Only ORCID and CILogon providers are supported'
      });
    }
    
    let response;
    let providerName;
    
    if (provider === 'orcid') {
      // Prepare token exchange request for ORCID
      const params = new URLSearchParams({
        client_id: ORCID_CONFIG.clientId,
        client_secret: ORCID_CONFIG.clientSecret,
        grant_type: 'authorization_code',
        redirect_uri: redirect_uri,
        code: code,
      });
      
      console.log('Making request to ORCID token endpoint...');
      console.log('Request params:', params.toString());
      
      // Exchange code for token with ORCID
      response = await fetch(ORCID_CONFIG.tokenUrl, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: params.toString(),
      });
      
      providerName = 'ORCID';
    } else if (provider === 'cilogon') {
      // CILogon requires PKCE flow - check for code_verifier
      if (!code_verifier) {
        return res.status(400).json({
          error: 'Missing code_verifier for CILogon PKCE flow'
        });
      }
      
      // Prepare token exchange request for CILogon with PKCE
      const params = new URLSearchParams({
        client_id: CILOGON_CONFIG.clientId,
        client_secret: CILOGON_CONFIG.clientSecret,
        grant_type: 'authorization_code',
        redirect_uri: redirect_uri,
        code: code,
        code_verifier: code_verifier, // Required for PKCE
      });
      
      console.log('Making request to CILogon token endpoint...');
      console.log('Request params:', params.toString());
      
      // Exchange code for token with CILogon
      response = await fetch(CILOGON_CONFIG.tokenUrl, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: params.toString(),
      });
      
      providerName = 'CILogon';
    }
    
    console.log(`${providerName} response status:`, response.status);
    
    const responseText = await response.text();
    console.log(`${providerName} response body:`, responseText);
    
    if (!response.ok) {
      return res.status(response.status).json({
        error: `${providerName} token exchange failed`,
        details: responseText,
        status: response.status
      });
    }
    
    let tokenData;
    try {
      tokenData = JSON.parse(responseText);
    } catch (parseError) {
      return res.status(500).json({
        error: 'Invalid JSON response from ORCID',
        details: responseText
      });
    }
    
    console.log('Token exchange successful:', tokenData);
    
    // Return the token data to frontend
    res.json({
      success: true,
      provider: provider,
      tokenData: tokenData,
      exchangedAt: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('OAuth exchange error:', error);
    res.status(500).json({
      error: 'Internal server error during token exchange',
      message: error.message
    });
  }
});

// =============================================================================
// SDX API ENDPOINTS
// =============================================================================

// Middleware to validate Bearer token (optional for now)
const validateToken = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (authHeader && authHeader.startsWith('Bearer ')) {
    const token = authHeader.substring(7);
    // TODO: Add JWT validation here if needed
    req.token = token;
    console.log('Request authenticated with token:', token.substring(0, 20) + '...');
  } else {
    console.log('Request without authentication token');
  }
  next(); // Continue regardless for now
};

// Topology endpoint
app.get('/api/topology', validateToken, async (req, res) => {
  try {
    console.log('Topology request received');
    
    const topologyUrl = `${SDX_API_CONFIG.baseUrl}${SDX_API_CONFIG.endpoints.topology}`;
    console.log('Fetching topology from:', topologyUrl);
    
    const response = await fetch(topologyUrl, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        ...(req.token && { 'Authorization': `Bearer ${req.token}` }),
      },
    });
    
    console.log('Topology API response status:', response.status);
    
    if (!response.ok) {
      console.error('Topology API error:', response.status, response.statusText);
      return res.status(response.status).json({
        error: 'Failed to fetch topology data',
        details: response.statusText,
        status: response.status
      });
    }
    
    const topologyData = await response.json();
    console.log('Topology data received, nodes:', topologyData.nodes?.length, 'links:', topologyData.links?.length);
    
    // Return the topology data
    res.json({
      success: true,
      data: topologyData,
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    console.error('Topology endpoint error:', error);
    res.status(500).json({
      error: 'Internal server error while fetching topology',
      message: error.message
    });
  }
});

// General SDX API proxy endpoint
app.all('/api/sdx/*', validateToken, async (req, res) => {
  try {
    const sdxPath = req.path.replace('/api/sdx', '');
    const sdxUrl = `${SDX_API_CONFIG.baseUrl}${sdxPath}`;
    
    console.log(`Proxying ${req.method} request to:`, sdxUrl);
    
    const response = await fetch(sdxUrl, {
      method: req.method,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        ...(req.token && { 'Authorization': `Bearer ${req.token}` }),
      },
      ...(req.method !== 'GET' && req.method !== 'HEAD' && { body: JSON.stringify(req.body) }),
    });
    
    console.log(`SDX API response status: ${response.status}`);
    
    const responseData = await response.json();
    
    res.status(response.status).json(responseData);
    
  } catch (error) {
    console.error('SDX API proxy error:', error);
    res.status(500).json({
      error: 'Internal server error while proxying SDX API request',
      message: error.message
    });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({ 
    message: 'SDX OAuth Backend Server',
    endpoints: {
      'POST /oauth/exchange': 'Exchange OAuth authorization code for tokens',
      'GET /health': 'Health check'
    }
  });
});

app.listen(PORT, () => {
  console.log(`🚀 SDX OAuth Backend Server running on http://localhost:${PORT}`);
  console.log(`📝 Endpoints:`);
  console.log(`   POST http://localhost:${PORT}/oauth/exchange`);
  console.log(`   GET  http://localhost:${PORT}/health`);
  console.log(`🔗 CORS enabled for: http://127.0.0.1:5002, http://localhost:5002`);
});

module.exports = app;