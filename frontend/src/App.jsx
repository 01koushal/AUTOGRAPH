import { Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar.jsx";
import Home from "./pages/Home.jsx";
import CarDetail from "./pages/CarDetail.jsx";
import ManufacturerDetail from "./pages/ManufacturerDetail.jsx";
import UpgradeExplorer from "./pages/UpgradeExplorer.jsx";

export default function App() {
  return (
    <div className="min-h-screen">
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/cars/:slug" element={<CarDetail />} />
          <Route path="/manufacturers/:slug" element={<ManufacturerDetail />} />
          <Route path="/upgrades" element={<UpgradeExplorer />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
      <footer className="border-t border-white/[0.06] px-6 py-8 text-center font-mono text-xs text-slate-600">
        AutoGraph — built on CognoDB, a Neo4j-compatible graph database
      </footer>
    </div>
  );
}

function NotFound() {
  return (
    <div className="mx-auto max-w-xl px-6 py-24 text-center">
      <p className="font-display text-3xl text-white">404</p>
      <p className="mt-2 font-mono text-sm text-slate-500">That node doesn&apos;t exist in the graph.</p>
    </div>
  );
}
