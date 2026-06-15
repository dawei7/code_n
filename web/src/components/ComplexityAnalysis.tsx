/**
 * ComplexityAnalysis — a *scientific* complexity panel for the
 * current challenge. Shows the user's AST-derived op count
 * against the reference's AST-derived op count, with a
 * deterministic ±5% tolerance band.
 *
 * Why AST-derived (not the runtime counter)?
 *   The runtime ``OperationCounter`` tracks ops that flow
 *   through the ``TrackedList`` / ``TrackedValue`` proxies —
 *   reads, writes, compares, swaps. It misses plain attribute
 *   access, subscripts on non-tracked lists, and the
 *   per-iteration cost of loops. The user looking at their
 *   source sees a ``for`` loop, an ``if``, an ``arr[i]`` —
 *   they want a count that matches that view, not a count of
 *   what happened to be tracked at runtime.
 *
 *   The server walks both the user's source and the
 *   reference's source through the AST, summing each
 *   operation (Compare, BinOp, UnaryOp, BoolOp, Call,
 *   Subscript, Attribute) and multiplying loop bodies by
 *   their iteration count. The result is a deterministic
 *   integer per (source, n) pair.
 *
 * The ±5% band:
 *   `low  = floor(μ * 0.95)`
 *   `high = ceil (μ * 1.05)`
 *   where μ is the reference's AST op count. Inside the
 *   band: as efficient as the reference. Below: likely a
 *   cheat. Above: correct but slower.
 *
 * Required vs achieved complexity:
 *   Shown as a secondary metric. The required complexity is
 *   the algorithm's known class (e.g. ``O(n²)`` for bubble
 *   sort). The achieved complexity is what the engine's
 *   heuristic classifier assigned to the actual op count.
 *   Both are useful for context but are *secondary* to the
 *   raw op count, which is the primary signal.
 */
import { useAppStore } from '../store/useAppStore';


export function ComplexityAnalysis() {
  const detail = useAppStore((s) => s.currentDetail);
  const runResult = useAppStore((s) => s.runResult);
  const n = useAppStore((s) => s.n);

  if (!detail) return null;

  // The reference's AST op count is the "true" optimal
  // (within the same algorithm family — bubble sort vs
  // quicksort would have different reference counts).
  const ref = runResult?.reference_ast_ops ?? null;
  const user = runResult?.user_ast_ops ?? null;
  const ciLow = runResult?.reference_ci_low ?? null;
  const ciHigh = runResult?.reference_ci_high ?? null;

  // Status: where the user's count lands relative to the
  // band. ``null`` when no run yet.
  const status: 'below' | 'inside' | 'above' | 'no-ref' | 'no-run' = (() => {
    if (!runResult) return 'no-run';
    if (ref === null || user === null) return 'no-ref';
    if (ciLow !== null && user < ciLow) return 'below';
    if (ciHigh !== null && user > ciHigh) return 'above';
    return 'inside';
  })();

  return (
    <div className="bg-coden-surface border border-coden-border rounded p-4 text-xs font-mono overflow-y-auto h-full">
      <div className="text-coden-muted text-[10px] uppercase tracking-wider font-semibold mb-3">
        Complexity analysis
      </div>

      {/* Side-by-side op counts (the primary metric) */}
      <div className="grid grid-cols-2 gap-3 mb-4">
        <MetricCard
          label="Your code (AST)"
          value={user}
          accent="text-coden-text"
          sublabel={detail.id}
        />
        <MetricCard
          label="Reference (AST)"
          value={ref}
          accent="text-coden-accent"
          sublabel="canonical solution"
        />
      </div>

      {/* The ±5% tolerance band (visual scale) */}
      {ref !== null && ciLow !== null && ciHigh !== null && (
        <ToleranceBand
          ref={ref}
          ciLow={ciLow}
          ciHigh={ciHigh}
          user={user}
          n={n}
        />
      )}

      {/* Verdict: where the user's count lands. */}
      {runResult && (
        <Verdict
          status={status}
          user={user}
          ref={ref}
          required={detail.required_complexity}
          actual={runResult.actual_complexity}
          tooEfficient={runResult.too_efficient}
        />
      )}

      {/* Required vs achieved complexity (secondary context) */}
      <div className="mt-4 pt-3 border-t border-coden-border">
        <div className="text-coden-muted text-[10px] uppercase tracking-wider font-semibold mb-2">
          Complexity class
        </div>
        <table className="w-full">
          <tbody>
            <tr>
              <td className="text-coden-muted pr-3 py-0.5">Required</td>
              <td className="text-coden-text font-semibold">{detail.required_complexity}</td>
            </tr>
            <tr>
              <td className="text-coden-muted pr-3 py-0.5">Achieved (heuristic)</td>
              <td className="text-coden-text">
                {runResult ? runResult.actual_complexity : '—'}
              </td>
            </tr>
          </tbody>
        </table>
        <p className="text-[10px] text-coden-muted mt-1.5 leading-relaxed">
          The required class is the algorithm's known
          complexity (e.g. <span className="text-coden-text">O(n²)</span> for
          bubble sort). The achieved class is the engine's
          heuristic — for small n the counts can land in
          different buckets. Use the raw AST op count above
          as the primary signal.
        </p>
      </div>
    </div>
  );
}


/** A single big-number card: label on top, value centered. */
function MetricCard({
  label,
  value,
  accent,
  sublabel,
}: {
  label: string;
  value: number | null;
  accent: string;
  sublabel?: string;
}) {
  return (
    <div className="border border-coden-border rounded p-3 bg-coden-bg">
      <div className="text-[10px] uppercase tracking-wider text-coden-muted font-semibold">
        {label}
      </div>
      <div className={`text-3xl font-bold tabular-nums mt-1 ${accent}`}>
        {value !== null ? value.toLocaleString() : '—'}
      </div>
      {sublabel && (
        <div className="text-[10px] text-coden-muted mt-0.5 truncate">
          {sublabel}
        </div>
      )}
      <div className="text-[10px] text-coden-muted mt-1">AST ops</div>
    </div>
  );
}


/** The ±5% band around the reference, with the user's
 *  count marked. A horizontal scale with the reference
 *  value in the center. */
function ToleranceBand({
  ref,
  ciLow,
  ciHigh,
  user,
  n,
}: {
  ref: number;
  ciLow: number;
  ciHigh: number;
  user: number | null;
  n: number;
}) {
  // Choose a scale that includes the reference and a
  // little padding. The lower bound is 0; the upper is
  // max(reference * 1.5, user * 1.1) — this gives a
  // visual frame for both.
  const scaleMax = Math.max(ref * 1.5, user !== null ? user * 1.1 : 0);
  const pct = (v: number) => Math.max(0, Math.min(100, (v / scaleMax) * 100));
  // The user's position on the scale (clamped to the
  // scale for visualization; the actual numeric value
  // is shown below the bar).
  const userPct = user !== null ? pct(user) : null;
  // Did the user's count fall outside the scale entirely?
  const userOffScale = user !== null && user > scaleMax;

  return (
    <div className="mb-4">
      <div className="text-coden-muted text-[10px] uppercase tracking-wider font-semibold mb-2">
        Tolerance band (±5% of reference)  ·  n = {n}
      </div>
      {/* The bar. Three segments: below band (red-tinted),
          band (accent-tinted), above band (amber-tinted). */}
      <div className="relative h-9 rounded border border-coden-border overflow-hidden bg-coden-bg">
        {/* The band itself (drawn first, on top of the bg) */}
        <div
          className="absolute top-0 bottom-0 bg-coden-accent/25 border-l border-r border-coden-accent/60"
          style={{ left: `${pct(ciLow)}%`, width: `${pct(ciHigh) - pct(ciLow)}%` }}
          title={`±5% band: [${ciLow}, ${ciHigh}]`}
        />
        {/* The reference's value as a vertical tick in the
            center of the band. */}
        <div
          className="absolute top-0 bottom-0 w-px bg-coden-accent"
          style={{ left: `${pct(ref)}%` }}
          title={`Reference: ${ref}`}
        />
        {/* The user's value as a larger dot. Color depends
            on whether it landed inside the band. */}
        {user !== null && userPct !== null && (
          <div
            className="absolute top-1/2 -translate-y-1/2 w-3 h-3 rounded-full border-2 border-coden-bg"
            style={{
              left: `calc(${userPct}% - 0.375rem)`,
              backgroundColor: userWithinBand(user, ciLow, ciHigh)
                ? '#22c55e'   // green: inside band
                : user < ciLow
                ? '#f87171'   // red: too cheap (cheat?)
                : '#fbbf24',  // amber: too slow
            }}
            title={`Your count: ${user}`}
          />
        )}
        {/* Labels under the bar */}
        <div className="absolute bottom-0 left-0 right-0 flex justify-between text-[10px] text-coden-muted px-1">
          <span>0</span>
          <span>{scaleMax.toLocaleString()}</span>
        </div>
      </div>
      {/* Numeric scale with the three key values. */}
      <div className="grid grid-cols-3 mt-2 text-[10px] tabular-nums">
        <div className="text-left">
          <div className="text-coden-muted">CI low</div>
          <div className="text-rose-300 font-semibold">{ciLow.toLocaleString()}</div>
        </div>
        <div className="text-center">
          <div className="text-coden-muted">Reference</div>
          <div className="text-coden-accent font-semibold">{ref.toLocaleString()}</div>
        </div>
        <div className="text-right">
          <div className="text-coden-muted">CI high</div>
          <div className="text-rose-300 font-semibold">{ciHigh.toLocaleString()}</div>
        </div>
      </div>
      {userOffScale && (
        <div className="text-[10px] text-amber-400 mt-1">
          Your count ({user}) is off-scale; the bar shows the band but your dot is past the right edge.
        </div>
      )}
    </div>
  );
}


function userWithinBand(user: number, lo: number, hi: number): boolean {
  return user >= lo && user <= hi;
}


function Verdict({
  status,
  user,
  ref,
  required,
  actual,
  tooEfficient,
}: {
  status: 'below' | 'inside' | 'above' | 'no-ref' | 'no-run';
  user: number | null;
  ref: number | null;
  required: string;
  actual: string;
  tooEfficient: boolean;
}) {
  // Compute the ratio (user / ref) as a percentage for
  // the verdict text.
  const ratioPct = (user !== null && ref !== null && ref > 0)
    ? (user / ref) * 100
    : null;

  if (status === 'no-run') {
    return (
      <div className="border border-coden-border rounded p-3 bg-coden-bg text-coden-muted">
        Run the challenge to see the analysis.
      </div>
    );
  }
  if (status === 'no-ref') {
    return (
      <div className="border border-coden-border rounded p-3 bg-coden-bg text-coden-muted">
        No reference comparison available for this run.
      </div>
    );
  }

  // The three outcome bands. Each has a colored icon,
  // a one-line verdict, and a short explanation.
  if (status === 'below') {
    return (
      <VerdictBlock
        color="rose"
        icon="⚠"
        title="Below the band — too efficient"
        body={
          tooEfficient
            ? 'The engine flagged this as too efficient — likely a hardcoded return or a missing loop body.'
            : 'Your code uses fewer AST operations than the reference. Double-check you actually implemented the algorithm.'
        }
        sub={`${user} ops vs ${ref} ref (${ratioPct?.toFixed(0)}% of optimal)`}
      />
    );
  }
  if (status === 'above') {
    return (
      <VerdictBlock
        color="amber"
        icon="△"
        title="Above the band — slower than optimal"
        body={
          actual === required
            ? 'Your solution is correct and within the required complexity class, but it does more work than the canonical solution.'
            : `Your solution is correct but slower than the required ${required} class. Consider optimizing.`
        }
        sub={`${user} ops vs ${ref} ref (${ratioPct?.toFixed(0)}% of optimal — ${user! - ref!} ops above)`}
      />
    );
  }
  // inside
  return (
    <VerdictBlock
      color="emerald"
      icon="✓"
      title="As efficient as the reference"
      body={`Your code's AST op count is within ±5% of the canonical solution's count for this input size.`}
      sub={`${user} ops vs ${ref} ref (${ratioPct?.toFixed(0)}% of optimal)`}
    />
  );
}


function VerdictBlock({
  color,
  icon,
  title,
  body,
  sub,
}: {
  color: 'rose' | 'amber' | 'emerald';
  icon: string;
  title: string;
  body: string;
  sub?: string;
}) {
  const colorMap = {
    rose:   { border: 'border-rose-500/40',  bg: 'bg-rose-500/10',     text: 'text-rose-300' },
    amber:  { border: 'border-amber-500/40', bg: 'bg-amber-500/10',    text: 'text-amber-300' },
    emerald: { border: 'border-emerald-500/40', bg: 'bg-emerald-500/10', text: 'text-emerald-300' },
  } as const;
  const c = colorMap[color];
  return (
    <div className={`border ${c.border} ${c.bg} rounded p-3 mb-3`}>
      <div className="flex items-start gap-2">
        <div className={`text-base ${c.text} font-bold shrink-0`}>{icon}</div>
        <div className="flex-1">
          <div className={`text-sm font-semibold ${c.text}`}>{title}</div>
          <div className="text-xs text-coden-text mt-1 leading-relaxed">{body}</div>
          {sub && (
            <div className="text-[10px] text-coden-muted mt-1.5 font-mono">{sub}</div>
          )}
        </div>
      </div>
    </div>
  );
}
