import { useAppStore } from '../store/useAppStore';


const SPEEDS = [1, 2, 4, 8, 16, 30] as const;


export function StepControls() {
  const runResult = useAppStore((s) => s.runResult);
  const frameIndex = useAppStore((s) => s.frameIndex);
  const isPlaying = useAppStore((s) => s.isPlaying);
  const speed = useAppStore((s) => s.speed);
  const step = useAppStore((s) => s.step);
  const play = useAppStore((s) => s.play);
  const pause = useAppStore((s) => s.pause);
  const setSpeed = useAppStore((s) => s.setSpeed);
  const jumpToFrame = useAppStore((s) => s.jumpToFrame);

  const disabled = !runResult;
  const last = runResult?.trace.length ? runResult.trace.length - 1 : 0;

  return (
    <div className="bg-coden-surface border border-coden-border rounded px-3 py-2 flex items-center gap-2">
      <button
        type="button"
        onClick={() => step('first')}
        disabled={disabled}
        className="px-2 py-1 text-sm rounded border border-coden-border hover:bg-coden-border disabled:opacity-30"
        title="Jump to first frame (Home)"
      >
        ⏮
      </button>
      <button
        type="button"
        onClick={() => step(-1)}
        disabled={disabled}
        className="px-2 py-1 text-sm rounded border border-coden-border hover:bg-coden-border disabled:opacity-30"
        title="Step back (←)"
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
        title="Step forward (→)"
      >
        ▶|
      </button>
      <button
        type="button"
        onClick={() => step('last')}
        disabled={disabled}
        className="px-2 py-1 text-sm rounded border border-coden-border hover:bg-coden-border disabled:opacity-30"
        title="Jump to last frame (End)"
      >
        ⏭
      </button>

      <input
        type="range"
        min={0}
        max={last}
        value={frameIndex}
        onChange={(e) => jumpToFrame(Number(e.target.value))}
        disabled={disabled}
        className="flex-1 mx-2 accent-coden-accent"
      />

      <select
        value={speed}
        onChange={(e) => setSpeed(Number(e.target.value))}
        className="bg-coden-bg border border-coden-border rounded px-2 py-1 text-xs font-mono"
      >
        {SPEEDS.map((s) => (
          <option key={s} value={s}>
            {s} step/s
          </option>
        ))}
      </select>
    </div>
  );
}
