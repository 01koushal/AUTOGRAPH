import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import SearchBar from "../components/SearchBar.jsx";
import CarCard from "../components/CarCard.jsx";
import { Loader, ErrorState } from "../components/States.jsx";

export default function Home() {
  const [recent, setRecent] = useState(null);
  const [popular, setPopular] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    Promise.all([api.cars.recent(), api.manufacturers.popular()])
      .then(([recentCars, popularManufacturers]) => {
        setRecent(recentCars);
        setPopular(popularManufacturers);
      })
      .catch((e) => setError(e.message));
  }, []);

  return (
    <div>
      <section className="relative overflow-hidden border-b border-white/[0.06] px-6 pb-20 pt-20">
        <div className="pointer-events-none absolute inset-0 opacity-[0.15] [background-image:radial-gradient(circle_at_1px_1px,rgba(255,255,255,0.4)_1px,transparent_0)] [background-size:28px_28px]" />
        <div className="relative mx-auto flex max-w-6xl flex-col items-start gap-6">
          <span className="eyebrow">Graph-native automotive data</span>
          <h1 className="font-display text-5xl font-semibold leading-[1.05] text-white sm:text-6xl">
            Every car is a node.
            <br />
            Every part is a <span className="text-gauge-amber">relationship</span>.
          </h1>
          <p className="max-w-xl font-body text-base text-slate-400">
            AutoGraph maps cars, engines, transmissions, drivetrains and performance
            upgrades as a connected graph — so questions like &ldquo;what shares this
            engine family&rdquo; are a single traversal, not a pile of joins.
          </p>
          <SearchBar />
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-6 py-14">
        <div className="mb-6 flex items-center justify-between">
          <h2 className="font-display text-2xl font-semibold text-white">Recently added</h2>
        </div>
        {error && <ErrorState message={error} />}
        {!error && !recent && <Loader label="Fetching cars" />}
        {recent && (
          <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {recent.map((car) => (
              <CarCard key={car.slug} car={car} />
            ))}
          </div>
        )}
      </section>

      <section className="mx-auto max-w-6xl px-6 pb-24">
        <div className="mb-6 flex items-center justify-between">
          <h2 className="font-display text-2xl font-semibold text-white">Popular manufacturers</h2>
        </div>
        {popular && (
          <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-5">
            {popular.map((m) => (
              <Link
                key={m.slug}
                to={`/manufacturers/${m.slug}`}
                className="glass-panel flex flex-col items-center gap-1 px-4 py-6 text-center transition-colors hover:border-edge-cyan/40"
              >
                <span className="font-display text-lg font-semibold text-white">{m.name}</span>
                <span className="font-mono text-xs text-slate-500">{m.carCount} cars</span>
              </Link>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
