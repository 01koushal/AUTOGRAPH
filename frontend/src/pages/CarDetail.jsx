import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { Loader, ErrorState } from "../components/States.jsx";
import RelationshipGraph from "../components/RelationshipGraph.jsx";

export default function CarDetail() {
  const { slug } = useParams();
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    setData(null);
    setError(null);
    api.cars
      .get(slug)
      .then(setData)
      .catch((e) => setError(e.message));
  }, [slug]);

  if (error) return <div className="px-6 py-16"><ErrorState message={error} /></div>;
  if (!data) return <Loader label="Loading car" />;

  const { car, manufacturer, engine, transmission, drivetrain, upgrades, similarCars, engineFamilyCars, recommended } = data;
  const realUpgrades = upgrades.filter((u) => u.name);
  const realSimilar = similarCars.filter((c) => c.name);

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <Link to="/" className="font-mono text-xs text-slate-500 hover:text-edge-cyan">
        ← back
      </Link>

      <div className="mt-4 grid grid-cols-1 gap-10 lg:grid-cols-[1.1fr_1fr]">
        <div>
          <span className="eyebrow">{manufacturer?.name}</span>
          <h1 className="mt-1 font-display text-4xl font-semibold text-white sm:text-5xl">{car.name}</h1>
          <p className="mt-2 font-mono text-sm text-slate-500">{car.year} · {car.bodyType}</p>

          <div className="mt-8 grid grid-cols-2 gap-4 sm:grid-cols-4">
            <Stat label="Horsepower" value={`${car.horsepower} hp`} />
            <Stat label="Torque" value={car.torque} />
            <Stat label="Drivetrain" value={drivetrain?.name} />
            <Stat label="Transmission" value={transmission?.gears ? `${transmission.gears}-spd` : transmission?.type} />
          </div>

          <div className="mt-8 glass-panel p-5">
            <h2 className="eyebrow mb-3">Engine</h2>
            {engine?.name ? (
              <div className="flex flex-wrap items-center gap-3">
                <span className="font-display text-xl text-white">{engine.name}</span>
                <span className="chip">{engine.cylinders}</span>
                <span className="chip">{engine.displacement}</span>
                <span className="chip">{engine.aspiration}</span>
                <span className="chip text-gauge-amber">{engine.horsepower} hp factory</span>
              </div>
            ) : (
              <p className="text-sm text-slate-500">No engine on file.</p>
            )}
          </div>
        </div>

        <div className="glass-panel flex flex-col p-4">
          <span className="eyebrow px-2 pb-1 pt-1">Graph relationships</span>
          <RelationshipGraph
            car={car}
            manufacturer={manufacturer}
            engine={engine}
            transmission={transmission}
            drivetrain={drivetrain}
            upgradeCount={realUpgrades.length}
            similarCount={realSimilar.length}
          />
        </div>
      </div>

      <Section title="Compatible upgrades" subtitle="Upgrade -[:COMPATIBLE_WITH]-> Engine">
        {realUpgrades.length === 0 && <EmptyNote text="No upgrades found for this engine yet." />}
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {realUpgrades.map((u) => (
            <div key={u.slug} className="glass-panel p-4">
              <span className="chip mb-2">{u.category}</span>
              <h3 className="font-display text-base font-semibold text-white">{u.name}</h3>
              <p className="mt-1 font-body text-xs text-slate-400">{u.description}</p>
              {u.priceEstimate && <p className="mt-2 font-mono text-xs text-gauge-amber">{u.priceEstimate}</p>}
            </div>
          ))}
        </div>
      </Section>

      <Section title="Similar cars" subtitle="Car -[:SIMILAR_TO]-> Car">
        {realSimilar.length === 0 && <EmptyNote text="No similar cars linked yet." />}
        <CarChipGrid cars={realSimilar} />
      </Section>

      <Section title="Same engine family" subtitle="Car -[:HAS_ENGINE]-> Engine <-[:HAS_ENGINE]- Car (2-hop)">
        {engineFamilyCars.length === 0 && <EmptyNote text="This engine family is unique to this car." />}
        <CarChipGrid cars={engineFamilyCars} />
      </Section>

      <Section title="Recommended for you" subtitle="Shared drivetrain + engine family, ranked">
        <CarChipGrid cars={recommended} />
      </Section>
    </div>
  );
}

function Stat({ label, value }) {
  return (
    <div className="glass-panel px-4 py-3">
      <p className="font-mono text-[10px] uppercase tracking-wider text-slate-500">{label}</p>
      <p className="stat-value">{value || "—"}</p>
    </div>
  );
}

function Section({ title, subtitle, children }) {
  return (
    <section className="mt-14">
      <div className="mb-5">
        <h2 className="font-display text-2xl font-semibold text-white">{title}</h2>
        <p className="font-mono text-[11px] text-edge-cyan/70">{subtitle}</p>
      </div>
      {children}
    </section>
  );
}

function EmptyNote({ text }) {
  return <p className="font-mono text-sm text-slate-500">{text}</p>;
}

function CarChipGrid({ cars }) {
  if (!cars || cars.length === 0) return null;
  return (
    <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
      {cars.map((c) => (
        <Link
          key={c.slug}
          to={`/cars/${c.slug}`}
          className="glass-panel flex items-center justify-between px-4 py-3 transition-colors hover:border-gauge-amber/40"
        >
          <div>
            <p className="font-display text-sm font-semibold text-white">{c.name}</p>
            <p className="font-mono text-[11px] text-slate-500">{c.manufacturer} · {c.year}</p>
          </div>
          {c.horsepower && <span className="font-mono text-xs text-gauge-amber">{c.horsepower} hp</span>}
        </Link>
      ))}
    </div>
  );
}
