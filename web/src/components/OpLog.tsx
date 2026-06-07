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
  const frameIndex = useAppStore((s) => s.frameIndex);
  const jumpToFrame = useAppStore((s) => s.jumpToFrame);
  const currentDetail = useAppStore((s) => s.currentDetail);

  if (!runResult) {
    return <div className="text-xs text-coden-muted">No run yet.</div>;
  }

  const { stats, ops_log, trace, actual_complexity, required_complexity } = runResult;
  const opIndexAtFrame = trace[frameIndex]?.op_index ?? 0;

  /**
   * Find the LAST trace frame whose op_index is <= the given op's index.
   *
   * The trace fires one frame per Python `line` event; multiple ops
   * can happen on the same line (e.g. `data[i] = data[j]` is one
   * read of data[i] + one read of data[j] + one write of data[i],
   * all on the same line). The op_index values are 0, 1, 2, 3, ...
   * but a frame might cover ops 0-3. So the right frame for op N
   * is the latest frame with op_index <= N.
   *
   * We precompute a `frameForOp` array so clicking is O(1) instead
   * of O(trace) per op.
   */
  const frameForOp: number[] = (() => {
    const map: number[] = new Array(ops_log.length);
    let lastFrame = 0;
    let traceIdx = 0;
    for (let i = 0; i < ops_log.length; i++) {
      // Advance traceIdx while the trace's next frame still has
      // op_index <= i. After this loop, traceIdx is the last frame
      // whose op_index is <= i.
      while (traceIdx < trace.length - 1 && trace[traceIdx + 1].op_index <= i) {
        traceIdx += 1;
      }
      lastFrame = traceIdx;
      map[i] = lastFrame;
    }
    return map;
  })();

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
      <div className="flex-1 overflow-y-auto font-mono bg-coden-bg rounded border border-coden-border">
        {ops_log.length === 0 ? (
          <div className="text-coden-muted p-2">No ops recorded.</div>
        ) : (
          ops_log.map((op, i) => {
            const isCurrent = i === opIndexAtFrame;
            return (
              <button
                type="button"
                key={i}
                onClick={() => jumpToFrame(frameForOp[i] ?? 0)}
                className={[
                  'w-full text-left px-2 py-0.5 hover:bg-coden-border cursor-pointer',
                  isCurrent ? 'bg-coden-border border-l-2 border-coden-accent' : '',
                ].join(' ')}
                title={`Op ${i} — click to jump to the trace frame showing this op`}
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
