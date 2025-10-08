import { TopologyResponse, TopologyNode, TopologyLink } from "@/lib/types";
import { LatLngExpression } from 'leaflet';

// Types matching the PHP processing structure
export interface ProcessedSubNode {
  sub_node_name: string;
  ports: any[];
  name: string;
  id: string;
}

export interface ProcessedLocationNode {
  sub_nodes: ProcessedSubNode[];
  latitude: number;
  longitude: number;
}

export interface ProcessedLink {
  link: string;
  latlngs: Record<string, [number[], number[]]>;
}

export interface ProcessedTopology {
  nodes_array: Record<string, ProcessedLocationNode>;
  links_array: Record<string, any[]>;
  latlng_array: ProcessedLink[];
}

/**
 * Find subnode by port ID - equivalent to PHP find_subnode_by_id()
 */
function findSubnodeById(nodesArray: Record<string, ProcessedLocationNode>, nodeId: string) {
  const temp: { node?: string; latlngs?: number[] } = {};
  
  for (const [key, value] of Object.entries(nodesArray)) {
    const subNodes = value.sub_nodes;
    
    for (const subNode of subNodes) {
      const ports = subNode.ports;
      for (const port of ports) {
        if (port.id === nodeId) {
          temp.node = key;
          temp.latlngs = [value.latitude, value.longitude];
          return temp;
        }
      }
    }
  }
  
  return temp;
}

/**
 * Process topology data - equivalent to the PHP processing logic
 */
export function processTopologyData(
  response: TopologyResponse, 
  allowedDomains: string[] = []
): ProcessedTopology {
  // Defensive checks for response structure
  if (!response || typeof response !== 'object') {
    console.error('Invalid topology response:', response);
    return { nodes_array: {}, links_array: {}, latlng_array: [] };
  }
  
  let { nodes, links } = response;
  
  // Ensure nodes and links are arrays
  if (!Array.isArray(nodes)) {
    console.warn('Nodes is not an array, setting to empty array:', nodes);
    nodes = [];
  }
  
  if (!Array.isArray(links)) {
    console.warn('Links is not an array, setting to empty array:', links);
    links = [];
  }
  
  // Filter nodes by allowed domains (equivalent to PHP filter)
  // If no domains specified, show all nodes
  if (allowedDomains.length > 0) {
    nodes = nodes.filter(node => {
      return allowedDomains.some(domain => node.id.includes(domain));
    });
  }
  // If allowedDomains is empty, keep all nodes (don't filter)
  
  // Process nodes into hierarchical structure
  const nodesArray: Record<string, ProcessedLocationNode> = {};
  
  for (const node of nodes) {
    const location = node.location;
    const ports = node.ports || []; // Ports are directly on the node
    
    if (!location?.iso3166_2_lvl4) continue;
    
    const locationKey = location.iso3166_2_lvl4;
    
    if (!nodesArray[locationKey]) {
      nodesArray[locationKey] = {
        sub_nodes: [],
        latitude: location.latitude || 0,
        longitude: location.longitude || 0
      };
    }
    
    const tempArr: ProcessedSubNode = {
      sub_node_name: location.address || '',
      ports: ports,
      name: node.name,
      id: node.id
    };
    
    nodesArray[locationKey].sub_nodes.push(tempArr);
  }
  
  // Process links
  const latlngArray: ProcessedLink[] = [];
  const linksArray: Record<string, any[]> = {};
  
  for (const link of links) {
    const ports = link.ports || []; // Ports are directly on the link
    if (ports.length < 2) continue;
    
    const latlng = findSubnodeById(nodesArray, ports[0]);
    const latlng2 = findSubnodeById(nodesArray, ports[1]);
    
    if (latlng.node && latlng2.node && latlng.latlngs && latlng2.latlngs) {
      const tempNode: ProcessedLink = {
        link: `${latlng.node}-${latlng2.node}`,
        latlngs: {
          [link.id]: [latlng.latlngs, latlng2.latlngs]
        }
      };
      
      latlngArray.push(tempNode);
      
      // Process links_array
      const linkKey = tempNode.link;
      if (!linksArray[linkKey]) {
        linksArray[linkKey] = [];
      }
      linksArray[linkKey].push({ ...link });
    }
  }
  
  return {
    nodes_array: nodesArray,
    links_array: linksArray,
    latlng_array: latlngArray
  };
}

/**
 * Convert processed topology to simple map format for rendering
 */
export function convertToMapFormat(processed: ProcessedTopology) {
  const mapNodes: Array<{
    id: string;
    name: string;
    city: string;
    coordinates: LatLngExpression;
    status: "active" | "inactive" | "maintenance";
    connections: number;
    subNodes: ProcessedSubNode[];
  }> = [];
  
  // Convert location nodes to map nodes
  for (const [locationKey, locationData] of Object.entries(processed.nodes_array)) {
    mapNodes.push({
      id: locationKey,
      name: locationKey,
      city: locationData.sub_nodes[0]?.sub_node_name || 'Unknown',
      coordinates: [locationData.latitude, locationData.longitude] as LatLngExpression,
      status: "active" as const,
      connections: locationData.sub_nodes.length,
      subNodes: locationData.sub_nodes
    });
  }
  
  // Convert links to map connections
  const mapConnections: Array<{
    id: string;
    name: string;
    source: string;
    target: string;
    type: string;
    status: "active" | "inactive" | "configuring";
    path: LatLngExpression[];
  }> = [];
  
  for (const linkData of processed.latlng_array) {
    for (const [linkId, coordinates] of Object.entries(linkData.latlngs)) {
      mapConnections.push({
        id: linkId,
        name: linkData.link,
        source: linkData.link.split('-')[0],
        target: linkData.link.split('-')[1],
        type: "L2VPN",
        status: "active" as const,
        path: coordinates as LatLngExpression[]
      });
    }
  }
  
  return { mapNodes, mapConnections };
}