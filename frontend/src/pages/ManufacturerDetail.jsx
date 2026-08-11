import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { Loader, ErrorState } from "../components/States.jsx";

export default function ManufacturerDetail() {
  const { slug } = useParams();
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    setData(null);
    setError(null);
    api.manufacturers
      .get(slug)
      .then(setData)
      .catch((e) => setError(e.message));
  }, [slug]);

  if (error) return <div className="px-6 py-16"><ErrorState message={error} /></div>;
  if (!data) return <Loader label="Loading manufacturer" />;

  const { manufacturer, cars, engines, relatedManufacturers } = data;
  const realEngines = engines.filter((e) => e.name);
  const realRelated = (relatedManufacturers || []).filter((r) => r.manufacturer?.name);

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <Link to="/" className="font-mono text-xs text-slate-500 hover:text-edge-cyan">
        ← back
      </Link>

      <div className="mt-4">
        <span className="eyebrow">{manufacturer.country} · est. {manufacturer.founded}</span>
        <h1 className="mt-1 font-display text-4xl font-semibold text-white sm:text-5xl">{manufacturer.name}</h1>
      </div>

      <section className="mt-10">
        <h2 className="mb-4 font-display text-2xl font-semibold text-white">Cars made</h2>
        <p className="mb-4 font-mono text-[11px] text-edge-cyan/70">Manufacturer -[:MAKES]-&gt; Car</p>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {cars.filter((c) => c.name).map((c) => (
            <Link key={c.slug} to={`/cars/${c.slug}`} className="glass-panel flex items-center justify-between px-4 py-3 hover:border-gauge-amber/40">
              <div>
                <p className="font-display text-sm font-semibold text-white">{c.name}</p>
                <p className="font-mono text-[11px] text-slate-500">{c.year}</p>
              </div>
              {c.horsepower && <span className="font-mono text-xs text-gauge-amber">{c.horsepower} hp</span>}
            </Link>
          ))}
        </div>
      </section>

      <section className="mt-14">
        <h2 className="mb-4 font-display text-2xl font-semibold text-white">Engine families used</h2>
        <p className="mb-4 font-mono text-[11px] text-edge-cyan/70">Manufacturer -[:MAKES]-&gt; Car -[:HAS_ENGINE]-&gt; Engine</p>
        <div className="flex flex-wrap gap-2">
          {realEngines.map((e) => (
            <span key={e.slug} className="chip">{e.name} <span className="text-slate-500">· {e.family} family</span></span>
          ))}
        </div>
      </section>

      <section className="mt-14">
        <h2 className="mb-4 font-display text-2xl font-semibold text-white">Related manufacturers</h2>
        <p className="mb-4 font-mono text-[11px] text-edge-cyan/70">Shared engine family (2-hop traversal)</p>
        {realRelated.length === 0 && <p className="font-mono text-sm text-slate-500">No shared engine families with other manufacturers.</p>}
        <div className="flex flex-wrap gap-3">
          {realRelated.map((r) => (
            <Link key={r.manufacturer.slug} to={`/manufacturers/${r.manufacturer.slug}`} className="glass-panel px-4 py-2.5 hover:border-edge-cyan/40">
              <span className="font-display text-sm text-white">{r.manufacturer.name}</span>
              <span className="ml-2 font-mono text-[11px] text-slate-500">
                {(r.sharedEngineFamilies || []).join(", ")}
              </span>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
