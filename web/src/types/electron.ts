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
 * that opens the player's exact ``solutions/<id>.py`` file
 * in VSCode.
 *
 * The auto-update surface (`checkForUpdates`, `onUpdateStatus`,
 * etc.) is wired in `electron/src/updater.ts` and surfaced to the
 * React UI via `web/src/components/UpdateToast.tsx`.
 *
 * The "Open in VSCode" flow takes a challenge id, computes the
 * file path inside the standard per-user appData dir, and
 * calls ``shell.openPath(filePath)`` in the Electron main
 * process. The file's parent folder is a self-contained VSCode
 * workspace (``.vscode/``, ``tools/``, ``server/``, etc. were
 * copied there on first launch), so F5 hits breakpoints in the
 * player's source without any further setup.
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


/**
 * Result of ``openInVSCode(challengeId)``.
 *
 * On success: ``ok: true`` + the absolute ``filePath`` that
 * was handed to ``shell.openPath`` (useful for the renderer's
 * "now editing" indicator).
 *
 * On failure: ``ok: false`` + a human-readable ``error``.
 * Common reasons:
 *   - The challenge id was invalid (renderer bug — should
 *     never happen in practice)
 *   - The solution file doesn't exist yet (the player clicked
 *     "Open in VSCode" before the challenge was selected in
 *     cOde(n))
 *   - VSCode isn't installed, or no app is associated with
 *     ``.py`` files (the OS error from ``shell.openPath``)
 */
export interface OpenInVSCodeResult {
  ok: boolean;
  filePath?: string;
  error?: string;
}


export type ElectronAPI = {
  /**
   * Open the player's exact ``solutions/<challengeId>.py`` file
   * in VSCode. The Electron main process calls
   * ``shell.openPath(filePath)`` where ``filePath`` is the
   * absolute path inside the standard per-user appData dir
   * (``app.getPath('userData')/solutions/<id>.py``). VSCode
   * (when installed + associated with ``.py``) opens the file
   * in its currently-active window. The parent folder is a
   * self-contained VSCode workspace with ``.vscode/launch.json``,
   * ``tools/run_solution.py``, and the engine source on the
   * Python path, so F5 hits breakpoints in the player's file.
   *
   * The renderer should have written the active-challenge
   * handoff file (via the ``/api/vscode/active`` HTTP route in
   * the FastAPI server) BEFORE calling this — the F5 launch
   * config in VSCode reads that file when no id is passed on
   * the command line.
   */
  openInVSCode: (challengeId: string) => Promise<OpenInVSCodeResult>;

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
