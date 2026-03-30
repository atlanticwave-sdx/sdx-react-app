import React, { useEffect, useRef, useState } from "react";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "@/styles/topology-map.css";
import {
  ProcessedTopology,
  ProcessedLocationNode,
  ProcessedLink,
  ProcessedSubNode,
} from "@/lib/topology-processor";
import { getRegionName } from "@/lib/region-coordinates";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { useTheme } from "@/components/ThemeProvider";

// Zoom threshold for switching between clustered and individual views
const ZOOM_THRESHOLD = 7;

// Fix for default markers in React
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png",
  iconUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png",
});

interface TopologyMapProps {
  processedData: ProcessedTopology;
  linksArray: Record<string, any[]>;
}

interface PortModalData {
  locationKey: string;
  locationData: ProcessedLocationNode;
}

interface LinkModalData {
  linkName: string;
  links: any[];
}

export const TopologyMap: React.FC<TopologyMapProps> = ({
  processedData,
  linksArray,
}) => {
  const mapRef = useRef<HTMLDivElement>(null);
  const mapInstanceRef = useRef<L.Map | null>(null);
  const tileLayerRef = useRef<L.TileLayer | null>(null);
  const markersLayerRef = useRef<L.LayerGroup | null>(null);
  const polylinesLayerRef = useRef<L.LayerGroup | null>(null);
  const [currentZoom, setCurrentZoom] = useState<number>(3);
  const [portModalData, setPortModalData] = useState<PortModalData | null>(
    null
  );
  const [linkModalData, setLinkModalData] = useState<LinkModalData | null>(
    null
  );
  const [portSearchTerm, setPortSearchTerm] = useState("");
  const [linkSearchTerm, setLinkSearchTerm] = useState("");
  const { theme } = useTheme();

  // Define tile layer configurations for different themes
  const tileConfigs = {
    light: {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution: "© OpenStreetMap contributors",
      className: "map-tiles-light",
    },
    dark: {
      url: "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png",
      attribution: "© OpenStreetMap contributors © CARTO",
      className: "map-tiles-dark",
    },
  };

  // Determine current theme (handle 'system' theme)
  const getCurrentTheme = (): "light" | "dark" => {
    if (theme === "system") {
      return window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";
    }
    return theme as "light" | "dark";
  };

  useEffect(() => {
    if (!mapRef.current || mapInstanceRef.current) return;

    // Initialize map
    const map = L.map(mapRef.current, { closePopupOnClick: false }).setView(
      [21.75, -80.57],
      3
    );

    // Add initial tile layer based on current theme
    const currentTheme = getCurrentTheme();
    const tileConfig = tileConfigs[currentTheme];
    const tileLayer = L.tileLayer(tileConfig.url, {
      maxZoom: 19,
      attribution: tileConfig.attribution,
      className: tileConfig.className,
    }).addTo(map);

    // Initialize layer groups for markers and polylines
    const markersLayer = L.layerGroup().addTo(map);
    const polylinesLayer = L.layerGroup().addTo(map);
    markersLayerRef.current = markersLayer;
    polylinesLayerRef.current = polylinesLayer;

    // Add zoom event listener
    map.on("zoomend", () => {
      const newZoom = map.getZoom();
      setCurrentZoom(newZoom);
    });

    mapInstanceRef.current = map;
    tileLayerRef.current = tileLayer;

    return () => {
      if (mapInstanceRef.current) {
        mapInstanceRef.current.off("zoomend");
        mapInstanceRef.current.remove();
        mapInstanceRef.current = null;
      }
    };
  }, []);

  // Handle theme changes - update tile layer
  useEffect(() => {
    if (!mapInstanceRef.current || !tileLayerRef.current) return;

    const map = mapInstanceRef.current;
    const currentTheme = getCurrentTheme();
    const tileConfig = tileConfigs[currentTheme];

    // Remove current tile layer
    map.removeLayer(tileLayerRef.current);

    // Add new tile layer for current theme
    const newTileLayer = L.tileLayer(tileConfig.url, {
      maxZoom: 19,
      attribution: tileConfig.attribution,
      className: tileConfig.className,
    }).addTo(map);

    tileLayerRef.current = newTileLayer;

    console.log(`Map theme changed to: ${currentTheme}`, {
      url: tileConfig.url,
      className: tileConfig.className,
    });
  }, [theme]);

  // Helper: Render clustered markers (zoomed out view)
  const renderClusteredMarkers = (
    markersLayer: L.LayerGroup,
    nodesArray: Record<string, ProcessedLocationNode>,
    isDark: boolean
  ) => {
    Object.entries(nodesArray).forEach(([locationKey, locationData]) => {
      // Use REGION center coordinates for clustered view
      const lat = locationData.regionLatitude;
      const lng = locationData.regionLongitude;
      const nodeCount = locationData.sub_nodes.length;

      // Create cluster marker with count badge
      const markerIcon = L.divIcon({
        className: "custom-cluster-marker",
        html: `
          <div style="
            position: relative;
            background-color: ${isDark ? "#3b82f6" : "#2563eb"};
            width: 20px;
            height: 20px;
            border-radius: 50%;
            border: 3px solid ${isDark ? "#1f2937" : "#ffffff"};
            box-shadow: 0 2px 8px ${isDark ? "rgba(0,0,0,0.8)" : "rgba(0,0,0,0.3)"};
          ">
            ${
              nodeCount > 1
                ? `<span style="
                position: absolute;
                top: -10px;
                right: -10px;
                background: #8b5cf6;
                color: white;
                font-size: 10px;
                font-weight: bold;
                padding: 2px 5px;
                border-radius: 10px;
                min-width: 16px;
                text-align: center;
              ">${nodeCount}</span>`
                : ""
            }
          </div>
        `,
        iconSize: [26, 26],
        iconAnchor: [13, 13],
      });

      const marker = L.marker([lat, lng], { icon: markerIcon });

      // Get region name and node names
      const regionName = getRegionName(locationKey);
      const nodeNames = locationData.sub_nodes
        .map((subNode) => subNode.sub_node_name)
        .filter((name) => name)
        .join(", ");

      // Tooltip shows region name
      const tooltip = L.tooltip({
        permanent: true,
        className: isDark ? "leaflet-tooltip-dark" : "leaflet-tooltip-light",
      }).setContent(nodeNames || regionName);
      marker.bindTooltip(tooltip);

      // Count ports down
      let portsDown = 0;
      locationData.sub_nodes.forEach((subNode) => {
        subNode.ports.forEach((port) => {
          if (
            (port.status !== "up" && port.state === "enabled") ||
            port.state === "disabled"
          ) {
            portsDown++;
          }
        });
      });

      // Add popup for ports down
      if (portsDown > 0) {
        const popup = L.popup({
          autoClose: false,
          closeOnClick: false,
          keepInView: true,
          interactive: true,
          className: isDark ? "leaflet-popup-dark" : "leaflet-popup-light",
        }).setContent(`
          <div style="
            color: ${isDark ? "#f3f4f6" : "#1f2937"};
            background: ${isDark ? "#1f2937" : "#ffffff"};
            padding: 4px;
            border-radius: 4px;
          ">
            ports down: <b style="color: #ef4444">${portsDown}</b>
          </div>
        `);
        marker.bindPopup(popup);
        marker.openPopup();
      }

      // Click handler opens the port modal
      marker.on("click", () => {
        setPortModalData({ locationKey, locationData });
      });

      markersLayer.addLayer(marker);
      marker.openTooltip();
    });
  };

  // Helper: Render individual node markers (zoomed in view)
  const renderIndividualMarkers = (
    markersLayer: L.LayerGroup,
    nodesArray: Record<string, ProcessedLocationNode>,
    isDark: boolean
  ) => {
    Object.entries(nodesArray).forEach(([locationKey, locationData]) => {
      locationData.sub_nodes.forEach((subNode: ProcessedSubNode) => {
        // Use INDIVIDUAL node coordinates
        const lat = subNode.latitude;
        const lng = subNode.longitude;

        // Skip if no valid coordinates
        if (!lat || !lng) return;

        const markerIcon = L.divIcon({
          className: "custom-node-marker",
          html: `
            <div style="
              background-color: ${isDark ? "#3b82f6" : "#2563eb"};
              width: 14px;
              height: 14px;
              border-radius: 50%;
              border: 2px solid ${isDark ? "#1f2937" : "#ffffff"};
              box-shadow: 0 2px 6px ${isDark ? "rgba(0,0,0,0.8)" : "rgba(0,0,0,0.3)"};
            "></div>
          `,
          iconSize: [18, 18],
          iconAnchor: [9, 9],
        });

        const marker = L.marker([lat, lng], { icon: markerIcon });

        // Tooltip shows individual node/location name
        const tooltip = L.tooltip({
          permanent: true,
          className: isDark ? "leaflet-tooltip-dark" : "leaflet-tooltip-light",
        }).setContent(subNode.sub_node_name || subNode.name);
        marker.bindTooltip(tooltip);

        // Count ports down for this specific node
        let portsDown = 0;
        subNode.ports.forEach((port) => {
          if (
            (port.status !== "up" && port.state === "enabled") ||
            port.state === "disabled"
          ) {
            portsDown++;
          }
        });

        // Add popup for ports down
        if (portsDown > 0) {
          const popup = L.popup({
            autoClose: false,
            closeOnClick: false,
            keepInView: true,
            interactive: true,
            className: isDark ? "leaflet-popup-dark" : "leaflet-popup-light",
          }).setContent(`
            <div style="
              color: ${isDark ? "#f3f4f6" : "#1f2937"};
              background: ${isDark ? "#1f2937" : "#ffffff"};
              padding: 4px;
              border-radius: 4px;
            ">
              ports down: <b style="color: #ef4444">${portsDown}</b>
            </div>
          `);
          marker.bindPopup(popup);
          marker.openPopup();
        }

        // Click opens the region modal (showing all ports in the region)
        marker.on("click", () => {
          setPortModalData({ locationKey, locationData });
        });

        markersLayer.addLayer(marker);
        marker.openTooltip();
      });
    });
  };

  // Helper: Render links using region centers (clustered view)
  const renderClusteredLinks = (
    polylinesLayer: L.LayerGroup,
    latlngArray: ProcessedLink[],
    nodesArray: Record<string, ProcessedLocationNode>,
    isDark: boolean
  ) => {
    // Track rendered links to avoid duplicates
    const renderedLinks = new Set<string>();

    latlngArray.forEach((linkData) => {
      const [sourceKey, targetKey] = linkData.link.split("::");
      const sourceNode = nodesArray[sourceKey];
      const targetNode = nodesArray[targetKey];

      if (!sourceNode || !targetNode) return;

      // Create a unique key for this link pair
      const linkPairKey = [sourceKey, targetKey].sort().join("-");
      if (renderedLinks.has(linkPairKey)) return;
      renderedLinks.add(linkPairKey);

      // Use region centers for clustered view
      const latlngs: [number, number][] = [
        [sourceNode.regionLatitude, sourceNode.regionLongitude],
        [targetNode.regionLatitude, targetNode.regionLongitude],
      ];

      const linkName = linkData.link;
      const links = linksArray[linkName] || [];
      const hasDownLinks = links.some((link) => link.status !== "up");

      const colors = {
        active: isDark ? "#60a5fa" : "#3b82f6",
        down: isDark ? "#fbbf24" : "#f59e0b",
      };

      const polyline = L.polyline(latlngs, {
        color: hasDownLinks ? colors.down : colors.active,
        weight: 3,
        opacity: isDark ? 0.9 : 0.7,
      }).bindTooltip(linkName, {
        className: isDark ? "leaflet-tooltip-dark" : "leaflet-tooltip-light",
      });

      polyline.on("click", () => {
        if (links.length > 0) {
          setLinkModalData({ linkName, links });
        }
      });

      polylinesLayer.addLayer(polyline);
    });
  };

  // Main rendering effect - responds to data and zoom changes
  useEffect(() => {
    if (
      !mapInstanceRef.current ||
      !markersLayerRef.current ||
      !polylinesLayerRef.current
    )
      return;

    const markersLayer = markersLayerRef.current;
    const polylinesLayer = polylinesLayerRef.current;

    // Clear existing layers
    markersLayer.clearLayers();
    polylinesLayer.clearLayers();

    const currentTheme = getCurrentTheme();
    const isDark = currentTheme === "dark";

    // Determine view mode based on zoom
    const isClusteredView = currentZoom < ZOOM_THRESHOLD;

    console.log("TopologyMap rendering with data:", {
      nodes: Object.keys(processedData.nodes_array).length,
      links: processedData.latlng_array.length,
      linksArray: Object.keys(linksArray).length,
      zoom: currentZoom,
      clustered: isClusteredView,
    });

    // Always render links using region centers (consistent across all zoom levels)
    renderClusteredLinks(
      polylinesLayer,
      processedData.latlng_array,
      processedData.nodes_array,
      isDark
    );

    if (isClusteredView) {
      // Zoomed out: show region markers
      renderClusteredMarkers(markersLayer, processedData.nodes_array, isDark);
    } else {
      // Zoomed in: show individual node markers
      renderIndividualMarkers(markersLayer, processedData.nodes_array, isDark);
    }
  }, [processedData, linksArray, currentZoom]);

  // Filter ports based on search term
  const filteredPorts = portModalData
    ? portModalData.locationData.sub_nodes.flatMap((subNode) =>
        subNode.ports
          .filter((port) => {
            const searchText =
              `${subNode.sub_node_name} ${port.id} ${port.name} ${port.node} ${port.type} ${port.status} ${port.state}`.toLowerCase();
            return searchText.includes(portSearchTerm.toLowerCase());
          })
          .map((port) => ({
            ...port,
            locationName: subNode.sub_node_name,
            entities: port.entities || [],
          }))
      )
    : [];

  // Filter links based on search term
  const filteredLinks = linkModalData
    ? linkModalData.links.filter((link) => {
        const searchText =
          `${link.id} ${link.name} ${link.bandwidth} ${link.type} ${link.status} ${link.state}`.toLowerCase();
        return searchText.includes(linkSearchTerm.toLowerCase());
      })
    : [];

  return (
    <div className="w-full h-full">
      <div ref={mapRef} className="w-full h-full" />

      {/* Port Details Modal */}
      <Dialog
        open={!!portModalData}
        onOpenChange={() => setPortModalData(null)}
      >
        <DialogContent
          className="max-w-[98vw] w-full sm:w-[90vw] lg:w-[95vw] xl:w-[95vw] max-h-[90vh] overflow-y-auto topology-modal-content"
          style={{ zIndex: 10000 }}
        >
          <DialogHeader className="space-y-3">
            <DialogTitle className="text-2xl font-bold text-primary flex items-center gap-2">
              📍 {portModalData?.locationKey}
            </DialogTitle>
            <p className="text-muted-foreground">
              Network ports and connections for this location
            </p>
          </DialogHeader>
          <div className="space-y-6">
            <div className="flex items-center gap-4">
              <div className="flex-1">
                <Input
                  placeholder="🔍 Search ports by name, ID, or status..."
                  value={portSearchTerm}
                  onChange={(e) => setPortSearchTerm(e.target.value)}
                  className="w-full"
                />
              </div>
              <div className="text-sm text-muted-foreground">
                {filteredPorts.length} port
                {filteredPorts.length !== 1 ? "s" : ""}
              </div>
            </div>
            <div className="rounded-md border overflow-hidden">
              <div className="overflow-x-auto">
                <Table className="w-full">
                  <TableHeader>
                    <TableRow className="bg-muted/50">
                      <TableHead className="font-semibold min-w-[180px]">
                        📍 Location
                      </TableHead>
                      <TableHead className="font-semibold min-w-[300px]">
                        🆔 Port ID
                      </TableHead>
                      <TableHead className="font-semibold min-w-[200px]">
                        🏷️ Name
                      </TableHead>
                      <TableHead className="font-semibold min-w-[150px]">
                        🖥️ Node
                      </TableHead>
                      <TableHead className="font-semibold min-w-[150px]">
                        🏢 Entities
                      </TableHead>
                      <TableHead className="font-semibold min-w-[100px]">
                        ⚡ Type
                      </TableHead>
                      <TableHead className="font-semibold min-w-[100px]">
                        🔄 Status
                      </TableHead>
                      <TableHead className="font-semibold min-w-[100px]">
                        ⚙️ State
                      </TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {filteredPorts.length === 0 ? (
                      <TableRow>
                        <TableCell
                          colSpan={8}
                          className="text-center py-8 text-muted-foreground"
                        >
                          {portSearchTerm
                            ? "🔍 No ports match your search"
                            : "📭 No ports found"}
                        </TableCell>
                      </TableRow>
                    ) : (
                      filteredPorts.map((port, index) => (
                        <TableRow
                          key={index}
                          className="hover:bg-muted/50 transition-colors"
                        >
                          <TableCell className="font-medium">
                            {port.locationName}
                          </TableCell>
                          <TableCell className="font-mono text-xs max-w-[200px]">
                            <div className="truncate" title={port.id}>
                              {port.id}
                            </div>
                          </TableCell>
                          <TableCell className="font-medium">
                            {port.name}
                          </TableCell>
                          <TableCell className="text-sm">
                            {port.node?.replace("urn:sdx:node:", "") || ""}
                          </TableCell>
                          <TableCell>
                            {port.entities.length > 0 ? (
                              <div className="flex flex-wrap gap-1">
                                {port.entities.map((entity: string, i: number) => (
                                  <span
                                    key={i}
                                    className="inline-flex items-center px-2 py-1 rounded-md bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200 text-xs font-medium"
                                  >
                                    {entity}
                                  </span>
                                ))}
                              </div>
                            ) : (
                              <span className="text-muted-foreground text-xs">-</span>
                            )}
                          </TableCell>
                          <TableCell>
                            <span className="inline-flex items-center px-2 py-1 rounded-md bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200 text-xs font-medium">
                              {port.type}
                            </span>
                          </TableCell>
                          <TableCell>
                            <span
                              className={`inline-flex items-center px-2 py-1 rounded-md text-xs font-medium ${
                                port.status === "up"
                                  ? "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200"
                                  : "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200"
                              }`}
                            >
                              {port.status === "up" ? "✅" : "❌"} {port.status}
                            </span>
                          </TableCell>
                          <TableCell>
                            <span
                              className={`inline-flex items-center px-2 py-1 rounded-md text-xs font-medium ${
                                port.state === "enabled"
                                  ? "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200"
                                  : "bg-gray-100 text-gray-800 dark:bg-gray-900 dark:text-gray-200"
                              }`}
                            >
                              {port.state}
                            </span>
                          </TableCell>
                        </TableRow>
                      ))
                    )}
                  </TableBody>
                </Table>
              </div>
            </div>
          </div>
        </DialogContent>
      </Dialog>

      {/* Link Details Modal */}
      <Dialog
        open={!!linkModalData}
        onOpenChange={() => setLinkModalData(null)}
      >
        <DialogContent
          className="max-w-[98vw] w-full sm:w-[90vw] lg:w-[95vw] xl:w-[95vw] max-h-[90vh] overflow-y-auto topology-modal-content"
          style={{ zIndex: 10000 }}
        >
          <DialogHeader className="space-y-3">
            <DialogTitle className="text-2xl font-bold text-primary flex items-center gap-2">
              🔗 {linkModalData?.linkName}
            </DialogTitle>
            <p className="text-muted-foreground">
              Network links and connection details for this path
            </p>
          </DialogHeader>
          <div className="space-y-6">
            <div className="flex items-center gap-4">
              <div className="flex-1">
                <Input
                  placeholder="🔍 Search links by ID, name, or status..."
                  value={linkSearchTerm}
                  onChange={(e) => setLinkSearchTerm(e.target.value)}
                  className="w-full"
                />
              </div>
              <div className="text-sm text-muted-foreground">
                {filteredLinks.length} link
                {filteredLinks.length !== 1 ? "s" : ""}
              </div>
            </div>
            <div className="rounded-md border overflow-hidden">
              <div className="overflow-x-auto">
                <Table className="w-full">
                  <TableHeader>
                    <TableRow className="bg-muted/50">
                      <TableHead className="font-semibold min-w-[300px]">
                        🆔 ID
                      </TableHead>
                      <TableHead className="font-semibold min-w-[200px]">
                        🏷️ Name
                      </TableHead>
                      <TableHead className="font-semibold min-w-[120px]">
                        📊 Bandwidth
                      </TableHead>
                      <TableHead className="font-semibold min-w-[150px]">
                        📈 Residual BW
                      </TableHead>
                      <TableHead className="font-semibold min-w-[100px]">
                        ⚡ Type
                      </TableHead>
                      <TableHead className="font-semibold min-w-[120px]">
                        📉 Packet Loss
                      </TableHead>
                      <TableHead className="font-semibold min-w-[100px]">
                        ⚡ Latency
                      </TableHead>
                      <TableHead className="font-semibold min-w-[120px]">
                        📊 Availability
                      </TableHead>
                      <TableHead className="font-semibold min-w-[100px]">
                        🔄 Status
                      </TableHead>
                      <TableHead className="font-semibold min-w-[100px]">
                        ⚙️ State
                      </TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {filteredLinks.map((link, index) => (
                      <TableRow key={index}>
                        <TableCell className="font-mono text-xs">
                          {link.id}
                        </TableCell>
                        <TableCell>{link.name}</TableCell>
                        <TableCell>{link.bandwidth}</TableCell>
                        <TableCell>{link.residual_bandwidth}</TableCell>
                        <TableCell>{link.type}</TableCell>
                        <TableCell>{link.packet_loss}</TableCell>
                        <TableCell>{link.latency}</TableCell>
                        <TableCell>{link.availability}</TableCell>
                        <TableCell
                          className="font-bold"
                          style={{
                            color: link.status === "up" ? "green" : "red",
                          }}
                        >
                          {link.status}
                        </TableCell>
                        <TableCell>{link.state}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </div>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
};
