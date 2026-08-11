import { useEffect, useState } from "react";
import { api } from "../api/client.js";
import { Loader, ErrorState } from "../components/States.jsx";

export default function UpgradeExplorer() {
  const [categories, setCategories] = useState(null);
  const [active, setActive] = useState(null);
  const [upgrades, setUpgrades] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.upgrades
      .categories()
      .then(setCategories)
      .catch((e) => setError(e.message));
  }, []);

  useEffect(() => {
    setUpgrades(null);
    api.upgrades
      .list(active)
      .then(setUpgrades)
      .catch((e) => setError(e.message));
  }, [active]);

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <span className="eyebrow">Upgrade -[:BELONGS_TO]-&gt; Category · Upgrade -[:COMPATIBLE_WITH]-&gt; Engine</span>
      <h1 className="mt-1 font-display text-4xl font-semibold text-white sm:text-5xl">Upgrade Explorer</h1>
      <p className="mt-2 max-w-lg font-body text-sm text-slate-400">
        Browse performance parts by category and see exactly which engines each one bolts onto.
      </p>

      <div className="mt-8 flex flex-wrap gap-2">
        <FilterChip label="All" active={active === null} onClick={() => setActive(null)} />
        {categories?.map((c) => (
          <FilterChip
            key={c.slug}
            label={`${c.name} (${c.upgradeCount})`}
            active={active === c.slug}
            onClick={() => setActive(c.slug)}
          />
        ))}
      </div>

      <div className="mt-8">
        {error && <ErrorState message={error} />}
        {!error && !upgrades && <Loader label="Loading upgrades" />}
        {upgrades && (
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {upgrades.map((u) => (
              <div key={u.slug} className="glass-panel p-5">
                <span className="chip mb-2">{u.category}</span>
                <h3 className="font-display text-lg font-semibold text-white">{u.name}</h3>
                <p className="mt-1.5 font-body text-xs text-slate-400">{u.description}</p>
                {u.priceEstimate && <p className="mt-3 font-mono text-xs text-gauge-amber">{u.priceEstimate}</p>}
                {u.compatibleEngines?.length > 0 && (
                  <div className="mt-3 flex flex-wrap gap-1.5">
                    {u.compatibleEngines.map((e) => (
                      <span key={e} className="rounded-full border border-edge-cyan/20 bg-edge-cyan/[0.06] px-2 py-0.5 font-mono text-[10px] text-edge-cyan">
                        {e}
                      </span>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function FilterChip({ label, active, onClick }) {
  return (
    <button
      onClick={onClick}
      className={`rounded-full border px-4 py-1.5 font-display text-sm font-medium transition-colors ${
        active
          ? "border-gauge-amber bg-gauge-amber/10 text-gauge-amber"
          : "border-white/10 bg-white/[0.02] text-slate-400 hover:text-white"
      }`}
    >
      {label}
    </button>
  );
}
