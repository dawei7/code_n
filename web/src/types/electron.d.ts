/**
 * Single source of truth for the `window.electronAPI` surface
 * that the preload script exposes. Renderer code imports this
 * type for the global Window augmentation; the preload script
 * imports it for its own runtime typing.
 */
export type ElectronAPI = {
  /**
   * Open a new BrowserWindow hosting the legacy pop-out Monaco
   * editor at `?view=editor`. Returns true on success.
   */
  popOutEditor: () => Promise<boolean>;
  /**
   * Open a new BrowserWindow hosting a detached pane at
   * `?view=pane&paneId=...&tabId=...`. Returns true on success.
   */
  popOutPane: (paneId: string, tabId: string) => Promise<boolean>;
  /**
   * Subscribe to "a detached pane window was closed" events.
   * Returns an unsubscribe function. The handler receives the
   * paneId of the window that just closed.
   */
  onPaneWindowClosed: (cb: (paneId: string) => void) => () => void;
};


declare global {
  interface Window {
    electronAPI?: ElectronAPI;
  }
}
