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

export interface LeetCodeCredentialInput {
  session: string;
  csrfToken: string;
  cloudflareClearance?: string;
}

export interface LeetCodeSessionStatus {
  configured: boolean;
  secureStorageAvailable: boolean;
  state: 'missing' | 'unchecked' | 'valid' | 'expired' | 'blocked' | 'unreachable' | 'unavailable';
  message: string;
  username?: string;
  real_name?: string;
  is_premium?: boolean;
  checked_at?: string;
}

export interface LeetCodeSubmissionResult {
  accepted: boolean;
  status: string;
  submission_id: string;
  runtime?: string;
  memory?: string;
  message: string;
}


export type ElectronAPI = {
  checkForUpdates: () => Promise<UpdateCheckResult>;
  installUpdateAndRestart: () => void;
  getAppVersion: () => Promise<AppVersionInfo>;
  onUpdateStatus: (cb: (payload: UpdateStatusPayload) => void) => () => void;
  saveLeetCodeCredentials: (input: LeetCodeCredentialInput) => Promise<LeetCodeSessionStatus>;
  clearLeetCodeCredentials: () => Promise<LeetCodeSessionStatus>;
  getLeetCodeSessionStatus: () => Promise<LeetCodeSessionStatus>;
  submitVerifiedToLeetCode: (challengeId: string) => Promise<LeetCodeSubmissionResult>;
};


declare global {
  interface Window {
    electronAPI?: ElectronAPI;
  }
}
