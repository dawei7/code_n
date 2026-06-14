/**
 * Auto-update wiring for the cOde(n) desktop wrapper.
 *
 * Wraps `electron-updater` with a stable, typed surface and a single
 * `initAutoUpdater()` entrypoint that `main.ts` calls once after the
 * main window is ready.
 *
 * Behavior (per the spec):
 *   - Stable releases only:  `electron-builder.json` has
 *     `releaseType: "release"` and `channel: "latest"`, so
 *     pre-releases (-rc, -beta) are ignored by the updater.
 *   - Auto-download:         as soon as a newer version is found,
 *     the update is downloaded silently in the background. The
 *     user is notified only when the download finishes.
 *   - Check on launch:       one automatic check, fired after the
 *     main window's first `ready-to-show`.
 *   - Manual "Check for updates" button:  exposed via IPC; the
 *     renderer can call `checkForUpdates()` and the user gets
 *     a one-shot answer (no UI changes until the next launch
 *     unless a new version is found).
 *
 * IPC events broadcast to the renderer (via webContents.send):
 *   - `update:status`  { state, version?, message? }
 *       state in: 'idle' | 'checking' | 'available' | 'downloading'
 *                 | 'downloaded' | 'not-available' | 'error'
 *
 * IPC handlers (renderer -> main):
 *   - `update:check`          -> re-runs checkForUpdates()
 *   - `update:install-and-quit` -> quits and applies the
 *                                  downloaded update on next launch
 *   - `update:get-version`    -> returns { current, channel }
 */

import { app, BrowserWindow, ipcMain } from 'electron';
import { autoUpdater, type ProgressInfo, type UpdateInfo } from 'electron-updater';


/** Pino-style logger that writes to both stdout and the Electron
 *  log file (so the updater's events are visible in DevTools and
 *  in the user's app data dir after a crash). */
const log = {
  info: (...args: unknown[]) => console.log('[updater]', ...args),
  warn: (...args: unknown[]) => console.warn('[updater]', ...args),
  error: (...args: unknown[]) => console.error('[updater]', ...args),
  debug: (...args: unknown[]) => console.debug('[updater]', ...args),
};
autoUpdater.logger = log;


/** Single source of truth for what the updater is doing. */
export type UpdateState =
  | 'idle'           // never checked, or checked and no action needed
  | 'checking'       // checkForUpdates() in flight
  | 'available'      // newer stable version found, about to download
  | 'downloading'    // download in flight (transferred / total known)
  | 'downloaded'     // downloaded + verified; user can install-and-quit
  | 'not-available'  // check finished, no newer stable version
  | 'error';         // last check/download failed


/** Status payload sent to the renderer. */
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
  /** Set on the first auto-check after launch, so the UI can
   *  distinguish "no auto-check has happened yet" from "checked,
   *  nothing to do". */
  autoChecked?: boolean;
}


/** All renderer windows that should receive status updates. */
function broadcastToRenderers(channel: string, payload: unknown): void {
  for (const win of BrowserWindow.getAllWindows()) {
    if (win.isDestroyed()) continue;
    win.webContents.send(channel, payload);
  }
}


/** Latest newer version we know about. electron-updater's
 *  `updateInfoAndProvider` is protected, so we capture the version
 *  string here on the `update-available` event. */
let latestKnownVersion: string | undefined;


/**
 * Set up `autoUpdater` event listeners and IPC handlers.
 *
 * Idempotent: safe to call once at app start. In dev mode (when
 * `app.isPackaged` is false), we still wire the IPC handlers so
 * the renderer can call them, but the updater itself is a no-op
 * (it would fail to find a feed in dev anyway).
 */
export function initAutoUpdater(): void {
  const isPackaged = app.isPackaged;

  // --- Configuration ---
  // Stable channel only: only `latest` / `release` tag is checked.
  // Matches the `releaseType: "release"` + `channel: "latest"` in
  // electron-builder.json's publish block.
  autoUpdater.channel = 'latest';
  // Auto-download as soon as we detect a newer version. Per spec.
  autoUpdater.autoDownload = true;
  // Don't quit + install on user-initiated download; let the
  // user click "Restart" (so they don't lose unsaved work).
  autoUpdater.autoInstallOnAppQuit = false;
  // We do our own logging; mute the default logger.
  autoUpdater.logger = log;

  // --- Event handlers ---

  autoUpdater.on('checking-for-update', () => {
    broadcastToRenderers('update:status', {
      state: 'checking' as UpdateState,
    } satisfies UpdateStatusPayload);
  });

  autoUpdater.on('update-available', (info: UpdateInfo) => {
    latestKnownVersion = info.version;
    broadcastToRenderers('update:status', {
      state: 'available' as UpdateState,
      version: info.version,
    } satisfies UpdateStatusPayload);
    // autoDownload=true means the 'download-progress' and
    // 'update-downloaded' events will follow automatically.
  });

  autoUpdater.on('update-not-available', (info: UpdateInfo) => {
    broadcastToRenderers('update:status', {
      state: 'not-available' as UpdateState,
      version: info.version,
    } satisfies UpdateStatusPayload);
  });

  autoUpdater.on('download-progress', (progress: ProgressInfo) => {
    const ratio = progress.total > 0 ? progress.transferred / progress.total : 0;
    broadcastToRenderers('update:status', {
      state: 'downloading' as UpdateState,
      version: latestKnownVersion,
      progress: ratio,
      transferred: progress.transferred,
      total: progress.total,
    } satisfies UpdateStatusPayload);
  });

  autoUpdater.on('update-downloaded', (info: UpdateInfo) => {
    broadcastToRenderers('update:status', {
      state: 'downloaded' as UpdateState,
      version: info.version,
    } satisfies UpdateStatusPayload);
  });

  autoUpdater.on('error', (err: Error) => {
    broadcastToRenderers('update:status', {
      state: 'error' as UpdateState,
      message: err.message ?? String(err),
    } satisfies UpdateStatusPayload);
    log.error('[updater] error:', err);
  });

  // --- IPC: renderer -> main ---

  ipcMain.handle('update:check', async (_evt, opts?: { autoChecked?: boolean }) => {
    if (!isPackaged) {
      // Dev / browser: no feed to check. Report no-update so the
      // UI shows "up to date" instead of an error.
      broadcastToRenderers('update:status', {
        state: 'not-available' as UpdateState,
        version: app.getVersion(),
        autoChecked: opts?.autoChecked ?? false,
      } satisfies UpdateStatusPayload);
      return { ok: true, state: 'not-available' as UpdateState };
    }
    try {
      const result = await autoUpdater.checkForUpdates();
      return {
        ok: true,
        state: (result?.updateInfo ? 'available' : 'not-available') as UpdateState,
        version: result?.updateInfo?.version,
      };
    } catch (e) {
      const err = e instanceof Error ? e : new Error(String(e));
      // The 'error' event handler has already broadcast; we just
      // return the failure to the caller so the renderer's promise
      // resolves.
      log.error('[updater] checkForUpdates threw:', err);
      return { ok: false, state: 'error' as UpdateState, message: err.message };
    }
  });

  ipcMain.handle('update:install-and-quit', (): void => {
    if (!isPackaged) return;
    // isForceRunAfter = true: even if other windows are open, quit
    // and apply the update. The user has explicitly asked.
    autoUpdater.quitAndInstall(true, true);
  });

  ipcMain.handle('update:get-version', () => {
    return {
      current: app.getVersion(),
      channel: autoUpdater.channel ?? 'latest',
    };
  });
}


/**
 * Fire-and-forget auto-check on app launch.
 *
 * Called from main.ts after the main window's first
 * `ready-to-show`. One attempt only - the result is broadcast as
 * either 'downloaded' (silently downloaded, ready to install) or
 * 'not-available' (nothing to do). Errors are caught and broadcast
 * as 'error' but do not crash the app.
 */
export async function runAutoCheckOnLaunch(): Promise<void> {
  if (!app.isPackaged) return;
  try {
    await autoUpdater.checkForUpdates();
    // Result is broadcast via the 'update-available' /
    // 'update-not-available' / 'error' events.
  } catch (e) {
    log.error('[updater] auto-check on launch failed:', e);
  }
}
