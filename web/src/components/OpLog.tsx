import { useAppStore } from '../store/useAppStore';


const OP_COLORS: Record<string, string> = {
  compare: 'text-amber-300',
  swap: 'text-rose-300',
  read: 'text-blue-300',
  write: 'text-rose-300',
  call: 'text-slate-400',
};


export function OpLog() {
  const runResult = useAppStore((s) => s.runResult);
  const frameIndex = useAppStore((s) => s.frameIndex);
  const jumpToFrame = useAppStore((s) => s.jumpToFrame);

  if (!runResult) {
    return (
      <div className="text-xs text-coden-muted">No run yet.</div>
    );
  }

  const { stats, ops_log, trace, actual_complexity, required_complexity } = runResult;
  const opIndexAtFrame = trace[frameIndex]?.op_index ?? 0;

  return (
    <div className="flex-1 flex flex-col min-h-0 text-xs">
      <div className="grid grid-cols-2 gap-2 mb-2 font-mono shrink-0">
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase">compares</div>
          <div>{stats.comparisons}</div>
        </div>
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase">swaps</div>
          <div>{stats.swaps}</div>
        </div>
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase">reads</div>
          <div>{stats.reads}</div>
        </div>
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border">
          <div className="text-coden-muted text-[10px] uppercase">writes</div>
          <div>{stats.writes}</div>
        </div>
        <div className="bg-coden-bg rounded px-2 py-1 border border-coden-border col-span-2">
          <div className="text-coden-muted text-[10px] uppercase">complexity</div>
          <div>
            {actual_complexity}{' '}
            <span className="text-coden-muted">/ need {required_complexity}</span>
          </div>
        </div>
      </div>

      <div className="text-[10px] uppercase text-coden-muted mb-1 shrink-0">
        Op log (click to jump)
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
                onClick={() => {
                  // Find the first frame with this op_index.
                  const frameIdx = trace.findIndex((f) => f.op_index === i);
                  jumpToFrame(frameIdx >= 0 ? frameIdx : 0);
                }}
                className={[
                  'w-full text-left px-2 py-0.5 hover:bg-coden-border',
                  isCurrent ? 'bg-coden-border border-l-2 border-coden-accent' : '',
                ].join(' ')}
              >
                <span className="text-coden-muted mr-1">{i.toString().padStart(4, ' ')}</span>
                <span className={OP_COLORS[op.op_type] ?? 'text-coden-text'}>
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
