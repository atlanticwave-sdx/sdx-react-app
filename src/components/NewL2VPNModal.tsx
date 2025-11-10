import { useState, useRef, useEffect } from "react";
import { useForm, useFieldArray, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { Checkbox } from "@/components/ui/checkbox";
import { toast } from "sonner";
import { Trash2, Plus, ChevronDown, ChevronUp } from "lucide-react";

// Zod schema for form validation
const endpointSchema = z.object({
  port_id: z.string().min(1, "Port ID is required"),
  vlan_type: z.enum(["any", "number", "untagged", "VLAN range", "all"]),
  vlan_value: z.string().optional(),
}).refine((data) => {
  if (data.vlan_type === "number" || data.vlan_type === "VLAN range") {
    return data.vlan_value && data.vlan_value.length > 0;
  }
  return true;
}, {
  message: "VLAN value is required for this type",
  path: ["vlan_value"],
});

const l2vpnSchema = z.object({
  name: z.string().min(1, "Connection name is required").max(50, "Name must be 50 characters or less"),
  endpoints: z.array(endpointSchema).min(2, "At least 2 endpoints are required"),
  description: z.string().max(255, "Description must be 255 characters or less").optional(),
  start_time: z.string().optional(),
  end_time: z.string().optional(),
  min_bw: z.number().min(0).max(100).optional(),
  min_bw_strict: z.boolean().optional(),
  max_delay: z.number().min(0).max(1000).optional(),
  max_delay_strict: z.boolean().optional(),
  max_number_oxps: z.number().min(0).max(100).optional(),
  max_number_oxps_strict: z.boolean().optional(),
  notifications: z.array(z.object({
    email: z.string().email("Invalid email address")
  })).max(10, "Maximum 10 notification emails allowed").optional(),
});

type L2VPNFormData = z.infer<typeof l2vpnSchema>;

interface NewL2VPNModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: (l2vpnData: any) => void;
  availablePorts?: Array<{ id: string; entities: string[]; vlan_range?: number[] }>;
}

export function NewL2VPNModal({ isOpen, onClose, onConfirm, availablePorts = [] }: NewL2VPNModalProps) {
  const [isLoading, setIsLoading] = useState(false);
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [searchTerms, setSearchTerms] = useState<{ [key: number]: string }>({});
  const [filteredPorts, setFilteredPorts] = useState<{ [key: number]: typeof availablePorts }>({});
  const [showDropdown, setShowDropdown] = useState<{ [key: number]: boolean }>({});
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

  const { fields: endpointFields, append: appendEndpoint, remove: removeEndpoint } = useFieldArray({
    control,
    name: "endpoints",
  });

  const { fields: notificationFields, append: appendNotification, remove: removeNotification } = useFieldArray({
    control,
    name: "notifications",
  });

  const watchedEndpoints = watch("endpoints");

  // Filter ports based on search term matching entities
  const getMatchingPorts = (searchTerm: string) => {
    if (!searchTerm) return availablePorts;
    const lowerSearch = searchTerm.toLowerCase();
    const matches = availablePorts.filter(port =>
      port.entities && port.entities.some(entity => entity.toLowerCase().includes(lowerSearch))
    );
    console.log(`Searching for "${searchTerm}": found ${matches.length} matches out of ${availablePorts.length} ports`);
    return matches;
  };

  // Handle search input change
  const handleSearchChange = (index: number, value: string) => {
    setSearchTerms(prev => ({ ...prev, [index]: value }));
    const filtered = getMatchingPorts(value);
    setFilteredPorts(prev => ({ ...prev, [index]: filtered }));
    setShowDropdown(prev => ({ ...prev, [index]: true }));
  };

  // Handle port selection from dropdown
  const handlePortSelect = (index: number, portId: string) => {
    const shortPortId = portId.replace("urn:sdx:port:", "");
    setSearchTerms(prev => ({ ...prev, [index]: shortPortId }));
    setValue(`endpoints.${index}.port_id`, portId);
    setShowDropdown(prev => ({ ...prev, [index]: false }));
  };

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      Object.keys(dropdownRefs.current).forEach(key => {
        const index = Number(key);
        const ref = dropdownRefs.current[index];
        if (ref && !ref.contains(event.target as Node)) {
          setShowDropdown(prev => ({ ...prev, [index]: false }));
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
        endpoints: data.endpoints.map(ep => ({
          port_id: ep.port_id,
          vlan: ep.vlan_type === "number" || ep.vlan_type === "VLAN range"
            ? ep.vlan_value
            : ep.vlan_type
        })),
        ...(data.description && { description: data.description }),
        ...(data.start_time || data.end_time ? {
          scheduling: {
            ...(data.start_time && { start_time: new Date(data.start_time).toISOString() }),
            ...(data.end_time && { end_time: new Date(data.end_time).toISOString() }),
          }
        } : {}),
        ...((data.min_bw !== undefined || data.max_delay !== undefined || data.max_number_oxps !== undefined) ? {
          qos_metrics: {
            ...(data.min_bw !== undefined && {
              min_bw: { value: data.min_bw, strict: data.min_bw_strict || false }
            }),
            ...(data.max_delay !== undefined && {
              max_delay: { value: data.max_delay, strict: data.max_delay_strict || false }
            }),
            ...(data.max_number_oxps !== undefined && {
              max_number_oxps: { value: data.max_number_oxps, strict: data.max_number_oxps_strict || false }
            }),
          }
        } : {}),
        ...(data.notifications && data.notifications.length > 0 && {
          notifications: data.notifications
        }),
      };

      console.log("Transformed L2VPN Data:", transformedData);

      // Simulate API call - replace with actual API integration
      await new Promise(resolve => setTimeout(resolve, 1500));

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
    const port = availablePorts.find(p => p.id === portId);
    return port?.vlan_range?.join(", ") || "N/A";
  };

  const handleReset = () => {
    reset();
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-[900px] max-h-[95vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="text-xl text-[rgb(64,143,204)] flex items-center gap-2">
            <span className="text-2xl">🔗</span>
            Create New L2VPN Connection
          </DialogTitle>
          <DialogDescription className="text-[rgb(50,135,200)]">
            Set up a Layer 2 Virtual Private Network connection between multiple endpoints in the SDX topology.
          </DialogDescription>
        </DialogHeader>

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
          {/* Connection Name */}
          <div className="space-y-2">
            <Label htmlFor="name" className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
              Connection Name <span className="text-red-500">*</span>
            </Label>
            <Input
              id="name"
              placeholder="e.g., Research-Miami-SP-Link"
              {...register("name")}
              className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)] focus:ring-2 focus:ring-[rgb(50,135,200)]/20"
            />
            {errors.name && (
              <p className="text-red-500 text-sm">{errors.name.message}</p>
            )}
          </div>

          {/* Endpoints Section */}
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <Label className="text-[rgb(64,143,204)] font-semibold text-lg flex items-center gap-2">
                <span className="text-xl">📍</span>
                Endpoints
              </Label>
              <Button
                type="button"
                onClick={() => appendEndpoint({ port_id: "", vlan_type: "any", vlan_value: "" })}
                className="bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-white"
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
                  className="p-4 bg-[rgb(248,251,255)] rounded-lg border border-[rgb(200,220,240)] space-y-4"
                >
                  <div className="flex items-center justify-between">
                    <h4 className="font-medium text-[rgb(64,143,204)]">Endpoint {index + 1}</h4>
                    {index >= 2 && (
                      <Button
                        type="button"
                        variant="destructive"
                        size="sm"
                        onClick={() => removeEndpoint(index)}
                        className="bg-red-500 hover:bg-red-600"
                      >
                        <Trash2 className="w-4 h-4 mr-1" />
                        Delete
                      </Button>
                    )}
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {/* Port ID - Searchable */}
                    <div className="space-y-2">
                      <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                        Port ID <span className="text-red-500">*</span>
                      </Label>
                      <div className="relative" ref={el => dropdownRefs.current[index] = el}>
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
                                  const filtered = getMatchingPorts(searchTerms[index] || "");
                                  setFilteredPorts(prev => ({ ...prev, [index]: filtered }));
                                  setShowDropdown(prev => ({ ...prev, [index]: true }));
                                }}
                                className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)] focus:ring-2 focus:ring-[rgb(50,135,200)]/20 text-black"
                              />

                              {/* Dropdown List */}
                              {showDropdown[index] && (
                                <div className="absolute z-50 w-full mt-1 bg-white border border-[rgb(120,176,219)] rounded-md shadow-lg max-h-60 overflow-auto">
                                  <ul>
                                    {(filteredPorts[index] || availablePorts).length === 0 ? (
                                      <li className="px-4 py-2 text-gray-500">No matches found</li>
                                    ) : (
                                      (filteredPorts[index] || availablePorts).map((port) => {
                                        const shortPortId = port.id.replace("urn:sdx:port:", "");
                                        const entitiesText = port.entities ? port.entities.join(", ") : "No entities";

                                        return (
                                          <li
                                            key={port.id}
                                            className="px-4 py-2 cursor-pointer hover:bg-[rgb(236,244,250)] transition-colors text-black"
                                            onClick={() => handlePortSelect(index, port.id)}
                                          >
                                            ({shortPortId}) <strong>{entitiesText}</strong>
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
                        <p className="text-red-500 text-sm">{errors.endpoints[index]?.port_id?.message}</p>
                      )}
                    </div>

                    {/* VLAN Type */}
                    <div className="space-y-2 md:col-span-1">
                      <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                        VLAN <span className="text-red-500">*</span>
                      </Label>
                      <Controller
                        control={control}
                        name={`endpoints.${index}.vlan_type`}
                        render={({ field }) => (
                          <Select value={field.value} onValueChange={field.onChange}>
                            <SelectTrigger className="border-[rgb(120,176,219)] text-black w-full bg-white">
                              <SelectValue className="text-black" />
                            </SelectTrigger>
                            <SelectContent className="text-black bg-white">
                              <SelectItem value="any" title="Any available VLAN ID is chosen">any</SelectItem>
                              <SelectItem value="number" title="Specific VLAN ID, e.g., '50'">VLAN ID</SelectItem>
                              <SelectItem value="untagged" title="Transports Ethernet frames without IEEE 802.1Q Ethertype">untagged</SelectItem>
                              <SelectItem value="VLAN range" title="Range of VLANs, e.g., '50:55'">VLAN range</SelectItem>
                              <SelectItem value="all" title="Transport all Ethernet frames with and without IEEE 802.Q Ethertype">all</SelectItem>
                            </SelectContent>
                          </Select>
                        )}
                      />
                    </div>
                  </div>

                  {/* Conditional VLAN Value Input */}
                  {(vlanType === "number" || vlanType === "VLAN range") && (
                    <div className="space-y-2">
                      <Label className="text-[rgb(64,143,204)] font-medium">
                        {vlanType === "number" ? "VLAN ID (1-4095)" : "VLAN Range (e.g., 50:55)"}
                      </Label>
                      <Input
                        placeholder={
                          portId
                            ? `Available VLANs: ${getVlanRangeForPort(portId)}`
                            : vlanType === "number" ? "Enter VLAN ID" : "Enter VLAN Range"
                        }
                        {...register(`endpoints.${index}.vlan_value`)}
                        className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)] text-black"
                      />
                      {errors.endpoints?.[index]?.vlan_value && (
                        <p className="text-red-500 text-sm">{errors.endpoints[index]?.vlan_value?.message}</p>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {/* Description */}
          <div className="space-y-2">
            <Label className="text-[rgb(64,143,204)] font-medium">
              Description
            </Label>
            <Textarea
              placeholder="Optional description for this L2VPN connection..."
              {...register("description")}
              className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)] min-h-[80px]"
            />
            {errors.description && (
              <p className="text-red-500 text-sm">{errors.description.message}</p>
            )}
          </div>

          {/* Start and End Time */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label className="text-[rgb(64,143,204)] font-medium">
                Start Time (optional)
              </Label>
              <Input
                type="date"
                {...register("start_time")}
                min={new Date().toISOString().split('T')[0]}
                className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
              />
            </div>
            <div className="space-y-2">
              <Label className="text-[rgb(64,143,204)] font-medium">
                End Time (optional)
              </Label>
              <Input
                type="date"
                {...register("end_time")}
                min={new Date().toISOString().split('T')[0]}
                className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
              />
            </div>
          </div>

          {/* Advanced Options Toggle */}
          <div>
            <Button
              type="button"
              variant="outline"
              onClick={() => setShowAdvanced(!showAdvanced)}
              className="w-full border-[rgb(120,176,219)] text-[rgb(64,143,204)] hover:bg-[rgb(236,244,250)]"
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
            <div className="space-y-4 p-4 bg-[rgb(248,251,255)] rounded-lg border border-[rgb(200,220,240)]">
              <h3 className="font-semibold text-[rgb(64,143,204)]">QoS Metrics</h3>

              {/* Minimum Bandwidth */}
              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium">
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
                    className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
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
                    <Label htmlFor="min_bw_strict" className="font-normal cursor-pointer text-[rgb(64,143,204)]">
                      Strict
                    </Label>
                  </div>
                </div>
              </div>

              {/* Maximum Delay */}
              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium">
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
                    className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
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
                    <Label htmlFor="max_delay_strict" className="font-normal cursor-pointer text-[rgb(64,143,204)]">
                      Strict
                    </Label>
                  </div>
                </div>
              </div>

              {/* Maximum Number of OXPs */}
              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium">
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
                    className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
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
                    <Label htmlFor="max_number_oxps_strict" className="font-normal cursor-pointer text-[rgb(64,143,204)]">
                      Strict
                    </Label>
                  </div>
                </div>
              </div>

              {/* Notifications */}
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <Label className="text-[rgb(64,143,204)] font-medium">
                    Notifications
                  </Label>
                  {notificationFields.length < 10 && (
                    <Button
                      type="button"
                      variant="outline"
                      size="sm"
                      onClick={() => appendNotification({ email: "" })}
                      className="border-[rgb(120,176,219)] text-[rgb(64,143,204)]"
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
                      className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
                    />
                    <Button
                      type="button"
                      variant="destructive"
                      size="sm"
                      onClick={() => removeNotification(index)}
                      className="bg-red-500 hover:bg-red-600"
                    >
                      <Trash2 className="w-4 h-4" />
                    </Button>
                  </div>
                ))}
              </div>
            </div>
          )}

          <DialogFooter className="flex gap-3">
            <Button
              type="button"
              variant="outline"
              onClick={handleReset}
              disabled={isLoading}
              className="border-[rgb(120,176,219)] text-[rgb(64,143,204)] hover:bg-[rgb(236,244,250)]"
            >
              Reset
            </Button>

            <Button
              type="button"
              variant="outline"
              onClick={onClose}
              disabled={isLoading}
              className="border-[rgb(120,176,219)] text-[rgb(64,143,204)] hover:bg-[rgb(236,244,250)]"
            >
              Cancel
            </Button>

            <Button
              type="submit"
              disabled={isLoading}
              className="bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-white px-6"
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
        </form>
      </DialogContent>
    </Dialog>
  );
}

export type { L2VPNFormData };
