import { useState } from "react";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { toast } from "sonner";

interface NewL2VPNModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: (l2vpnData: L2VPNData) => void;
}

interface L2VPNData {
  name: string;
  description?: string;
  endpoints: {
    a: {
      node: string;
      port: string;
      vlan: string;
    };
    z: {
      node: string;
      port: string;
      vlan: string;
    };
  };
  bandwidth: string;
  priority: "high" | "medium" | "low";
}

export function NewL2VPNModal({ isOpen, onClose, onConfirm }: NewL2VPNModalProps) {
  const [formData, setFormData] = useState<L2VPNData>({
    name: "",
    description: "",
    endpoints: {
      a: {
        node: "",
        port: "",
        vlan: ""
      },
      z: {
        node: "",
        port: "",
        vlan: ""
      }
    },
    bandwidth: "",
    priority: "medium"
  });

  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    // Validate required fields
    if (!formData.name || 
        !formData.endpoints.a.node || !formData.endpoints.a.port || !formData.endpoints.a.vlan ||
        !formData.endpoints.z.node || !formData.endpoints.z.port || !formData.endpoints.z.vlan ||
        !formData.bandwidth) {
      toast.error("Please fill in all required fields");
      return;
    }

    // Validate VLAN IDs are numbers
    if (isNaN(Number(formData.endpoints.a.vlan)) || isNaN(Number(formData.endpoints.z.vlan))) {
      toast.error("VLAN IDs must be valid numbers");
      return;
    }

    // Check VLAN range (1-4094)
    const vlanA = Number(formData.endpoints.a.vlan);
    const vlanZ = Number(formData.endpoints.z.vlan);
    if (vlanA < 1 || vlanA > 4094 || vlanZ < 1 || vlanZ > 4094) {
      toast.error("VLAN IDs must be between 1 and 4094");
      return;
    }

    setIsLoading(true);
    
    try {
      // Simulate API call - will integrate with backend later
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      onConfirm(formData);
      toast.success(`L2VPN "${formData.name}" request submitted successfully!`);
      
      // Reset form
      setFormData({
        name: "",
        description: "",
        endpoints: {
          a: { node: "", port: "", vlan: "" },
          z: { node: "", port: "", vlan: "" }
        },
        bandwidth: "",
        priority: "medium"
      });
      
      onClose();
    } catch (error) {
      toast.error("Failed to create L2VPN connection");
      console.error("L2VPN creation error:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleInputChange = (field: keyof L2VPNData, value: string) => {
    if (field === 'priority') {
      setFormData(prev => ({
        ...prev,
        [field]: value as "high" | "medium" | "low"
      }));
    } else {
      setFormData(prev => ({
        ...prev,
        [field]: value
      }));
    }
  };

  const handleEndpointChange = (endpoint: 'a' | 'z', field: 'node' | 'port' | 'vlan', value: string) => {
    setFormData(prev => ({
      ...prev,
      endpoints: {
        ...prev.endpoints,
        [endpoint]: {
          ...prev.endpoints[endpoint],
          [field]: value
        }
      }
    }));
  };

  const handleReset = () => {
    setFormData({
      name: "",
      description: "",
      endpoints: {
        a: { node: "", port: "", vlan: "" },
        z: { node: "", port: "", vlan: "" }
      },
      bandwidth: "",
      priority: "medium"
    });
  };

  // Predefined options - will be replaced with backend data later
  const networkNodes = [
    "ampath-miami",
    "ampath-boca",
    "sax-saopaulo", 
    "reuna-santiago",
    "rnp-fortaleza",
    "rnp-recife",
    "ansp-saopaulo",
    "tenet-cape-town"
  ];

  const bandwidthOptions = [
    "1 Gbps",
    "10 Gbps", 
    "40 Gbps",
    "100 Gbps"
  ];

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-[700px] max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="text-xl text-[rgb(64,143,204)] flex items-center gap-2">
            <span className="text-2xl">🔗</span>
            Create New L2VPN Connection
          </DialogTitle>
          <DialogDescription className="text-[rgb(50,135,200)]">
            Set up a Layer 2 Virtual Private Network connection between two endpoints in the SDX topology.
          </DialogDescription>
        </DialogHeader>

        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Connection Name */}
          <div className="space-y-2">
            <Label htmlFor="name" className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
              Connection Name <span className="text-red-500">*</span>
            </Label>
            <Input
              id="name"
              placeholder="e.g., Research-Miami-SP-Link"
              value={formData.name}
              onChange={(e) => handleInputChange("name", e.target.value)}
              className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)] focus:ring-2 focus:ring-[rgb(50,135,200)]/20"
              required
            />
          </div>

          {/* Endpoint A */}
          <div className="space-y-4 p-4 bg-[rgb(248,251,255)] rounded-lg border border-[rgb(200,220,240)]">
            <div className="flex items-center gap-2 mb-2">
              <span className="text-lg">📍</span>
              <h3 className="font-semibold text-[rgb(64,143,204)]">Endpoint A</h3>
            </div>
            
            <div className="grid grid-cols-3 gap-4">
              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                  Node <span className="text-red-500">*</span>
                </Label>
                <Select 
                  value={formData.endpoints.a.node} 
                  onValueChange={(value) => handleEndpointChange('a', 'node', value)}
                >
                  <SelectTrigger className="border-[rgb(120,176,219)]">
                    <SelectValue placeholder="Select node" />
                  </SelectTrigger>
                  <SelectContent>
                    {networkNodes.map((node) => (
                      <SelectItem key={node} value={node}>
                        {node}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                  Port <span className="text-red-500">*</span>
                </Label>
                <Input
                  placeholder="e.g., eth1"
                  value={formData.endpoints.a.port}
                  onChange={(e) => handleEndpointChange('a', 'port', e.target.value)}
                  className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
                  required
                />
              </div>

              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                  VLAN ID <span className="text-red-500">*</span>
                </Label>
                <Input
                  placeholder="100"
                  type="number"
                  min="1"
                  max="4094"
                  value={formData.endpoints.a.vlan}
                  onChange={(e) => handleEndpointChange('a', 'vlan', e.target.value)}
                  className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
                  required
                />
              </div>
            </div>
          </div>

          {/* Endpoint Z */}
          <div className="space-y-4 p-4 bg-[rgb(248,251,255)] rounded-lg border border-[rgb(200,220,240)]">
            <div className="flex items-center gap-2 mb-2">
              <span className="text-lg">📍</span>
              <h3 className="font-semibold text-[rgb(64,143,204)]">Endpoint Z</h3>
            </div>
            
            <div className="grid grid-cols-3 gap-4">
              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                  Node <span className="text-red-500">*</span>
                </Label>
                <Select 
                  value={formData.endpoints.z.node} 
                  onValueChange={(value) => handleEndpointChange('z', 'node', value)}
                >
                  <SelectTrigger className="border-[rgb(120,176,219)]">
                    <SelectValue placeholder="Select node" />
                  </SelectTrigger>
                  <SelectContent>
                    {networkNodes.filter(node => node !== formData.endpoints.a.node).map((node) => (
                      <SelectItem key={node} value={node}>
                        {node}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                  Port <span className="text-red-500">*</span>
                </Label>
                <Input
                  placeholder="e.g., eth2"
                  value={formData.endpoints.z.port}
                  onChange={(e) => handleEndpointChange('z', 'port', e.target.value)}
                  className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
                  required
                />
              </div>

              <div className="space-y-2">
                <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                  VLAN ID <span className="text-red-500">*</span>
                </Label>
                <Input
                  placeholder="200"
                  type="number"
                  min="1"
                  max="4094"
                  value={formData.endpoints.z.vlan}
                  onChange={(e) => handleEndpointChange('z', 'vlan', e.target.value)}
                  className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
                  required
                />
              </div>
            </div>
          </div>

          {/* Connection Parameters */}
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label className="text-[rgb(64,143,204)] font-medium flex items-center gap-1">
                Bandwidth <span className="text-red-500">*</span>
              </Label>
              <Select value={formData.bandwidth} onValueChange={(value) => handleInputChange("bandwidth", value)}>
                <SelectTrigger className="border-[rgb(120,176,219)]">
                  <SelectValue placeholder="Select bandwidth" />
                </SelectTrigger>
                <SelectContent>
                  {bandwidthOptions.map((bandwidth) => (
                    <SelectItem key={bandwidth} value={bandwidth}>
                      {bandwidth}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label className="text-[rgb(64,143,204)] font-medium">
                Priority
              </Label>
              <Select value={formData.priority} onValueChange={(value) => handleInputChange("priority", value)}>
                <SelectTrigger className="border-[rgb(120,176,219)]">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="high">High Priority</SelectItem>
                  <SelectItem value="medium">Medium Priority</SelectItem>
                  <SelectItem value="low">Low Priority</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>

          {/* Description */}
          <div className="space-y-2">
            <Label className="text-[rgb(64,143,204)] font-medium">
              Description
            </Label>
            <Textarea
              placeholder="Optional description for this L2VPN connection..."
              value={formData.description}
              onChange={(e) => handleInputChange("description", e.target.value)}
              className="border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)] min-h-[80px]"
            />
          </div>

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

export type { L2VPNData };