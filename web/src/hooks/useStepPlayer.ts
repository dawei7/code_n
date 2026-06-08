/**
 * useStepPlayer — drives the play loop for the visualizer.
 *
 * Uses setInterval (not requestAnimationFrame) because the
 * animation rate is set by `frameIntervalMs` (how long each
 * step is shown) — typically 250-2000 ms, much slower than
 * 60 fps, so a 1-step-per-tick interval is exactly the right
 * granularity.
 *
 * Stepping is in **op** units: each tick advances one op. The
 * LocalsPanel computes the corresponding frame (latest frame
 * with op_index <= current opIndex) and renders the locals
 * for that frame. CSS transitions give the visual smoothness
 * for the bars / cells; the React state update changes the
 * data behind the cells.
 *
 * NB: `opIndex` is intentionally NOT in the effect deps.
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
      const last = s.runResult.ops_log.length - 1;
      if (s.opIndex >= last) {
        s.pause();
        return;
      }
      s.step(1);
    }, Math.max(50, frameIntervalMs));
    return () => clearInterval(id);
  }, [isPlaying, runResult, frameIntervalMs]);
}
