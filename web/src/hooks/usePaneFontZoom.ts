import { useEffect } from 'react';

import { useAppStore } from '../store/useAppStore';


const WHEEL_THRESHOLD = 24;
const ZOOM_STEP = 0.1;


/** Ctrl+wheel zooms only the workspace pane below the pointer. */
export function usePaneFontZoom(): void {
  useEffect(() => {
    let accumulatedDelta = 0;
    let accumulatedScope = '';

    const onWheel = (event: WheelEvent) => {
      if (!event.ctrlKey) return;
      event.preventDefault();

      const element = event.target instanceof Element
        ? event.target.closest<HTMLElement>('[data-font-scope]')
        : null;
      const scope = element?.dataset.fontScope;
      if (!scope) return;

      if (scope !== accumulatedScope) {
        accumulatedScope = scope;
        accumulatedDelta = 0;
      }
      accumulatedDelta += event.deltaY;
      if (Math.abs(accumulatedDelta) < WHEEL_THRESHOLD) return;

      const state = useAppStore.getState();
      const current = state.paneFontScales[scope] ?? 1;
      state.setPaneFontScale(
        scope,
        current + (accumulatedDelta < 0 ? ZOOM_STEP : -ZOOM_STEP),
      );
      accumulatedDelta = 0;
    };

    window.addEventListener('wheel', onWheel, { capture: true, passive: false });
    return () => window.removeEventListener('wheel', onWheel, { capture: true });
  }, []);
}
