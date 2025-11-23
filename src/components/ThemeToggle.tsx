import { useTheme } from "@/components/ThemeProvider";
import { useEffect, useState } from "react";

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();
  const [resolvedTheme, setResolvedTheme] = useState<"light" | "dark">("light");

  // Determine the actual theme being used (resolves system theme)
  useEffect(() => {
    const updateResolvedTheme = () => {
      if (theme === "system") {
        const systemTheme = window.matchMedia("(prefers-color-scheme: dark)")
          .matches
          ? "dark"
          : "light";
        setResolvedTheme(systemTheme);
      } else {
        setResolvedTheme(theme);
      }
    };

    updateResolvedTheme();

    // Listen for system theme changes when in system mode
    if (theme === "system") {
      const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
      const handleChange = (e: MediaQueryListEvent) => {
        setResolvedTheme(e.matches ? "dark" : "light");
      };
      mediaQuery.addEventListener("change", handleChange);
      return () => mediaQuery.removeEventListener("change", handleChange);
    }
  }, [theme]);

  const handleToggle = () => {
    // Toggle between light and dark only
    if (resolvedTheme === "dark") {
      setTheme("light");
    } else {
      setTheme("dark");
    }
  };

  return (
    <button
      onClick={handleToggle}
      className="relative cursor-pointer focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[rgb(50,135,200)] rounded-lg transition-all"
      aria-label={`Toggle theme (current: ${theme})`}
    >
      {resolvedTheme === "dark" ? (
        // Dark Mode Toggle
        <svg
          width="58"
          height="36"
          viewBox="0 0 58 36"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="w-[58px] h-[36px]"
        >
          <rect x="2" width="56" height="32" rx="16" fill="#1F1F22" />
          <g filter="url(#filter0_ddd_518_249)">
            <rect x="4" y="2" width="28" height="28" rx="14" fill="#3287C8" />
          </g>
          <circle cx="18" cy="16" r="5" stroke="#1F1F22" strokeWidth="1.5" />
          <path
            d="M18 23.5V26"
            stroke="#1F1F22"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
          <path
            d="M18 6V8.5"
            stroke="#1F1F22"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
          <path
            d="M10.5 16L8 16"
            stroke="#1F1F22"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
          <path
            d="M28 16L25.5 16"
            stroke="#1F1F22"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
          <path
            d="M23.3033 10.6968L25.0711 8.92901"
            stroke="#1F1F22"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
          <path
            d="M10.9289 23.071L12.6967 21.3033"
            stroke="#1F1F22"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
          <path
            d="M23.3033 21.3032L25.0711 23.071"
            stroke="#1F1F22"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
          <path
            d="M10.929 8.92896L12.6967 10.6967"
            stroke="#1F1F22"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
          <defs>
            <filter
              id="filter0_ddd_518_249"
              x="0"
              y="0"
              width="36"
              height="36"
              filterUnits="userSpaceOnUse"
              colorInterpolationFilters="sRGB"
            >
              <feFlood floodOpacity="0" result="BackgroundImageFix" />
              <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                result="hardAlpha"
              />
              <feOffset dy="1" />
              <feGaussianBlur stdDeviation="1.5" />
              <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0"
              />
              <feBlend
                mode="normal"
                in2="BackgroundImageFix"
                result="effect1_dropShadow_518_249"
              />
              <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                result="hardAlpha"
              />
              <feOffset dy="1" />
              <feGaussianBlur stdDeviation="1" />
              <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0"
              />
              <feBlend
                mode="normal"
                in2="effect1_dropShadow_518_249"
                result="effect2_dropShadow_518_249"
              />
              <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                result="hardAlpha"
              />
              <feOffset dy="2" />
              <feGaussianBlur stdDeviation="2" />
              <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0"
              />
              <feBlend
                mode="normal"
                in2="effect2_dropShadow_518_249"
                result="effect3_dropShadow_518_249"
              />
              <feBlend
                mode="normal"
                in="SourceGraphic"
                in2="effect3_dropShadow_518_249"
                result="shape"
              />
            </filter>
          </defs>
        </svg>
      ) : (
        // Light Mode Toggle
        <svg
          width="58"
          height="36"
          viewBox="0 0 58 36"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="w-[58px] h-[36px]"
        >
          <rect width="56" height="32" rx="16" fill="#3287C8" />
          <g filter="url(#filter0_ddd_519_354)">
            <rect x="26" y="2" width="28" height="28" rx="14" fill="#09090A" />
          </g>
          <path
            fillRule="evenodd"
            clipRule="evenodd"
            d="M45.9562 19.1359C44.4234 18.8673 42.8947 17.7416 41.9736 16.0223C40.8847 13.9896 40.9628 11.7204 42.0142 10.2794C42.122 10.1318 42.24 9.99276 42.368 9.86362C42.6149 9.61455 42.5435 9.14979 42.1963 9.09307C41.9699 9.05608 41.7399 9.02981 41.5067 9.01481C41.354 9.00499 41.2 9 41.0447 9C37.154 9 34 12.134 34 16C34 19.866 37.154 23 41.0447 23C43.2587 23 45.2342 21.9852 46.5256 20.3981C46.6724 20.2178 46.8103 20.0301 46.9387 19.8356C47.1217 19.5585 46.8679 19.2066 46.5345 19.1961C46.3425 19.19 46.1493 19.1697 45.9562 19.1359Z"
            stroke="#3287C8"
            strokeWidth="1.5"
          />
          <defs>
            <filter
              id="filter0_ddd_519_354"
              x="22"
              y="0"
              width="36"
              height="36"
              filterUnits="userSpaceOnUse"
              colorInterpolationFilters="sRGB"
            >
              <feFlood floodOpacity="0" result="BackgroundImageFix" />
              <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                result="hardAlpha"
              />
              <feOffset dy="1" />
              <feGaussianBlur stdDeviation="1.5" />
              <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0"
              />
              <feBlend
                mode="normal"
                in2="BackgroundImageFix"
                result="effect1_dropShadow_519_354"
              />
              <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                result="hardAlpha"
              />
              <feOffset dy="1" />
              <feGaussianBlur stdDeviation="1" />
              <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0"
              />
              <feBlend
                mode="normal"
                in2="effect1_dropShadow_519_354"
                result="effect2_dropShadow_519_354"
              />
              <feColorMatrix
                in="SourceAlpha"
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                result="hardAlpha"
              />
              <feOffset dy="2" />
              <feGaussianBlur stdDeviation="2" />
              <feColorMatrix
                type="matrix"
                values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0"
              />
              <feBlend
                mode="normal"
                in2="effect2_dropShadow_519_354"
                result="effect3_dropShadow_519_354"
              />
              <feBlend
                mode="normal"
                in="SourceGraphic"
                in2="effect3_dropShadow_519_354"
                result="shape"
              />
            </filter>
          </defs>
        </svg>
      )}
    </button>
  );
}
