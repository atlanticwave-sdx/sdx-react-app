const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
const PORT = 3001;

// Enable CORS for frontend
app.use(cors({
  origin: ['http://127.0.0.1:5002', 'http://localhost:5002', 'http://127.0.0.1:5173', 'http://localhost:5173'],
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

// OAuth token exchange endpoint
app.post('/oauth/exchange', async (req, res) => {
  try {
    console.log('OAuth exchange request:', req.body);
    
    const { provider, code, state, redirect_uri } = req.body;
    
    if (!provider || !code) {
      return res.status(400).json({
        error: 'Missing required parameters: provider and code'
      });
    }
    
    if (provider !== 'orcid') {
      return res.status(400).json({
        error: 'Only ORCID provider is currently supported'
      });
    }
    
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
    const response = await fetch(ORCID_CONFIG.tokenUrl, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: params.toString(),
    });
    
    console.log('ORCID response status:', response.status);
    
    const responseText = await response.text();
    console.log('ORCID response body:', responseText);
    
    if (!response.ok) {
      return res.status(response.status).json({
        error: 'ORCID token exchange failed',
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
      provider: 'orcid',
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