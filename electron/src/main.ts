/**
 * Electron main process for the cOde(n) desktop wrapper.
 *
 * Flow:
 *   1. Spawn uvicorn as a child process (server-process.ts).
 *   2. Wait for the FastAPI server to write its port file.
 *   3. Open a BrowserWindow at the server's URL.
 *   4. The renderer can request a "pop out editor" via IPC, which
 *      creates a second BrowserWindow loading ?view=editor.
 *   5. The renderer can request "pop out a pane" via IPC, which
 *      creates a BrowserWindow loading ?view=pane&paneId=...&tabId=...
 *   6. On quit, kill the uvicorn process so it doesn't outlive
 *      the app.
 */

import { app, BrowserWindow, dialog, ipcMain } from 'electron';
import * as path from 'node:path';
import { startServer, ServerHandle } from './server-process';
import { initAutoUpdater, runAutoCheckOnLaunch } from './updater';


let mainWindow: BrowserWindow | null = null;
let server: ServerHandle | null = null;

/** Track every detached BrowserWindow so we can notify the main
 *  window when one closes (so it can clear the "detached" flag
 *  for that pane). Keyed by paneId for both pop-out-editor and
 *  pop-out-pane. */
const detachedWindows = new Map<string, BrowserWindow>();

/** Fixed key for the popped-out debug window. There's at most one
 *  debug pop-out at a time (it's per-session, and there's only one
 *  active session at a time). */
const DEBUG_POPOUT_KEY = 'debug';


/** Resolve the repo root by walking up from electron/dist/main.js. */
function resolveRepoRoot(): string {
  // In dev, this file is at electron/dist/main.js; the repo root
  // is three parents up.
  return path.resolve(__dirname, '..', '..', '..');
}


async function createWindow(): Promise<void> {
  const repoRoot = resolveRepoRoot();
  // In production, progress.json + solutions/ live in the user's
  // app data dir (writable on Windows, where Program Files is not).
  // In dev, they live in the repo root.
  const codenHome = app.isPackaged
    ? app.getPath('userData')
    : repoRoot;
  console.log(`[coden-electron] repo root: ${repoRoot}`);
  console.log(`[coden-electron] CODEN_HOME: ${codenHome} (packaged=${app.isPackaged})`);
  console.log(`[coden-electron] process.resourcesPath: ${process.resourcesPath}`);

  try {
    server = await startServer(repoRoot, codenHome);
  } catch (e) {
    const message = e instanceof Error ? e.message : String(e);
    console.error(`[coden-electron] failed to start server:\n${message}`);
    const webDist = path.join(process.resourcesPath, 'web-dist');
    const serverExe = path.join(process.resourcesPath, 'coden-server',
      process.platform === 'win32' ? 'coden-server.exe' : 'coden-server');
    const bundledExists = require('fs').existsSync(serverExe);
    const hint = bundledExists
      ? `The bundled server exists at:\n  ${serverExe}\n\n` +
        'Try running it directly from a terminal to see the actual error.'
      : `Bundled server NOT found at:\n  ${serverExe}\n\n` +
        `For dev: cd "${repoRoot}" && python -m venv .venv && .venv/Scripts/pip install -r requirements.txt`;
    void webDist; // keep referenced for diagnostic
    dialog.showErrorBox(
      'Failed to start cOde(n) server',
      `${message}\n\n${hint}`,
    );
    app.quit();
    return;
  }

  console.log(`[coden-electron] server up at http://127.0.0.1:${server.port} (source=${server.source})`);

  // Register the IPC handler that opens a pop-out editor window.
  // The renderer calls window.electronAPI.popOutEditor() (exposed
  // by preload.ts); we open a new BrowserWindow here.
  ipcMain.handle('pop-out-editor', () => {
    const port = server?.port;
    if (!port) return false;
    const win = new BrowserWindow({
      width: 900,
      height: 700,
      minWidth: 500,
      minHeight: 400,
      title: 'cOde(n)',  // same title as the main window by design —
                       // the pop-out IS a peer of the main window
      backgroundColor: '#020617',
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
        contextIsolation: true,
        nodeIntegration: false,
      },
    });
    // Use a stable key for the legacy pop-out so we can also
    // notify the main window if the editor window is closed.
    const key = 'editor';
    detachedWindows.set(key, win);
    win.on('closed', () => {
      detachedWindows.delete(key);
      mainWindow?.webContents.send('pane-window-closed', key);
    });
    const url = `http://127.0.0.1:${port}/?view=editor`;
    void win.loadURL(url);
    return true;
  });

  // Generic "pop out a pane" handler. Opens a new BrowserWindow
  // at ?view=pane&paneId=...&tabId=... that hosts the DetachedPaneHost
  // component. When the window closes, the main window is notified
  // so it can clear the corresponding detached flag.
  ipcMain.handle('pop-out-pane', (_evt, paneId: string, tabId: string) => {
    const port = server?.port;
    if (!port) return false;
    if (!paneId || !tabId) return false;
    // If a window for this pane is already open, focus it instead
    // of opening a duplicate.
    const existing = detachedWindows.get(paneId);
    if (existing && !existing.isDestroyed()) {
      existing.focus();
      return true;
    }
    const win = new BrowserWindow({
      width: 700,
      height: 600,
      minWidth: 400,
      minHeight: 300,
      title: `cOde(n) · ${tabId}`,
      backgroundColor: '#020617',
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
        contextIsolation: true,
        nodeIntegration: false,
      },
    });
    detachedWindows.set(paneId, win);
    win.on('closed', () => {
      detachedWindows.delete(paneId);
      mainWindow?.webContents.send('pane-window-closed', paneId);
    });
    const url =
      `http://127.0.0.1:${port}/?view=pane` +
      `&paneId=${encodeURIComponent(paneId)}` +
      `&tabId=${encodeURIComponent(tabId)}`;
    void win.loadURL(url);
    return true;
  });

  // Pop out the debug window. The main window calls this when
  // a breakpoint is hit during a debug session. There's at most
  // one debug pop-out at a time (per DEBUG_POPOUT_KEY); calling
  // it again focuses the existing window. The sessionId is
  // passed as a URL param so the pop-out window can show it in
  // its header.
  ipcMain.handle('pop-out-debug', (_evt, sessionId: string) => {
    const port = server?.port;
    if (!port) return false;
    const existing = detachedWindows.get(DEBUG_POPOUT_KEY);
    if (existing && !existing.isDestroyed()) {
      existing.focus();
      return true;
    }
    const win = new BrowserWindow({
      width: 900,
      height: 700,
      minWidth: 600,
      minHeight: 400,
      title: 'cOde(n) · Debug',
      backgroundColor: '#020617',
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
        contextIsolation: true,
        nodeIntegration: false,
      },
    });
    detachedWindows.set(DEBUG_POPOUT_KEY, win);
    win.on('closed', () => {
      detachedWindows.delete(DEBUG_POPOUT_KEY);
      // Notify the main window that the debug pop-out is gone
      // (it may have been closed manually, not via the session
      // ending). The main window listens for this so it doesn't
      // try to call close() on a destroyed window.
      mainWindow?.webContents.send('pane-window-closed', DEBUG_POPOUT_KEY);
    });
    const url =
      `http://127.0.0.1:${port}/?view=debug` +
      `&sessionId=${encodeURIComponent(sessionId ?? '')}`;
    void win.loadURL(url);
    return true;
  });

  // Close the popped-out debug window if one is open. Called by
  // the main window when the debug session transitions to
  // 'exited' / 'error' / 'idle'.
  ipcMain.handle('close-debug-popout', () => {
    const win = detachedWindows.get(DEBUG_POPOUT_KEY);
    if (!win || win.isDestroyed()) return false;
    win.close();
    return true;
  });

  const mainUrl = `http://127.0.0.1:${server.port}/`;
  console.log(`[coden-electron] loading ${mainUrl}`);

  mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    title: 'cOde(n)',
    backgroundColor: '#020617',
    show: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  mainWindow.once('ready-to-show', () => {
    mainWindow?.show();
  });

  await mainWindow.loadURL(mainUrl);

  // Open devtools in dev builds (F12 toggles, but the console
  // is useful for the developer too).
  if (process.env.CODEN_DEVTOOLS === '1') {
    mainWindow.webContents.openDevTools({ mode: 'detach' });
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}


app.whenReady().then(() => {
  // Wire the auto-updater event listeners + IPC handlers before
  // createWindow() so the renderer can call 'update:check' as soon
  // as it boots, even before the first auto-check on launch fires.
  initAutoUpdater();

  void createWindow();

  // One auto-check on launch, after the main window is up. In
  // dev (app.isPackaged === false) this is a no-op. The check
  // broadcasts a 'update:status' event to the renderer with the
  // result; no UI prompt unless an update is found + downloaded.
  runAutoCheckOnLaunch();

  app.on('activate', () => {
    // macOS: re-create the window when the dock icon is clicked.
    if (BrowserWindow.getAllWindows().length === 0) {
      void createWindow();
    }
  });
});


app.on('window-all-closed', () => {
  // Quit on all platforms (the macOS convention is to keep the
  // app alive, but the cOde(n) launcher is single-window; quit
  // is the right behavior for a learning app).
  if (server) {
    server.kill();
    server = null;
  }
  app.quit();
});


app.on('before-quit', () => {
  if (server) {
    server.kill();
    server = null;
  }
});
