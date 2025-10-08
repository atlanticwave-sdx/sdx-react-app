import { useState, useEffect } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { toast } from "sonner";
import { TokenData, TopologyResponse, TopologyNode, TopologyLink } from "@/lib/types";
import { TokenStorage } from "@/lib/token-storage";
import { ApiService } from "@/lib/api";
import { processTopologyData, convertToMapFormat, ProcessedTopology } from "@/lib/topology-processor";
import { config } from "@/lib/config";
import { NewL2VPNModal, L2VPNData } from "@/components/NewL2VPNModal";
import { TopologyMap } from "@/components/TopologyMap";
import { ThemeToggle } from "@/components/ThemeToggle";
import sdxLogo from "@/assets/images/sdx-logo.svg";


interface DashboardProps {
  onBack: () => void;
  onNavigateToTokens: () => void;
  onLogout?: () => void;
}


export function Dashboard({ onBack, onNavigateToTokens, onLogout }: DashboardProps) {
  const [tokens, setTokens] = useState<{
    cilogon?: TokenData;
    orcid?: TokenData;
  }>({});
  const [showNewL2VPNModal, setShowNewL2VPNModal] = useState(false);
  const [topology, setTopology] = useState<TopologyResponse | null>(null);
  const [processedTopology, setProcessedTopology] = useState<ProcessedTopology | null>(null);
  const [isLoadingTopology, setIsLoadingTopology] = useState(false);
  const [topologyError, setTopologyError] = useState<string | null>(null);
  const [allowedDomains] = useState<string[]>(config.topology.allowedDomains);

  useEffect(() => {
    loadTokens();
  }, []);

  useEffect(() => {
    // Load topology when we have valid authentication
    if (Object.keys(tokens).length > 0 && ApiService.hasValidAuth()) {
      loadTopology();
    }
  }, [tokens]);

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

  const loadTopology = async () => {
    setIsLoadingTopology(true);
    setTopologyError(null);
    
    try {
      console.log('Loading topology data from API...');
      const topologyData = await ApiService.getTopology();
      console.log('Raw topology data received:', topologyData);
      
      setTopology(topologyData);
      
      // Process topology data using PHP-equivalent logic
      console.log('Processing topology data with allowed domains:', allowedDomains);
      const processed = processTopologyData(topologyData, allowedDomains);
      console.log('Processed topology data:', processed);
      
      setProcessedTopology(processed);
      
      
      const nodeCount = Object.keys(processed.nodes_array).length;
      const linkCount = processed.latlng_array.length;
      
      toast.success(`Topology processed: ${nodeCount} location groups, ${linkCount} connections`);
      
    } catch (error) {
      console.error('Failed to load topology:', error);
      const errorMessage = error instanceof Error ? error.message : 'Unknown error occurred';
      setTopologyError(errorMessage);
      
      if (errorMessage.includes('authentication')) {
        toast.error('Authentication failed. Please login again.');
      } else {
        toast.error(`Failed to load topology: ${errorMessage}`);
      }
    } finally {
      setIsLoadingTopology(false);
    }
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
    toast.success(`L2VPN request "${l2vpnData.name}" received. Backend integration pending.`);
    
    // TODO: Integrate with backend API to create actual L2VPN connections
    // This will involve:
    // 1. Send L2VPN request to backend with endpoint details
    // 2. Backend processes topology and creates L2VPN circuit
    // 3. Update map with new L2VPN connection data
    // 4. Show connection status updates
  };


  const nodeCount = processedTopology ? Object.keys(processedTopology.nodes_array).length : 0;
  const linkCount = processedTopology ? processedTopology.latlng_array.length : 0;
  const availableTokens = Object.entries(tokens);
  const hasValidTokens = availableTokens.length > 0;

  return (
    <div className="min-h-screen bg-background text-foreground">
      {/* Beautiful Clean Header */}
      <div className="bg-gradient-to-r from-background to-muted border-b border-border shadow-sm">
        <div className="max-w-7xl mx-auto px-8 py-6">
          {/* Top Row - Logo, Title & Status */}
          <div className="flex items-center justify-between mb-6">
            <div className="flex items-center gap-6">
              {/* Logo */}
              <div className="w-14 h-14 bg-white border-2 border-[rgb(120,176,219)] rounded-2xl flex items-center justify-center shadow-lg hover:shadow-xl transition-shadow duration-200">
                <img src={sdxLogo} alt="SDX Logo" className="h-9 w-auto object-contain" />
              </div>
              
              {/* Title Section */}
              <div>
                <h1 className="text-2xl font-bold text-[rgb(64,143,204)] mb-1">
                  AtlanticWave-SDX Dashboard
                </h1>
                <p className="text-[rgb(50,135,200)] font-medium">
                  Network Topology & Connection Management
                </p>
              </div>
            </div>

            {/* Status Info & Theme Toggle */}
            <div className="flex items-center gap-6">
              <div className="text-right">
                <div className="flex items-center gap-2 mb-1">
                  <div className={`w-2 h-2 rounded-full ${hasValidTokens ? 'bg-green-500' : 'bg-gray-400'}`}></div>
                  <span className="text-sm font-semibold text-[rgb(64,143,204)]">
                    {hasValidTokens ? `Authenticated via ${Object.keys(tokens).map(k => k.toUpperCase()).join(', ')}` : 'Not authenticated'}
                  </span>
                </div>
                <div className="text-xs text-[rgb(50,135,200)] opacity-80">
                  {nodeCount === 0 ? 'Ready for topology data' : `${nodeCount} locations • ${linkCount} connections`}
                </div>
              </div>
              <ThemeToggle />
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
              
              {onLogout && (
                <Button
                  onClick={onLogout}
                  variant="outline"
                  size="sm"
                  className="text-red-600 border-red-300 hover:bg-red-50 transition-all duration-200"
                >
                  🚪 Logout
                </Button>
              )}
            </div>

            {/* Primary Action Buttons */}
            <div className="flex items-center gap-4">
              <Button
                onClick={loadTopology}
                disabled={!hasValidTokens || isLoadingTopology}
                variant="outline"
                size="sm"
                className="border-[rgb(120,176,219)] text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)] disabled:opacity-50"
              >
                {isLoadingTopology ? (
                  <>🔄 Loading...</>
                ) : (
                  <>🔄 Refresh Topology</>
                )}
              </Button>
              
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
                <span className="font-semibold">Authentication required.</span> Please{" "}
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

      {/* Topology Error */}
      {topologyError && (
        <div className="px-6 py-4">
          <div className="max-w-7xl mx-auto">
            <Alert className="border-2 border-red-200 bg-red-50">
              <AlertDescription className="text-red-800">
                <span className="font-semibold">Failed to load topology:</span> {topologyError}{" "}
                <button 
                  onClick={loadTopology}
                  disabled={isLoadingTopology}
                  className="underline hover:no-underline font-medium disabled:opacity-50"
                >
                  {isLoadingTopology ? 'Loading...' : 'Retry'}
                </button>
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
              <CardTitle className="text-xl text-[rgb(64,143,204)]">Network Topology</CardTitle>
              <CardDescription className="text-[rgb(50,135,200)]">
                {isLoadingTopology ? (
                  "Loading topology data from API..."
                ) : topology ? (
                  `Showing ${topology.nodes.length} nodes and ${topology.links.length} links from SDX API`
                ) : (
                  "Interactive map view - click 'Refresh Topology' to load data"
                )}
              </CardDescription>
            </CardHeader>
            <CardContent className="p-4 h-[600px]">
              <div className="h-full rounded-lg overflow-hidden border border-[rgb(120,176,219)]">
                {processedTopology ? (
                  <TopologyMap 
                    processedData={processedTopology} 
                    linksArray={processedTopology.links_array}
                  />
                ) : (
                  <div className="h-full flex items-center justify-center text-gray-500">
                    {isLoadingTopology ? "Loading topology map..." : "Click 'Refresh Topology' to load the map"}
                  </div>
                )}
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