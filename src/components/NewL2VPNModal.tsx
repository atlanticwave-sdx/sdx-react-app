import { useState, useRef, useEffect } from "react";
import { useForm, useFieldArray, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { Checkbox } from "@/components/ui/checkbox";
import { toast } from "sonner";
import { Trash2, Plus, ChevronDown, ChevronUp } from "lucide-react";

// Zod schema for form validation
const endpointSchema = z
  .object({
    port_id: z.string().min(1, "Port ID is required"),
    vlan_type: z.enum(["any", "number", "untagged", "VLAN range", "all"]),
    vlan_value: z.string().optional(),
  })
  .refine(
    (data) => {
      if (data.vlan_type === "number" || data.vlan_type === "VLAN range") {
        return data.vlan_value && data.vlan_value.length > 0;
      }
      return true;
    },
    {
      message: "VLAN value is required for this type",
      path: ["vlan_value"],
    }
  );

const l2vpnSchema = z.object({
  name: z
    .string()
    .min(1, "Connection name is required")
    .max(50, "Name must be 50 characters or less"),
  endpoints: z
    .array(endpointSchema)
    .min(2, "At least 2 endpoints are required"),
  description: z
    .string()
    .max(255, "Description must be 255 characters or less")
    .optional(),
  start_time: z.string().optional(),
  end_time: z.string().optional(),
  min_bw: z.number().min(0).max(100).optional(),
  min_bw_strict: z.boolean().optional(),
  max_delay: z.number().min(0).max(1000).optional(),
  max_delay_strict: z.boolean().optional(),
  max_number_oxps: z.number().min(0).max(100).optional(),
  max_number_oxps_strict: z.boolean().optional(),
  notifications: z
    .array(
      z.object({
        email: z.string().email("Invalid email address"),
      })
    )
    .max(10, "Maximum 10 notification emails allowed")
    .optional(),
});

type L2VPNFormData = z.infer<typeof l2vpnSchema>;

interface NewL2VPNModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: (l2vpnData: any) => void;
  availablePorts?: Array<{
    id: string;
    entities: string[];
    vlan_range?: number[];
  }>;
  inline?: boolean; // If true, renders inline without Dialog wrapper
}

export function NewL2VPNModal({
  isOpen,
  onClose,
  onConfirm,
  availablePorts = [],
  inline = false,
}: NewL2VPNModalProps) {
  const [isLoading, setIsLoading] = useState(false);
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [searchTerms, setSearchTerms] = useState<{ [key: number]: string }>({});
  const [filteredPorts, setFilteredPorts] = useState<{
    [key: number]: typeof availablePorts;
  }>({});
  const [showDropdown, setShowDropdown] = useState<{ [key: number]: boolean }>(
    {}
  );
  const dropdownRefs = useRef<{ [key: number]: HTMLDivElement | null }>({});

  const {
    register,
    control,
    handleSubmit,
    watch,
    setValue,
    reset,
    formState: { errors },
  } = useForm<L2VPNFormData>({
    resolver: zodResolver(l2vpnSchema),
    defaultValues: {
      name: "",
      endpoints: [
        { port_id: "", vlan_type: "any", vlan_value: "" },
        { port_id: "", vlan_type: "any", vlan_value: "" },
      ],
      description: "",
      start_time: "",
      end_time: "",
      min_bw_strict: false,
      max_delay_strict: false,
      max_number_oxps_strict: false,
      notifications: [],
    },
  });

  const {
    fields: endpointFields,
    append: appendEndpoint,
    remove: removeEndpoint,
  } = useFieldArray({
    control,
    name: "endpoints",
  });

  const {
    fields: notificationFields,
    append: appendNotification,
    remove: removeNotification,
  } = useFieldArray({
    control,
    name: "notifications",
  });

  const watchedEndpoints = watch("endpoints");

  // Filter ports based on search term matching entities
  const getMatchingPorts = (searchTerm: string) => {
    if (!searchTerm) return availablePorts;
    const lowerSearch = searchTerm.toLowerCase();
    const matches = availablePorts.filter(
      (port) =>
        port.entities &&
        port.entities.some((entity) =>
          entity.toLowerCase().includes(lowerSearch)
        )
    );
    console.log(
      `Searching for "${searchTerm}": found ${matches.length} matches out of ${availablePorts.length} ports`
    );
    return matches;
  };

  // Handle search input change
  const handleSearchChange = (index: number, value: string) => {
    setSearchTerms((prev) => ({ ...prev, [index]: value }));
    const filtered = getMatchingPorts(value);
    setFilteredPorts((prev) => ({ ...prev, [index]: filtered }));
    setShowDropdown((prev) => ({ ...prev, [index]: true }));
  };

  // Handle port selection from dropdown
  const handlePortSelect = (index: number, portId: string) => {
    const shortPortId = portId.replace("urn:sdx:port:", "");
    setSearchTerms((prev) => ({ ...prev, [index]: shortPortId }));
    setValue(`endpoints.${index}.port_id`, portId);
    setShowDropdown((prev) => ({ ...prev, [index]: false }));
  };

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      Object.keys(dropdownRefs.current).forEach((key) => {
        const index = Number(key);
        const ref = dropdownRefs.current[index];
        if (ref && !ref.contains(event.target as Node)) {
          setShowDropdown((prev) => ({ ...prev, [index]: false }));
        }
      });
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const onSubmit = async (data: L2VPNFormData) => {
    setIsLoading(true);

    try {
      // Transform data to match backend API format
      const transformedData = {
        name: data.name,
        endpoints: data.endpoints.map((ep) => ({
          port_id: ep.port_id,
          vlan:
            ep.vlan_type === "number" || ep.vlan_type === "VLAN range"
              ? ep.vlan_value
              : ep.vlan_type,
        })),
        ...(data.description && { description: data.description }),
        ...(data.start_time || data.end_time
          ? {
              scheduling: {
                ...(data.start_time && {
                  start_time: new Date(data.start_time).toISOString(),
                }),
                ...(data.end_time && {
                  end_time: new Date(data.end_time).toISOString(),
                }),
              },
            }
          : {}),
        ...(data.min_bw !== undefined ||
        data.max_delay !== undefined ||
        data.max_number_oxps !== undefined
          ? {
              qos_metrics: {
                ...(data.min_bw !== undefined && {
                  min_bw: {
                    value: data.min_bw,
                    strict: data.min_bw_strict || false,
                  },
                }),
                ...(data.max_delay !== undefined && {
                  max_delay: {
                    value: data.max_delay,
                    strict: data.max_delay_strict || false,
                  },
                }),
                ...(data.max_number_oxps !== undefined && {
                  max_number_oxps: {
                    value: data.max_number_oxps,
                    strict: data.max_number_oxps_strict || false,
                  },
                }),
              },
            }
          : {}),
        ...(data.notifications &&
          data.notifications.length > 0 && {
            notifications: data.notifications,
          }),
      };

      console.log("Transformed L2VPN Data:", transformedData);

      // Simulate API call - replace with actual API integration
      await new Promise((resolve) => setTimeout(resolve, 1500));

      onConfirm(transformedData);
      toast.success(`L2VPN "${data.name}" request submitted successfully!`);

      reset();
      onClose();
    } catch (error) {
      toast.error("Failed to create L2VPN connection");
      console.error("L2VPN creation error:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const getVlanRangeForPort = (portId: string) => {
    const port = availablePorts.find((p) => p.id === portId);
    return port?.vlan_range?.join(", ") || "N/A";
  };

  const handleReset = () => {
    reset();
  };

  const formContent = (
    <>
      {!inline && (
        <DialogHeader className="pb-4 border-b border-[rgb(50,135,200)]/20 dark:border-[rgb(100,180,255)]/20 mb-6">
          <DialogTitle className="text-2xl font-bold text-[rgb(50,135,200)] dark:text-[rgb(100,180,255)] flex items-center gap-3">
            <span className="text-3xl">🔗</span>
            <span>Create New L2VPN Connection</span>
          </DialogTitle>
          <DialogDescription className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] mt-2 text-base font-medium">
            Set up a Layer 2 Virtual Private Network connection between multiple
            endpoints in the SDX topology.
          </DialogDescription>
        </DialogHeader>
      )}

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        {/* Connection Name */}
        <div className="space-y-2 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
          <Label
            htmlFor="name"
            className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold flex items-center gap-1 text-sm"
          >
            Connection Name <span className="text-red-500 font-bold">*</span>
          </Label>
          <Input
            id="name"
            placeholder="e.g., Research-Miami-SP-Link"
            {...register("name")}
            className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
          />
          {errors.name && (
            <p className="text-red-500 dark:text-red-400 text-sm font-medium mt-1 flex items-center gap-1">
              <span>⚠️</span> {errors.name.message}
            </p>
          )}
        </div>

        {/* Endpoints Section */}
        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 bg-gradient-to-r from-[rgb(236,244,250)] to-[rgb(248,251,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md">
            <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-bold text-lg flex items-center gap-2">
              <span className="text-xl">📍</span>
              <span>Endpoints</span>
            </Label>
            <Button
              type="button"
              onClick={() =>
                appendEndpoint({
                  port_id: "",
                  vlan_type: "any",
                  vlan_value: "",
                })
              }
              className="bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] dark:bg-[rgb(100,180,255)] dark:hover:bg-[rgb(120,200,255)] text-white shadow-md hover:shadow-lg transition-all duration-200 hover:scale-105 active:scale-95"
              size="sm"
            >
              <Plus className="w-4 h-4 mr-1" />
              Add Endpoint
            </Button>
          </div>

          {endpointFields.map((field, index) => {
            const vlanType = watchedEndpoints[index]?.vlan_type;
            const portId = watchedEndpoints[index]?.port_id;

            return (
              <div
                key={field.id}
                className="p-6 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-md hover:shadow-lg transition-all duration-200 space-y-4"
              >
                <div className="flex items-center justify-between pb-3 border-b-2 border-[rgb(200,220,240)] dark:border-blue-500/20">
                  <h4 className="font-bold text-[rgb(50,135,200)] dark:text-[rgb(150,200,255)] text-lg">
                    Endpoint {index + 1}
                  </h4>
                  {index >= 2 && (
                    <Button
                      type="button"
                      variant="destructive"
                      size="sm"
                      onClick={() => removeEndpoint(index)}
                      className="bg-red-500 hover:bg-red-600 dark:bg-red-600 dark:hover:bg-red-700 shadow-sm hover:shadow-md transition-all hover:scale-105 active:scale-95"
                    >
                      <Trash2 className="w-4 h-4 mr-1" />
                      Delete
                    </Button>
                  )}
                </div>

                <div className="space-y-4">
                  {/* Port ID - Searchable */}
                  <div className="space-y-2">
                    <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold flex items-center gap-1 text-sm">
                      Port ID <span className="text-red-500 font-bold">*</span>
                    </Label>
                    <div
                      className="relative"
                      ref={(el) => {
                        dropdownRefs.current[index] = el;
                      }}
                    >
                      <Controller
                        control={control}
                        name={`endpoints.${index}.port_id`}
                        render={({ field }) => (
                          <>
                            <Input
                              type="text"
                              placeholder="Search institute/organization"
                              value={searchTerms[index] || ""}
                              onChange={(e) => {
                                handleSearchChange(index, e.target.value);
                                field.onChange(e.target.value);
                              }}
                              onFocus={() => {
                                const filtered = getMatchingPorts(
                                  searchTerms[index] || ""
                                );
                                setFilteredPorts((prev) => ({
                                  ...prev,
                                  [index]: filtered,
                                }));
                                setShowDropdown((prev) => ({
                                  ...prev,
                                  [index]: true,
                                }));
                              }}
                              className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
                            />

                            {/* Dropdown List */}
                            {showDropdown[index] && (
                              <div className="absolute z-50 w-full mt-1 bg-background dark:bg-gray-800 border-2 border-[rgb(50,135,200)] dark:border-[rgb(100,180,255)] rounded-lg shadow-xl max-h-[192px] overflow-y-auto">
                                <ul>
                                  {(filteredPorts[index] || availablePorts)
                                    .length === 0 ? (
                                    <li className="px-4 py-3 text-muted-foreground text-sm">
                                      No matches found
                                    </li>
                                  ) : (
                                    (
                                      filteredPorts[index] || availablePorts
                                    ).map((port) => {
                                      const shortPortId = port.id.replace(
                                        "urn:sdx:port:",
                                        ""
                                      );
                                      const entitiesText = port.entities
                                        ? port.entities.join(", ")
                                        : "No entities";

                                      return (
                                        <li
                                          key={port.id}
                                          className="px-4 py-3 cursor-pointer hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 transition-colors border-b border-border/50 last:border-b-0"
                                          onClick={() =>
                                            handlePortSelect(index, port.id)
                                          }
                                        >
                                          <span className="text-xs text-muted-foreground">
                                            ({shortPortId})
                                          </span>{" "}
                                          <strong className="text-foreground">
                                            {entitiesText}
                                          </strong>
                                        </li>
                                      );
                                    })
                                  )}
                                </ul>
                              </div>
                            )}
                          </>
                        )}
                      />
                    </div>
                    {errors.endpoints?.[index]?.port_id && (
                      <p className="text-red-500 dark:text-red-400 text-sm font-medium mt-1 flex items-center gap-1">
                        <span>⚠️</span>{" "}
                        {errors.endpoints[index]?.port_id?.message}
                      </p>
                    )}
                  </div>

                  {/* VLAN Type */}
                  <div className="space-y-2">
                    <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold flex items-center gap-1 text-sm">
                      VLAN <span className="text-red-500 font-bold">*</span>
                    </Label>
                    <Controller
                      control={control}
                      name={`endpoints.${index}.vlan_type`}
                      render={({ field }) => (
                        <Select
                          value={field.value}
                          onValueChange={field.onChange}
                        >
                          <SelectTrigger className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 w-full bg-white dark:bg-gray-800 transition-all text-base">
                            <SelectValue />
                          </SelectTrigger>
                          <SelectContent className="bg-white dark:bg-gray-800 border-2 border-[rgb(50,135,200)] dark:border-[rgb(100,180,255)] shadow-lg">
                            <SelectItem
                              value="any"
                              title="Any available VLAN ID is chosen"
                              className="hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20"
                            >
                              any
                            </SelectItem>
                            <SelectItem
                              value="number"
                              title="Specific VLAN ID, e.g., '50'"
                              className="hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20"
                            >
                              VLAN ID
                            </SelectItem>
                            <SelectItem
                              value="untagged"
                              title="Transports Ethernet frames without IEEE 802.1Q Ethertype"
                              className="hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20"
                            >
                              untagged
                            </SelectItem>
                            <SelectItem
                              value="VLAN range"
                              title="Range of VLANs, e.g., '50:55'"
                              className="hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20"
                            >
                              VLAN range
                            </SelectItem>
                            <SelectItem
                              value="all"
                              title="Transport all Ethernet frames with and without IEEE 802.Q Ethertype"
                              className="hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20"
                            >
                              all
                            </SelectItem>
                          </SelectContent>
                        </Select>
                      )}
                    />
                  </div>
                </div>

                {/* Conditional VLAN Value Input */}
                {(vlanType === "number" || vlanType === "VLAN range") && (
                  <div className="space-y-2 p-3 bg-[rgb(248,251,255)] dark:bg-blue-500/5 rounded-lg border border-[rgb(200,220,240)] dark:border-blue-500/20">
                    <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold text-sm">
                      {vlanType === "number"
                        ? "VLAN ID (1-4095)"
                        : "VLAN Range (e.g., 50:55)"}
                    </Label>
                    <Input
                      placeholder={
                        portId
                          ? `Available VLANs: ${getVlanRangeForPort(portId)}`
                          : vlanType === "number"
                          ? "Enter VLAN ID"
                          : "Enter VLAN Range"
                      }
                      {...register(`endpoints.${index}.vlan_value`)}
                      className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
                    />
                    {errors.endpoints?.[index]?.vlan_value && (
                      <p className="text-red-500 dark:text-red-400 text-sm font-medium mt-1 flex items-center gap-1">
                        <span>⚠️</span>{" "}
                        {errors.endpoints[index]?.vlan_value?.message}
                      </p>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* Description */}
        <div className="space-y-2 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
          <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold text-sm">
            Description
          </Label>
          <Textarea
            placeholder="Optional description for this L2VPN connection..."
            {...register("description")}
            className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 min-h-[100px] bg-white dark:bg-gray-800 transition-all resize-none text-base"
          />
          {errors.description && (
            <p className="text-red-500 dark:text-red-400 text-sm font-medium mt-1 flex items-center gap-1">
              <span>⚠️</span> {errors.description.message}
            </p>
          )}
        </div>

        {/* Start and End Time */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="space-y-2 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
            <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold text-sm">
              Start Time (optional)
            </Label>
            <Input
              type="date"
              {...register("start_time")}
              min={new Date().toISOString().split("T")[0]}
              className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
            />
          </div>
          <div className="space-y-2 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-sm hover:shadow-md transition-all duration-200">
            <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold text-sm">
              End Time (optional)
            </Label>
            <Input
              type="date"
              {...register("end_time")}
              min={new Date().toISOString().split("T")[0]}
              className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
            />
          </div>
        </div>

        {/* Advanced Options Toggle */}
        <div>
          <Button
            type="button"
            variant="outline"
            onClick={() => setShowAdvanced(!showAdvanced)}
            className="w-full border-2 border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(50,135,200)] dark:hover:border-[rgb(100,180,255)] transition-all duration-200 font-semibold shadow-sm hover:shadow-md hover:scale-[1.02] active:scale-[0.98]"
          >
            {showAdvanced ? (
              <>
                <ChevronUp className="w-4 h-4 mr-2" />
                Hide Advanced Options
              </>
            ) : (
              <>
                <ChevronDown className="w-4 h-4 mr-2" />
                Show Advanced Options
              </>
            )}
          </Button>
        </div>

        {/* Advanced Options */}
        {showAdvanced && (
          <div className="space-y-4 p-5 bg-gradient-to-br from-[rgb(248,251,255)] to-[rgb(240,247,255)] dark:from-blue-500/10 dark:to-blue-500/5 rounded-xl border-2 border-[rgb(200,220,240)] dark:border-blue-500/20 shadow-lg">
            <h3 className="font-bold text-[rgb(50,135,200)] dark:text-[rgb(150,200,255)] text-lg mb-2 pb-2 border-b border-[rgb(200,220,240)] dark:border-blue-500/20">
              QoS Metrics
            </h3>

            {/* Minimum Bandwidth */}
            <div className="space-y-2">
              <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold text-sm">
                Minimum Bandwidth (Gbps)
              </Label>
              <div className="flex items-center gap-4">
                <Input
                  type="number"
                  placeholder="0-100"
                  {...register("min_bw", { valueAsNumber: true })}
                  min="0"
                  max="100"
                  step="1"
                  className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
                />
                <div className="flex items-center gap-2 whitespace-nowrap">
                  <Controller
                    control={control}
                    name="min_bw_strict"
                    render={({ field }) => (
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                        id="min_bw_strict"
                        className="border-[rgb(120,176,219)] data-[state=checked]:bg-[rgb(50,135,200)] data-[state=checked]:border-[rgb(50,135,200)]"
                      />
                    )}
                  />
                  <Label
                    htmlFor="min_bw_strict"
                    className="font-normal cursor-pointer text-[rgb(64,143,204)]"
                  >
                    Strict
                  </Label>
                </div>
              </div>
            </div>

            {/* Maximum Delay */}
            <div className="space-y-2">
              <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold text-sm">
                Maximum Delay (ms)
              </Label>
              <div className="flex items-center gap-4">
                <Input
                  type="number"
                  placeholder="0-1000"
                  {...register("max_delay", { valueAsNumber: true })}
                  min="0"
                  max="1000"
                  step="1"
                  className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
                />
                <div className="flex items-center gap-2 whitespace-nowrap">
                  <Controller
                    control={control}
                    name="max_delay_strict"
                    render={({ field }) => (
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                        id="max_delay_strict"
                        className="border-[rgb(120,176,219)] data-[state=checked]:bg-[rgb(50,135,200)] data-[state=checked]:border-[rgb(50,135,200)]"
                      />
                    )}
                  />
                  <Label
                    htmlFor="max_delay_strict"
                    className="font-normal cursor-pointer text-[rgb(64,143,204)]"
                  >
                    Strict
                  </Label>
                </div>
              </div>
            </div>

            {/* Maximum Number of OXPs */}
            <div className="space-y-2">
              <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold text-sm">
                Maximum Number of OXPs
              </Label>
              <div className="flex items-center gap-4">
                <Input
                  type="number"
                  placeholder="0-100"
                  {...register("max_number_oxps", { valueAsNumber: true })}
                  min="0"
                  max="100"
                  step="1"
                  className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
                />
                <div className="flex items-center gap-2 whitespace-nowrap">
                  <Controller
                    control={control}
                    name="max_number_oxps_strict"
                    render={({ field }) => (
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                        id="max_number_oxps_strict"
                        className="border-[rgb(120,176,219)] data-[state=checked]:bg-[rgb(50,135,200)] data-[state=checked]:border-[rgb(50,135,200)]"
                      />
                    )}
                  />
                  <Label
                    htmlFor="max_number_oxps_strict"
                    className="font-normal cursor-pointer text-[rgb(64,143,204)]"
                  >
                    Strict
                  </Label>
                </div>
              </div>
            </div>

            {/* Notifications */}
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <Label className="text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] font-semibold text-sm">
                  Notifications
                </Label>
                {notificationFields.length < 10 && (
                  <Button
                    type="button"
                    variant="outline"
                    size="sm"
                    onClick={() => appendNotification({ email: "" })}
                    className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(50,135,200)] dark:hover:border-[rgb(100,180,255)] transition-all shadow-sm hover:shadow-md"
                  >
                    <Plus className="w-4 h-4 mr-1" />
                    Add Notification
                  </Button>
                )}
              </div>

              {notificationFields.map((field, index) => (
                <div key={field.id} className="flex items-center gap-2">
                  <Input
                    type="email"
                    placeholder={`Notification Email ${index + 1} (optional)`}
                    {...register(`notifications.${index}.email`)}
                    className="border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] focus:border-[rgb(50,135,200)] dark:focus:border-[rgb(100,180,255)] focus:ring-2 focus:ring-[rgb(50,135,200)]/30 dark:focus:ring-[rgb(100,180,255)]/30 bg-white dark:bg-gray-800 transition-all text-base"
                  />
                  <Button
                    type="button"
                    variant="destructive"
                    size="sm"
                    onClick={() => removeNotification(index)}
                    className="bg-red-500 hover:bg-red-600 dark:bg-red-600 dark:hover:bg-red-700 shadow-sm hover:shadow-md transition-all hover:scale-105 active:scale-95"
                  >
                    <Trash2 className="w-4 h-4" />
                  </Button>
                </div>
              ))}
            </div>
          </div>
        )}

        {inline ? (
          <div className="flex gap-3 pt-6 border-t-2 border-[rgb(200,220,240)] dark:border-blue-500/20 mt-6">
            <Button
              type="button"
              variant="outline"
              onClick={handleReset}
              disabled={isLoading}
              className="border-2 border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(50,135,200)] dark:hover:border-[rgb(100,180,255)] transition-all duration-200 shadow-sm hover:shadow-md disabled:opacity-50 hover:scale-105 active:scale-95 font-medium"
            >
              Reset
            </Button>

            <Button
              type="button"
              variant="outline"
              onClick={onClose}
              disabled={isLoading}
              className="border-2 border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(50,135,200)] dark:hover:border-[rgb(100,180,255)] transition-all duration-200 shadow-sm hover:shadow-md disabled:opacity-50 hover:scale-105 active:scale-95 font-medium"
            >
              Cancel
            </Button>

            <Button
              type="submit"
              disabled={isLoading}
              className="bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] dark:bg-[rgb(100,180,255)] dark:hover:bg-[rgb(120,200,255)] text-white px-8 shadow-lg hover:shadow-xl transition-all duration-200 font-semibold disabled:opacity-50 hover:scale-105 active:scale-95 ml-auto"
            >
              {isLoading ? (
                <span className="flex items-center gap-2">
                  <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
                  Creating...
                </span>
              ) : (
                "Create L2VPN"
              )}
            </Button>
          </div>
        ) : (
          <DialogFooter className="flex gap-3 pt-6 border-t-2 border-[rgb(200,220,240)] dark:border-blue-500/20 mt-6">
            <Button
              type="button"
              variant="outline"
              onClick={handleReset}
              disabled={isLoading}
              className="border-2 border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(50,135,200)] dark:hover:border-[rgb(100,180,255)] transition-all duration-200 shadow-sm hover:shadow-md disabled:opacity-50 hover:scale-105 active:scale-95 font-medium"
            >
              Reset
            </Button>

            <Button
              type="button"
              variant="outline"
              onClick={onClose}
              disabled={isLoading}
              className="border-2 border-[rgb(120,176,219)] dark:border-[rgb(100,150,200)] text-[rgb(64,143,204)] dark:text-[rgb(150,200,255)] hover:bg-[rgb(236,244,250)] dark:hover:bg-blue-500/20 hover:border-[rgb(50,135,200)] dark:hover:border-[rgb(100,180,255)] transition-all duration-200 shadow-sm hover:shadow-md disabled:opacity-50 hover:scale-105 active:scale-95 font-medium"
            >
              Cancel
            </Button>

            <Button
              type="submit"
              disabled={isLoading}
              className="bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] dark:bg-[rgb(100,180,255)] dark:hover:bg-[rgb(120,200,255)] text-white px-8 shadow-lg hover:shadow-xl transition-all duration-200 font-semibold disabled:opacity-50 hover:scale-105 active:scale-95"
            >
              {isLoading ? (
                <span className="flex items-center gap-2">
                  <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
                  Creating...
                </span>
              ) : (
                "Create L2VPN"
              )}
            </Button>
          </DialogFooter>
        )}
      </form>
    </>
  );

  if (inline) {
    return <div className="overflow-y-auto">{formContent}</div>;
  }

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-[900px] max-h-[95vh] overflow-y-auto bg-gradient-to-br from-background via-background to-muted/20 border-2 border-[rgb(50,135,200)]/40 dark:border-[rgb(100,180,255)]/40 shadow-2xl backdrop-blur-sm">
        {formContent}
      </DialogContent>
    </Dialog>
  );
}

export type { L2VPNFormData };
