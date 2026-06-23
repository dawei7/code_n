/**
 * Single source of truth for the `window.electronAPI` surface.
 *
 * The renderer uses HTTP/WebSocket calls for app behavior. Electron
 * only exposes desktop-only update controls here.
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
  version?: string;
  progress?: number;
  transferred?: number;
  total?: number;
  message?: string;
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
  checkForUpdates: () => Promise<UpdateCheckResult>;
  installUpdateAndRestart: () => void;
  getAppVersion: () => Promise<AppVersionInfo>;
  onUpdateStatus: (cb: (payload: UpdateStatusPayload) => void) => () => void;
};


declare global {
  interface Window {
    electronAPI?: ElectronAPI;
  }
}
