const NODES = [
  { key: "manufacturer", label: "MANUFACTURER", angle: 200, color: "#00D9FF" },
  { key: "engine", label: "ENGINE", angle: 340, color: "#FFB020" },
  { key: "transmission", label: "TRANSMISSION", angle: 20, color: "#00D9FF" },
  { key: "drivetrain", label: "DRIVETRAIN", angle: 90, color: "#00D9FF" },
];

/**
 * Renders the car's direct graph relationships as an actual node-link
 * diagram — the literal Cypher traversal, drawn. This is the piece that
 * makes the "why a graph database" argument visually obvious.
 */
export default function RelationshipGraph({ car, manufacturer, engine, transmission, drivetrain, upgradeCount, similarCount }) {
  const cx = 260;
  const cy = 190;
  const r = 130;

  const points = NODES.map((n) => {
    const rad = (n.angle * Math.PI) / 180;
    return {
      ...n,
      x: cx + r * Math.cos(rad),
      y: cy + r * Math.sin(rad),
    };
  });

  const values = {
    manufacturer: manufacturer?.name,
    engine: engine?.name,
    transmission: transmission?.name,
    drivetrain: drivetrain?.name,
  };

  return (
    <svg viewBox="0 0 520 380" className="h-full w-full">
      <defs>
        <radialGradient id="centerGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#FFB020" stopOpacity="0.35" />
          <stop offset="100%" stopColor="#FFB020" stopOpacity="0" />
        </radialGradient>
      </defs>

      {points.map((p) => (
        <line
          key={`edge-${p.key}`}
          x1={cx}
          y1={cy}
          x2={p.x}
          y2={p.y}
          stroke={p.color}
          strokeOpacity="0.35"
          strokeWidth="1.5"
        />
      ))}

      <circle cx={cx} cy={cy} r="70" fill="url(#centerGlow)" />
      <circle cx={cx} cy={cy} r="42" fill="#15181D" stroke="#FFB020" strokeWidth="2" />
      <text x={cx} y={cy - 4} textAnchor="middle" className="fill-white" fontFamily="Rajdhani" fontWeight="600" fontSize="13">
        {car?.name?.split(" ").slice(0, 2).join(" ")}
      </text>
      <text x={cx} y={cy + 14} textAnchor="middle" fill="#FFB020" fontFamily="JetBrains Mono" fontSize="11">
        :Car
      </text>

      {points.map((p) => (
        <g key={p.key}>
          <circle cx={p.x} cy={p.y} r="34" fill="#15181D" stroke={p.color} strokeWidth="1.5" />
          <text
            x={p.x}
            y={p.y - 3}
            textAnchor="middle"
            fill={p.color}
            fontFamily="JetBrains Mono"
            fontSize="8.5"
            letterSpacing="0.5"
          >
            {p.label}
          </text>
          <text
            x={p.x}
            y={p.y + 11}
            textAnchor="middle"
            fill="#CBD5E1"
            fontFamily="Inter"
            fontSize="9"
          >
            {truncate(values[p.key], 14)}
          </text>
        </g>
      ))}

      <text x="16" y="24" fill="#5B6472" fontFamily="JetBrains Mono" fontSize="10">
        {upgradeCount ?? 0} compatible upgrades · {similarCount ?? 0} similar cars
      </text>
    </svg>
  );
}

function truncate(str, n) {
  if (!str) return "—";
  return str.length > n ? `${str.slice(0, n - 1)}…` : str;
}
