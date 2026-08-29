import { useState, useEffect, useRef } from 'react';

export interface TraceStep {
  step: number;
  line?: number;
  event?: string;
  func_name?: string;
  depth?: number;
  locals: Record<string, any>;
  changed_keys?: string[];
}

interface ExecutionTraceVisualizerProps {
  steps: TraceStep[];
  sourceCode?: string;
}

export function ExecutionTraceVisualizer({ steps }: ExecutionTraceVisualizerProps) {
  const [currentStepIndex, setCurrentStepIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [playbackSpeed, setPlaybackSpeed] = useState(1);
  const playTimerRef = useRef<number | null>(null);

  useEffect(() => {
    setCurrentStepIndex(0);
    setIsPlaying(false);
  }, [steps]);

  useEffect(() => {
    if (isPlaying) {
      playTimerRef.current = window.setInterval(() => {
        setCurrentStepIndex((prev) => {
          if (prev >= steps.length - 1) {
            setIsPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, 700 / playbackSpeed);
    } else if (playTimerRef.current) {
      clearInterval(playTimerRef.current);
    }
    return () => {
      if (playTimerRef.current) clearInterval(playTimerRef.current);
    };
  }, [isPlaying, playbackSpeed, steps.length]);

  if (!steps || steps.length === 0) {
    return (
      <div className="rounded border border-coden-border bg-coden-surface/30 p-4 text-center text-sm text-coden-muted">
        No execution trace available for this test case. Run or debug to capture step-by-step state.
      </div>
    );
  }

  const currentStep = steps[currentStepIndex] || steps[0];
  const locals = currentStep.locals || {};
  const changedKeys = currentStep.changed_keys || [];

  // Identify arrays and index pointers in locals
  const arrayVars: Array<{ name: string; values: any[] }> = [];
  const pointerVars: Array<{ name: string; value: number }> = [];

  Object.entries(locals).forEach(([k, v]) => {
    if (Array.isArray(v) && v.length <= 50) {
      arrayVars.push({ name: k, values: v });
    } else if (typeof v === 'number' && Number.isInteger(v) && v >= 0 && v <= 100) {
      if (['i', 'j', 'k', 'l', 'r', 'left', 'right', 'mid', 'idx', 'low', 'high', 'start', 'end', 'curr', 'head', 'tail', 'p', 'ptr'].includes(k.toLowerCase())) {
        pointerVars.push({ name: k, value: v });
      }
    }
  });

  return (
    <div className="rounded-lg border border-coden-border bg-coden-surface/60 overflow-hidden my-4">
      {/* Visualizer Header Controls */}
      <div className="flex flex-wrap items-center justify-between gap-2 border-b border-coden-border bg-coden-surface px-4 py-2 text-xs">
        <div className="flex items-center gap-2">
          <span className="font-semibold text-coden-accent flex items-center gap-1">
            <svg className="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor">
              <path d="M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z" />
            </svg>
            Execution Stepper
          </span>
          <span className="rounded bg-coden-border/60 px-2 py-0.5 text-[11px] font-mono text-coden-muted">
            Step {currentStepIndex + 1} / {steps.length}
          </span>
          {currentStep.func_name && (
            <span className="rounded border border-coden-border bg-coden-surface px-1.5 py-0.5 font-mono text-coden-text text-[11px]">
              {currentStep.func_name}() (depth {currentStep.depth ?? 1})
            </span>
          )}
        </div>

        {/* Playback Controls */}
        <div className="flex items-center gap-1.5">
          <button
            type="button"
            onClick={() => setCurrentStepIndex(0)}
            disabled={currentStepIndex === 0}
            title="Reset to beginning"
            className="rounded p-1 text-coden-muted hover:bg-coden-border/40 hover:text-coden-text disabled:opacity-40"
          >
            ↺
          </button>
          <button
            type="button"
            onClick={() => setCurrentStepIndex((i) => Math.max(0, i - 1))}
            disabled={currentStepIndex === 0}
            title="Previous step"
            className="rounded p-1 text-coden-muted hover:bg-coden-border/40 hover:text-coden-text disabled:opacity-40"
          >
            ◀
          </button>
          <button
            type="button"
            onClick={() => setIsPlaying((p) => !p)}
            title={isPlaying ? 'Pause' : 'Auto Play'}
            className="rounded bg-coden-accent/20 px-2.5 py-1 text-coden-accent hover:bg-coden-accent/30 font-semibold text-xs"
          >
            {isPlaying ? '❚❚ Pause' : '▶ Play'}
          </button>
          <button
            type="button"
            onClick={() => setCurrentStepIndex((i) => Math.min(steps.length - 1, i + 1))}
            disabled={currentStepIndex === steps.length - 1}
            title="Next step"
            className="rounded p-1 text-coden-muted hover:bg-coden-border/40 hover:text-coden-text disabled:opacity-40"
          >
            ▶
          </button>

          {/* Speed selector */}
          <div className="ml-2 flex items-center gap-1 text-[11px] text-coden-muted">
            <span>Speed:</span>
            <select
              value={playbackSpeed}
              onChange={(e) => setPlaybackSpeed(parseFloat(e.target.value))}
              className="rounded border border-coden-border bg-coden-surface px-1 py-0.5 text-coden-text"
            >
              <option value={0.5}>0.5x</option>
              <option value={1}>1.0x</option>
              <option value={2}>2.0x</option>
            </select>
          </div>
        </div>
      </div>

      {/* Scrubber Progress Bar */}
      <div className="bg-coden-border/20 px-4 py-1.5 border-b border-coden-border">
        <input
          type="range"
          min={0}
          max={steps.length - 1}
          value={currentStepIndex}
          onChange={(e) => setCurrentStepIndex(parseInt(e.target.value, 10))}
          className="w-full h-1.5 bg-coden-border rounded-lg appearance-none cursor-pointer accent-coden-accent"
        />
      </div>

      {/* Main Visualizer Content */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 p-4">
        {/* Left Column: Visual Data Structures & Arrays */}
        <div className="space-y-3">
          <h4 className="text-xs font-semibold uppercase tracking-wider text-coden-muted flex items-center gap-1.5">
            <span>Visual Data & Pointers</span>
          </h4>

          {arrayVars.length > 0 ? (
            arrayVars.map(({ name, values }) => (
              <div key={name} className="rounded border border-coden-border bg-coden-surface/80 p-3">
                <div className="text-xs font-mono font-bold text-coden-accent mb-2">{name} (len={values.length})</div>
                <div className="flex flex-wrap gap-1.5 items-end overflow-x-auto pb-1">
                  {values.map((val, idx) => {
                    const activePointers = pointerVars.filter((p) => p.value === idx);
                    const isTargeted = activePointers.length > 0;
                    return (
                      <div key={idx} className="flex flex-col items-center">
                        {/* Pointer label */}
                        <div className="h-4 text-[10px] font-mono font-bold text-amber-400">
                          {activePointers.map((p) => p.name).join(', ')}
                        </div>
                        {/* Array Cell */}
                        <div
                          className={`w-8 h-8 flex items-center justify-center font-mono text-xs font-semibold rounded border transition-colors ${
                            isTargeted
                              ? 'border-amber-400 bg-amber-400/20 text-amber-200'
                              : 'border-coden-border bg-coden-surface text-coden-text'
                          }`}
                        >
                          {typeof val === 'object' ? JSON.stringify(val) : String(val)}
                        </div>
                        {/* Index */}
                        <span className="text-[9px] font-mono text-coden-muted mt-0.5">{idx}</span>
                      </div>
                    );
                  })}
                </div>
              </div>
            ))
          ) : (
            <div className="rounded border border-dashed border-coden-border p-3 text-center text-xs text-coden-muted">
              No arrays in local variables to display.
            </div>
          )}

          {/* Pointer list summary */}
          {pointerVars.length > 0 && (
            <div className="flex flex-wrap gap-2 text-xs font-mono">
              {pointerVars.map((p) => (
                <span key={p.name} className="rounded border border-amber-400/40 bg-amber-400/10 px-2 py-0.5 text-amber-300">
                  {p.name} = {p.value}
                </span>
              ))}
            </div>
          )}
        </div>

        {/* Right Column: Local Variables Table */}
        <div>
          <h4 className="text-xs font-semibold uppercase tracking-wider text-coden-muted mb-2 flex items-center justify-between">
            <span>Local Variables</span>
            {currentStep.line && (
              <span className="text-[11px] font-mono text-coden-accent flex items-center gap-1">
                Line {currentStep.line}
              </span>
            )}
          </h4>

          <div className="rounded border border-coden-border bg-coden-surface/80 overflow-hidden">
            <table className="w-full text-left text-xs font-mono">
              <thead>
                <tr className="border-b border-coden-border bg-coden-surface text-coden-muted">
                  <th className="px-3 py-1.5 font-semibold">Variable</th>
                  <th className="px-3 py-1.5 font-semibold">Value</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-coden-border/40">
                {Object.entries(locals).length > 0 ? (
                  Object.entries(locals).map(([key, val]) => {
                    const isChanged = changedKeys.includes(key);
                    return (
                      <tr key={key} className={isChanged ? 'bg-emerald-500/10' : ''}>
                        <td className="px-3 py-1.5 font-bold text-coden-text flex items-center gap-1.5">
                          {key}
                          {isChanged && (
                            <span className="rounded bg-emerald-500/20 px-1 py-0.2 text-[9px] text-emerald-300 font-sans">
                              updated
                            </span>
                          )}
                        </td>
                        <td className="px-3 py-1.5 text-coden-text break-all">
                          {typeof val === 'object' ? JSON.stringify(val) : String(val)}
                        </td>
                      </tr>
                    );
                  })
                ) : (
                  <tr>
                    <td colSpan={2} className="px-3 py-2 text-center text-coden-muted italic">
                      No local variables recorded at this step.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
