import { useState, useEffect } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { toast } from "sonner";
import { TokenData, TokenClaims } from "@/lib/types";
import { TokenStorage, decodeJWT } from "@/lib/token-storage";
import { CheckCircle, XCircle, Envelope } from "@phosphor-icons/react";
import { FullSDXLogo } from "@/components/FullSDXLogo";

interface EmailValidationPageProps {
  onComplete: () => void;
  onBack: () => void;
}

export function EmailValidationPage({
  onComplete,
  onBack,
}: EmailValidationPageProps) {
  const [email, setEmail] = useState("");
  const [isVerifying, setIsVerifying] = useState(false);
  const [verificationStep, setVerificationStep] = useState<
    "input" | "verify" | "success" | "confirm"
  >("input");
  const [verificationCode, setVerificationCode] = useState("");
  const [userToken, setUserToken] = useState<TokenData | null>(null);
  const [userClaims, setUserClaims] = useState<TokenClaims | null>(null);

  useEffect(() => {
    // Check if there's a pre-validated email from the callback
    const preValidatedEmail = sessionStorage.getItem("pre_validated_email");

    // Load the most recent valid token to get user info
    const cilogon = TokenStorage.getToken("cilogon");
    const orcid = TokenStorage.getToken("orcid");

    const tokens = [cilogon, orcid].filter(
      (token) => token && TokenStorage.isTokenValid(token)
    ) as TokenData[];

    // Get the most recent token
    const mostRecentToken = tokens.sort((a, b) => b.issued_at - a.issued_at)[0];

    if (mostRecentToken) {
      setUserToken(mostRecentToken);
      const claims = decodeJWT(mostRecentToken.id_token);
      setUserClaims(claims);

      // Check if we have a pre-validated email or email from claims
      const emailToUse = preValidatedEmail || claims?.email;
      if (emailToUse) {
        setEmail(emailToUse);
        // If we have both eppn and email from claims, skip to confirmation
        if (claims?.eppn && claims?.email && !preValidatedEmail) {
          setVerificationStep("confirm");
        }
      }
    }

    // Clean up the pre-validated email from session storage
    if (preValidatedEmail) {
      sessionStorage.removeItem("pre_validated_email");
    }
  }, []);

  const handleSendVerification = async () => {
    if (!email) {
      toast.error("Please enter your email address");
      return;
    }

    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      toast.error("Please enter a valid email address");
      return;
    }

    setIsVerifying(true);

    try {
      // Simulate sending verification email
      await new Promise((resolve) => setTimeout(resolve, 1500));

      setVerificationStep("verify");
      toast.success("📧 Verification code sent to your email!");
    } catch (error) {
      console.error("Failed to send verification:", error);
      toast.error("Failed to send verification email. Please try again.");
    } finally {
      setIsVerifying(false);
    }
  };

  const handleVerifyCode = async () => {
    if (!verificationCode) {
      toast.error("Please enter the verification code");
      return;
    }

    if (verificationCode.length !== 6) {
      toast.error("Verification code must be 6 digits");
      return;
    }

    setIsVerifying(true);

    try {
      // Simulate code verification
      await new Promise((resolve) => setTimeout(resolve, 1000));

      // For demo purposes, accept any 6-digit code
      if (verificationCode.match(/^\d{6}$/)) {
        setVerificationStep("success");
        toast.success("✅ Email verified successfully!");

        // Wait a moment then complete
        setTimeout(() => {
          onComplete();
        }, 2000);
      } else {
        toast.error("Invalid verification code. Please check and try again.");
      }
    } catch (error) {
      console.error("Failed to verify code:", error);
      toast.error("Verification failed. Please try again.");
    } finally {
      setIsVerifying(false);
    }
  };

  const handleSkip = () => {
    toast.info("Email verification skipped. You can verify later in settings.");
    onComplete();
  };

  const handleConfirmEmail = () => {
    toast.success("✅ Email confirmed!");
    setVerificationStep("success");
    setTimeout(() => {
      onComplete();
    }, 2000);
  };

  const handleEditEmail = () => {
    setVerificationStep("input");
  };

  return (
    <div className="container mx-auto px-6 py-16 max-w-3xl bg-[rgb(255,255,255)] min-h-screen">
      {/* Header */}
      <FullSDXLogo />

      <Button
        variant="ghost"
        onClick={onBack}
        className="mb-8 -ml-2 text-base text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
      >
        ← Back to authentication
      </Button>

      <Card className="shadow-lg border-2 border-[rgb(120,176,219)] bg-[rgb(255,255,255)]">
        <CardHeader className="pb-8 text-center">
          <CardTitle className="text-2xl text-[rgb(64,143,204)] flex items-center justify-center gap-3">
            <Envelope className="h-6 w-6" />
            Email Verification
          </CardTitle>
          <CardDescription className="text-lg mt-2 text-[rgb(50,135,200)]">
            {verificationStep === "input" &&
              "Please verify your email address to continue"}
            {verificationStep === "verify" &&
              "Enter the verification code sent to your email"}
            {verificationStep === "confirm" &&
              "Please confirm this is your email address"}
            {verificationStep === "success" && "Email verified successfully!"}
          </CardDescription>
        </CardHeader>

        <CardContent className="space-y-6 pt-0">
          {/* User Info Display */}
          {userClaims && (
            <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
              <AlertDescription className="text-base text-[rgb(64,143,204)]">
                <div className="space-y-2">
                  <div>
                    <strong>Authenticated as:</strong>{" "}
                    {userClaims.sub || "Unknown user"}
                  </div>
                  <div>
                    <strong>Provider:</strong>{" "}
                    {userToken?.provider?.toUpperCase()}
                  </div>
                  {userClaims.email && (
                    <div>
                      <strong>Email from token:</strong> {userClaims.email}
                    </div>
                  )}
                </div>
              </AlertDescription>
            </Alert>
          )}

          {verificationStep === "input" && (
            <div className="space-y-6">
              <div className="space-y-3">
                <label
                  htmlFor="email"
                  className="text-base font-semibold text-[rgb(64,143,204)]"
                >
                  Email Address
                </label>
                <Input
                  id="email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Enter your email address"
                  className="w-full py-4 text-lg border-2 border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
                  disabled={isVerifying}
                />
                <p className="text-sm text-[rgb(50,135,200)] opacity-70">
                  We'll send a verification code to this email address.
                </p>
              </div>

              <Button
                onClick={handleSendVerification}
                disabled={isVerifying || !email}
                className="w-full py-4 text-lg font-semibold bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)]"
                size="lg"
              >
                {isVerifying ? "Sending..." : "Send Verification Code"}
              </Button>
            </div>
          )}

          {verificationStep === "verify" && (
            <div className="space-y-6">
              <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
                <AlertDescription className="text-base text-[rgb(64,143,204)]">
                  <div className="space-y-2">
                    <div>
                      <strong>Verification code sent to:</strong> {email}
                    </div>
                    <div className="text-sm opacity-70">
                      Please check your email and enter the 6-digit code below.
                      The code will expire in 10 minutes.
                    </div>
                  </div>
                </AlertDescription>
              </Alert>

              <div className="space-y-3">
                <label
                  htmlFor="code"
                  className="text-base font-semibold text-[rgb(64,143,204)]"
                >
                  Verification Code
                </label>
                <Input
                  id="code"
                  type="text"
                  value={verificationCode}
                  onChange={(e) =>
                    setVerificationCode(
                      e.target.value.replace(/\D/g, "").slice(0, 6)
                    )
                  }
                  placeholder="Enter 6-digit code"
                  className="w-full py-4 text-lg text-center tracking-widest font-mono border-2 border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
                  disabled={isVerifying}
                  maxLength={6}
                />
                <p className="text-sm text-[rgb(50,135,200)] opacity-70">
                  Didn't receive the code? Check your spam folder or try again.
                </p>
              </div>

              <div className="flex gap-4">
                <Button
                  onClick={handleVerifyCode}
                  disabled={isVerifying || verificationCode.length !== 6}
                  className="flex-1 py-4 text-lg font-semibold bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)]"
                  size="lg"
                >
                  {isVerifying ? "Verifying..." : "Verify Code"}
                </Button>

                <Button
                  onClick={() => {
                    setVerificationStep("input");
                    setVerificationCode("");
                  }}
                  variant="outline"
                  className="border-2 border-[rgb(120,176,219)] text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
                  size="lg"
                  disabled={isVerifying}
                >
                  Back
                </Button>
              </div>

              <Button
                onClick={handleSendVerification}
                variant="ghost"
                className="w-full text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
                disabled={isVerifying}
              >
                Resend Code
              </Button>
            </div>
          )}

          {verificationStep === "confirm" && (
            <div className="space-y-6">
              <Alert className="border-2 border-[rgb(120,176,219)] bg-[rgb(236,244,250)]">
                <AlertDescription className="text-base text-[rgb(64,143,204)]">
                  <div className="space-y-2">
                    <div>
                      <strong>
                        Email address from your identity provider:
                      </strong>
                    </div>
                    <div className="text-lg font-mono bg-white p-3 rounded border">
                      {email}
                    </div>
                    <div className="text-sm opacity-70">
                      This email was verified by your identity provider. Is this
                      correct?
                    </div>
                  </div>
                </AlertDescription>
              </Alert>

              <div className="flex gap-4">
                <Button
                  onClick={handleConfirmEmail}
                  className="flex-1 py-4 text-lg font-semibold bg-[rgb(50,135,200)] hover:bg-[rgb(64,143,204)] text-[rgb(255,255,255)]"
                  size="lg"
                >
                  ✅ Yes, this is correct
                </Button>

                <Button
                  onClick={handleEditEmail}
                  variant="outline"
                  className="border-2 border-[rgb(120,176,219)] text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
                  size="lg"
                >
                  ✏️ Use different email
                </Button>
              </div>
            </div>
          )}

          {verificationStep === "success" && (
            <div className="space-y-6 text-center">
              <Alert className="border-2 border-green-200 bg-green-50">
                <CheckCircle className="h-5 w-5 text-green-600" />
                <AlertDescription className="text-base ml-2 text-green-800">
                  <div className="space-y-2">
                    <div>
                      <strong>Email verified successfully!</strong>
                    </div>
                    <div>
                      Your email <strong>{email}</strong> has been confirmed.
                    </div>
                    <div className="text-sm opacity-70">
                      Redirecting to your dashboard...
                    </div>
                  </div>
                </AlertDescription>
              </Alert>

              <div className="flex justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[rgb(50,135,200)]"></div>
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
