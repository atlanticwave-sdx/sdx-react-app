import React, { useEffect, useRef, useState } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import '@/styles/topology-map.css';
import { ProcessedTopology, ProcessedLocationNode, ProcessedLink } from '@/lib/topology-processor';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { useTheme } from '@/components/ThemeProvider';

// Fix for default markers in React
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
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

export const TopologyMap: React.FC<TopologyMapProps> = ({ processedData, linksArray }) => {
  const mapRef = useRef<HTMLDivElement>(null);
  const mapInstanceRef = useRef<L.Map | null>(null);
  const tileLayerRef = useRef<L.TileLayer | null>(null);
  const [portModalData, setPortModalData] = useState<PortModalData | null>(null);
  const [linkModalData, setLinkModalData] = useState<LinkModalData | null>(null);
  const [portSearchTerm, setPortSearchTerm] = useState('');
  const [linkSearchTerm, setLinkSearchTerm] = useState('');
  const { theme } = useTheme();

  // Define tile layer configurations for different themes
  const tileConfigs = {
    light: {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution: '© OpenStreetMap contributors',
      className: 'map-tiles-light'
    },
    dark: {
      url: 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png',
      attribution: '© OpenStreetMap contributors © CARTO',
      className: 'map-tiles-dark'
    }
  };

  // Determine current theme (handle 'system' theme)
  const getCurrentTheme = (): 'light' | 'dark' => {
    if (theme === 'system') {
      return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    return theme as 'light' | 'dark';
  };

  useEffect(() => {
    if (!mapRef.current || mapInstanceRef.current) return;

    // Initialize map
    const map = L.map(mapRef.current, { closePopupOnClick: false })
      .setView([25.75, -80.37], 2);

    // Add initial tile layer based on current theme
    const currentTheme = getCurrentTheme();
    const tileConfig = tileConfigs[currentTheme];
    const tileLayer = L.tileLayer(tileConfig.url, {
      maxZoom: 19,
      attribution: tileConfig.attribution,
      className: tileConfig.className
    }).addTo(map);

    mapInstanceRef.current = map;
    tileLayerRef.current = tileLayer;

    return () => {
      if (mapInstanceRef.current) {
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
      className: tileConfig.className
    }).addTo(map);

    tileLayerRef.current = newTileLayer;

    console.log(`Map theme changed to: ${currentTheme}`, {
      url: tileConfig.url,
      className: tileConfig.className
    });
  }, [theme]);

  useEffect(() => {
    if (!mapInstanceRef.current) return;

    const map = mapInstanceRef.current;
    
    console.log('TopologyMap rendering with data:', {
      nodes: Object.keys(processedData.nodes_array).length,
      links: processedData.latlng_array.length,
      linksArray: Object.keys(linksArray).length
    });

    // Clear existing layers
    map.eachLayer((layer) => {
      if (layer instanceof L.Marker || layer instanceof L.Polyline) {
        layer.remove();
      }
    });

    // Add markers for each location
    const currentTheme = getCurrentTheme();
    const isDark = currentTheme === 'dark';
    
    Object.entries(processedData.nodes_array).forEach(([locationKey, locationData]) => {
      // Create custom marker icon based on theme
      const markerIcon = L.divIcon({
        className: 'custom-node-marker',
        html: `
          <div style="
            background-color: ${isDark ? '#3b82f6' : '#2563eb'};
            width: 16px;
            height: 16px;
            border-radius: 50%;
            border: 3px solid ${isDark ? '#1f2937' : '#ffffff'};
            box-shadow: 0 2px 8px ${isDark ? 'rgba(0,0,0,0.8)' : 'rgba(0,0,0,0.3)'};
          "></div>
        `,
        iconSize: [22, 22],
        iconAnchor: [11, 11]
      });
      
      const marker = L.marker([locationData.latitude, locationData.longitude], { icon: markerIcon });
      
      // Create location names string
      const locations = locationData.sub_nodes
        .map(subNode => subNode.sub_node_name)
        .join(' ');

      // Count ports down
      let portsDown = 0;
      locationData.sub_nodes.forEach(subNode => {
        subNode.ports.forEach(port => {
          if ((port.status !== 'up' && port.state === 'enabled') || port.state === 'disabled') {
            portsDown++;
          }
        });
      });

      // Add permanent tooltip with theme-aware styling
      const tooltip = L.tooltip({ 
        permanent: true,
        className: isDark ? 'leaflet-tooltip-dark' : 'leaflet-tooltip-light'
      }).setContent(locations);
      marker.bindTooltip(tooltip);

      // Add click handler for port modal
      marker.on('click', () => {
        setPortModalData({ locationKey, locationData });
      });

      // Add popup for ports down with theme-aware styling
      if (portsDown > 0) {
        const popup = L.popup({
          autoClose: false,
          closeOnClick: false,
          keepInView: true,
          permanent: true,
          interactive: true,
          className: isDark ? 'leaflet-popup-dark' : 'leaflet-popup-light'
        }).setContent(`
          <div style="
            color: ${isDark ? '#f3f4f6' : '#1f2937'};
            background: ${isDark ? '#1f2937' : '#ffffff'};
            padding: 4px;
            border-radius: 4px;
          ">
            ports down: <b style="color: #ef4444">${portsDown}</b>
          </div>
        `);
        
        marker.bindPopup(popup);
        marker.openPopup();
      }

      marker.addTo(map);
      marker.openTooltip();
    });

    // Add polylines for connections with theme-aware colors
    processedData.latlng_array.forEach(linkData => {
      Object.entries(linkData.latlngs).forEach(([linkId, coordinates]) => {
        const latlngs = coordinates as [number[], number[]];
        const linkName = linkData.link;

        // Check if any links are down for this polyline
        const links = linksArray[linkName] || [];
        const hasDownLinks = links.some(link => link.status !== 'up');
        
        // Theme-aware colors
        const colors = {
          active: isDark ? '#60a5fa' : '#3b82f6', // Blue
          down: isDark ? '#fbbf24' : '#f59e0b'    // Yellow/Orange
        };

        const polyline = L.polyline(latlngs, {
          color: hasDownLinks ? colors.down : colors.active,
          weight: 3,
          opacity: isDark ? 0.9 : 0.7,
        }).bindTooltip(linkName, {
          className: isDark ? 'leaflet-tooltip-dark' : 'leaflet-tooltip-light'
        }).addTo(map);

        // Add click handler for link modal
        polyline.on('click', () => {
          if (links.length > 0) {
            setLinkModalData({ linkName, links });
          }
        });
      });
    });

  }, [processedData, linksArray]);

  // Filter ports based on search term
  const filteredPorts = portModalData ? 
    portModalData.locationData.sub_nodes.flatMap(subNode =>
      subNode.ports
        .filter(port => {
          const searchText = `${subNode.sub_node_name} ${port.id} ${port.name} ${port.node} ${port.type} ${port.status} ${port.state}`.toLowerCase();
          return searchText.includes(portSearchTerm.toLowerCase());
        })
        .map(port => ({ ...port, locationName: subNode.sub_node_name, entities: port.entities || [] }))
    ) : [];

  // Filter links based on search term
  const filteredLinks = linkModalData ?
    linkModalData.links.filter(link => {
      const searchText = `${link.id} ${link.name} ${link.bandwidth} ${link.type} ${link.status} ${link.state}`.toLowerCase();
      return searchText.includes(linkSearchTerm.toLowerCase());
    }) : [];

  return (
    <div className="w-full h-full">
      <div ref={mapRef} className="w-full h-full" />

      {/* Port Details Modal */}
      <Dialog open={!!portModalData} onOpenChange={() => setPortModalData(null)}>
        <DialogContent className="max-w-[98vw] w-full sm:w-[90vw] lg:w-[95vw] xl:w-[95vw] max-h-[90vh] overflow-y-auto topology-modal-content" style={{ zIndex: 10000 }}>
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
                {filteredPorts.length} port{filteredPorts.length !== 1 ? 's' : ''}
              </div>
            </div>
            <div className="rounded-md border overflow-hidden">
              <div className="overflow-x-auto">
                <Table className="w-full">
                  <TableHeader>
                    <TableRow className="bg-muted/50">
                      <TableHead className="font-semibold min-w-[180px]">📍 Location</TableHead>
                      <TableHead className="font-semibold min-w-[300px]">🆔 Port ID</TableHead>
                      <TableHead className="font-semibold min-w-[200px]">🏷️ Name</TableHead>
                      <TableHead className="font-semibold min-w-[150px]">🖥️ Node</TableHead>
                      <TableHead className="font-semibold min-w-[100px]">⚡ Type</TableHead>
                      <TableHead className="font-semibold min-w-[100px]">🔄 Status</TableHead>
                      <TableHead className="font-semibold min-w-[100px]">⚙️ State</TableHead>
                    </TableRow>
                  </TableHeader>
                <TableBody>
                  {filteredPorts.length === 0 ? (
                    <TableRow>
                      <TableCell colSpan={7} className="text-center py-8 text-muted-foreground">
                        {portSearchTerm ? '🔍 No ports match your search' : '📭 No ports found'}
                      </TableCell>
                    </TableRow>
                  ) : (
                    filteredPorts.map((port, index) => (
                      <TableRow key={index} className="hover:bg-muted/50 transition-colors">
                        <TableCell>
                          <div className="space-y-1">
                            <div className="font-medium">{port.locationName}</div>
                            {port.entities.length > 0 && (
                              <div className="text-xs text-muted-foreground">
                                <span className="inline-flex items-center gap-1 px-2 py-1 bg-primary/10 text-primary rounded-md">
                                  🏢 {port.entities.join(', ')}
                                </span>
                              </div>
                            )}
                          </div>
                        </TableCell>
                        <TableCell className="font-mono text-xs max-w-[200px]">
                          <div className="truncate" title={port.id}>
                            {port.id}
                          </div>
                        </TableCell>
                        <TableCell className="font-medium">{port.name}</TableCell>
                        <TableCell className="text-sm">
                          {port.node?.replace('urn:sdx:node:', '') || ''}
                        </TableCell>
                        <TableCell>
                          <span className="inline-flex items-center px-2 py-1 rounded-md bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200 text-xs font-medium">
                            {port.type}
                          </span>
                        </TableCell>
                        <TableCell>
                          <span className={`inline-flex items-center px-2 py-1 rounded-md text-xs font-medium ${
                            port.status === 'up' 
                              ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
                              : 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200'
                          }`}>
                            {port.status === 'up' ? '✅' : '❌'} {port.status}
                          </span>
                        </TableCell>
                        <TableCell>
                          <span className={`inline-flex items-center px-2 py-1 rounded-md text-xs font-medium ${
                            port.state === 'enabled'
                              ? 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200'
                              : 'bg-gray-100 text-gray-800 dark:bg-gray-900 dark:text-gray-200'
                          }`}>
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
      <Dialog open={!!linkModalData} onOpenChange={() => setLinkModalData(null)}>
        <DialogContent className="max-w-[98vw] w-full sm:w-[90vw] lg:w-[95vw] xl:w-[95vw] max-h-[90vh] overflow-y-auto topology-modal-content" style={{ zIndex: 10000 }}>
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
                {filteredLinks.length} link{filteredLinks.length !== 1 ? 's' : ''}
              </div>
            </div>
            <div className="rounded-md border overflow-hidden">
              <div className="overflow-x-auto">
                <Table className="w-full">
                  <TableHeader>
                    <TableRow className="bg-muted/50">
                      <TableHead className="font-semibold min-w-[300px]">🆔 ID</TableHead>
                      <TableHead className="font-semibold min-w-[200px]">🏷️ Name</TableHead>
                      <TableHead className="font-semibold min-w-[120px]">📊 Bandwidth</TableHead>
                      <TableHead className="font-semibold min-w-[150px]">📈 Residual BW</TableHead>
                      <TableHead className="font-semibold min-w-[100px]">⚡ Type</TableHead>
                      <TableHead className="font-semibold min-w-[120px]">📉 Packet Loss</TableHead>
                      <TableHead className="font-semibold min-w-[100px]">⚡ Latency</TableHead>
                      <TableHead className="font-semibold min-w-[120px]">📊 Availability</TableHead>
                      <TableHead className="font-semibold min-w-[100px]">🔄 Status</TableHead>
                      <TableHead className="font-semibold min-w-[100px]">⚙️ State</TableHead>
                    </TableRow>
                  </TableHeader>
                <TableBody>
                  {filteredLinks.map((link, index) => (
                    <TableRow key={index}>
                      <TableCell className="font-mono text-xs">{link.id}</TableCell>
                      <TableCell>{link.name}</TableCell>
                      <TableCell>{link.bandwidth}</TableCell>
                      <TableCell>{link.residual_bandwidth}</TableCell>
                      <TableCell>{link.type}</TableCell>
                      <TableCell>{link.packet_loss}</TableCell>
                      <TableCell>{link.latency}</TableCell>
                      <TableCell>{link.availability}</TableCell>
                      <TableCell 
                        className="font-bold"
                        style={{ color: link.status === 'up' ? 'green' : 'red' }}
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