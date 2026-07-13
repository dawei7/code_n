/**
 * Electron main process for the cOde(n) desktop wrapper.
 *
 * Flow:
 *   1. Spawn uvicorn as a child process (server-process.ts).
 *   2. Wait for the FastAPI server to write its port file.
 *   3. Open a BrowserWindow at the server's URL.
 *   4. On quit, kill the uvicorn process so it doesn't outlive
 *      the app.
 */

import { execFile } from 'node:child_process';
import { randomBytes } from 'node:crypto';
import { app, BrowserWindow, dialog, shell } from 'electron';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { startServer, ServerHandle } from './server-process';
import { initAutoUpdater, runAutoCheckOnLaunch } from './updater';
import { initLeetCodeIntegration } from './leetcode';


let mainWindow: BrowserWindow | null = null;
let server: ServerHandle | null = null;
const desktopBridgeToken = randomBytes(32).toString('hex');


function waitForProcessExit(child: ServerHandle['process'], timeoutMs: number): Promise<boolean> {
  if (child.exitCode !== null || child.signalCode !== null) return Promise.resolve(true);
  return new Promise((resolve) => {
    const timer = setTimeout(() => {
      child.off('exit', onExit);
      resolve(false);
    }, timeoutMs);
    const onExit = () => {
      clearTimeout(timer);
      resolve(true);
    };
    child.once('exit', onExit);
  });
}


function taskkillProcessTree(pid: number): Promise<void> {
  return new Promise((resolve) => {
    execFile(
      'taskkill',
      ['/PID', String(pid), '/T', '/F'],
      { windowsHide: true },
      (error) => {
        if (error) {
          console.warn(`[coden-electron] taskkill failed for server pid ${pid}: ${error.message}`);
        }
        resolve();
      },
    );
  });
}


async function stopServer(reason: string): Promise<void> {
  const handle = server;
  if (!handle) return;
  server = null;

  const child = handle.process;
  const pid = child.pid;
  console.log(`[coden-electron] stopping server for ${reason} (pid=${pid ?? 'unknown'})`);

  if (child.exitCode !== null || child.signalCode !== null) return;

  try {
    child.kill();
  } catch (e) {
    console.warn(`[coden-electron] failed to signal server shutdown: ${e instanceof Error ? e.message : String(e)}`);
  }

  if (await waitForProcessExit(child, 2_500)) {
    console.log(`[coden-electron] server stopped for ${reason}`);
    return;
  }

  if (process.platform === 'win32' && pid) {
    console.warn(`[coden-electron] server did not stop promptly; killing process tree for ${reason}`);
    await taskkillProcessTree(pid);
    await waitForProcessExit(child, 2_500);
  }
}


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


/** Resolve the source repository root when Electron runs in development. */
function resolveDevRepoRoot(): string {
  return path.resolve(__dirname, '..', '..', '..', '..');
}


async function createWindow(): Promise<void> {
  // The dev repo root is the source tree (for the FastAPI server
  // to find engine modules and canonical challenge data). In the
  // packaged app the server reads everything from the bundled
  // resources, so the dev heuristic isn't useful here â€” but we
  // still log it for diagnostic purposes.
  const repoRoot = resolveDevRepoRoot();
  // Production uses Electron's writable user profile. Development uses an
  // ignored local profile so personal progress and solutions never mix with
  // the source tree or canonical dsa/leetcode packages.
  const codenHome = app.isPackaged
    ? app.getPath('userData')
    : path.join(repoRoot, '.coden-data');
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

  try {
    server = await startServer(repoRoot, codenHome, desktopBridgeToken);
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
  initLeetCodeIntegration({ serverPort: server.port, codenHome, bridgeToken: desktopBridgeToken });

  const devWebUrl = !app.isPackaged ? process.env.CODEN_DEV_WEB_URL?.replace(/\/$/, '') : undefined;
  const mainUrl = devWebUrl ? `${devWebUrl}/` : `http://127.0.0.1:${server.port}/`;
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
  initAutoUpdater({
    beforeInstallAndQuit: () => stopServer('auto-update install'),
  });

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
  void stopServer('window-all-closed');
  app.quit();
});


app.on('before-quit', () => {
  void stopServer('before-quit');
});
