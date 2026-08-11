import { Link } from "react-router-dom";

export default function CarCard({ car }) {
  return (
    <Link
      to={`/cars/${car.slug}`}
      className="glass-panel group relative flex flex-col overflow-hidden p-5 transition-transform hover:-translate-y-1 hover:shadow-glow-amber"
    >
      <div className="mb-4 flex aspect-[16/10] items-center justify-center rounded-xl border border-white/[0.06] bg-gradient-to-br from-graphite-700 to-graphite-900">
        <CarSilhouette />
      </div>
      <span className="eyebrow mb-1">{car.manufacturer}</span>
      <h3 className="font-display text-lg font-semibold text-white">{car.name}</h3>
      <div className="mt-3 flex items-center gap-4 font-mono text-xs text-slate-400">
        <span>{car.year}</span>
        {car.engine && <span className="truncate">{car.engine}</span>}
        {car.horsepower && <span className="text-gauge-amber">{car.horsepower} hp</span>}
      </div>
    </Link>
  );
}

function CarSilhouette() {
  return (
    <svg width="64" height="36" viewBox="0 0 64 36" fill="none" className="text-slate-600 transition-colors group-hover:text-gauge-amber/60">
      <path
        d="M4 24 L10 14 Q14 9 22 9 H40 Q47 9 52 14 L58 24"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
      <path d="M2 24h60" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
      <circle cx="16" cy="26" r="4.5" stroke="currentColor" strokeWidth="2" />
      <circle cx="48" cy="26" r="4.5" stroke="currentColor" strokeWidth="2" />
    </svg>
  );
}
