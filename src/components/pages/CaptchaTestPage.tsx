// src/pages/CaptchaTestPage.tsx
import React, { useState } from "react";
import ReCAPTCHA from "react-google-recaptcha";

export const CaptchaTestPage: React.FC<{ onBack: () => void }> = ({
  onBack,
}) => {
  const [captchaValue, setCaptchaValue] = useState<string | null>(null);
  const [status, setStatus] = useState<string>("Idle");

  const handleCaptchaChange = (value: string | null) => {
    console.log("Captcha value:", value);
    setCaptchaValue(value);
  };

  const handleSubmit = async () => {
    if (!captchaValue) {
      alert("Please complete the captcha first!");
      return;
    }

    setStatus("Verifying...");

    try {
      const response = await fetch("http://localhost:5000/verify-captcha", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token: captchaValue }),
      });

      const data = await response.json();

      if (data.success) {
        setStatus("Captcha Verified ✅ (Human)");
      } else {
        setStatus("Captcha Failed ❌ (Bot suspected)");
      }
    } catch (error) {
      console.error("Error verifying captcha:", error);
      setStatus("Error verifying captcha");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Captcha Testing Page</h2>

      <ReCAPTCHA
        sitekey={import.meta.env.VITE_RECAPTCHA_SITE_KEY as string}
        onChange={handleCaptchaChange}
      />

      <br />
      <button onClick={handleSubmit}>Submit</button>
      <br />
      <button onClick={onBack} style={{ marginTop: "20px" }}>
        ⬅ Back
      </button>

      <p style={{ marginTop: "20px" }}>Status: {status}</p>
    </div>
  );
};
