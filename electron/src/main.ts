/**
 * Electron main process for the cOde(n) desktop wrapper.
 *
 * Flow:
 *   1. Spawn uvicorn as a child process (server-process.ts).
 *   2. Wait for the FastAPI server to write its port file.
 *   3. Open a BrowserWindow at the server's URL.
 *   4. The renderer can request "open in VSCode" via IPC,
 *      which calls ``shell.openPath(repoRoot)``. VSCode on
 *      the user's machine handles the rest — opening the
 *      project at the repo root, with the cOde(n)-written
 *      ``solutions/.vscode-active`` file telling the launch
 *      config which challenge to default to.
 *   5. On quit, kill the uvicorn process so it doesn't outlive
 *      the app.
 *
 * The v0.9.0 pivot removed the pop-out-editor, pop-out-debug,
 * and pop-out-pane BrowserWindows (the cOde(n) app is now a
 * single window; editing + debugging happens in VSCode).
 * The detachedWindows map is gone.
 */

import { app, BrowserWindow, dialog, ipcMain, shell } from 'electron';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { startServer, ServerHandle } from './server-process';
import { initAutoUpdater, runAutoCheckOnLaunch } from './updater';


let mainWindow: BrowserWindow | null = null;
let server: ServerHandle | null = null;


/**
 * Path to the JSON file that stores the user's cOde(n) source
 * repo location. Lives in `app.getPath('userData')` (writable on
 * Windows) so it persists across upgrades.
 *
 * Why we need this: in dev, the repo is the parent of electron/,
 * so we can resolve it from __dirname. In the packaged app, the
 * EXE is installed in AppData/Local/Programs/coden-electron/ —
 * not where the user actually has the source code (where their
 * `solutions/<id>.py` files live). The user picks the source
 * folder once on first launch, we save it here, and every
 * subsequent "Open in VSCode" uses it.
 */
const REPO_PATH_FILE = 'repo-path.json';


interface RepoPathConfig {
  path: string;
}


/** Resolve the repo root by walking up from electron/dist/main.js. */
function resolveDevRepoRoot(): string {
  // In dev, this file is at electron/dist/main.js; the repo root
  // is three parents up. In the packaged app this returns the
  // install dir, which is NOT where the user's source lives —
  // use getUserRepoPath() for that.
  return path.resolve(__dirname, '..', '..', '..');
}


/** Path to the user-chosen repo path JSON (in userData). */
function repoPathFile(): string {
  return path.join(app.getPath('userData'), REPO_PATH_FILE);
}


/** Read the user-chosen repo path from disk. Returns null
 *  if the file doesn't exist, can't be parsed, or points to
 *  a directory that no longer exists. */
function getUserRepoPath(): string | null {
  try {
    const raw = fs.readFileSync(repoPathFile(), 'utf-8');
    const data = JSON.parse(raw) as Partial<RepoPathConfig>;
    if (data && typeof data.path === 'string' && data.path.length > 0) {
      // Verify the path still exists; if not, drop the stale
      // config and let the user re-pick.
      if (fs.existsSync(data.path)) {
        return data.path;
      }
      console.warn(`[coden-electron] stored repo path ${data.path} no longer exists; clearing`);
      try {
        fs.unlinkSync(repoPathFile());
      } catch {
        // best-effort
      }
    }
  } catch {
    // file doesn't exist or isn't valid JSON — fine, first run
  }
  return null;
}


/** Write the user-chosen repo path to disk. */
function setUserRepoPath(repoPath: string): void {
  const data: RepoPathConfig = { path: repoPath };
  fs.writeFileSync(repoPathFile(), JSON.stringify(data, null, 2), 'utf-8');
}


/** Heuristic: does this folder look like a cOde(n) source repo?
 *  We check for the three markers that always exist: .vscode/
 *  (the launch config), solutions/ (the player's saved code),
 *  and tools/run_solution.py (the F5 entry point). */
function looksLikeRepo(repoPath: string): boolean {
  return (
    fs.existsSync(path.join(repoPath, '.vscode')) &&
    fs.existsSync(path.join(repoPath, 'solutions')) &&
    fs.existsSync(path.join(repoPath, 'tools', 'run_solution.py'))
  );
}


/** Show the OS folder picker. Returns the chosen path or null
 *  if the user cancelled. */
async function pickRepoFolder(): Promise<string | null> {
  const result = await dialog.showOpenDialog({
    title: 'Select your cOde(n) source folder',
    message: 'Pick the folder where you cloned the cOde(n) repository ' +
            '(the one with .vscode/, solutions/, and tools/ subfolders). ' +
            'This is where your solutions/<id>.py files live.',
    properties: ['openDirectory'],
  });
  if (result.canceled || result.filePaths.length === 0) return null;
  return result.filePaths[0];
}


/** The "Open in VSCode" target. Falls back through three tiers:
 *  1. The user-chosen path (stored in userData on first run).
 *  2. The dev heuristic (resolveDevRepoRoot) — only correct in
 *     a dev launch, but harmless to try.
 *  3. Prompt the user to pick a folder, then save it.
 *
 *  Returns the resolved path, or null if the user cancelled
 *  the picker. The renderer can show a "please pick your repo"
 *  prompt if it gets null. */
async function resolveOpenRepoPath(): Promise<string | null> {
  const stored = getUserRepoPath();
  if (stored && looksLikeRepo(stored)) return stored;
  const dev = resolveDevRepoRoot();
  if (looksLikeRepo(dev)) return dev;
  const picked = await pickRepoFolder();
  if (!picked) return null;
  if (!looksLikeRepo(picked)) {
    // Picked the wrong folder. Clear the stored path (if any
    // — none here, but be defensive) and bail.
    return null;
  }
  setUserRepoPath(picked);
  return picked;
}


async function createWindow(): Promise<void> {
  // The dev repo root is the source tree (for the FastAPI server
  // to find solutions/, progress.json, .vscode/, etc.). In the
  // packaged app the server reads everything from the bundled
  // resources, so the dev heuristic isn't useful here — but we
  // still log it for diagnostic purposes.
  const repoRoot = resolveDevRepoRoot();
  // In production, progress.json + solutions/ live in the user's
  // app data dir (writable on Windows, where Program Files is not).
  // In dev, they live in the repo root.
  const codenHome = app.isPackaged
    ? app.getPath('userData')
    : repoRoot;
  console.log(`[coden-electron] dev repo root: ${repoRoot}`);
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

  // Open the project in VSCode. Called by the renderer's
  // "Open in VSCode" button (in the transport bar + the VSCode
  // tab). Routes through ``shell.openPath`` — on Windows, that
  // invokes the OS file-association handler; VSCode (when
  // installed) registers itself for the project's folder, so
  // it opens at the repo root with the .vscode/ launch config
  // active. The renderer should have written
  // solutions/.vscode-active FIRST so the F5 launch config
  // defaults to the right challenge.
  //
  // The path comes from ``resolveOpenRepoPath`` which uses the
  // user-stored repo path (saved on first launch), falling
  // back to a folder picker if nothing's stored yet. The result
  // is the absolute path to the user's cOde(n) source repo —
  // NOT the install dir. This is what powers the
  // "Open solutions/<id>.py" use case.
  ipcMain.handle('open-in-vscode', async () => {
    const target = await resolveOpenRepoPath();
    if (!target) return false;
    try {
      const errMsg = await shell.openPath(target);
      if (errMsg) {
        console.warn(`[coden-electron] shell.openPath(${target}): ${errMsg}`);
        return false;
      }
      return true;
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      console.error(`[coden-electron] openInVSCode failed: ${message}`);
      return false;
    }
  });

  // Read the stored repo path (returns null if none / stale).
  // The renderer calls this on mount to decide whether to show
  // a "set your repo path" prompt.
  ipcMain.handle('get-repo-path', () => getUserRepoPath());

  // Manually change the repo path. Pops the OS folder picker,
  // validates the chosen folder, and saves it. Returns the new
  // path on success or null on cancel/invalid. Used by the
  // renderer's "Change" button in the VSCode tab.
  ipcMain.handle('set-repo-path', async () => {
    const picked = await pickRepoFolder();
    if (!picked) return null;
    if (!looksLikeRepo(picked)) return null;
    setUserRepoPath(picked);
    return picked;
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
