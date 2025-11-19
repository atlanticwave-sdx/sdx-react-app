import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Alert, AlertDescription } from "@/components/ui/alert";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { toast } from "sonner";
import {
  TokenData,
  TopologyResponse,
  TopologyNode,
  TopologyLink,
} from "@/lib/types";
import {
  TokenStorage,
  calculateOwnership,
  decodeJWT,
} from "@/lib/token-storage";
import { ApiService } from "@/lib/api";
import {
  processTopologyData,
  convertToMapFormat,
  ProcessedTopology,
} from "@/lib/topology-processor";
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

export function Dashboard({
  onBack,
  onNavigateToTokens,
  onLogout,
}: DashboardProps) {
  const [tokens, setTokens] = useState<{
    cilogon?: TokenData;
    orcid?: TokenData;
  }>({});
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
  const [showNewL2VPNModal, setShowNewL2VPNModal] = useState(false);
  const [showTopologyInfo, setShowTopologyInfo] = useState(false);
  const [showAuthInfo, setShowAuthInfo] = useState(false);
  const [topology, setTopology] = useState<TopologyResponse | null>(null);
  const [processedTopology, setProcessedTopology] =
    useState<ProcessedTopology | null>(null);
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
      console.log("Loading topology data from API...");
      const topologyData = await ApiService.getTopology();
      console.log("Raw topology data received:", topologyData);

      setTopology(topologyData);

      // Process topology data using PHP-equivalent logic
      console.log(
        "Processing topology data with allowed domains:",
        allowedDomains
      );
      const processed = processTopologyData(topologyData, allowedDomains);
      console.log("Processed topology data:", processed);

      setProcessedTopology(processed);

      const nodeCount = Object.keys(processed.nodes_array).length;
      const linkCount = processed.latlng_array.length;

      toast.success(
        `Topology processed: ${nodeCount} location groups, ${linkCount} connections`
      );
    } catch (error) {
      console.error("Failed to load topology:", error);
      const errorMessage =
        error instanceof Error ? error.message : "Unknown error occurred";
      setTopologyError(errorMessage);

      if (errorMessage.includes("authentication")) {
        toast.error("Authentication failed. Please login again.");
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

  // Extract all ports from topology for the L2VPN modal
  const extractAllPorts = () => {
    if (!processedTopology) return [];

    const allPorts: Array<{
      id: string;
      entities: string[];
      vlan_range?: number[];
    }> = [];

    Object.values(processedTopology.nodes_array).forEach((location) => {
      location.sub_nodes.forEach((subNode) => {
        subNode.ports.forEach((port: any) => {
          allPorts.push({
            id: port.id,
            entities: port.entities || [],
            vlan_range: port.services?.l2vpn_ptp?.vlan_range || [],
          });
        });
      });
    });

    return allPorts;
  };

  const handleNewL2VPN = async (l2vpnData: L2VPNData) => {
    let loadingToast: any = null;

    try {
      console.log("L2VPN Data received from form:", l2vpnData);

      // Get the most recent token to extract sub field
      const orcidToken = TokenStorage.getToken("orcid");
      const cilogonToken = TokenStorage.getToken("cilogon");
      const validTokens = [orcidToken, cilogonToken].filter(
        (token) => token && TokenStorage.isTokenValid(token)
      );

      if (validTokens.length === 0) {
        toast.error("No valid authentication token found. Please login again.");
        return;
      }

      const mostRecentToken = validTokens.sort(
        (a, b) => b!.issued_at - a!.issued_at
      )[0];

      if (!mostRecentToken?.id_token) {
        toast.error("No ID token found. Please login again.");
        return;
      }

      // Decode JWT to get sub field
      const claims = decodeJWT(mostRecentToken.id_token);
      if (!claims?.sub) {
        toast.error("Could not extract user information from token.");
        return;
      }

      console.log("Extracted sub from JWT:", claims.sub);

      // Calculate ownership hash from sub
      const ownership = await calculateOwnership(claims.sub);
      console.log("Calculated ownership:", ownership);

      // Build request payload matching PHP format
      const requestPayload = {
        name: l2vpnData.name,
        endpoints: l2vpnData.endpoints,
        ownership: ownership,
      };

      console.log("Final L2VPN request payload:", requestPayload);

      // Show loading toast
      loadingToast = toast.loading("Creating L2VPN connection...");

      console.log("About to call API with payload:", requestPayload);

      // Make API call
      const response = await ApiService.createL2VPN(requestPayload);

      console.log("L2VPN API Response received:", response);

      // Show response in alert - SUCCESS
      alert(
        `✅ L2VPN Created Successfully!\n\nResponse:\n${JSON.stringify(
          response,
          null,
          2
        )}`
      );

      // Dismiss loading toast
      if (loadingToast) toast.dismiss(loadingToast);

      toast.success(`L2VPN "${l2vpnData.name}" created successfully!`);

      // Optionally reload topology to show new connection
      // await loadTopology();
    } catch (error: any) {
      console.error("Failed to create L2VPN:", error);
      console.log("Error object:", error);
      console.log("Error responseData:", error.responseData);

      // Dismiss loading toast first
      if (loadingToast) toast.dismiss(loadingToast);

      // Show error in alert with full response data
      const errorMessage =
        error instanceof Error ? error.message : "Unknown error";
      const errorData = error.responseData
        ? JSON.stringify(error.responseData, null, 2)
        : errorMessage;

      console.log("About to show alert with data:", errorData);
      alert(`❌ L2VPN Creation Failed!\n\nFull Response:\n${errorData}`);
      console.log("Alert was shown");

      toast.error(
        error instanceof Error
          ? `Failed to create L2VPN: ${error.message}`
          : "Failed to create L2VPN connection"
      );
    }
  };

  const nodeCount = processedTopology
    ? Object.keys(processedTopology.nodes_array).length
    : 0;
  const linkCount = processedTopology
    ? processedTopology.latlng_array.length
    : 0;
  const availableTokens = Object.entries(tokens);
  const hasValidTokens = availableTokens.length > 0;

  return (
    <div className="min-h-screen bg-background text-foreground flex">
      {/* Left Sidebar */}
      <div
        className={`${
          isSidebarCollapsed ? "w-20" : "w-80"
        } bg-gradient-to-b from-background via-background to-muted/30 border-r border-border/50 shadow-xl flex flex-col backdrop-blur-sm transition-all duration-300`}
      >
        {/* Sidebar Header - Logo & Title */}
        <div className="p-6 border-b border-border/50 bg-gradient-to-br from-background to-muted/20 relative">
          {!isSidebarCollapsed && (
            <div className="text-left">
              <h1 className="text-3xl tracking-tight leading-tight font-serif mb-2">
                <span className="text-sky-500 font-extrabold">Atlantic</span>
                <span className="text-blue-800 dark:text-blue-300">Wave </span>
                <span className="inline-block bg-sky-400 text-white rounded-md pl-[4px] pr-[10px] pt-[6px] text-lg font-serif tracking-wide shadow-sm">
                  SDX
                </span>
              </h1>
              <h2 className="text-xs uppercase tracking-[0.05em] leading-tight text-blue-800 dark:text-blue-300/80 mt-[-4px] mb-3 font-medium">
                International Distributed Software-Defined Exchange
              </h2>
              <div className="space-y-2 pt-2 border-t border-border/30">
                <p className="text-sm text-[rgb(50,135,200)] dark:text-blue-400 font-semibold">
                  Network Topology & Connection Management
                </p>
              </div>
            </div>
          )}
          {isSidebarCollapsed && (
            <div className="flex items-center justify-center">
              <div className="text-2xl font-serif">
                <span className="text-sky-500 font-extrabold">A</span>
                <span className="text-blue-800 dark:text-blue-300">W</span>
                <span className="inline-block bg-sky-400 text-white rounded-md px-1.5 py-0.5 text-sm">
                  S
                </span>
              </div>
            </div>
          )}
          {/* Toggle Button */}
          <Button
            onClick={() => setIsSidebarCollapsed(!isSidebarCollapsed)}
            variant="ghost"
            size="sm"
            className="absolute top-2 right-2 h-8 w-8 p-0"
          >
            {isSidebarCollapsed ? "→" : "←"}
          </Button>
        </div>

        {/* Sidebar Navigation */}
        <div
          className={`flex-1 ${
            isSidebarCollapsed ? "p-2" : "p-5"
          } space-y-3 overflow-y-auto scrollbar-thin scrollbar-thumb-border scrollbar-track-transparent`}
        >
          {/* Navigation Section Label */}
          {!isSidebarCollapsed && (
            <div className="px-2 pt-2">
              <h3 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground/70">
                Navigation
              </h3>
            </div>
          )}

          {/* Navigation Buttons */}
          <div className="space-y-2">
            <Tooltip>
              <TooltipTrigger asChild>
                <Button
                  onClick={onNavigateToTokens}
                  variant="outline"
                  size="sm"
                  className={`w-full ${
                    isSidebarCollapsed ? "justify-center px-0" : "justify-start"
                  } border-border/50 text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 hover:border-[rgb(64,143,204)] dark:hover:border-blue-400/50 transition-all duration-200 hover:shadow-sm hover:translate-x-0.5`}
                >
                  <span
                    className={`text-base ${
                      !isSidebarCollapsed ? "mr-2.5" : ""
                    }`}
                  >
                    🔐
                  </span>
                  {!isSidebarCollapsed && "Manage Tokens"}
                </Button>
              </TooltipTrigger>
              {isSidebarCollapsed && (
                <TooltipContent side="right">
                  <p>Manage Tokens</p>
                </TooltipContent>
              )}
            </Tooltip>

            <Tooltip>
              <TooltipTrigger asChild>
                <Button
                  onClick={loadTopology}
                  disabled={!hasValidTokens || isLoadingTopology}
                  variant="outline"
                  size="sm"
                  className={`w-full ${
                    isSidebarCollapsed ? "justify-center px-0" : "justify-start"
                  } border-border/50 text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 hover:border-[rgb(64,143,204)] dark:hover:border-blue-400/50 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 disabled:hover:translate-x-0`}
                >
                  <span
                    className={`text-base ${
                      !isSidebarCollapsed ? "mr-2.5" : ""
                    }`}
                  >
                    {isLoadingTopology ? "⏳" : "🔄"}
                  </span>
                  {!isSidebarCollapsed &&
                    (isLoadingTopology ? "Loading..." : "Refresh Topology")}
                </Button>
              </TooltipTrigger>
              {isSidebarCollapsed && (
                <TooltipContent side="right">
                  <p>{isLoadingTopology ? "Loading..." : "Refresh Topology"}</p>
                </TooltipContent>
              )}
            </Tooltip>

            <div className="pt-2">
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={() => {
                      console.log("New Connection button clicked");
                      setShowNewL2VPNModal(true);
                    }}
                    disabled={!hasValidTokens}
                    size="sm"
                    className={`w-full ${
                      isSidebarCollapsed
                        ? "justify-center px-0"
                        : "justify-start"
                    } bg-[rgb(50,135,200)] dark:bg-blue-600 hover:bg-[rgb(40,120,185)] dark:hover:bg-blue-700 text-white shadow-md hover:shadow-lg disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 hover:scale-[1.02] active:scale-[0.98] font-semibold`}
                  >
                    <span
                      className={`text-base ${
                        !isSidebarCollapsed ? "mr-2.5" : ""
                      }`}
                    >
                      🔗
                    </span>
                    {!isSidebarCollapsed && "New L2VPN"}
                  </Button>
                </TooltipTrigger>
                {isSidebarCollapsed && (
                  <TooltipContent side="right">
                    <p>New L2VPN</p>
                  </TooltipContent>
                )}
              </Tooltip>
            </div>
          </div>

          {/* Status Section */}
          <div className="pt-4 mt-4 border-t border-border/50">
            {!isSidebarCollapsed && (
              <div className="px-2 pt-2 pb-2">
                <h3 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground/70">
                  Status
                </h3>
              </div>
            )}
            <div className="space-y-2">
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={() => setShowAuthInfo(true)}
                    variant="outline"
                    size="sm"
                    className={`w-full ${
                      isSidebarCollapsed
                        ? "justify-center px-0"
                        : "justify-start"
                    } border-border/50 text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 hover:border-[rgb(64,143,204)] dark:hover:border-blue-400/50 transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-x-0`}
                    disabled={!hasValidTokens}
                  >
                    <span
                      className={`text-base ${
                        !isSidebarCollapsed ? "mr-2.5" : ""
                      }`}
                    >
                      🌐
                    </span>
                    {!isSidebarCollapsed && "Connection Status"}
                  </Button>
                </TooltipTrigger>
                {isSidebarCollapsed && (
                  <TooltipContent side="right">
                    <p>Connection Status</p>
                  </TooltipContent>
                )}
              </Tooltip>

              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={() => setShowTopologyInfo(true)}
                    variant="outline"
                    size="sm"
                    className={`w-full ${
                      isSidebarCollapsed
                        ? "justify-center px-0"
                        : "justify-start"
                    } border-border/50 text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 hover:border-[rgb(64,143,204)] dark:hover:border-blue-400/50 transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-x-0`}
                    disabled={!topology && !isLoadingTopology}
                  >
                    <span
                      className={`text-base ${
                        !isSidebarCollapsed ? "mr-2.5" : ""
                      }`}
                    >
                      📊
                    </span>
                    {!isSidebarCollapsed && "Topology Stats"}
                  </Button>
                </TooltipTrigger>
                {isSidebarCollapsed && (
                  <TooltipContent side="right">
                    <p>Topology Stats</p>
                  </TooltipContent>
                )}
              </Tooltip>
            </div>
          </div>

          {/* Sidebar Footer */}
          <div
            className={`${
              isSidebarCollapsed ? "p-2" : "p-5"
            } border-t border-border/50 bg-gradient-to-t from-muted/20 to-transparent space-y-3`}
          >
            {!isSidebarCollapsed && (
              <div className="flex items-center justify-between px-1">
                <span className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
                  Appearance
                </span>
                <ThemeToggle />
              </div>
            )}
            {isSidebarCollapsed && (
              <div className="flex justify-center">
                <ThemeToggle />
              </div>
            )}
            <div
              className={`flex ${
                isSidebarCollapsed ? "flex-col gap-2" : "gap-2"
              }`}
            >
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={onBack}
                    variant="ghost"
                    size="sm"
                    className={`${
                      isSidebarCollapsed
                        ? "w-full justify-center px-0"
                        : "flex-1 justify-start"
                    } text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 font-medium`}
                  >
                    <span
                      className={`text-base ${
                        !isSidebarCollapsed ? "mr-2.5" : ""
                      }`}
                    >
                      🏠
                    </span>
                    {!isSidebarCollapsed && "Back to Main"}
                  </Button>
                </TooltipTrigger>
                {isSidebarCollapsed && (
                  <TooltipContent side="right">
                    <p>Back to Main</p>
                  </TooltipContent>
                )}
              </Tooltip>
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={handleLogout}
                    variant="outline"
                    size="sm"
                    className={`${
                      isSidebarCollapsed
                        ? "w-full justify-center px-0"
                        : "flex-1 justify-start"
                    } text-red-600 dark:text-red-400 border-red-300 dark:border-red-800/50 hover:bg-red-50 dark:hover:bg-red-950/30 hover:border-red-400 dark:hover:border-red-700/50 transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 font-medium`}
                  >
                    <span
                      className={`text-base ${
                        !isSidebarCollapsed ? "mr-2.5" : ""
                      }`}
                    >
                      🚪
                    </span>
                    {!isSidebarCollapsed && "Logout"}
                  </Button>
                </TooltipTrigger>
                {isSidebarCollapsed && (
                  <TooltipContent side="right">
                    <p>Logout</p>
                  </TooltipContent>
                )}
              </Tooltip>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content Area - Full Screen Map */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Authentication Warning */}
        {!hasValidTokens && (
          <div className="px-6 py-4 border-b border-border">
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
        )}

        {/* Topology Error */}
        {topologyError && (
          <div className="px-6 py-4 border-b border-border">
            <Alert className="border-2 border-red-200 bg-red-50">
              <AlertDescription className="text-red-800">
                <span className="font-semibold">Failed to load topology:</span>{" "}
                {topologyError}{" "}
                <button
                  onClick={loadTopology}
                  disabled={isLoadingTopology}
                  className="underline hover:no-underline font-medium disabled:opacity-50"
                >
                  {isLoadingTopology ? "Loading..." : "Retry"}
                </button>
              </AlertDescription>
            </Alert>
          </div>
        )}

        {/* Full Screen Map */}
        <div className="flex-1 relative overflow-hidden">
          {processedTopology ? (
            <TopologyMap
              processedData={processedTopology}
              linksArray={processedTopology.links_array}
            />
          ) : (
            <div className="h-full flex items-center justify-center text-gray-500 bg-muted/30">
              {isLoadingTopology
                ? "Loading topology map..."
                : "Click 'Refresh Topology' to load the map"}
            </div>
          )}
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
        availablePorts={extractAllPorts()}
      />

      {/* Topology Info Dialog */}
      <Dialog open={showTopologyInfo} onOpenChange={setShowTopologyInfo}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2">
              <span className="text-xl">ℹ️</span>
              Topology Information
            </DialogTitle>
            <DialogDescription>
              Network topology data from SDX API
            </DialogDescription>
          </DialogHeader>
          <div className="space-y-4 py-4">
            {isLoadingTopology ? (
              <p className="text-sm text-muted-foreground">
                Loading topology data from API...
              </p>
            ) : topology ? (
              <div className="space-y-3">
                <div className="flex items-center justify-between p-3 bg-muted rounded-lg">
                  <span className="text-sm font-medium">Nodes</span>
                  <span className="text-lg font-bold text-primary">
                    {topology.nodes.length}
                  </span>
                </div>
                <div className="flex items-center justify-between p-3 bg-muted rounded-lg">
                  <span className="text-sm font-medium">Links</span>
                  <span className="text-lg font-bold text-primary">
                    {topology.links.length}
                  </span>
                </div>
                <div className="pt-2 border-t">
                  <p className="text-xs text-muted-foreground">
                    Showing {topology.nodes.length} nodes and{" "}
                    {topology.links.length} links from SDX API
                  </p>
                </div>
              </div>
            ) : (
              <p className="text-sm text-muted-foreground">
                Interactive map view - click 'Refresh Topology' to load data
              </p>
            )}
          </div>
        </DialogContent>
      </Dialog>

      {/* Authentication Info Dialog */}
      <Dialog open={showAuthInfo} onOpenChange={setShowAuthInfo}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2">
              <span className="text-xl">🌐</span>
              Authentication Status
            </DialogTitle>
            <DialogDescription>
              Current authentication and connection information
            </DialogDescription>
          </DialogHeader>
          <div className="space-y-4 py-4">
            {hasValidTokens ? (
              <>
                <div className="flex items-center gap-3 p-3 bg-muted rounded-lg">
                  <div className="relative">
                    <div className="w-3 h-3 rounded-full bg-green-500 shadow-sm"></div>
                    {hasValidTokens && (
                      <div className="absolute inset-0 w-3 h-3 rounded-full bg-green-500 animate-ping opacity-75"></div>
                    )}
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-medium">Authenticated via</p>
                    <p className="text-lg font-bold text-primary">
                      {Object.keys(tokens)
                        .map((k) => k.toUpperCase())
                        .join(", ")}
                    </p>
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <div className="p-3 bg-muted rounded-lg">
                    <p className="text-xs text-muted-foreground mb-1">
                      Locations
                    </p>
                    <p className="text-2xl font-bold text-primary">
                      {nodeCount}
                    </p>
                  </div>
                  <div className="p-3 bg-muted rounded-lg">
                    <p className="text-xs text-muted-foreground mb-1">
                      Connections
                    </p>
                    <p className="text-2xl font-bold text-primary">
                      {linkCount}
                    </p>
                  </div>
                </div>
                <div className="pt-2 border-t">
                  <p className="text-xs text-muted-foreground">
                    {nodeCount === 0
                      ? "Ready for topology data"
                      : `${nodeCount} locations • ${linkCount} connections`}
                  </p>
                </div>
              </>
            ) : (
              <div className="p-3 bg-muted rounded-lg">
                <p className="text-sm text-muted-foreground">
                  Not authenticated. Please authenticate with an identity
                  provider to access full functionality.
                </p>
              </div>
            )}
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
