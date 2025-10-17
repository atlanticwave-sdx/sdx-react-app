// src/components/pages/emailValidationPage.tsx
import { useState, useEffect, useRef } from "react";
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
import { CheckCircle, Envelope } from "@phosphor-icons/react";
import sdxLogo from "@/assets/images/sdx-logo.svg";

interface EmailValidationPageProps {
  onComplete: () => void;
  onBack: () => void;
}

export function EmailValidationPage({
  onComplete,
  onBack,
}: EmailValidationPageProps) {
  // Environment detection
  const isDevelopment = import.meta.env.DEV;

  // refs & local state
  const codeInputRef = useRef<HTMLInputElement | null>(null);
  const hasAutoSubmittedRef = useRef<string>("");
  const [resendCooldown, setResendCooldown] = useState(0);
  const RESEND_COOLDOWN_SECONDS = 60;

  const [email, setEmail] = useState("");
  const [isVerifying, setIsVerifying] = useState(false);
  const [verificationStep, setVerificationStep] = useState<
    "input" | "verify" | "success" | "confirm"
  >("input");
  const [verificationCode, setVerificationCode] = useState("");
  const [userToken, setUserToken] = useState<TokenData | null>(null);
  const [userClaims, setUserClaims] = useState<TokenClaims | null>(null);

  // load tokens / pre-validated email
  useEffect(() => {
    const preValidatedEmail = sessionStorage.getItem("pre_validated_email");

    const cilogon = TokenStorage.getToken("cilogon");
    const orcid = TokenStorage.getToken("orcid");

    const tokens = [cilogon, orcid].filter(
      (token) => token && TokenStorage.isTokenValid(token)
    ) as TokenData[];

    const mostRecentToken = tokens.sort((a, b) => b.issued_at - a.issued_at)[0];

    if (mostRecentToken) {
      setUserToken(mostRecentToken);

      if (mostRecentToken.id_token) {
        const claims = decodeJWT(mostRecentToken.id_token);
        setUserClaims(claims);

        const emailToUse = preValidatedEmail || claims?.email;
        if (emailToUse) {
          setEmail(emailToUse);
          if (claims?.eppn && claims?.email && !preValidatedEmail) {
            setVerificationStep("confirm");
          }
        }
      }
    }

    if (preValidatedEmail) {
      sessionStorage.removeItem("pre_validated_email");
    }
  }, []);

  async function postJson(path: string, body: any) {
    const base = import.meta.env.VITE_API_BASE || "http://localhost:3002";
    const url = `${base}${path.startsWith("/") ? path : `/${path}`}`;

    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
      credentials: "include",
    });

    let data: any = null;
    try {
      data = await resp.json();
    } catch (err) {
      data = null;
    }

    return { ok: resp.ok, status: resp.status, data };
  }

  // handlers
  const handleSendVerification = async () => {
    if (!email) {
      toast.error("Please enter your email");
      return;
    }
    const normalized = String(email).trim().toLowerCase();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(normalized)) {
      toast.error("Enter a valid email");
      return;
    }

    setIsVerifying(true);
    try {
      const { ok, status, data } = await postJson("/api/send-verification", {
        email: normalized,
      });

      if (!ok) {
        if (isDevelopment) {
          console.error("send failed", status, data);
        }

        if (status === 429) {
          toast.error("Too many requests. Please wait a moment and try again.");
        } else {
          toast.error(data?.error || "Failed to send verification code");
        }
        return;
      }

      setEmail(normalized);
      setVerificationStep("verify");
      setVerificationCode("");
      toast.success("📧 Verification code sent to your email!");

      setResendCooldown(RESEND_COOLDOWN_SECONDS);

      setTimeout(() => {
        if (codeInputRef.current) {
          codeInputRef.current.focus();
          codeInputRef.current.select?.();
        } else {
          const el = document.getElementById("code") as HTMLInputElement | null;
          if (el) {
            el.focus();
            el.select();
          }
        }
      }, 150);
    } catch (err) {
      if (isDevelopment) {
        console.error("Send verification error:", err);
      }
      toast.error("Network error. Please check your connection.");
    } finally {
      setIsVerifying(false);
    }
  };

  const handleVerifyCode = async () => {
    if (!verificationCode) {
      toast.error("Please enter the code");
      return;
    }
    if (!/^\d{6}$/.test(verificationCode)) {
      toast.error("Code must be 6 digits");
      return;
    }

    setIsVerifying(true);
    try {
      const { ok, status, data } = await postJson("/api/verify-code", {
        email: String(email).trim().toLowerCase(),
        code: verificationCode,
      });

      if (!ok) {
        if (isDevelopment) {
          console.error("verify failed", status, data);
        }

        if (status === 429) {
          toast.error("Too many attempts. Please try again later.");
        } else if (status === 400) {
          toast.error("Invalid or expired code. Please try again.");
        } else {
          toast.error(data?.error || "Verification failed");
        }

        setVerificationCode("");
        hasAutoSubmittedRef.current = "";

        setTimeout(() => {
          if (codeInputRef.current) {
            codeInputRef.current.focus();
          }
        }, 100);

        return;
      }

      setVerificationStep("success");
      toast.success("✅ Email verified successfully!");
      setTimeout(() => onComplete(), 1200);
    } catch (err) {
      if (isDevelopment) {
        console.error("Verify code error:", err);
      }
      toast.error("Network error. Please check your connection.");

      setVerificationCode("");
      hasAutoSubmittedRef.current = "";
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

  // Auto-submit when 6 digits entered (but only once per code)
  useEffect(() => {
    if (
      verificationStep === "verify" &&
      verificationCode.length === 6 &&
      !isVerifying &&
      hasAutoSubmittedRef.current !== verificationCode
    ) {
      hasAutoSubmittedRef.current = verificationCode;
      const t = setTimeout(() => handleVerifyCode(), 200);
      return () => clearTimeout(t);
    }
  }, [verificationCode, verificationStep, isVerifying]);

  // Reset the auto-submit tracker when code changes
  useEffect(() => {
    if (verificationCode.length < 6) {
      hasAutoSubmittedRef.current = "";
    }
  }, [verificationCode]);

  // autofocus when entering verify step
  useEffect(() => {
    if (verificationStep === "verify") {
      const t = setTimeout(() => {
        if (codeInputRef.current) codeInputRef.current.focus();
        else {
          const el = document.getElementById("code") as HTMLInputElement | null;
          if (el) el.focus();
        }
      }, 120);
      return () => clearTimeout(t);
    }
  }, [verificationStep]);

  // resend cooldown timer
  useEffect(() => {
    if (!resendCooldown) return;
    const interval = setInterval(() => {
      setResendCooldown((s) => {
        if (s <= 1) {
          clearInterval(interval);
          return 0;
        }
        return s - 1;
      });
    }, 1000);
    return () => clearInterval(interval);
  }, [resendCooldown]);

  // render
  return (
    <div className="container mx-auto px-6 py-16 max-w-3xl bg-[rgb(255,255,255)] min-h-screen">
      {/* Header */}
      <div className="text-center space-y-4 mb-12">
        <div className="flex flex-col items-center space-y-6">
          <div className="flex items-center justify-center gap-4">
            <img
              src={sdxLogo}
              alt="SDX Logo"
              className="w-12 h-12 object-contain"
            />
            <h1 className="text-4xl font-bold tracking-tight leading-tight">
              <span style={{ color: "rgb(50, 135, 200)" }}>AtlanticWave</span>
              <span style={{ color: "rgb(64, 143, 204)" }}>-</span>
              <span
                className="px-3 py-1 rounded-md font-bold"
                style={{
                  color: "rgb(255, 255, 255)",
                  backgroundColor: "rgb(120, 176, 219)",
                }}
              >
                SDX
              </span>
            </h1>
          </div>

          <h2
            className="text-xs font-light uppercase tracking-wide opacity-70"
            style={{ color: "rgb(64, 143, 204)" }}
          >
            International Distributed Software-Defined Exchange
          </h2>
        </div>
      </div>

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
                    {userToken?.provider?.toUpperCase?.() || "UNKNOWN"}
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
                  className="text-black w-full py-4 text-lg border-2 border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
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

                <div className="flex gap-2">
                  <Input
                    id="code"
                    ref={codeInputRef as any}
                    type="text"
                    value={verificationCode}
                    onChange={(e) =>
                      setVerificationCode(
                        e.target.value.replace(/\D/g, "").slice(0, 6)
                      )
                    }
                    placeholder="Enter 6-digit code"
                    className="text-black flex-1 py-4 text-lg text-center tracking-widest font-mono border-2 border-[rgb(120,176,219)] focus:border-[rgb(50,135,200)]"
                    disabled={isVerifying}
                    maxLength={6}
                  />

                  <div className="flex flex-col gap-2">
                    <Button
                      onClick={async () => {
                        try {
                          const text = await navigator.clipboard.readText();
                          const digits = (text || "")
                            .replace(/\D/g, "")
                            .slice(0, 6);
                          if (!digits) {
                            toast.error("No valid code found in clipboard");
                            return;
                          }
                          setVerificationCode(digits);
                          if (digits.length === 6) {
                            setTimeout(() => handleVerifyCode(), 150);
                          } else {
                            toast.info(
                              `Pasted ${digits.length} digits. Need 6 digits.`
                            );
                          }
                        } catch (err) {
                          if (isDevelopment) {
                            console.error("clipboard read error:", err);
                          }
                          toast.error(
                            "Unable to access clipboard. Please paste manually."
                          );
                        }
                      }}
                      variant="ghost"
                      className="text-[rgb(50,135,200)] whitespace-nowrap"
                    >
                      Paste code
                    </Button>

                    <Button
                      onClick={async () => {
                        if (resendCooldown > 0) {
                          toast.info(
                            `Please wait ${resendCooldown}s before resending`
                          );
                          return;
                        }
                        await handleSendVerification();
                      }}
                      variant="outline"
                      className="border-2 border-[rgb(120,176,219)] text-[rgb(50,135,200)] hover:bg-[rgb(236,244,250)]"
                      disabled={isVerifying || resendCooldown > 0}
                      size="sm"
                    >
                      {resendCooldown > 0
                        ? `Resend (${resendCooldown}s)`
                        : "Resend"}
                    </Button>
                  </div>
                </div>

                <p className="text-sm text-[rgb(50,135,200)] opacity-70">
                  Didn't receive the code? Check your spam folder.
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
