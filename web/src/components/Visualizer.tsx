import { useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';


/**
 * Visualizer — DOM-based 1D sort visualizer.
 *
 * At each step, one cell can be in one of four states:
 *   unsorted (slate) | comparing (amber) | swapped (rose) | sorted (emerald)
 *
 * The state is derived from the *op at the current frame*. We
 * don't have a per-cell "post-state" map from the server (the
 * engine doesn't compute one), so we use the op detail to figure
 * out which cells are involved. The CSS class drives both the
 * color and the `transition-colors` animation.
 */
type CellState = 'unsorted' | 'comparing' | 'swapped' | 'sorted';


const STATE_CLASS: Record<CellState, string> = {
  unsorted: 'bg-slate-500',
  comparing: 'bg-amber-400',
  swapped: 'bg-rose-400',
  sorted: 'bg-emerald-500',
};


function parseIndicesFromDetail(detail: string): number[] {
  // OpRecord.detail strings are like "list[3]=5 vs list[4]=7" or
  // "list[3] = <slice>" or "list[3]<->list[7]". Extract the indices
  // by a simple regex.
  const out: number[] = [];
  const re = /\[(\d+)\]/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(detail)) !== null) {
    out.push(Number(m[1]));
  }
  return out;
}


function stateFromOp(opType: string): CellState {
  if (opType === 'compare') return 'comparing';
  if (opType === 'swap') return 'swapped';
  if (opType === 'write') return 'swapped';  // same flash
  return 'unsorted';
}


function isReadOrOp(opType: string): boolean {
  return opType === 'read' || opType === 'compare' || opType === 'swap' || opType === 'write';
}


export function Visualizer() {
  const runResult = useAppStore((s) => s.runResult);
  const frameIndex = useAppStore((s) => s.frameIndex);

  // Pull the current data array out of the trace frame's locals,
  // and the current op from the ops_log.
  const { data, cellStates } = useMemo(() => {
    if (!runResult) return { data: [] as number[], cellStates: [] as CellState[] };
    const frame = runResult.trace[frameIndex];
    const rawData = (frame?.locals?.data ?? frame?.locals?.arr) as unknown;
    const data: number[] = Array.isArray(rawData) ? (rawData as number[]) : [];
    if (data.length === 0) return { data, cellStates: data.map(() => 'unsorted' as CellState) };

    // Figure out the per-cell state at this step. The op at this
    // frame is runResult.ops_log[frame.op_index] (or the closest
    // one ≤ frame.op_index). Cells touched by that op get a flash
    // state; everything else is "unsorted" (the engine doesn't tell
    // us which cells are "permanently sorted" yet — that requires a
    // second pass over the data; the follow-up is to compute it on
    // the server side as `cell_states: list[CellState]`).
    const cellStates: CellState[] = data.map(() => 'unsorted');
    const op = runResult.ops_log[frame.op_index];
    if (op && isReadOrOp(op.op_type)) {
      const indices = parseIndicesFromDetail(op.detail);
      const state = stateFromOp(op.op_type);
      for (const i of indices) {
        if (i >= 0 && i < cellStates.length) {
          cellStates[i] = state;
        }
      }
    }
    return { data, cellStates };
  }, [runResult, frameIndex]);

  if (!runResult) {
    return (
      <div className="h-full flex items-center justify-center text-coden-muted text-sm">
        Click Run to see the algorithm step through.
      </div>
    );
  }

  if (data.length === 0) {
    return (
      <div className="h-full flex items-center justify-center text-coden-muted text-sm">
        (No array data captured at this step — the player code may not have entered its loop yet.)
      </div>
    );
  }

  const max = Math.max(...data, 1);

  return (
    <div className="h-full flex flex-col">
      <div className="flex-1 flex items-end gap-0.5 px-2 pb-2">
        {data.map((value, i) => (
          <div
            key={i}
            className={[
              'flex-1 rounded-t transition-colors duration-150',
              'flex items-end justify-center pb-1',
              STATE_CLASS[cellStates[i] ?? 'unsorted'],
            ].join(' ')}
            style={{ height: `${Math.max(2, (value / max) * 100)}%` }}
          >
            <span className="text-[10px] text-coden-bg font-mono font-semibold">
              {value}
            </span>
          </div>
        ))}
      </div>
      <div className="flex gap-3 text-[10px] text-coden-muted px-2 pb-1 font-mono">
        <span><span className="inline-block w-2 h-2 bg-slate-500 rounded-sm mr-1" />unsorted</span>
        <span><span className="inline-block w-2 h-2 bg-amber-400 rounded-sm mr-1" />compare</span>
        <span><span className="inline-block w-2 h-2 bg-rose-400 rounded-sm mr-1" />swap/write</span>
        <span className="ml-auto">step {frameIndex + 1} / {runResult.trace.length}</span>
      </div>
    </div>
  );
}
