import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../api/client.js";

export default function SearchBar({ autoFocus = false }) {
  const [term, setTerm] = useState("");
  const [results, setResults] = useState([]);
  const [open, setOpen] = useState(false);
  const containerRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (term.trim().length < 2) {
      setResults([]);
      return;
    }
    const handle = setTimeout(() => {
      api
        .search(term)
        .then((data) => {
          setResults(data);
          setOpen(true);
        })
        .catch(() => setResults([]));
    }, 220);
    return () => clearTimeout(handle);
  }, [term]);

  useEffect(() => {
    function handleClick(e) {
      if (containerRef.current && !containerRef.current.contains(e.target)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClick);
    return () => document.removeEventListener("mousedown", handleClick);
  }, []);

  return (
    <div ref={containerRef} className="relative w-full max-w-xl">
      <div className="glass-panel flex items-center gap-3 px-4 py-3">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" className="shrink-0 text-slate-500">
          <circle cx="11" cy="11" r="7" stroke="currentColor" strokeWidth="2" />
          <path d="m20 20-3.5-3.5" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
        </svg>
        <input
          autoFocus={autoFocus}
          value={term}
          onChange={(e) => setTerm(e.target.value)}
          onFocus={() => results.length > 0 && setOpen(true)}
          placeholder="Search cars or manufacturers — try “Supra” or “BMW”"
          className="w-full bg-transparent font-body text-sm text-white placeholder:text-slate-500 focus:outline-none"
        />
      </div>
      {open && results.length > 0 && (
        <ul className="glass-panel absolute z-50 mt-2 max-h-80 w-full overflow-auto py-2">
          {results.map((car) => (
            <li key={car.slug}>
              <button
                onClick={() => {
                  navigate(`/cars/${car.slug}`);
                  setOpen(false);
                  setTerm("");
                }}
                className="flex w-full items-center justify-between px-4 py-2.5 text-left text-sm text-slate-200 hover:bg-white/5"
              >
                <span>{car.name}</span>
                <span className="font-mono text-xs text-slate-500">{car.manufacturer}</span>
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
