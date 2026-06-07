/**
 * Electron main process for the cOde(n) desktop wrapper.
 *
 * Dev launcher flow:
 *   1. Spawn uvicorn as a child process (server-process.ts).
 *   2. Wait for the FastAPI server to become healthy on /api/health.
 *   3. Open a BrowserWindow at the FastAPI server's URL.
 *   4. On quit, kill the uvicorn process so it doesn't outlive the app.
 *
 * The FastAPI server mounts `web/dist/` as static files, so the
 * BrowserWindow's URL points at the same uvicorn process that
 * serves the API. In dev, run `npm run build` in web/ first so
 * the static mount has something to serve.
 */

import { app, BrowserWindow, dialog } from 'electron';
import * as path from 'node:path';
import { startServer, ServerHandle } from './server-process';


let mainWindow: BrowserWindow | null = null;
let server: ServerHandle | null = null;


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

  try {
    server = await startServer(repoRoot, codenHome);
  } catch (e) {
    const message = e instanceof Error ? e.message : String(e);
    console.error(`[coden-electron] failed to start server:\n${message}`);
    dialog.showErrorBox(
      'Failed to start cOde(n) server',
      `${message}\n\nMake sure the venv is set up: cd "${repoRoot}" && python -m venv .venv && .venv/Scripts/pip install -r requirements.txt`,
    );
    app.quit();
    return;
  }

  console.log(`[coden-electron] server up at http://127.0.0.1:${server.port} (source=${server.source})`);

  mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    title: 'cOde(n)',
    backgroundColor: '#020617',
    show: false,
    webPreferences: {
      // No preload for MVP; the React app talks to the FastAPI
      // server directly via fetch. Future work: expose a typed
      // IPC bridge for native features (open file dialog, etc.).
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  const url = `http://127.0.0.1:${server.port}/`;
  console.log(`[coden-electron] loading ${url}`);

  mainWindow.once('ready-to-show', () => {
    mainWindow?.show();
  });

  await mainWindow.loadURL(url);

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
  void createWindow();

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
