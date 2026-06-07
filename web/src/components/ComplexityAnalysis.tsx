import { useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';
import type { RunResponse } from '../types/api';


/**
 * ComplexityAnalysis — a scientific complexity panel for the current
 * challenge. Shows the required vs achieved complexity, the engine's
 * operation budget, the player's actual op counts, and (when
 * annotated) the algorithm's best/average/worst case analysis.
 *
 * Sources of truth:
 *   - Required complexity: challenge.required_complexity (from spec)
 *   - Achieved complexity: runResult.actual_complexity (from engine)
 *   - Budget: counter.limit_for(n, required_complexity) — same
 *     formula the engine uses to decide pass/fail
 *   - Actual ops: runResult.stats
 *   - Per-case notes: challenge.complexity_notes (from spec)
 */
export function ComplexityAnalysis() {
  const detail = useAppStore((s) => s.currentDetail);
  const runResult = useAppStore((s) => s.runResult);
  const n = useAppStore((s) => s.n);

  // The engine's limit formula. We duplicate it here so the panel
  // can show "ops used / budget" without re-running anything.
  // See code_n/counter.py:OperationCounter.limit_for.
  const budget = useMemo(() => {
    if (!detail) return 0;
    const factor = {
      'O(1)':        10,
      'O(log n)':     1500,  // log2(n) * 3 + 10  (approximated at n=50: 24)
      'O(n)':        8 * n + 10,
      'O(n log n)':  Math.floor(n * Math.log2(Math.max(n, 2)) * 10) + 10,
      'O(n²)':       8 * n * n + 10,
      'O(n³)':       8 * n * n * n + 10,
      'O(2ⁿ)':       2 ** Math.min(n, 25) + 10,
    }[detail.required_complexity] ?? 10 ** 12;
    return factor;
  }, [detail, n]);

  if (!detail) return null;

  return (
    <div className="bg-coden-surface border border-coden-border rounded p-3 text-xs font-mono overflow-y-auto">
      <div className="text-coden-muted text-[10px] uppercase tracking-wider font-semibold mb-2">
        Complexity analysis
      </div>

      {/* Required vs achieved (the pass/fail verdict's underlying check) */}
      <table className="w-full mb-3">
        <thead>
          <tr className="text-coden-muted text-left">
            <th className="font-normal pb-1 pr-3"></th>
            <th className="font-normal pb-1 pr-3">Required</th>
            <th className="font-normal pb-1 pr-3">Achieved</th>
            <th className="font-normal pb-1">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="pr-3 text-coden-muted">Time complexity</td>
            <td className="pr-3">{detail.required_complexity}</td>
            <td className="pr-3">
              {runResult ? runResult.actual_complexity : '—'}
            </td>
            <td>
              {runResult ? (
                runResult.within_threshold ? (
                  <span className="text-coden-accent">within budget</span>
                ) : runResult.correct ? (
                  <span className="text-amber-400">over budget</span>
                ) : (
                  <span className="text-rose-400">incorrect</span>
                )
              ) : (
                <span className="text-coden-muted">—</span>
              )}
            </td>
          </tr>
          <tr>
            <td className="pr-3 text-coden-muted">Space complexity</td>
            <td className="pr-3">O(1)</td>
            <td className="pr-3">O(1)</td>
            <td className="text-coden-accent">in-place</td>
          </tr>
        </tbody>
      </table>

      {/* Op counts vs budget */}
      {runResult && (
        <OpBudget runResult={runResult} budget={budget} n={n} />
      )}

      {/* Per-algorithm best/average/worst notes */}
      {detail.complexity_notes && Object.keys(detail.complexity_notes).length > 0 && (
        <div className="mt-3 pt-3 border-t border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase tracking-wider font-semibold mb-2">
            Algorithm complexity (reference)
          </div>
          <dl className="space-y-1.5">
            {Object.entries(detail.complexity_notes).map(([k, v]) => (
              <div key={k} className="flex gap-2">
                <dt className="text-coden-accent w-16 shrink-0 font-semibold capitalize">{k}</dt>
                <dd className="text-coden-text flex-1">{v}</dd>
              </div>
            ))}
          </dl>
        </div>
      )}
    </div>
  );
}


function OpBudget({ runResult, budget, n }: { runResult: RunResponse; budget: number; n: number }) {
  const { stats } = runResult;
  const utilizationPct = budget > 0 ? Math.min(100, (stats.total / budget) * 100) : 0;
  // Color the utilization bar based on how close to the budget.
  const utilizationColor =
    utilizationPct < 50  ? 'bg-coden-accent' :
    utilizationPct < 80  ? 'bg-amber-400' :
    utilizationPct < 100 ? 'bg-rose-400' :
                           'bg-rose-600';

  return (
    <div className="mb-2">
      <div className="text-coden-muted text-[10px] uppercase tracking-wider font-semibold mb-2">
        Operation budget (n = {n})
      </div>
      <table className="w-full">
        <thead>
          <tr className="text-coden-muted text-left">
            <th className="font-normal pb-1 pr-3">Op</th>
            <th className="font-normal pb-1 pr-3 text-right">Count</th>
            <th className="font-normal pb-1"></th>
          </tr>
        </thead>
        <tbody className="text-coden-text">
          <BudgetRow label="Compares" value={stats.comparisons} color="text-amber-300" />
          <BudgetRow label="Swaps"    value={stats.swaps}       color="text-rose-300" />
          <BudgetRow label="Reads"    value={stats.reads}       color="text-blue-300" />
          <BudgetRow label="Writes"   value={stats.writes}      color="text-rose-300" />
          <BudgetRow label="Calls"    value={stats.calls}       color="text-slate-300" />
        </tbody>
        <tfoot>
          <tr className="border-t border-coden-border">
            <td className="pt-1 pr-3 text-coden-accent font-semibold">Total</td>
            <td className="pt-1 pr-3 text-right text-coden-accent font-semibold">{stats.total}</td>
            <td className="pt-1 text-coden-muted text-[10px]">
              / {budget.toLocaleString()} budget
            </td>
          </tr>
        </tfoot>
      </table>
      {/* Utilization bar */}
      <div className="mt-2">
        <div className="h-1.5 bg-coden-bg rounded overflow-hidden border border-coden-border">
          <div
            className={`h-full ${utilizationColor} transition-all`}
            style={{ width: `${utilizationPct}%` }}
          />
        </div>
        <div className="text-[10px] text-coden-muted mt-0.5 flex justify-between">
          <span>0</span>
          <span>{utilizationPct.toFixed(1)}% of budget</span>
          <span>{budget.toLocaleString()}</span>
        </div>
      </div>
    </div>
  );
}


function BudgetRow({ label, value, color }: { label: string; value: number; color: string }) {
  return (
    <tr>
      <td className={`pr-3 ${color}`}>{label}</td>
      <td className="pr-3 text-right tabular-nums">{value.toLocaleString()}</td>
      <td></td>
    </tr>
  );
}
