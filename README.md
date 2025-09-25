# SDX MEICAN React Application

A modern React-based replacement for the PHP MEICAN SDX topology visualization and connection management system.

## Features

- **Authentication**: OAuth integration with ORCID and CILogon
- **Topology Visualization**: Interactive Leaflet maps showing network topology
- **Connection Management**: Create, edit, and manage L2VPN connections
- **Auto-refresh**: Real-time topology updates
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Frontend**: React 18 + TypeScript
- **Build Tool**: Vite
- **Routing**: React Router v6
- **Maps**: Leaflet + React-Leaflet
- **HTTP Client**: Axios
- **Styling**: Tailwind CSS (to be added)

## Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── auth/           # Authentication-related components
│   ├── topology/       # Topology visualization components
│   ├── connections/    # Connection management components
│   └── common/         # Shared components
├── contexts/           # React contexts for state management
├── services/           # API service layer
├── types/             # TypeScript type definitions
├── utils/             # Utility functions
├── hooks/             # Custom React hooks
└── pages/             # Page components
```

## Setup Instructions

### Prerequisites

- Node.js 18+ and npm
- Access to a running MEICAN backend instance
- ORCID and/or CILogon OAuth application credentials

After cloning the repository, follow these steps:

  1. Install dependencies:
  npm install --legacy-peer-deps
  2. Start the development server:
  npm run dev
  3. Access the application:
  Open your browser and navigate to
  http://localhost:5173

  Optional steps:

  4. Build for production:
  npm run build
  5. Preview production build:
  npm run preview

  Notes:
  - The --legacy-peer-deps flag is required due to
  React version compatibility with react-leaflet
  - The app will run on port 5173 by default (Vite's
  default port)
  - Hot reload is enabled, so changes will
  automatically refresh the browser