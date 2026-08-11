export function Loader({ label = "Loading" }) {
  return (
    <div className="flex flex-col items-center justify-center gap-3 py-24 text-slate-500">
      <div className="h-8 w-8 animate-spin rounded-full border-2 border-white/10 border-t-gauge-amber" />
      <span className="font-mono text-xs uppercase tracking-widest">{label}</span>
    </div>
  );
}

export function ErrorState({ message = "Something went wrong." }) {
  return (
    <div className="glass-panel mx-auto max-w-md px-6 py-10 text-center">
      <p className="font-display text-lg text-white">Unable to load data</p>
      <p className="mt-2 font-mono text-sm text-slate-400">{message}</p>
    </div>
  );
}
