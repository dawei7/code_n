/**
 * useStepPlayer — drives the play loop for the visualizer.
 *
 * Uses setInterval (not requestAnimationFrame) because the
 * animation rate is set by `speed` (steps per second) which is
 * typically 1-30 fps — well below 60 fps, so a 1-frame-per-tick
 * interval is exactly the right granularity. CSS transitions on
 * the cells give the visual smoothness; the React state update
 * is what changes the data behind the cells.
 */
import { useEffect } from 'react';
import { useAppStore } from '../store/useAppStore';


export function useStepPlayer(): void {
  const isPlaying = useAppStore((s) => s.isPlaying);
  const speed = useAppStore((s) => s.speed);
  const runResult = useAppStore((s) => s.runResult);
  const frameIndex = useAppStore((s) => s.frameIndex);

  useEffect(() => {
    if (!isPlaying || !runResult) return;
    const interval = 1000 / Math.max(1, speed);
    const id = setInterval(() => {
      const s = useAppStore.getState();
      if (!s.runResult) return;
      const last = s.runResult.trace.length - 1;
      if (s.frameIndex >= last) {
        s.pause();
        return;
      }
      s.step(1);
    }, interval);
    return () => clearInterval(id);
  }, [isPlaying, speed, runResult, frameIndex]);
}
