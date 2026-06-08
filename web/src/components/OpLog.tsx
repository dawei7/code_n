import { useEffect, useRef } from 'react';
import { useAppStore } from '../store/useAppStore';
import type { OpRecordOut } from '../types/api';


const OP_COLORS: Record<string, string> = {
  compare: 'text-amber-300',
  swap: 'text-rose-300',
  read: 'text-blue-300',
  write: 'text-rose-300',
  call: 'text-slate-300',
};


function opColor(op: string): string {
  return OP_COLORS[op] ?? 'text-coden-text';
}


function exportOpsCsv(ops: OpRecordOut[], challengeId: string) {
  // CSV with proper quoting. Columns: step, op_type, detail.
  const escape = (s: string) => '"' + s.replace(/"/g, '""') + '"';
  const rows: string[] = ['step,op_type,detail'];
  for (let i = 0; i < ops.length; i++) {
    rows.push(`${i},${ops[i].op_type},${escape(ops[i].detail)}`);
  }
  const csv = rows.join('\r\n');
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${challengeId}-ops.csv`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}


export function OpLog() {
  const runResult = useAppStore((s) => s.runResult);
  const opIndex = useAppStore((s) => s.opIndex);
  const jumpToOpIndex = useAppStore((s) => s.jumpToOpIndex);
  const currentDetail = useAppStore((s) => s.currentDetail);

  // Ref to the scrollable op log container, used to keep the
  // highlighted op in view as the user steps / clicks / plays.
  const containerRef = useRef<HTMLDivElement>(null);

  if (!runResult) {
    return <div className="text-xs text-coden-muted">No run yet.</div>;
  }

  const { stats, ops_log, actual_complexity, required_complexity } = runResult;

  /**
   * Auto-scroll the highlighted op into the center of the visible
   * area whenever opIndex changes. Triggered on:
   *   - Run (opIndex resets to 0; no scroll needed since 0 is at the top)
   *   - Step / play / slider drag (opIndex advances or jumps)
   *   - Clicking an op in the op log (jumpToOpIndex)
   * 'nearest' is subtle — it scrolls only if the active op is not
   * currently visible, so the user's manual scrolling within the
   * op log isn't yanked around. The user requested "center of
   * the focus", so we use 'center' to keep the active row
   * centered as you step through.
   */
  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;
    const el = container.querySelector<HTMLElement>(`[data-op-index="${opIndex}"]`);
    if (el) {
      el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    }
  }, [opIndex, ops_log.length]);

  return (
    <div className="flex-1 flex flex-col min-h-0 text-xs">
      <div className="grid grid-cols-2 gap-2 mb-2 font-mono shrink-0">
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase">compares</div>
          <div>{stats.comparisons.toLocaleString()}</div>
        </div>
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase">swaps</div>
          <div>{stats.swaps.toLocaleString()}</div>
        </div>
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase">reads</div>
          <div>{stats.reads.toLocaleString()}</div>
        </div>
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase">writes</div>
          <div>{stats.writes.toLocaleString()}</div>
        </div>
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border col-span-2">
          <div className="text-coden-muted text-[10px] uppercase">complexity</div>
          <div>
            {actual_complexity}{' '}
            <span className="text-coden-muted">/ need {required_complexity}</span>
          </div>
        </div>
      </div>

      <div className="flex items-center justify-between mb-1 shrink-0">
        <div className="text-[10px] uppercase text-coden-muted">Op log (click any op to jump)</div>
        <button
          type="button"
          onClick={() => currentDetail && exportOpsCsv(ops_log, currentDetail.id)}
          className="text-[10px] text-coden-muted hover:text-coden-accent border border-coden-border hover:border-coden-accent rounded px-1.5 py-0.5"
          title="Download the full op log as a CSV file for scientific analysis"
        >
          ⬇ CSV
        </button>
      </div>
      <div
        ref={containerRef}
        className="flex-1 overflow-y-auto font-mono bg-coden-bg rounded border border-coden-border"
      >
        {ops_log.length === 0 ? (
          <div className="text-coden-muted p-2">No ops recorded.</div>
        ) : (
          ops_log.map((op, i) => {
            const isCurrent = i === opIndex;
            return (
              <button
                type="button"
                key={i}
                data-op-index={i}
                onClick={() => jumpToOpIndex(i)}
                className={[
                  'w-full text-left px-2 py-0.5 hover:bg-coden-border cursor-pointer',
                  isCurrent ? 'bg-coden-border border-l-2 border-coden-accent' : '',
                ].join(' ')}
                title={`Op ${i} — click to jump to this op`}
              >
                <span className="text-coden-muted mr-1">{i.toString().padStart(4, ' ')}</span>
                <span className={opColor(op.op_type)}>
                  {op.op_type.padEnd(7)}
                </span>
                <span className="text-coden-text">{op.detail}</span>
              </button>
            );
          })
        )}
      </div>
    </div>
  );
}
