import { NavLink } from "react-router-dom";

const links = [
  { to: "/", label: "Home", end: true },
  { to: "/upgrades", label: "Upgrades" },
];

export default function Navbar() {
  return (
    <header className="sticky top-0 z-40 border-b border-white/[0.06] bg-graphite-950/80 backdrop-blur-xl">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <NavLink to="/" className="flex items-center gap-2.5">
          <svg width="26" height="26" viewBox="0 0 26 26" fill="none">
            <circle cx="6" cy="20" r="3" stroke="#00D9FF" strokeWidth="1.6" />
            <circle cx="20" cy="6" r="3" stroke="#FFB020" strokeWidth="1.6" />
            <circle cx="20" cy="20" r="3" stroke="#00D9FF" strokeWidth="1.6" />
            <path d="M8.5 18.5 17.5 8.5M9 20h8" stroke="#5B6472" strokeWidth="1.4" />
          </svg>
          <span className="font-display text-xl font-semibold tracking-wide text-white">
            AUTO<span className="text-gauge-amber">GRAPH</span>
          </span>
        </NavLink>
        <nav className="flex items-center gap-6">
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              end={link.end}
              className={({ isActive }) =>
                `font-display text-sm font-medium tracking-wide transition-colors ${
                  isActive ? "text-gauge-amber" : "text-slate-400 hover:text-white"
                }`
              }
            >
              {link.label}
            </NavLink>
          ))}
        </nav>
      </div>
    </header>
  );
}
