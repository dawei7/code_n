/**
 * useStepPlayer — drives the play loop for the visualizer.
 *
 * Uses setInterval (not requestAnimationFrame) because the
 * animation rate is set by `frameIntervalMs` (how long each
 * frame is shown) — typically 250-2000 ms, much slower than
 * 60 fps, so a 1-frame-per-tick interval is exactly the
 * right granularity. CSS transitions on the cells give the
 * visual smoothness; the React state update changes the data
 * behind the cells.
 *
 * NB: `frameIndex` is intentionally NOT in the effect deps.
 * Including it would cause the effect to re-run (and clear+restart
 * the interval) on every step, which would prevent the play
 * loop from actually advancing at the configured speed.
 */
import { useEffect } from 'react';
import { useAppStore } from '../store/useAppStore';


export function useStepPlayer(): void {
  const isPlaying = useAppStore((s) => s.isPlaying);
  const runResult = useAppStore((s) => s.runResult);
  const frameIntervalMs = useAppStore((s) => s.frameIntervalMs);

  useEffect(() => {
    if (!isPlaying || !runResult) return;
    const id = setInterval(() => {
      const s = useAppStore.getState();
      if (!s.runResult) return;
      const last = s.runResult.trace.length - 1;
      if (s.frameIndex >= last) {
        s.pause();
        return;
      }
      s.step(1);
    }, Math.max(50, frameIntervalMs));
    return () => clearInterval(id);
  }, [isPlaying, runResult, frameIntervalMs]);
}
