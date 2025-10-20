import { createRoot } from "react-dom/client";
import { ErrorBoundary } from "react-error-boundary";
import { GoogleReCaptchaProvider } from "react-google-recaptcha-v3";
import "@github/spark/spark";

import App from "./App.tsx";
import { ErrorFallback } from "./ErrorFallback.tsx";
import { ThemeProvider } from "./components/ThemeProvider";

import "./main.css";

createRoot(document.getElementById("root")!).render(
  <ErrorBoundary FallbackComponent={ErrorFallback}>
    <ThemeProvider defaultTheme="system" storageKey="sdx-ui-theme">
      <GoogleReCaptchaProvider
        reCaptchaKey={import.meta.env.VITE_RECAPTCHA_SITE_KEY}
        scriptProps={{
          async: false,
          defer: false,
          appendTo: "head",
        }}
      >
        <App />
      </GoogleReCaptchaProvider>
    </ThemeProvider>
  </ErrorBoundary>
);
