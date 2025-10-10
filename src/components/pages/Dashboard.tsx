import { useState, useEffect } from "react";
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  Polyline,
} from "react-leaflet";
import { LatLngExpression } from "leaflet";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { toast } from "sonner";
import { TokenData } from "@/lib/types";
import { TokenStorage } from "@/lib/token-storage";
import { NewL2VPNModal, L2VPNData } from "@/components/NewL2VPNModal";
import sdxLogo from "@/assets/images/sdx-logo.svg";
import "@/styles/leaflet.css";

// Fix Leaflet default markers
import L from "leaflet";
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon-2x.png",
  iconUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png",
});

interface DashboardProps {
  onBack: () => void;
  onNavigateToTokens: () => void;
}

interface NetworkNode {
  id: string;
  name: string;
  city: string;
  coordinates: LatLngExpression;
  status: "active" | "inactive" | "maintenance";
  connections: number;
}

interface Connection {
  id: string;
  name: string;
  source: string;
  destination: string;
  type: "L2VPN" | "L3VPN" | "P2P";
  bandwidth: string;
  status: "active" | "inactive" | "configuring";
  path: LatLngExpression[];
}

export function Dashboard({ onBack, onNavigateToTokens }: DashboardProps) {
  const [tokens, setTokens] = useState<{
    cilogon?: TokenData;
    orcid?: TokenData;
  }>({});
  const [showNewL2VPNModal, setShowNewL2VPNModal] = useState(false);
  const [connections] = useState<Connection[]>([]);

  // Empty network nodes - will be populated with topology data later
  const [networkNodes] = useState<NetworkNode[]>([]);

  useEffect(() => {
    loadTokens();
  }, []);

  const loadTokens = () => {
    const cilogon = TokenStorage.getToken("cilogon");
    const orcid = TokenStorage.getToken("orcid");

    const validTokens: any = {};

    if (cilogon && TokenStorage.isTokenValid(cilogon)) {
      validTokens.cilogon = cilogon;
    }

    if (orcid && TokenStorage.isTokenValid(orcid)) {
      validTokens.orcid = orcid;
    }

    setTokens(validTokens);
  };

  const handleLogout = () => {
    TokenStorage.clearAllTokens();
    setTokens({});
    toast.success("Successfully logged out");
    onBack();
  };

  const handleNewL2VPN = (l2vpnData: L2VPNData) => {
    // For now, just show a message that the L2VPN request has been received
    // Later this will integrate with backend to create actual L2VPN connections
    console.log("L2VPN Data:", l2vpnData);
    toast.success(
      `L2VPN request "${l2vpnData.name}" received. Backend integration pending.`
    );

    // TODO: Integrate with backend API to create actual L2VPN connections
    // This will involve:
    // 1. Send L2VPN request to backend with endpoint details
    // 2. Backend processes topology and creates L2VPN circuit
    // 3. Update map with new L2VPN connection data
    // 4. Show connection status updates
  };

  const getNodeColor = (status: string) => {
    switch (status) {
      case "active":
        return "#22c55e"; // green
      case "inactive":
        return "#ef4444"; // red
      case "maintenance":
        return "#f59e0b"; // yellow
      default:
        return "#6b7280"; // gray
    }
  };

  const getConnectionColor = (status: string) => {
    switch (status) {
      case "active":
        return "#22c55e";
      case "inactive":
        return "#ef4444";
      case "configuring":
        return "#f59e0b";
      default:
        return "#6b7280";
    }
  };

  const activeNodes = networkNodes.filter(
    (node) => node.status === "active"
  ).length;
  const activeConnections = connections.filter(
    (conn) => conn.status === "active"
  ).length;
  const availableTokens = Object.entries(tokens);
  const hasValidTokens = availableTokens.length > 0;

  return (
    <div className="min-h-screen bg-[rgb(255,255,255)]">
      {/* Beautiful Clean Header */}
      <div className="bg-gradient-to-r from-white to-[rgb(248,251,255)] border-b border-[rgb(200,220,240)] shadow-sm">
        <div className="max-w-7xl mx-auto px-8 py-6">
          {/* Top Row - Logo, Title & Status */}
          <div className="flex items-center justify-between mb-6">
            <div className="flex items-center gap-6">
              {/* Title Section */}
              <div>
                {/* Logo Start*/}
                <div className="flex items-center justify-center gap-4 -ml-[1.5rem]">
                  <img
                    src={sdxLogo}
                    alt="SDX Logo"
                    className="h-[110px] w-[110px] object-contain"
                  />
                  <div className="text-left">
                    <h1 className="text-4xl tracking-tight leading-tight font-serif">
                      <span className="text-sky-500 font-extrabold">
                        Atlantic
                      </span>
                      <span className="text-blue-800">Wave </span>
                      <span className="inline-block bg-sky-400 text-white rounded-md pl-[4px] pr-[10px] pt-[8px] text-xl font-serif tracking-wide text-superbold">
                        SDX
                      </span>
                    </h1>
                    <h2 className="text-xs uppercase tracking-tight leading-tight text-blue-800 mt-[-6px]">
                      International Distributed Software-Defined Exchange
                    </h2>
                  </div>
                </div>
                {/* Logo End*/}
                <p className="text-[rgb(50,135,200)] font-medium">
                  Network Topology & Connection Management
                </p>
              </div>
            </div>

            {/* Status Info */}
            <div className="flex items-center gap-6">
              <div className="text-right">
                <div className="flex items-center gap-2 mb-1">
                  <div
                    className={`w-2 h-2 rounded-full ${
                      hasValidTokens ? "bg-green-500" : "bg-gray-400"
                    }`}
                  ></div>
                  <span className="text-sm font-semibold text-[rgb(64,143,204)]">
                    {hasValidTokens
                      ? `Authenticated via ${Object.keys(tokens)
                          .map((k) => k.toUpperCase())
                          .join(", ")}`
                      : "Not authenticated"}
                  </span>
                </div>
                <div className="text-xs text-[rgb(50,135,200)] opacity-80">
                  {networkNodes.length === 0
                    ? "Ready for topology data"
                    : `${activeNodes} active nodes • ${activeConnections} active connections`}
                </div>
              </div>
            </div>
          </div>

          {/* Bottom Row - Action Buttons */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Button
                onClick={onNavigateToTokens}
                variant="outline"
                size="sm"
                className="border-[rgb(120,176,219)] text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)] hover:border-[rgb(64,143,204)] transition-all duration-200"
              >
                🔐 Manage Tokens
              </Button>

              <Button
                onClick={onBack}
                variant="ghost"
                size="sm"
                className="text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)] transition-all duration-200"
              >
                ← Back to Main
              </Button>
            </div>

            {/* Primary Action Buttons */}
            <div className="flex items-center gap-4">
              <Button
                onClick={() => {
                  console.log("New Connection button clicked");
                  setShowNewL2VPNModal(true);
                }}
                disabled={!hasValidTokens}
                size="lg"
                className="bg-[rgb(50,135,200)] hover:bg-[rgb(40,120,185)] text-white shadow-lg hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed px-6 py-3 text-base font-semibold rounded-xl transition-all duration-200 transform hover:scale-105 active:scale-95"
              >
                <span className="mr-2 text-lg">🔗</span>
                New L2VPN
              </Button>

              <Button
                onClick={handleLogout}
                variant="outline"
                size="lg"
                className="border-2 border-red-200 text-red-600 hover:bg-red-50 hover:border-red-300 hover:text-red-700 px-5 py-3 text-base font-medium rounded-xl transition-all duration-200 hover:shadow-lg"
              >
                <span className="mr-2">🚪</span>
                Logout
              </Button>
            </div>
          </div>
        </div>
      </div>

      {/* Authentication Warning */}
      {!hasValidTokens && (
        <div className="px-6 py-4">
          <div className="max-w-7xl mx-auto">
            <Alert className="border-2 border-yellow-200 bg-yellow-50">
              <AlertDescription className="text-yellow-800">
                <span className="font-semibold">Authentication required.</span>{" "}
                Please{" "}
                <button
                  onClick={onNavigateToTokens}
                  className="underline hover:no-underline font-medium"
                >
                  authenticate with an identity provider
                </button>{" "}
                to create new connections and access full functionality.
              </AlertDescription>
            </Alert>
          </div>
        </div>
      )}

      {/* Main Content - Full Width Map */}
      <div className="px-6 py-6">
        <div className="max-w-7xl mx-auto">
          {/* Map - Full Width */}
          <Card className="shadow-lg border-2 border-[rgb(120,176,219)] h-[700px]">
            <CardHeader className="pb-4">
              <CardTitle className="text-xl text-[rgb(64,143,204)]">
                Network Topology
              </CardTitle>
              <CardDescription className="text-[rgb(50,135,200)]">
                Interactive map view - topology data will be loaded here
              </CardDescription>
            </CardHeader>
            <CardContent className="p-4 h-[600px]">
              <div className="h-full rounded-lg overflow-hidden border border-[rgb(120,176,219)]">
                <MapContainer
                  center={[39.8283, -98.5795]} // Geographic center of US
                  zoom={4}
                  style={{ height: "100%", width: "100%" }}
                  zoomControl={true}
                >
                  <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                  />

                  {/* Network Nodes - Empty for now, will be populated with topology data */}
                  {networkNodes.map((node) => (
                    <Marker
                      key={node.id}
                      position={node.coordinates}
                      icon={L.divIcon({
                        className: "custom-node-marker",
                        html: `<div style="background-color: ${getNodeColor(
                          node.status
                        )}; width: 16px; height: 16px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.3);"></div>`,
                        iconSize: [22, 22],
                        iconAnchor: [11, 11],
                      })}
                    >
                      <Popup>
                        <div className="p-2">
                          <div className="font-semibold text-[rgb(64,143,204)]">
                            {node.name}
                          </div>
                          <div className="text-sm text-[rgb(50,135,200)]">
                            {node.city}
                          </div>
                          <div className="text-xs mt-1">
                            <Badge
                              className={`text-xs ${
                                node.status === "active"
                                  ? "bg-green-100 text-green-800"
                                  : node.status === "maintenance"
                                  ? "bg-yellow-100 text-yellow-800"
                                  : "bg-red-100 text-red-800"
                              }`}
                            >
                              {node.status}
                            </Badge>
                          </div>
                          <div className="text-xs text-[rgb(50,135,200)] mt-1">
                            {node.connections} connections
                          </div>
                        </div>
                      </Popup>
                    </Marker>
                  ))}

                  {/* Connection Lines - Empty for now, will be populated with topology data */}
                  {connections.map((connection) => (
                    <Polyline
                      key={connection.id}
                      positions={connection.path}
                      color={getConnectionColor(connection.status)}
                      weight={connection.status === "active" ? 4 : 2}
                      opacity={connection.status === "active" ? 0.8 : 0.5}
                      dashArray={
                        connection.status === "configuring"
                          ? "10, 10"
                          : undefined
                      }
                    >
                      <Popup>
                        <div className="p-2">
                          <div className="font-semibold text-[rgb(64,143,204)]">
                            {connection.name}
                          </div>
                          <div className="text-sm text-[rgb(50,135,200)]">
                            {connection.source} → {connection.destination}
                          </div>
                          <div className="text-xs mt-1">
                            <Badge
                              className={`text-xs mr-2 ${
                                connection.status === "active"
                                  ? "bg-green-100 text-green-800"
                                  : connection.status === "configuring"
                                  ? "bg-yellow-100 text-yellow-800"
                                  : "bg-red-100 text-red-800"
                              }`}
                            >
                              {connection.status}
                            </Badge>
                            <span className="text-[rgb(50,135,200)]">
                              {connection.type}
                            </span>
                          </div>
                          <div className="text-xs text-[rgb(50,135,200)] mt-1">
                            {connection.bandwidth}
                          </div>
                        </div>
                      </Popup>
                    </Polyline>
                  ))}
                </MapContainer>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* New L2VPN Modal */}
      <NewL2VPNModal
        isOpen={showNewL2VPNModal}
        onClose={() => {
          console.log("Closing L2VPN modal");
          setShowNewL2VPNModal(false);
        }}
        onConfirm={handleNewL2VPN}
      />
    </div>
  );
}
