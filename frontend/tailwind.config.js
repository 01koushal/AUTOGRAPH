/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        graphite: {
          950: "#08090B",
          900: "#0E1013",
          800: "#15181D",
          700: "#1D2128",
          600: "#282D36",
          500: "#3A4150",
        },
        gauge: {
          amber: "#FFB020",
          amberDim: "#8A5E1A",
        },
        edge: {
          cyan: "#00D9FF",
          cyanDim: "#0A7A8F",
        },
      },
      fontFamily: {
        display: ["Rajdhani", "sans-serif"],
        body: ["Inter", "sans-serif"],
        mono: ["JetBrains Mono", "monospace"],
      },
      backgroundImage: {
        "grid-fade":
          "radial-gradient(circle at 1px 1px, rgba(255,255,255,0.06) 1px, transparent 0)",
      },
      boxShadow: {
        glass: "0 8px 32px rgba(0,0,0,0.45)",
        "glow-amber": "0 0 24px rgba(255,176,32,0.25)",
        "glow-cyan": "0 0 24px rgba(0,217,255,0.25)",
      },
    },
  },
  plugins: [],
};
