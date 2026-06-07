/**
 * Electron preload script.
 *
 * Runs in an isolated context with access to a small subset of
 * Node APIs (ipcRenderer) and the ability to expose a typed API
 * to the renderer via contextBridge. The renderer (React app)
 * sees this as ``window.electronAPI`` and calls these functions
 * to invoke native capabilities.
 *
 * For MVP we expose just one function: ``popOutEditor``, which
 * asks the main process to open a new BrowserWindow that loads
 * the React app in editor-only mode (?view=editor). The user
 * can then drag the new window to a second monitor.
 */

import { contextBridge, ipcRenderer } from 'electron';


contextBridge.exposeInMainWorld('electronAPI', {
  /** Ask the main process to open a new BrowserWindow in editor-only mode. */
  popOutEditor: (): Promise<boolean> => ipcRenderer.invoke('pop-out-editor'),
});


export type ElectronAPI = {
  popOutEditor: () => Promise<boolean>;
};

declare global {
  interface Window {
    electronAPI: ElectronAPI;
  }
}
