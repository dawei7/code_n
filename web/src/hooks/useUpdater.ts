/**
 * useUpdater — React hook for the auto-update flow.
 *
 * Subscribes to the main-process "update:status" events and
 * exposes the current state + a `checkNow()` trigger.
 *
 * Used by:
 *   - web/src/components/UpdateToast.tsx (the floating "downloading…"
 *     / "restart to install" pill at the bottom-right)
 *   - web/src/components/AppShell.tsx (the "Check for updates" button
 *     in the TopHeader)
 *
 * Behavior matrix (per spec):
 *   - idle / not-available / error: no UI changes; the "Check for
 *     updates" button briefly shows the last status as a tooltip.
 *   - available / downloading: a small toast appears in the
 *     bottom-right with a progress bar.
 *   - downloaded: a "Restart to install" button is shown.
 *
 * In dev (no `window.electronAPI`), the hook is a no-op; status
 * stays 'idle' forever.
 */

import { useCallback, useEffect, useRef, useState } from 'react';
import type { AppVersionInfo, UpdateStatusPayload } from '../types/electron';


/** Latest state we have observed from the main process. */
export interface UpdaterState {
  status: UpdateStatusPayload;
  appVersion: AppVersionInfo | null;
  /** True if checkForUpdates() is currently in flight. */
  checking: boolean;
}


const INITIAL: UpdaterState = {
  status: { state: 'idle' },
  appVersion: null,
  checking: false,
};


export function useUpdater(): {
  state: UpdaterState;
  checkNow: () => Promise<void>;
  install: () => void;
} {
  const [state, setState] = useState<UpdaterState>(INITIAL);
  /** Ref guard so the onUpdateStatus handler isn't installed twice
   *  in dev (StrictMode double-invokes effects). */
  const installedRef = useRef(false);

  // ---- Subscribe to main-process status events ----
  useEffect(() => {
    if (installedRef.current) return;
    installedRef.current = true;
    const api = window.electronAPI;
    if (!api?.onUpdateStatus) return;
    const unsubscribe = api.onUpdateStatus((payload) => {
      setState((prev) => ({ ...prev, status: payload }));
    });
    return () => {
      installedRef.current = false;
      unsubscribe();
    };
  }, []);

  // ---- Fetch the app version once on mount ----
  useEffect(() => {
    const api = window.electronAPI;
    if (!api?.getAppVersion) return;
    let cancelled = false;
    void api.getAppVersion().then((info) => {
      if (!cancelled) setState((prev) => ({ ...prev, appVersion: info }));
    });
    return () => { cancelled = true; };
  }, []);

  // ---- Manual check trigger ----
  const checkNow = useCallback(async () => {
    const api = window.electronAPI;
    if (!api?.checkForUpdates) return;
    setState((prev) => ({ ...prev, checking: true }));
    try {
      const result = await api.checkForUpdates();
      // The "result" is the synchronous answer; richer state
      // transitions arrive via onUpdateStatus. Show them
      // immediately if the renderer hasn't seen them yet.
      setState((prev) => ({
        ...prev,
        checking: false,
        status: {
          // Only overwrite the state if the result is "later" than
          // what we already have - e.g. avoid clobbering a
          // 'downloading' status with a stale 'available'.
          state: rankState(result.state) > rankState(prev.status.state)
            ? result.state
            : prev.status.state,
          version: result.version ?? prev.status.version,
          message: result.message ?? prev.status.message,
        },
      }));
    } catch (e) {
      setState((prev) => ({
        ...prev,
        checking: false,
        status: {
          state: 'error',
          message: e instanceof Error ? e.message : String(e),
        },
      }));
    }
  }, []);

  // ---- Restart-and-install trigger ----
  const install = useCallback(() => {
    const api = window.electronAPI;
    if (!api?.installUpdateAndRestart) return;
    api.installUpdateAndRestart();
    // quitAndInstall() will kill the process; the state update
    // below is best-effort.
  }, []);

  return { state, checkNow, install };
}


/** Numeric ranking for "which state is more interesting / further along
 *  the update lifecycle". Used so a fast IPC reply doesn't clobber
 *  a later state we already received. */
function rankState(s: UpdateStatusPayload['state']): number {
  switch (s) {
    case 'idle': return 0;
    case 'error': return 1;
    case 'not-available': return 2;
    case 'checking': return 3;
    case 'available': return 4;
    case 'downloading': return 5;
    case 'downloaded': return 6;
  }
}
