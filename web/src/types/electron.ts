/**
 * Single source of truth for the `window.electronAPI` surface
 * that the preload script exposes. Renderer code imports this
 * type for the global Window augmentation; the preload script
 * imports it for its own runtime typing.
 *
 * The in-app debug surface, the editor pop-out, and the
 * detached-pane host were all removed in the v0.9.0 pivot
 * (the player edits + debugs in VSCode). The remaining IPC
 * surface is the auto-updater + an "Open in VSCode" button
 * that calls ``shell.openPath(repoRoot)`` in the Electron
 * main process.
 *
 * The auto-update surface (`checkForUpdates`, `onUpdateStatus`,
 * etc.) is wired in `electron/src/updater.ts` and surfaced to the
 * React UI via `web/src/components/UpdateToast.tsx`.
 */
export type UpdateState =
  | 'idle'
  | 'checking'
  | 'available'
  | 'downloading'
  | 'downloaded'
  | 'not-available'
  | 'error';


export interface UpdateStatusPayload {
  state: UpdateState;
  /** Newer version that's available / downloading / downloaded. */
  version?: string;
  /** Download progress (0..1) when state === 'downloading'. */
  progress?: number;
  /** Bytes transferred / total (when known). */
  transferred?: number;
  total?: number;
  /** Human-readable error message when state === 'error'. */
  message?: string;
  /** Set when the auto-check on launch fires, so the UI can
   *  distinguish "no auto-check has happened yet" from "checked,
   *  nothing to do". */
  autoChecked?: boolean;
}


export interface UpdateCheckResult {
  ok: boolean;
  state: UpdateState;
  version?: string;
  message?: string;
}


export interface AppVersionInfo {
  current: string;
  channel: string;
}


export type ElectronAPI = {
  /**
   * Open the repo root in VSCode (the player's default editor
   * for editing solutions/<id>.py). The Electron main process
   * calls ``shell.openPath(repoRoot)`` which routes through
   * the OS file-association handler — VSCode on Windows opens
   * the project; macOS / Linux do the same via xdg-open /
   * the equivalent. Returns true on success, false if VSCode
   * isn't installed (the UI should fall back to a toast).
   *
   * The renderer should have written the active-challenge
   * handoff file (via the ``/api/vscode/active`` HTTP route
   * in the FastAPI server) BEFORE calling this — the F5
   * launch config in VSCode reads that file when no id is
   * passed on the command line.
   */
  openInVSCode: () => Promise<boolean>;

  /**
   * Trigger a manual update check. Returns a structured result
   * with the state observed (for synchronous UI feedback); the
   * longer-running state transitions arrive via onUpdateStatus.
   * In dev (browser) this is a no-op that resolves to
   * `state: 'not-available'`.
   */
  checkForUpdates: () => Promise<UpdateCheckResult>;
  /**
   * Quit the app and apply the most recently downloaded update on
   * next launch. The user is the one who clicks "Restart", so
   * we don't auto-install on quit (configurable in updater.ts).
   * No-op in dev.
   */
  installUpdateAndRestart: () => void;
  /**
   * Current installed version + the update channel we're
   * listening to. Used by the React UI to show "v0.1.0" in
   * the header next to the "Check for updates" button.
   */
  getAppVersion: () => Promise<AppVersionInfo>;
  /**
   * Subscribe to "update:status" events broadcast by the main
   * process whenever the auto-updater state changes. Returns
   * an unsubscribe function. React UI uses this to drive the
   * "downloading…" / "restart to install" toast.
   */
  onUpdateStatus: (cb: (payload: UpdateStatusPayload) => void) => () => void;
};


declare global {
  interface Window {
    electronAPI?: ElectronAPI;
  }
}
