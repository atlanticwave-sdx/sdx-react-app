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
import { TokenPage } from "@/components/pages/TokenPage";
import sdxLogo from "@/assets/images/sdx-logo.svg";
import logoImage from "@/assets/images/no-background-logo 2.png";

interface DashboardProps {
  onBack: () => void;
  onNavigateToTokens: () => void;
  onLogout?: () => void;
}

// Icon Components
const HomeIcon = ({ className }: { className?: string }) => (
  <svg
    width="36"
    height="36"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className={className}
  >
    <path
      d="M10 20.9999H5C3.89543 20.9999 3 20.1045 3 18.9999V12.2968C3 11.7851 3.19615 11.2928 3.54809 10.9214L10.5481 3.53247C11.3369 2.69979 12.663 2.69979 13.4519 3.53247L20.4519 10.9214C20.8038 11.2928 21 11.7851 21 12.2968V18.9999C21 20.1045 20.1046 20.9999 19 20.9999H14M10 20.9999V15.4999C10 15.2238 10.2239 14.9999 10.5 14.9999H13.5C13.7761 14.9999 14 15.2238 14 15.4999V20.9999M10 20.9999H14"
      stroke="currentColor"
      strokeWidth="1.5"
    />
  </svg>
);

const KeyIcon = ({ className }: { className?: string }) => (
  <svg
    width="36"
    height="36"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className={className}
  >
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M17.0645 12.1579L20.9592 16.0526C21.2212 16.3525 21.3124 16.765 21.2013 17.1474L20.4856 19.6421C20.3753 20.0196 20.0826 20.3163 19.7066 20.4316L17.1487 21.2C16.741 21.3105 16.3053 21.1986 16.0013 20.9053L12.0961 17C11.5653 16.4697 10.8464 16.1708 10.0961 16.1684C9.73491 16.17 9.37746 16.2415 9.04345 16.3789C8.70814 16.5108 8.35111 16.5786 7.99082 16.5789C7.23959 16.5813 6.51893 16.2816 5.99082 15.7474L2.83292 12.5895C2.11555 11.8746 1.83459 10.831 2.09608 9.85263L3.32766 5.29474C3.57794 4.30573 4.34269 3.5289 5.32766 3.26316L9.92766 2.09474C10.1683 2.03221 10.4159 2.00037 10.6645 2C11.4148 2.00233 12.1337 2.30126 12.6645 2.83158L15.8224 5.98947C16.6314 6.79876 16.8762 8.01434 16.4434 9.07368C16.0107 10.133 16.2555 11.3486 17.0645 12.1579ZM16.9803 19.6526L19.0856 19.0316L19.6645 16.9684L15.9487 13.2526C14.6842 11.9957 14.3056 10.0987 14.9908 8.45263C15.1717 7.97833 15.0561 7.44201 14.6961 7.08421L11.5382 3.92632C11.3059 3.6882 10.9866 3.55514 10.654 3.55789C10.5458 3.5419 10.4358 3.5419 10.3277 3.55789L5.73819 4.78947C5.30689 4.9055 4.97 5.24239 4.85398 5.67368L3.6224 10.3053C3.50688 10.7381 3.63131 11.1997 3.94871 11.5158L7.10661 14.6737C7.33886 14.9118 7.65821 15.0449 7.99082 15.0421C8.1523 15.0406 8.31239 15.0121 8.4645 14.9579C8.98451 14.7403 9.54292 14.6293 10.1066 14.6316C11.291 14.6183 12.4303 15.0854 13.2645 15.9263L16.9803 19.6526Z"
      fill="currentColor"
    />
    <path
      d="M10.2961 6.96843L7.03291 10.2316C6.72507 10.5398 6.72507 11.0391 7.03291 11.3474C7.34114 11.6552 7.84047 11.6552 8.1487 11.3474L11.4119 8.08422C11.5623 7.9376 11.6472 7.73642 11.6472 7.52633C11.6472 7.31623 11.5623 7.11505 11.4119 6.96843C11.1036 6.66059 10.6043 6.66059 10.2961 6.96843Z"
      fill="currentColor"
    />
  </svg>
);

const PlusIcon = ({ className }: { className?: string }) => (
  <svg
    width="36"
    height="36"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className={className}
  >
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M6 2H18C20.2091 2 22 3.79086 22 6V18C22 20.2091 20.2091 22 18 22H6C3.79086 22 2 20.2091 2 18V6C2 3.79086 3.79086 2 6 2ZM19.7041 19.7041C20.1561 19.2522 20.41 18.6392 20.41 18V6C20.41 5.36083 20.1561 4.74784 19.7041 4.29587C19.2522 3.84391 18.6392 3.59 18 3.59H6C4.66899 3.59 3.59 4.66899 3.59 6V18C3.59 18.6392 3.84391 19.2522 4.29587 19.7041C4.74784 20.1561 5.36083 20.41 6 20.41H18C18.6392 20.41 19.2522 20.1561 19.7041 19.7041Z"
      fill="currentColor"
    />
    <path
      d="M16 11.25H12.75V8C12.75 7.58579 12.4142 7.25 12 7.25C11.5858 7.25 11.25 7.58579 11.25 8V11.25H8C7.58579 11.25 7.25 11.5858 7.25 12C7.25 12.4142 7.58579 12.75 8 12.75H11.25V16C11.25 16.4142 11.5858 16.75 12 16.75C12.4142 16.75 12.75 16.4142 12.75 16V12.75H16C16.4142 12.75 16.75 12.4142 16.75 12C16.75 11.5858 16.4142 11.25 16 11.25Z"
      fill="currentColor"
    />
  </svg>
);

const RefreshIcon = ({ className }: { className?: string }) => (
  <svg
    width="36"
    height="36"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className={className}
  >
    <path
      d="M12.5122 4.02129L13.2722 3.26129C13.5476 2.96578 13.5395 2.50528 13.2539 2.21967C12.9682 1.93406 12.5077 1.92593 12.2122 2.20129L10.2122 4.20129C9.91978 4.49411 9.91978 4.96847 10.2122 5.26129L12.2122 7.26129C12.505 7.55375 12.9794 7.55375 13.2722 7.26129C13.5647 6.96847 13.5647 6.49411 13.2722 6.20129L12.6122 5.54129C15.9796 5.95841 18.6039 8.66112 18.9217 12.0393C19.2395 15.4175 17.1653 18.5622 13.9347 19.6C10.7042 20.6378 7.18665 19.2894 5.47757 16.3581C3.76849 13.4269 4.32777 9.70148 6.82223 7.40129C7.06396 7.11386 7.05582 6.69195 6.80319 6.41405C6.55056 6.13616 6.13133 6.08797 5.82223 6.30129C2.78041 9.1031 2.11554 13.6519 4.2282 17.2071C6.34086 20.7623 10.6541 22.353 14.5692 21.0207C18.4842 19.6884 20.9319 15.797 20.4375 11.6911C19.9431 7.58524 16.6417 4.38614 12.5222 4.02129H12.5122Z"
      fill="currentColor"
    />
  </svg>
);

const BarChartIcon = ({ className }: { className?: string }) => (
  <svg
    width="36"
    height="36"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className={className}
  >
    <path
      d="M12.0502 10.96H8.93018C8.51597 10.96 8.18018 10.6242 8.18018 10.21C8.18018 9.79575 8.51597 9.45996 8.93018 9.45996H12.0502C12.4644 9.45996 12.8002 9.79575 12.8002 10.21C12.8002 10.6242 12.4644 10.96 12.0502 10.96Z"
      fill="currentColor"
    />
    <path
      d="M8.93018 12.5698H15.0702C15.4844 12.5698 15.8202 12.9056 15.8202 13.3198C15.8202 13.734 15.4844 14.0698 15.0702 14.0698H8.93018C8.51597 14.0698 8.18018 13.734 8.18018 13.3198C8.18018 12.9056 8.51597 12.5698 8.93018 12.5698Z"
      fill="currentColor"
    />
    <path
      d="M14.2302 15.5H8.93018C8.51597 15.5 8.18018 15.8358 8.18018 16.25C8.18018 16.6642 8.51597 17 8.93018 17H14.2302C14.6444 17 14.9802 16.6642 14.9802 16.25C14.9802 15.8358 14.6444 15.5 14.2302 15.5Z"
      fill="currentColor"
    />
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M14.27 2C15.0792 1.99888 15.7474 2.63193 15.79 3.44C18.1649 3.70703 19.9696 5.70032 20 8.09V18.18C19.9945 20.8011 17.8711 22.9245 15.25 22.93H8.75C6.12893 22.9245 4.0055 20.8011 4 18.18V8.09C4.03041 5.70032 5.83508 3.70703 8.21 3.44C8.25747 2.63419 8.9228 2.00388 9.73 2H14.27ZM14.29 3.44H9.73V4.63H14.29V3.44ZM18.5 18.18C18.5 19.9766 17.0465 21.4345 15.25 21.44H8.75C6.95345 21.4345 5.49999 19.9766 5.5 18.18V8.09C5.50398 6.49887 6.65936 5.14458 8.23 4.89C8.35276 5.62136 8.98843 6.15532 9.73 6.15H14.27C15.0116 6.15532 15.6472 5.62136 15.77 4.89C17.3406 5.14458 18.496 6.49887 18.5 8.09V18.18Z"
      fill="currentColor"
    />
  </svg>
);

const LogoutIcon = ({ className }: { className?: string }) => (
  <svg
    width="36"
    height="36"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className={className}
  >
    <path
      d="M10 12H19M19 12L17 10M19 12L17 14M15 16V19C15 20.1046 14.1046 21 13 21H7C5.89543 21 5 20.1046 5 19V5C5 3.89543 5.89543 3 7 3H13C14.1046 3 15 3.89543 15 5V8"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
    />
  </svg>
);

const GlobeIcon = ({ className }: { className?: string }) => (
  <svg
    width="36"
    height="36"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className={className}
  >
    <path
      d="M12 20V10M18 20V4M6 20V16"
      stroke="currentColor"
      strokeWidth="4"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

export function Dashboard({
  onBack,
  onNavigateToTokens,
  onLogout,
}: DashboardProps) {
  const [tokens, setTokens] = useState<{
    cilogon?: TokenData;
    orcid?: TokenData;
  }>({});
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(true);
  const [selectedSection, setSelectedSection] = useState<
    "newL2VPN" | "connectionStatus" | "topologyStats" | null
  >(null);
  const [showNewL2VPNModal, setShowNewL2VPNModal] = useState(false);
  const [showTokenModal, setShowTokenModal] = useState(false);
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
    <div className="min-h-screen bg-background text-foreground relative">
      {/* Left Sidebar */}
      <div
        className={`${
          selectedSection || !isSidebarCollapsed ? "w-80" : "w-20"
        } absolute left-0 top-0 bottom-0 z-50 bg-gradient-to-b from-background via-background to-muted/30 border-r border-border/50 shadow-xl flex flex-col backdrop-blur-sm transition-all duration-300`}
      >
        {/* Sidebar Header - Logo & Title */}
        <div className="p-6 border-b border-border/50 bg-gradient-to-br from-background to-muted/20 relative">
          {(selectedSection || !isSidebarCollapsed) && (
            <div
              className="text-left flex items-center gap-3 mb-4"
              style={{ marginLeft: "8px" }}
            >
              <img
                src={logoImage}
                alt="AtlanticWave SDX Logo"
                className="w-12 h-12 max-w-12 max-h-12 object-contain flex-shrink-0"
                style={{ width: "64px", height: "64px" }}
              />
              <h1 className="text-3xl tracking-tight leading-tight font-serif">
                <span className="text-sky-500 font-extrabold">Atlantic</span>
                <span className="text-blue-800 dark:text-blue-300">Wave </span>
                <span className="inline-block bg-sky-400 text-white rounded-md pl-[4px] pr-[10px] pt-[6px] text-lg font-serif tracking-wide shadow-sm">
                  SDX
                </span>
              </h1>
            </div>
          )}
          {!selectedSection && isSidebarCollapsed && (
            <div className="flex items-center justify-center">
              <img
                src={logoImage}
                alt="AtlanticWave SDX Logo"
                className="w-12 h-12 max-w-12 max-h-12 object-contain flex-shrink-0"
                style={{ width: "64px", height: "64px" }}
              />
            </div>
          )}
        </div>

        {/* Sidebar Navigation */}
        <div className="flex flex-1 overflow-hidden">
          {/* Icons Column */}
          <div
            className={`${
              selectedSection || !isSidebarCollapsed ? "p-2" : "p-2"
            } space-y-3 overflow-y-auto scrollbar-thin scrollbar-thumb-border scrollbar-track-transparent border-r border-border/50`}
            style={{ width: "80px", minWidth: "80px" }}
          >
            {/* All Buttons */}
            <div className="space-y-4">
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={onBack}
                    variant="ghost"
                    size="sm"
                    className="w-full justify-center px-0 text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 font-medium"
                  >
                    <HomeIcon className="w-6 h-6" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent side="right">
                  <p>Back to Main</p>
                </TooltipContent>
              </Tooltip>

              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={() => setShowTokenModal(true)}
                    variant="ghost"
                    size="sm"
                    className="w-full justify-center px-0 text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 transition-all duration-200 hover:shadow-sm hover:translate-x-0.5"
                  >
                    <KeyIcon className="w-6 h-6" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent side="right">
                  <p>Manage Tokens</p>
                </TooltipContent>
              </Tooltip>

              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={loadTopology}
                    disabled={!hasValidTokens || isLoadingTopology}
                    variant="ghost"
                    size="sm"
                    className="w-full justify-center px-0 text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 disabled:hover:translate-x-0"
                  >
                    {isLoadingTopology ? (
                      <span className="text-base">⏳</span>
                    ) : (
                      <RefreshIcon className="w-5 h-5" />
                    )}
                  </Button>
                </TooltipTrigger>
                <TooltipContent side="right">
                  <p>{isLoadingTopology ? "Loading..." : "Refresh Topology"}</p>
                </TooltipContent>
              </Tooltip>

              <div className="pt-2">
                <Tooltip>
                  <TooltipTrigger asChild>
                    <Button
                      onClick={() => {
                        console.log("New Connection button clicked");
                        if (selectedSection === "newL2VPN") {
                          setSelectedSection(null);
                        } else {
                          setSelectedSection("newL2VPN");
                        }
                      }}
                      disabled={!hasValidTokens}
                      variant="ghost"
                      size="sm"
                      className={`w-full justify-center px-0 ${
                        selectedSection === "newL2VPN"
                          ? "bg-[rgb(236,244,250)] dark:bg-blue-500/20 border border-[rgb(64,143,204)] dark:border-blue-400/50"
                          : ""
                      } text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 disabled:hover:translate-x-0`}
                    >
                      <PlusIcon className="w-5 h-5" />
                    </Button>
                  </TooltipTrigger>
                  {isSidebarCollapsed && (
                    <TooltipContent side="right">
                      <p>New L2VPN</p>
                    </TooltipContent>
                  )}
                </Tooltip>
              </div>

              {/* Status Section Buttons */}
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={() => {
                      if (selectedSection === "connectionStatus") {
                        setSelectedSection(null);
                      } else {
                        setSelectedSection("connectionStatus");
                      }
                    }}
                    variant="ghost"
                    size="sm"
                    className={`w-full justify-center px-0 ${
                      selectedSection === "connectionStatus"
                        ? "bg-[rgb(236,244,250)] dark:bg-blue-500/20 border border-[rgb(64,143,204)] dark:border-blue-400/50"
                        : ""
                    } text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 disabled:hover:translate-x-0`}
                    disabled={!hasValidTokens}
                  >
                    <GlobeIcon className="w-5 h-5" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent side="right">
                  <p>Connection Status</p>
                </TooltipContent>
              </Tooltip>

              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={() => {
                      if (selectedSection === "topologyStats") {
                        setSelectedSection(null);
                      } else {
                        setSelectedSection("topologyStats");
                      }
                    }}
                    variant="ghost"
                    size="sm"
                    className={`w-full justify-center px-0 ${
                      selectedSection === "topologyStats"
                        ? "bg-[rgb(236,244,250)] dark:bg-blue-500/20 border border-[rgb(64,143,204)] dark:border-blue-400/50"
                        : ""
                    } text-[rgb(50,135,200)] dark:text-blue-400 hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/10 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 disabled:hover:translate-x-0`}
                    disabled={!topology && !isLoadingTopology}
                  >
                    <BarChartIcon className="w-5 h-5" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent side="right">
                  <p>Topology Stats</p>
                </TooltipContent>
              </Tooltip>

              {/* Theme Toggle */}
              <div className="flex justify-center">
                <ThemeToggle />
              </div>

              {/* Logout Button */}
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    onClick={handleLogout}
                    variant="ghost"
                    size="sm"
                    className="w-full justify-center px-0 text-[#3287C8] dark:text-[#3287C8] hover:bg-[#3287C8]/10 dark:hover:bg-[#3287C8]/10 transition-all duration-200 hover:shadow-sm hover:translate-x-0.5 font-medium"
                  >
                    <LogoutIcon className="w-5 h-5" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent side="right">
                  <p>Logout</p>
                </TooltipContent>
              </Tooltip>
            </div>
          </div>

          {/* Content Area */}
          {selectedSection && (
            <div className="flex-1 p-5 overflow-y-auto scrollbar-thin scrollbar-thumb-border scrollbar-track-transparent">
              {selectedSection === "newL2VPN" && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between mb-4">
                    <h2 className="text-xl font-semibold">
                      New L2VPN Connection
                    </h2>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => setSelectedSection(null)}
                      className="h-8 w-8 p-0"
                    >
                      ×
                    </Button>
                  </div>
                  <NewL2VPNModal
                    isOpen={true}
                    onClose={() => setSelectedSection(null)}
                    onConfirm={(data) => {
                      handleNewL2VPN(data);
                      setSelectedSection(null);
                    }}
                    availablePorts={extractAllPorts()}
                    inline={true}
                  />
                </div>
              )}
              {selectedSection === "connectionStatus" && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between mb-4">
                    <h2 className="text-xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                      Connection Status
                    </h2>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => setSelectedSection(null)}
                      className="h-8 w-8 p-0 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20"
                    >
                      ×
                    </Button>
                  </div>
                  {hasValidTokens ? (
                    <>
                      <div className="flex items-center gap-4 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md">
                        <div className="relative">
                          <div className="w-4 h-4 rounded-full bg-green-500 shadow-lg"></div>
                          {hasValidTokens && (
                            <div className="absolute inset-0 w-4 h-4 rounded-full bg-green-500 animate-ping opacity-75"></div>
                          )}
                        </div>
                        <div className="flex-1">
                          <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] mb-1">
                            Authenticated via
                          </p>
                          <p className="text-lg font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                            {Object.keys(tokens)
                              .map((k) => k.toUpperCase())
                              .join(", ")}
                          </p>
                        </div>
                      </div>
                      <div className="grid grid-cols-2 gap-4">
                        <div className="p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md hover:shadow-lg transition-all duration-200">
                          <p className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] mb-2 uppercase tracking-wide">
                            Locations
                          </p>
                          <p className="text-3xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                            {nodeCount}
                          </p>
                        </div>
                        <div className="p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md hover:shadow-lg transition-all duration-200">
                          <p className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] mb-2 uppercase tracking-wide">
                            Connections
                          </p>
                          <p className="text-3xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                            {linkCount}
                          </p>
                        </div>
                      </div>
                      <div className="pt-4 border-t-2 border-[rgb(200,220,240)] dark:border-blue-500/20">
                        <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)]">
                          {nodeCount === 0
                            ? "Ready for topology data"
                            : `${nodeCount} locations • ${linkCount} connections`}
                        </p>
                      </div>
                    </>
                  ) : (
                    <div className="p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md">
                      <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)]">
                        Not authenticated. Please authenticate with an identity
                        provider to access full functionality.
                      </p>
                    </div>
                  )}
                </div>
              )}
              {selectedSection === "topologyStats" && (
                <div className="space-y-4">
                  <div className="flex items-center justify-between mb-4">
                    <h2 className="text-xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                      Topology Statistics
                    </h2>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => setSelectedSection(null)}
                      className="h-8 w-8 p-0 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20"
                    >
                      ×
                    </Button>
                  </div>
                  {isLoadingTopology ? (
                    <div className="p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md">
                      <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] flex items-center gap-2">
                        <div className="w-4 h-4 border-2 border-[rgb(50,135,200)]/30 border-t-[rgb(50,135,200)] rounded-full animate-spin"></div>
                        Loading topology data from API...
                      </p>
                    </div>
                  ) : topology ? (
                    <div className="space-y-4">
                      <div className="flex items-center justify-between p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md hover:shadow-lg transition-all duration-200">
                        <span className="text-sm font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">
                          Nodes
                        </span>
                        <span className="text-2xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                          {topology.nodes.length}
                        </span>
                      </div>
                      <div className="flex items-center justify-between p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md hover:shadow-lg transition-all duration-200">
                        <span className="text-sm font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">
                          Links
                        </span>
                        <span className="text-2xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                          {topology.links.length}
                        </span>
                      </div>
                      <div className="pt-4 border-t-2 border-[rgb(200,220,240)] dark:border-blue-500/20">
                        <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)]">
                          Showing {topology.nodes.length} nodes and{" "}
                          {topology.links.length} links from SDX API
                        </p>
                      </div>
                    </div>
                  ) : (
                    <div className="p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md">
                      <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)]">
                        Interactive map view - click 'Refresh Topology' to load
                        data
                      </p>
                    </div>
                  )}
                </div>
              )}
            </div>
          )}
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
                  onClick={() => setShowTokenModal(true)}
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
        <div className="w-full h-screen relative overflow-hidden">
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

      {/* Token Management Modal */}
      <Dialog open={showTokenModal} onOpenChange={setShowTokenModal}>
        <DialogContent className="sm:max-w-[900px] max-h-[95vh] overflow-y-auto bg-gradient-to-br from-background via-background to-muted/20 border-2 border-[rgb(50,135,200)]/40 dark:border-[rgb(100,180,255)]/40 shadow-2xl backdrop-blur-sm">
          <TokenPage
            onBack={() => setShowTokenModal(false)}
            onNavigateToDashboard={() => {
              setShowTokenModal(false);
              // Already on dashboard, so just close the modal
            }}
            modal={true}
          />
        </DialogContent>
      </Dialog>
    </div>
  );
}
