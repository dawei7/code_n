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
 *   - popOutEditor() — opens the legacy pop-out Monaco editor
 *     window at `?view=editor`.
 *   - popOutPane(paneId, tabId) — opens a new BrowserWindow at
 *     `?view=pane&paneId=...&tabId=...` that hosts a single tab
 *     in its own window.
 *   - onPaneWindowClosed(cb) — subscribe to "a detached window
 *     was closed" events. Returns an unsubscribe function. Used
 *     by the main window to clear the corresponding "detached"
 *     flag in the layout store.
 *   - checkForUpdates() / installUpdateAndRestart() / getAppVersion()
 *     — see the auto-update wiring in `electron/src/updater.ts`
 *     and the React UI in `web/src/components/UpdateToast.tsx`.
 *   - onUpdateStatus(cb) — subscribe to "update:status" events
 *     broadcast by the main process whenever the auto-updater
 *     state changes. Returns an unsubscribe function.
 *
 * The `ElectronAPI` type and the `Window.electronAPI` global
 * augmentation are declared in `web/src/types/electron.d.ts` so
 * both the renderer and the preload agree on a single shape.
 */

import { contextBridge, ipcRenderer } from 'electron';
import type {
  ElectronAPI,
  UpdateState,
  UpdateStatusPayload,
} from '../../web/src/types/electron';


contextBridge.exposeInMainWorld('electronAPI', {
  popOutEditor: (): Promise<boolean> => ipcRenderer.invoke('pop-out-editor'),

  popOutPane: (paneId: string, tabId: string): Promise<boolean> =>
    ipcRenderer.invoke('pop-out-pane', paneId, tabId),

  onPaneWindowClosed: (cb: (paneId: string) => void): (() => void) => {
    const handler = (_evt: unknown, paneId: string) => cb(paneId);
    ipcRenderer.on('pane-window-closed', handler);
    return () => { ipcRenderer.removeListener('pane-window-closed', handler); };
  },

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
