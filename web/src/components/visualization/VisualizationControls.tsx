import type { PlaybackSpeed } from './useVisualizationPlayback';

export function VisualizationControls({
  current,
  total,
  playing,
  speed,
  stepTitle,
  onPrevious,
  onNext,
  onTogglePlayback,
  onSelect,
  onSpeedChange,
}: {
  current: number;
  total: number;
  playing: boolean;
  speed: PlaybackSpeed;
  stepTitle: string;
  onPrevious: () => void;
  onNext: () => void;
  onTogglePlayback: () => void;
  onSelect: (index: number) => void;
  onSpeedChange: (speed: PlaybackSpeed) => void;
}) {
  return (
    <div className="flex flex-col gap-3 border-t border-coden-border bg-coden-inner/60 px-4 py-3 lg:flex-row lg:items-center">
      <div className="grid w-full shrink-0 grid-cols-3 gap-2 sm:flex sm:w-auto sm:items-center">
        <button
          type="button"
          onClick={onPrevious}
          disabled={current === 0}
          className="inline-flex h-9 items-center justify-center gap-1 rounded border border-coden-border px-2 text-xs font-semibold text-coden-text hover:bg-coden-border/50 disabled:cursor-not-allowed disabled:opacity-35 sm:gap-1.5 sm:px-3"
        >
          <PlaybackIcon kind="previous" /> Previous
        </button>
        <button
          type="button"
          onClick={onTogglePlayback}
          aria-label={playing ? 'Pause walkthrough' : current === total - 1 ? 'Replay walkthrough' : 'Play walkthrough'}
          className="inline-flex h-9 items-center justify-center gap-1.5 rounded bg-coden-accent px-2 text-xs font-semibold text-coden-accentContrast hover:opacity-90 sm:min-w-24 sm:px-3"
        >
          <PlaybackIcon kind={playing ? 'pause' : current === total - 1 ? 'replay' : 'play'} />
          {playing ? 'Pause' : current === total - 1 ? 'Replay' : 'Play'}
        </button>
        <button
          type="button"
          onClick={onNext}
          disabled={current === total - 1}
          className="inline-flex h-9 items-center justify-center gap-1 rounded border border-coden-border px-2 text-xs font-semibold text-coden-text hover:bg-coden-border/50 disabled:cursor-not-allowed disabled:opacity-35 sm:gap-1.5 sm:px-3"
        >
          Next <PlaybackIcon kind="next" />
        </button>
      </div>
      <div className="flex min-w-0 flex-1 items-center gap-3">
        <label htmlFor="visualization-progress" className="sr-only">Walkthrough step</label>
        <input
          id="visualization-progress"
          type="range"
          min={0}
          max={total - 1}
          value={current}
          onChange={(event) => onSelect(Number(event.target.value))}
          aria-valuetext={`Step ${current + 1} of ${total}: ${stepTitle}`}
          className="h-1.5 min-w-24 flex-1 cursor-pointer accent-[var(--coden-accent)]"
        />
        <span className="shrink-0 font-mono text-[11px] text-coden-muted">
          {current + 1} / {total}
        </span>
      </div>
      <div className="flex shrink-0 items-center justify-between gap-3 lg:justify-end">
        <span className="hidden text-[10px] text-coden-muted xl:inline">← → step · Space play/pause</span>
        <label className="flex items-center gap-2 text-[10px] font-semibold uppercase tracking-wide text-coden-muted">
          Speed
          <select
            value={speed}
            onChange={(event) => onSpeedChange(Number(event.target.value) as PlaybackSpeed)}
            className="h-8 rounded border border-coden-border bg-coden-bg px-2 font-mono text-xs text-coden-text"
          >
            <option value={0.75}>0.75×</option>
            <option value={1}>1×</option>
            <option value={1.5}>1.5×</option>
          </select>
        </label>
      </div>
    </div>
  );
}

function PlaybackIcon({ kind }: { kind: 'previous' | 'next' | 'play' | 'pause' | 'replay' }) {
  if (kind === 'pause') {
    return (
      <svg aria-hidden="true" viewBox="0 0 16 16" className="h-3.5 w-3.5 fill-current">
        <rect x="3" y="2" width="3" height="12" rx="1" />
        <rect x="10" y="2" width="3" height="12" rx="1" />
      </svg>
    );
  }
  if (kind === 'replay') {
    return (
      <svg aria-hidden="true" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.7" className="h-3.5 w-3.5">
        <path d="M3.2 5.1A5.5 5.5 0 1 1 2.7 10" />
        <path d="M3.3 1.9v3.5H6.8" />
      </svg>
    );
  }
  if (kind === 'play') {
    return (
      <svg aria-hidden="true" viewBox="0 0 16 16" className="h-3.5 w-3.5 fill-current">
        <path d="M4 2.7v10.6c0 .7.8 1.1 1.4.7l7.1-5.3a.85.85 0 0 0 0-1.4L5.4 2C4.8 1.6 4 2 4 2.7Z" />
      </svg>
    );
  }
  const next = kind === 'next';
  return (
    <svg aria-hidden="true" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" className="h-3.5 w-3.5">
      <path d={next ? 'm6 3 5 5-5 5' : 'm10 3-5 5 5 5'} />
    </svg>
  );
}
