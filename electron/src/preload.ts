/**
 * Electron preload script.
 *
 * Runs in an isolated context with access to a small subset of
 * Node APIs (ipcRenderer) and the ability to expose a typed API
 * to the renderer via contextBridge. The renderer (React app)
 * sees this as ``window.electronAPI`` and calls these functions
 * to invoke native capabilities.
 *
 * Exposed functions:
 *   - openInVSCode(challengeId) — opens the player's exact
 *     ``solutions/<challengeId>.py`` file in VSCode. The file
 *     lives in the standard per-user appData dir
 *     (``app.getPath('userData')/solutions/<id>.py``), and the
 *     parent folder is a self-contained VSCode workspace
 *     (``.vscode/`` + ``tools/`` + ``server/`` etc. were copied
 *     there on first launch by the main process). So F5 hits
 *     breakpoints in the player's file. Returns a result
 *     object with ``ok``, the resolved ``filePath``, and an
 *     ``error`` string on failure.
 *   - checkForUpdates() / installUpdateAndRestart() / getAppVersion()
 *     — see the auto-update wiring in `electron/src/updater.ts`
 *     and the React UI in `web/src/components/UpdateToast.tsx`.
 *   - onUpdateStatus(cb) — subscribe to "update:status" events
 *     broadcast by the main process whenever the auto-updater
 *     state changes. Returns an unsubscribe function.
 *
 * The v0.9.0 pivot removed the pop-out-editor, pop-out-debug,
 * and pop-out-pane IPC handlers (no detached BrowserWindows).
 *
 * The `ElectronAPI` type and the `Window.electronAPI` global
 * augmentation are declared in `web/src/types/electron.ts` so
 * both the renderer and the preload agree on a single shape.
 */

import { contextBridge, ipcRenderer } from 'electron';
import type {
  ElectronAPI,
  OpenInVSCodeResult,
  UpdateState,
  UpdateStatusPayload,
} from '../../web/src/types/electron';


contextBridge.exposeInMainWorld('electronAPI', {
  openInVSCode: (challengeId: string): Promise<OpenInVSCodeResult> =>
    ipcRenderer.invoke('open-in-vscode', { challengeId }),

  // ---- Auto-update surface ----

  checkForUpdates: (): Promise<{ ok: boolean; state: UpdateState; version?: string; message?: string }> =>
    ipcRenderer.invoke('update:check'),

  installUpdateAndRestart: (): void => {
    ipcRenderer.invoke('update:install-and-quit');
  },

  getAppVersion: (): Promise<{ current: string; channel: string }> =>
    ipcRenderer.invoke('update:get-version'),

  onUpdateStatus: (cb: (payload: UpdateStatusPayload) => void): (() => void) => {
    const handler = (_evt: unknown, payload: UpdateStatusPayload) => cb(payload);
    ipcRenderer.on('update:status', handler);
    return () => { ipcRenderer.removeListener('update:status', handler); };
  },
} satisfies ElectronAPI);
