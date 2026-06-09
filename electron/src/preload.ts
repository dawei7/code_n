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
 *
 * The `ElectronAPI` type and the `Window.electronAPI` global
 * augmentation are declared in `web/src/types/electron.d.ts` so
 * both the renderer and the preload agree on a single shape.
 */

import { contextBridge, ipcRenderer } from 'electron';
import type { ElectronAPI } from '../../web/src/types/electron';


contextBridge.exposeInMainWorld('electronAPI', {
  popOutEditor: (): Promise<boolean> => ipcRenderer.invoke('pop-out-editor'),

  popOutPane: (paneId: string, tabId: string): Promise<boolean> =>
    ipcRenderer.invoke('pop-out-pane', paneId, tabId),

  onPaneWindowClosed: (cb: (paneId: string) => void): (() => void) => {
    const handler = (_evt: unknown, paneId: string) => cb(paneId);
    ipcRenderer.on('pane-window-closed', handler);
    return () => { ipcRenderer.removeListener('pane-window-closed', handler); };
  },
} satisfies ElectronAPI);
