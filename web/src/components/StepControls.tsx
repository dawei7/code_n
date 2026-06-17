import { useAppStore } from '../store/useAppStore';


// Frame interval (ms) options. The label is "Xms / Xs per frame" so
// it's obvious that higher = slower. The default is 1000ms (1s per
// frame), which gives the player a full second to read each step.
const FRAME_INTERVALS: ReadonlyArray<{ ms: number; label: string }> = [
  { ms: 100,  label: '100ms / frame (very fast)' },
  { ms: 250,  label: '250ms / frame' },
  { ms: 500,  label: '500ms / frame' },
  { ms: 1000, label: '1s / frame' },
  { ms: 2000, label: '2s / frame (slow)' },
];


export function StepControls() {
  const runResult = useAppStore((s) => s.runResult);
  const opIndex = useAppStore((s) => s.opIndex);
  const isPlaying = useAppStore((s) => s.isPlaying);
  const frameIntervalMs = useAppStore((s) => s.frameIntervalMs);
  const step = useAppStore((s) => s.step);
  const play = useAppStore((s) => s.play);
  const pause = useAppStore((s) => s.pause);
  const setFrameIntervalMs = useAppStore((s) => s.setFrameIntervalMs);
  const jumpToOpIndex = useAppStore((s) => s.jumpToOpIndex);

  const disabled = !runResult;
  // Step in frame units — each click of next/prev advances one
  // Python line event captured by the tracer. The slider goes
  // 0..trace.length-1.
  const last = runResult?.trace.length ? runResult.trace.length - 1 : 0;

  return (
    <div className="bg-coden-surface border border-coden-border rounded px-3 py-2 flex items-center gap-2">
      <button
        type="button"
        onClick={() => step('first')}
        disabled={disabled}
        className="px-2 py-1 text-sm rounded border border-coden-border hover:bg-coden-border disabled:opacity-30"
        title="Jump to first op (Home)"
      >
        ⏮
      </button>
      <button
        type="button"
        onClick={() => step(-1)}
        disabled={disabled}
        className="px-2 py-1 text-sm rounded border border-coden-border hover:bg-coden-border disabled:opacity-30"
        title="Step back one op (←)"
      >
        ◀
      </button>
      <button
        type="button"
        onClick={() => (isPlaying ? pause() : play())}
        disabled={disabled}
        className="px-3 py-1 text-sm rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-30"
        title="Play / pause (Space)"
      >
        {isPlaying ? '⏸' : '▶'}
      </button>
      <button
        type="button"
        onClick={() => step(1)}
        disabled={disabled}
        className="px-2 py-1 text-sm rounded border border-coden-border hover:bg-coden-border disabled:opacity-30"
        title="Step forward one op (→)"
      >
        ▶|
      </button>
      <button
        type="button"
        onClick={() => step('last')}
        disabled={disabled}
        className="px-2 py-1 text-sm rounded border border-coden-border hover:bg-coden-border disabled:opacity-30"
        title="Jump to last op (End)"
      >
        ⏭
      </button>

      <input
        type="range"
        min={0}
        max={last}
        value={opIndex}
        onChange={(e) => jumpToOpIndex(Number(e.target.value))}
        disabled={disabled}
        className="flex-1 mx-2 accent-coden-accent"
      />

      <select
        value={frameIntervalMs}
        onChange={(e) => setFrameIntervalMs(Number(e.target.value))}
        className="bg-coden-bg border border-coden-border rounded px-2 py-1 text-xs font-mono"
        title="How long each step is shown in the play loop"
      >
        {FRAME_INTERVALS.map((opt) => (
          <option key={opt.ms} value={opt.ms}>
            {opt.label}
          </option>
        ))}
      </select>
    </div>
  );
}
