/**
 * Electron main process for the cOde(n) desktop wrapper.
 *
 * Flow:
 *   1. Spawn uvicorn as a child process (server-process.ts).
 *   2. Wait for the FastAPI server to write its port file.
 *   3. On startup, ensure the per-user engine workspace is in
 *      place under `app.getPath('userData')` by copying the bundled
 *      `tools/`, `server/`, `code_n/`, and `challenges/` sources.
 *      The in-app debugger imports these files when launching
 *      debugpy against the player's solution.
 *   4. Open a BrowserWindow at the server's URL.
 *   5. On quit, kill the uvicorn process so it doesn't outlive
 *      the app.
 */

import { app, BrowserWindow, dialog, shell } from 'electron';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { startServer, ServerHandle } from './server-process';
import { initAutoUpdater, runAutoCheckOnLaunch } from './updater';


let mainWindow: BrowserWindow | null = null;
let server: ServerHandle | null = null;


function isInternalAppUrl(rawUrl: string, appOrigin: string): boolean {
  try {
    const url = new URL(rawUrl);
    return url.origin === appOrigin;
  } catch {
    return false;
  }
}


function openExternalUrl(rawUrl: string): void {
  try {
    const url = new URL(rawUrl);
    if (!['http:', 'https:', 'mailto:'].includes(url.protocol)) {
      console.warn(`[coden-electron] blocked external navigation to unsupported URL: ${rawUrl}`);
      return;
    }
    void shell.openExternal(rawUrl);
  } catch {
    console.warn(`[coden-electron] blocked malformed external URL: ${rawUrl}`);
  }
}


// --- Diagnostic log file -------------------------------------------
// We write every console.log/warn/error to a small log file
// in the user's userData dir so the user can see the main
// process's output without having to run the app from a
// terminal. The file is overwritten on each launch; size
// is bounded by the number of clicks.
//
// The packaged app is a GUI subsystem binary on Windows, so its
// stdout isn't easily visible to the user. The log file is.
const LOG_FILENAME = 'coden.log';
let logFilePath: string | null = null;

function writeLog(level: string, args: unknown[]): void {
  if (!logFilePath) return;
  try {
    const ts = new Date().toISOString();
    const line = `[${ts}] [${level}] ${args
      .map((a) => (typeof a === 'string' ? a : JSON.stringify(a)))
      .join(' ')}\n`;
    fs.appendFileSync(logFilePath, line, 'utf-8');
  } catch {
    // best-effort
  }
}


/**
 * Workspace files copied into the per-user dir on first launch.
 * Order matters only for the log output â€” they're all
 * independent at copy time. The source must live in
 * `process.resourcesPath/bundled-workspace/<name>/` in packaged
 * mode (it's there because `electron-builder.json` declares
 * it as an extraResource); in dev, the staging step in
 * `build_app.py` puts the same files at
 * `<repo>/bundled-workspace/<name>/` and we read them from
 * there instead.
 */
const WORKSPACE_DIRS = ['tools', 'server', 'code_n', 'challenges'] as const;


/** Heuristic: does this folder look like a cOde(n) source repo?
 *  Used by the dev fallback to know whether to bother copying
 *  workspace files from a source-tree staging area. In
 *  packaged mode, we copy from the bundled resource, not from
 *  the dev tree, so this is a dev-only check. */
function resolveDevRepoRoot(): string {
  // In dev, this file is at electron/dist/electron/src/main.js; the repo root
  // is four parents up. In the packaged app this returns the
  // install dir, which is NOT where the user's source lives â€”
  // we never use it for workspace files in packaged mode.
  return path.resolve(__dirname, '..', '..', '..', '..');
}


/**
 * Where to find the bundled workspace tree. In packaged mode,
 * the resource is at `process.resourcesPath/bundled-workspace/`.
 * In dev, the `build_app.py` step stages the same files at
 * `<repo>/bundled-workspace/`. We prefer the bundled resource;
 * if it doesn't exist (e.g. someone running `npm start` in
 * electron/ without first running `build_app.py`), we fall back
 * to the dev staging dir.
 */
function resolveBundledWorkspaceRoot(): string | null {
  const packaged = path.join(process.resourcesPath ?? '', 'bundled-workspace');
  if (fs.existsSync(packaged)) return packaged;
  const dev = path.join(resolveDevRepoRoot(), 'bundled-workspace');
  if (fs.existsSync(dev)) return dev;
  return null;
}


/** Recursively copy a directory. Uses `fs.cpSync` (Node 16+)
 *  with `dereference: true` so any symlinks in the source
 *  resolve to the target file (we don't want to copy a
 *  symlink-as-symlink because the debug runner imports real
 *  source files from this workspace). */
function copyDirSync(src: string, dst: string): void {
  fs.cpSync(src, dst, { recursive: true, dereference: true });
}


/**
 * Copy the bundled workspace files (``tools``, ``server``,
 * ``code_n``, ``challenges``) into the user's
 * per-user appData dir if they're missing. Idempotent â€”
 * each dir is copied only if it doesn't already exist in
 * the destination, so subsequent launches are a no-op
 * (just one ``existsSync`` per dir). Player data
 * (``solutions/``, ``progress.json``) is never touched.
 */
function ensureWorkspaceFiles(codenHome: string): void {
  const bundled = resolveBundledWorkspaceRoot();
  if (!bundled) {
    // Dev mode without a staging step (e.g. someone running
    // `npm start` in electron/ without first running
    // `build_app.py`). Log and bail; the user can still edit
    // debugger still needs the engine source modules.
    console.warn(
      '[coden-electron] no bundled-workspace found; skipping ' +
      'workspace setup. Run `python build_app.py` to stage it.',
    );
    return;
  }
  for (const name of WORKSPACE_DIRS) {
    const dst = path.join(codenHome, name);
    if (fs.existsSync(dst)) {
      // Already there (from a previous launch). Never overwrite
      // because the user might have edited these files. To force
      // a refresh, the user can delete the dir and relaunch.
      continue;
    }
    const src = path.join(bundled, name);
    if (!fs.existsSync(src)) {
      console.warn(
        `[coden-electron] bundled workspace dir missing: ${src}`,
      );
      continue;
    }
    try {
      copyDirSync(src, dst);
      console.log(`[coden-electron] staged ${name}/ -> ${dst}`);
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      console.error(
        `[coden-electron] failed to stage ${name}/: ${message}`,
      );
    }
  }
}


async function createWindow(): Promise<void> {
  // The dev repo root is the source tree (for the FastAPI server
  // to find solutions/, progress.json, and engine modules). In the
  // packaged app the server reads everything from the bundled
  // resources, so the dev heuristic isn't useful here â€” but we
  // still log it for diagnostic purposes.
  const repoRoot = resolveDevRepoRoot();
  // In production, progress.json + solutions/ live in the user's
  // app data dir (writable on Windows, where Program Files is not).
  // In dev, they live in the repo root.
  const codenHome = app.isPackaged
    ? app.getPath('userData')
    : repoRoot;
  // Use ``app.getVersion()`` instead of requiring package.json
  // directly: from the tsconfig's ``rootDir: ".."`` output path
  // (``dist/electron/src/main.js``), a relative require would
  // resolve to a non-existent ``dist/electron/package.json`` and
  // throw on startup. ``app.getVersion()`` reads from the
  // app's own package.json (the asar root), which is always
  // present.
  const electronPkgVersion = app.getVersion();
  // Set up the diagnostic log file as early as possible so
  // even crashes during startup are captured.
  logFilePath = path.join(codenHome, LOG_FILENAME);
  try {
    fs.writeFileSync(
      logFilePath,
      `=== cOde(n) v${electronPkgVersion} starting at ${new Date().toISOString()} ===\n` +
        `CODEN_HOME: ${codenHome}\n` +
        `install dir: ${path.dirname(app.getPath('exe'))}\n` +
        `process.resourcesPath: ${process.resourcesPath}\n` +
        `app.isPackaged: ${app.isPackaged}\n` +
        `\n`,
      'utf-8',
    );
  } catch {
    // best-effort
  }
  // Mirror the console.* calls to the log file.
  const origLog = console.log.bind(console);
  const origWarn = console.warn.bind(console);
  const origError = console.error.bind(console);
  console.log = (...args: unknown[]) => { writeLog('INFO', args); origLog(...args); };
  console.warn = (...args: unknown[]) => { writeLog('WARN', args); origWarn(...args); };
  console.error = (...args: unknown[]) => { writeLog('ERROR', args); origError(...args); };

  console.log(`[coden-electron] === cOde(n) v${electronPkgVersion} starting ===`);
  console.log(`[coden-electron] dev repo root: ${repoRoot}`);
  console.log(`[coden-electron] CODEN_HOME: ${codenHome} (packaged=${app.isPackaged})`);
  console.log(`[coden-electron] process.resourcesPath: ${process.resourcesPath}`);
  console.log(`[coden-electron] install dir (executable): ${path.dirname(app.getPath('exe'))}`);
  console.log(`[coden-electron] log file: ${logFilePath}`);

  // Stage the per-user engine/debug workspace files into codenHome
  // if they're missing. Idempotent: no-op on subsequent launches.
  // We do this before starting the server so the debugger can import
  // the engine modules immediately.
  ensureWorkspaceFiles(codenHome);

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

  const appOrigin = new URL(mainUrl).origin;
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    if (!isInternalAppUrl(url, appOrigin)) {
      openExternalUrl(url);
      return { action: 'deny' };
    }
    return { action: 'allow' };
  });
  mainWindow.webContents.on('will-navigate', (event, url) => {
    if (!isInternalAppUrl(url, appOrigin)) {
      event.preventDefault();
      openExternalUrl(url);
    }
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
