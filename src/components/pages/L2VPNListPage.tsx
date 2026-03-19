import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { toast } from "sonner";
import { Pencil, Trash2, Save, X, ArrowLeft, RefreshCw, Columns2 } from "lucide-react";
import { TokenStorage } from "@/lib/token-storage";
import { ApiService } from "@/lib/api";
import {
  processTopologyData,
  ProcessedTopology,
} from "@/lib/topology-processor";
import { config } from "@/lib/config";
import { TopologyResponse } from "@/lib/types";

interface L2VPNListPageProps {
  onBack: () => void;
}

export function L2VPNListPage({ onBack }: L2VPNListPageProps) {
  const [l2vpns, setL2vpns] = useState<any[]>([]);
  const [isLoadingL2VPNs, setIsLoadingL2VPNs] = useState(false);
  const [l2vpnError, setL2vpnError] = useState<string | null>(null);
  const [deletingL2VPNId, setDeletingL2VPNId] = useState<string | null>(null);
  const [showDeleteConfirm, setShowDeleteConfirm] = useState<string | null>(null);
  const [editingL2VPNId, setEditingL2VPNId] = useState<string | null>(null);
  const [editFormData, setEditFormData] = useState<any | null>(null);
  const [isSavingEdit, setIsSavingEdit] = useState(false);
  const [expandedL2VPNs, setExpandedL2VPNs] = useState<Set<string>>(new Set());
  const [l2vpnTwoColumns, setL2vpnTwoColumns] = useState(true);
  const [l2vpnSearchQuery, setL2vpnSearchQuery] = useState("");
  const [processedTopology, setProcessedTopology] = useState<ProcessedTopology | null>(null);

  const hasValidTokens = (() => {
    const cilogon = TokenStorage.getToken("cilogon");
    const orcid = TokenStorage.getToken("orcid");
    const valid: any[] = [];
    if (cilogon && TokenStorage.isTokenValid(cilogon)) valid.push(cilogon);
    if (orcid && TokenStorage.isTokenValid(orcid)) valid.push(orcid);
    return valid.length > 0;
  })();

  useEffect(() => {
    if (hasValidTokens) {
      loadL2VPNs();
      loadTopology();
    }
  }, []);

  const loadTopology = async () => {
    try {
      const topologyData: TopologyResponse = await ApiService.getTopology();
      const allowedDomains = [...config.topology.allowedDomains];
      const processed = processTopologyData(topologyData, allowedDomains);
      setProcessedTopology(processed);
    } catch (error) {
      console.error("Failed to load topology for port list:", error);
    }
  };

  const extractAllPorts = () => {
    if (!processedTopology) return [];
    const allPorts: Array<{ id: string; entities: string[]; vlan_range?: number[] }> = [];
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

  const loadL2VPNs = async () => {
    setIsLoadingL2VPNs(true);
    setL2vpnError(null);
    try {
      const l2vpnData = await ApiService.getL2VPNs();
      setL2vpns(l2vpnData);
      toast.success(`Loaded ${l2vpnData.length} L2VPN connection(s)`);
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : "Unknown error occurred";
      setL2vpnError(errorMessage);
      if (errorMessage.includes("authentication")) {
        toast.error("Authentication failed. Please login again.");
      } else {
        toast.error(`Failed to load L2VPNs: ${errorMessage}`);
      }
    } finally {
      setIsLoadingL2VPNs(false);
    }
  };

  const handleDeleteL2VPN = async (serviceId: string) => {
    setDeletingL2VPNId(serviceId);
    try {
      await ApiService.deleteL2VPN(serviceId);
      setL2vpns((prev) =>
        prev.filter((l2vpn) => (l2vpn.id || l2vpn.uuid || l2vpn.service_id) !== serviceId),
      );
      toast.success("L2VPN deleted successfully");
      setShowDeleteConfirm(null);
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : "Unknown error occurred";
      toast.error(`Failed to delete L2VPN: ${errorMessage}`);
    } finally {
      setDeletingL2VPNId(null);
    }
  };

  const handleStartEdit = (l2vpn: any) => {
    const serviceId = l2vpn.id || l2vpn.uuid || l2vpn.service_id;
    setEditingL2VPNId(serviceId);
    setEditFormData({
      name: l2vpn.name || "",
      description: l2vpn.description || "",
      endpoints: Array.isArray(l2vpn.endpoints)
        ? l2vpn.endpoints.map((ep: any) =>
            typeof ep === "string"
              ? { port_id: ep, vlan: "" }
              : { port_id: ep.port_id || ep.port || "", vlan: ep.vlan || "" },
          )
        : [],
      qos_metrics: {
        min_bw: {
          value: l2vpn.qos_metrics?.min_bw?.value ?? 0,
          strict: l2vpn.qos_metrics?.min_bw?.strict ?? false,
        },
        max_delay: {
          value: l2vpn.qos_metrics?.max_delay?.value ?? 0,
          strict: l2vpn.qos_metrics?.max_delay?.strict ?? false,
        },
        max_number_oxps: {
          value: l2vpn.qos_metrics?.max_number_oxps?.value ?? 0,
          strict: l2vpn.qos_metrics?.max_number_oxps?.strict ?? false,
        },
      },
    });
  };

  const handleCancelEdit = () => {
    setEditingL2VPNId(null);
    setEditFormData(null);
  };

  const handleEditL2VPN = async () => {
    if (!editingL2VPNId || !editFormData) return;
    setIsSavingEdit(true);
    try {
      const patchBody: any = {
        service_id: editingL2VPNId,
        name: editFormData.name,
        endpoints: editFormData.endpoints,
      };
      if (editFormData.description) {
        patchBody.description = editFormData.description;
      }
      const qm = editFormData.qos_metrics;
      const hasQos =
        qm &&
        ((qm.min_bw && qm.min_bw.value > 0) ||
          (qm.max_delay && qm.max_delay.value > 0) ||
          (qm.max_number_oxps && qm.max_number_oxps.value > 0));
      if (hasQos) {
        const qos_metrics: any = {};
        if (qm.min_bw && qm.min_bw.value > 0)
          qos_metrics.min_bw = { value: Number(qm.min_bw.value), strict: qm.min_bw.strict };
        if (qm.max_delay && qm.max_delay.value > 0)
          qos_metrics.max_delay = { value: Number(qm.max_delay.value), strict: qm.max_delay.strict };
        if (qm.max_number_oxps && qm.max_number_oxps.value > 0)
          qos_metrics.max_number_oxps = { value: Number(qm.max_number_oxps.value), strict: qm.max_number_oxps.strict };
        patchBody.qos_metrics = qos_metrics;
      }
      await ApiService.updateL2VPN(editingL2VPNId, patchBody);
      setL2vpns((prev) =>
        prev.map((l2vpn) => {
          const id = l2vpn.id || l2vpn.uuid || l2vpn.service_id;
          if (id !== editingL2VPNId) return l2vpn;
          return {
            ...l2vpn,
            name: editFormData.name,
            description: editFormData.description || l2vpn.description,
            endpoints: editFormData.endpoints,
            ...(hasQos && { qos_metrics: patchBody.qos_metrics }),
          };
        }),
      );
      toast.success("L2VPN updated successfully");
      setEditingL2VPNId(null);
      setEditFormData(null);
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : "Unknown error occurred";
      toast.error(`Failed to update L2VPN: ${errorMessage}`);
    } finally {
      setIsSavingEdit(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(235,245,255)] dark:from-gray-900 dark:to-gray-800">
      {/* Header */}
      <header className="bg-white dark:bg-gray-900 border-b border-[rgb(200,220,240)] dark:border-gray-700 shadow-sm">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button onClick={onBack} className="text-[rgb(50,135,200)] hover:text-[rgb(40,115,175)] transition-colors">
              <ArrowLeft className="w-6 h-6" />
            </button>
            <h1 className="text-xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
              L2VPN Connections
            </h1>
          </div>
          <div className="flex items-center gap-2">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setL2vpnTwoColumns((prev) => !prev)}
              disabled={l2vpns.length === 0}
              className="h-8 px-3 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 disabled:opacity-50"
              title={l2vpnTwoColumns ? "Single column" : "Two columns"}
            >
              <Columns2 className="w-4 h-4" />
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={loadL2VPNs}
              disabled={isLoadingL2VPNs || !hasValidTokens}
              className="h-8 px-3 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 disabled:opacity-50"
              title="Refresh L2VPN list"
            >
              <RefreshCw className={`w-4 h-4 ${isLoadingL2VPNs ? "animate-spin" : ""}`} />
            </Button>
          </div>
        </div>
      </header>

      {/* Content */}
      <main className="max-w-6xl mx-auto px-6 py-6">
        <input
          type="text"
          value={l2vpnSearchQuery}
          onChange={(e) => setL2vpnSearchQuery(e.target.value)}
          placeholder="Search by name..."
          className="w-full px-3 py-2 mb-4 text-sm rounded-lg border-2 border-[rgb(200,220,240)] dark:border-blue-500/30 bg-white dark:bg-blue-500/5 focus:outline-none focus:border-[rgb(50,135,200)] dark:focus:border-blue-400 transition-colors placeholder:text-muted-foreground"
        />

        {l2vpnError && (
          <Alert className="mb-4 border-2 border-red-200 bg-red-50 dark:border-red-800 dark:bg-red-900/20">
            <AlertDescription className="text-red-800 dark:text-red-200">
              <span className="font-semibold">Error loading L2VPNs:</span> {l2vpnError}
            </AlertDescription>
          </Alert>
        )}

        {isLoadingL2VPNs ? (
          <div className="p-5 bg-white dark:bg-gray-800 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md">
            <div className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] flex items-center gap-2">
              <div className="w-4 h-4 border-2 border-[rgb(50,135,200)]/30 border-t-[rgb(50,135,200)] rounded-full animate-spin"></div>
              Loading L2VPN connections...
            </div>
          </div>
        ) : l2vpns.length === 0 ? (
          <div className="p-5 bg-white dark:bg-gray-800 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md">
            <p className="text-sm font-medium text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)]">
              No L2VPN connections found. Click the refresh button to load connections.
            </p>
          </div>
        ) : (
          <div className="rounded-md border border-[rgb(200,220,240)] dark:border-blue-500/20 overflow-hidden">
            {editingL2VPNId && (
              <div className="flex items-center gap-2 px-4 py-2.5 bg-[rgb(236,244,250)] dark:bg-blue-500/10 border-b border-[rgb(200,220,240)] dark:border-blue-500/30">
                <Pencil className="w-4 h-4 text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]" />
                <span className="text-sm font-medium text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)]">
                  Editing L2VPN
                </span>
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={handleCancelEdit}
                  className="ml-auto h-7 px-2 text-xs text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(200,220,240)] dark:hover:bg-blue-500/20"
                >
                  <X className="w-3.5 h-3.5 mr-1" />
                  Back to all
                </Button>
              </div>
            )}
            <div className={l2vpnTwoColumns ? "grid grid-cols-2 gap-px bg-background" : "divide-y divide-[rgb(200,220,240)] dark:divide-blue-500/20"}>
              {(editingL2VPNId
                ? l2vpns.filter((l) => (l.id || l.uuid || l.service_id) === editingL2VPNId)
                : l2vpns.filter((l) => (l.name || "").toLowerCase().includes(l2vpnSearchQuery.toLowerCase()))
              ).map((l2vpn, index) => {
                const l2vpnId = l2vpn.id || l2vpn.uuid || l2vpn.service_id;
                const isEditing = editingL2VPNId === l2vpnId;

                return (
                  <div
                    key={l2vpnId || index}
                    className={`p-4 space-y-3 bg-background bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 hover:from-[rgb(240,247,255)] hover:to-[rgb(232,243,255)] dark:hover:from-blue-500/15 dark:hover:to-blue-500/10 transition-colors${isEditing && l2vpnTwoColumns ? " col-span-2" : ""}`}
                  >
                    {isEditing && editFormData ? (
                      <>
                        {/* Edit Mode */}
                        <div className="flex flex-col gap-1">
                          <label className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">Name</label>
                          <input
                            type="text"
                            value={editFormData.name}
                            onChange={(e) => setEditFormData({ ...editFormData, name: e.target.value })}
                            className="w-full px-3 py-2 text-sm border border-[rgb(200,220,240)] dark:border-blue-500/30 rounded-md bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-[rgb(50,135,200)] dark:focus:ring-blue-400"
                          />
                        </div>

                        <div className="flex flex-col gap-1">
                          <label className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">Description</label>
                          <textarea
                            value={editFormData.description}
                            onChange={(e) => setEditFormData({ ...editFormData, description: e.target.value })}
                            rows={2}
                            className="w-full px-3 py-2 text-sm border border-[rgb(200,220,240)] dark:border-blue-500/30 rounded-md bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-[rgb(50,135,200)] dark:focus:ring-blue-400 resize-vertical"
                          />
                        </div>

                        <div className="flex flex-col gap-1">
                          <label className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">Endpoints</label>
                          <div className="flex flex-col gap-2">
                            {editFormData.endpoints.map((ep: any, epIdx: number) => (
                              <div key={epIdx} className="flex flex-col gap-1 p-2 border border-[rgb(200,220,240)] dark:border-blue-500/20 rounded-md">
                                <label className="text-xs text-muted-foreground">Port ID</label>
                                <select
                                  value={ep.port_id}
                                  onChange={(e) => {
                                    const newEndpoints = [...editFormData.endpoints];
                                    newEndpoints[epIdx] = { ...newEndpoints[epIdx], port_id: e.target.value };
                                    setEditFormData({ ...editFormData, endpoints: newEndpoints });
                                  }}
                                  className="w-full px-3 py-2 text-sm border border-[rgb(200,220,240)] dark:border-blue-500/30 rounded-md bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-[rgb(50,135,200)] dark:focus:ring-blue-400"
                                >
                                  <option value="">Select a port...</option>
                                  {extractAllPorts().map((port) => (
                                    <option key={port.id} value={port.id}>{port.id}</option>
                                  ))}
                                  {ep.port_id && !extractAllPorts().find((p) => p.id === ep.port_id) && (
                                    <option value={ep.port_id}>{ep.port_id}</option>
                                  )}
                                </select>
                                <label className="text-xs text-muted-foreground mt-1">VLAN</label>
                                <input
                                  type="text"
                                  value={ep.vlan}
                                  onChange={(e) => {
                                    const newEndpoints = [...editFormData.endpoints];
                                    newEndpoints[epIdx] = { ...newEndpoints[epIdx], vlan: e.target.value };
                                    setEditFormData({ ...editFormData, endpoints: newEndpoints });
                                  }}
                                  placeholder="e.g. 100"
                                  className="w-full px-3 py-2 text-sm border border-[rgb(200,220,240)] dark:border-blue-500/30 rounded-md bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-[rgb(50,135,200)] dark:focus:ring-blue-400"
                                />
                                {editFormData.endpoints.length > 2 && (
                                  <Button
                                    variant="ghost"
                                    size="sm"
                                    onClick={() => {
                                      const newEndpoints = editFormData.endpoints.filter((_: any, i: number) => i !== epIdx);
                                      setEditFormData({ ...editFormData, endpoints: newEndpoints });
                                    }}
                                    className="h-7 px-2 text-xs text-red-500 hover:bg-red-100 dark:hover:bg-red-500/20 self-end"
                                  >
                                    Remove
                                  </Button>
                                )}
                              </div>
                            ))}
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => {
                                setEditFormData({
                                  ...editFormData,
                                  endpoints: [...editFormData.endpoints, { port_id: "", vlan: "" }],
                                });
                              }}
                              className="h-8 text-xs text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20"
                            >
                              + Add Endpoint
                            </Button>
                          </div>
                        </div>

                        {/* QoS Metrics */}
                        <details className="group">
                          <summary className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide cursor-pointer select-none list-none flex items-center gap-1">
                            <span className="transition-transform group-open:rotate-90">&#9654;</span>
                            QoS Metrics
                          </summary>
                          <div className="mt-2 flex flex-col gap-3 pl-2">
                            <div className="flex flex-col gap-1">
                              <label className="text-xs text-muted-foreground">Min Bandwidth</label>
                              <div className="flex items-center gap-2">
                                <input
                                  type="number"
                                  min="0"
                                  value={editFormData.qos_metrics.min_bw.value}
                                  onChange={(e) =>
                                    setEditFormData({
                                      ...editFormData,
                                      qos_metrics: { ...editFormData.qos_metrics, min_bw: { ...editFormData.qos_metrics.min_bw, value: e.target.value } },
                                    })
                                  }
                                  className="flex-1 px-3 py-1.5 text-sm border border-[rgb(200,220,240)] dark:border-blue-500/30 rounded-md bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-[rgb(50,135,200)]"
                                />
                                <label className="flex items-center gap-1 text-xs text-muted-foreground whitespace-nowrap">
                                  <input
                                    type="checkbox"
                                    checked={editFormData.qos_metrics.min_bw.strict}
                                    onChange={(e) =>
                                      setEditFormData({
                                        ...editFormData,
                                        qos_metrics: { ...editFormData.qos_metrics, min_bw: { ...editFormData.qos_metrics.min_bw, strict: e.target.checked } },
                                      })
                                    }
                                  />
                                  Strict
                                </label>
                              </div>
                            </div>
                            <div className="flex flex-col gap-1">
                              <label className="text-xs text-muted-foreground">Max Delay</label>
                              <div className="flex items-center gap-2">
                                <input
                                  type="number"
                                  min="0"
                                  value={editFormData.qos_metrics.max_delay.value}
                                  onChange={(e) =>
                                    setEditFormData({
                                      ...editFormData,
                                      qos_metrics: { ...editFormData.qos_metrics, max_delay: { ...editFormData.qos_metrics.max_delay, value: e.target.value } },
                                    })
                                  }
                                  className="flex-1 px-3 py-1.5 text-sm border border-[rgb(200,220,240)] dark:border-blue-500/30 rounded-md bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-[rgb(50,135,200)]"
                                />
                                <label className="flex items-center gap-1 text-xs text-muted-foreground whitespace-nowrap">
                                  <input
                                    type="checkbox"
                                    checked={editFormData.qos_metrics.max_delay.strict}
                                    onChange={(e) =>
                                      setEditFormData({
                                        ...editFormData,
                                        qos_metrics: { ...editFormData.qos_metrics, max_delay: { ...editFormData.qos_metrics.max_delay, strict: e.target.checked } },
                                      })
                                    }
                                  />
                                  Strict
                                </label>
                              </div>
                            </div>
                            <div className="flex flex-col gap-1">
                              <label className="text-xs text-muted-foreground">Max OXPs</label>
                              <div className="flex items-center gap-2">
                                <input
                                  type="number"
                                  min="0"
                                  value={editFormData.qos_metrics.max_number_oxps.value}
                                  onChange={(e) =>
                                    setEditFormData({
                                      ...editFormData,
                                      qos_metrics: { ...editFormData.qos_metrics, max_number_oxps: { ...editFormData.qos_metrics.max_number_oxps, value: e.target.value } },
                                    })
                                  }
                                  className="flex-1 px-3 py-1.5 text-sm border border-[rgb(200,220,240)] dark:border-blue-500/30 rounded-md bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-[rgb(50,135,200)]"
                                />
                                <label className="flex items-center gap-1 text-xs text-muted-foreground whitespace-nowrap">
                                  <input
                                    type="checkbox"
                                    checked={editFormData.qos_metrics.max_number_oxps.strict}
                                    onChange={(e) =>
                                      setEditFormData({
                                        ...editFormData,
                                        qos_metrics: { ...editFormData.qos_metrics, max_number_oxps: { ...editFormData.qos_metrics.max_number_oxps, strict: e.target.checked } },
                                      })
                                    }
                                  />
                                  Strict
                                </label>
                              </div>
                            </div>
                          </div>
                        </details>

                        {/* Save / Cancel */}
                        <div className="flex justify-end gap-2 pt-3 border-t border-[rgb(200,220,240)] dark:border-blue-500/20 mt-2">
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={handleCancelEdit}
                            disabled={isSavingEdit}
                            className="h-9 px-4 border-2 border-[rgb(180,200,220)] dark:border-[rgb(100,150,200)] text-[rgb(80,120,160)] dark:text-[rgb(150,200,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(120,176,219)] transition-all duration-200 shadow-sm hover:shadow-md font-medium"
                          >
                            <X className="w-4 h-4 mr-1.5" />
                            Cancel
                          </Button>
                          <Button
                            size="sm"
                            onClick={handleEditL2VPN}
                            disabled={isSavingEdit || !editFormData.name.trim()}
                            className="h-9 px-4 bg-green-600 hover:bg-green-700 dark:bg-green-600 dark:hover:bg-green-500 text-white shadow-sm hover:shadow-md transition-all duration-200 font-medium disabled:opacity-50"
                          >
                            {isSavingEdit ? (
                              <>
                                <div className="w-4 h-4 mr-1.5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                                Saving...
                              </>
                            ) : (
                              <>
                                <Save className="w-4 h-4 mr-1.5" />
                                Save
                              </>
                            )}
                          </Button>
                        </div>
                      </>
                    ) : (
                      <>
                        {/* Read-Only Mode */}
                        <div
                          className="flex items-center justify-between cursor-pointer"
                          onClick={() => {
                            setExpandedL2VPNs((prev) => {
                              const next = new Set(prev);
                              if (next.has(l2vpnId!)) next.delete(l2vpnId!);
                              else next.add(l2vpnId!);
                              return next;
                            });
                          }}
                        >
                          <div className="flex items-center gap-2">
                            <span className={`text-xs text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] transition-transform ${expandedL2VPNs.has(l2vpnId!) ? "rotate-90" : ""}`}>&#9654;</span>
                            <span className="text-sm font-medium text-foreground">
                              {l2vpn.name || "Unnamed"}
                            </span>
                          </div>
                          <div className="flex items-center gap-2" onClick={(e) => e.stopPropagation()}>
                            <Button
                              variant="outline"
                              size="sm"
                              onClick={() => handleStartEdit(l2vpn)}
                              className="h-7 px-2 border-2 border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] hover:bg-[rgb(50,135,200)] hover:text-white dark:hover:bg-[rgb(100,180,255)] dark:hover:text-gray-900 transition-all duration-200 shadow-sm hover:shadow-md font-medium"
                              title="Edit L2VPN"
                              disabled={editingL2VPNId !== null}
                            >
                              <Pencil className="w-3.5 h-3.5 mr-1" />
                              Edit
                            </Button>
                            <Button
                              variant="outline"
                              size="sm"
                              onClick={() => setShowDeleteConfirm(l2vpnId)}
                              className="h-7 px-2 border-2 border-red-300 dark:border-red-500/50 text-red-600 dark:text-red-400 hover:bg-red-600 hover:text-white hover:border-red-600 dark:hover:bg-red-600 dark:hover:text-white dark:hover:border-red-600 transition-all duration-200 shadow-sm hover:shadow-md font-medium"
                              title="Delete L2VPN"
                              disabled={deletingL2VPNId === l2vpnId}
                            >
                              {deletingL2VPNId === l2vpnId ? (
                                <>
                                  <div className="w-3.5 h-3.5 mr-1 border-2 border-red-300 border-t-red-600 rounded-full animate-spin" />
                                  Deleting...
                                </>
                              ) : (
                                <>
                                  <Trash2 className="w-3.5 h-3.5 mr-1" />
                                  Delete
                                </>
                              )}
                            </Button>
                          </div>
                        </div>

                        {/* Expanded Details */}
                        {expandedL2VPNs.has(l2vpnId!) && (
                          <div className="space-y-3 pt-2">
                            <div className="flex flex-col gap-1">
                              <span className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">Status</span>
                              <span className={`text-sm font-medium ${
                                (l2vpn.state || l2vpn.status || "").toLowerCase() === "up"
                                  ? "text-green-600 dark:text-green-400"
                                  : (l2vpn.state || l2vpn.status || "").toLowerCase() === "down"
                                    ? "text-red-600 dark:text-red-400"
                                    : "text-amber-600 dark:text-amber-400"
                              }`}>
                                {l2vpn.state || l2vpn.status || "Under provisioning"}
                              </span>
                            </div>

                            <div className="flex flex-col gap-1">
                              <span className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">ID</span>
                              <span className="font-mono text-sm text-foreground break-all">
                                {l2vpn.id || l2vpn.uuid || "N/A"}
                              </span>
                            </div>

                            {l2vpn.description && (
                              <div className="flex flex-col gap-1">
                                <span className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">Description</span>
                                <span className="text-sm text-foreground">{l2vpn.description}</span>
                              </div>
                            )}

                            <div className="flex flex-col gap-1">
                              <span className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">Endpoints</span>
                              <div className="flex flex-col gap-2">
                                {Array.isArray(l2vpn.endpoints) ? (
                                  l2vpn.endpoints.map((endpoint: any, epIndex: number) => (
                                    <div key={epIndex} className="text-sm text-foreground">
                                      {typeof endpoint === "string" ? (
                                        <span className="break-all">{endpoint}</span>
                                      ) : (
                                        <span className="break-all">
                                          {endpoint.port_id || endpoint.port || "N/A"}
                                          {endpoint.vlan && ` (VLAN: ${endpoint.vlan})`}
                                        </span>
                                      )}
                                    </div>
                                  ))
                                ) : (
                                  <span className="text-sm text-muted-foreground">
                                    {JSON.stringify(l2vpn.endpoints || "N/A")}
                                  </span>
                                )}
                              </div>
                            </div>

                            {l2vpn.qos_metrics && (
                              <div className="flex flex-col gap-1">
                                <span className="text-xs font-semibold text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] uppercase tracking-wide">QoS Metrics</span>
                                <div className="flex flex-col gap-1 text-sm text-foreground">
                                  {l2vpn.qos_metrics.min_bw && (
                                    <span>Min Bandwidth: {l2vpn.qos_metrics.min_bw.value} {l2vpn.qos_metrics.min_bw.strict ? "(strict)" : "(flexible)"}</span>
                                  )}
                                  {l2vpn.qos_metrics.max_delay && (
                                    <span>Max Delay: {l2vpn.qos_metrics.max_delay.value} {l2vpn.qos_metrics.max_delay.strict ? "(strict)" : "(flexible)"}</span>
                                  )}
                                  {l2vpn.qos_metrics.max_number_oxps && (
                                    <span>Max OXPs: {l2vpn.qos_metrics.max_number_oxps.value} {l2vpn.qos_metrics.max_number_oxps.strict ? "(strict)" : "(flexible)"}</span>
                                  )}
                                </div>
                              </div>
                            )}
                          </div>
                        )}
                      </>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </main>

      {/* Delete Confirmation Dialog */}
      <Dialog
        open={showDeleteConfirm !== null}
        onOpenChange={(open) => !open && setShowDeleteConfirm(null)}
      >
        <DialogContent>
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2 text-red-600 dark:text-red-400">
              <span className="text-xl">&#9888;&#65039;</span>
              Confirm Delete
            </DialogTitle>
            <DialogDescription>
              Are you sure you want to delete this L2VPN connection? This action cannot be undone.
            </DialogDescription>
          </DialogHeader>
          <div className="space-y-4 py-4">
            {showDeleteConfirm && (
              <div className="p-3 bg-muted rounded-lg">
                <p className="text-sm font-medium">L2VPN ID:</p>
                <p className="text-xs font-mono text-muted-foreground break-all">{showDeleteConfirm}</p>
              </div>
            )}
            <div className="flex justify-end gap-3">
              <Button
                variant="outline"
                onClick={() => setShowDeleteConfirm(null)}
                disabled={deletingL2VPNId !== null}
                className="border-2 border-[rgb(180,200,220)] dark:border-[rgb(100,150,200)] text-[rgb(80,120,160)] dark:text-[rgb(150,200,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(120,176,219)] transition-all duration-200 shadow-sm hover:shadow-md font-medium"
              >
                <X className="w-4 h-4 mr-1.5" />
                Cancel
              </Button>
              <Button
                variant="destructive"
                onClick={() => showDeleteConfirm && handleDeleteL2VPN(showDeleteConfirm)}
                disabled={deletingL2VPNId !== null}
                className="bg-red-600 hover:bg-red-700 dark:bg-red-600 dark:hover:bg-red-500 text-white shadow-sm hover:shadow-md transition-all duration-200 font-medium"
              >
                {deletingL2VPNId ? (
                  <>
                    <div className="w-4 h-4 mr-1.5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                    Deleting...
                  </>
                ) : (
                  <>
                    <Trash2 className="w-4 h-4 mr-1.5" />
                    Delete
                  </>
                )}
              </Button>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
