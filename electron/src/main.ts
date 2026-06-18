/**
 * Electron main process for the cOde(n) desktop wrapper.
 *
 * Flow:
 *   1. Spawn uvicorn as a child process (server-process.ts).
 *   2. Wait for the FastAPI server to write its port file.
 *   3. On startup, ensure the per-user VSCode workspace is in
 *      place under `app.getPath('userData')` — copy the bundled
 *      `.vscode/`, `tools/`, `server/`, `code_n/`, `challenges/`
 *      from the packaged resources if they're missing. This
 *      makes the userData dir a self-contained VSCode workspace
 *      so "Open in VSCode" can open a specific file with F5
 *      debugging intact.
 *   4. Open a BrowserWindow at the server's URL.
 *   5. The renderer can request "open in VSCode" via IPC. The
 *      handler takes a challenge id, computes the absolute path
 *      to the player's source file (`<userData>/solutions/<id>.py`),
 *      and calls `shell.openPath(filePath)`. VSCode opens the
 *      file (not a folder). The file is in a folder with
 *      `.vscode/launch.json`, so F5 works.
 *   6. On quit, kill the uvicorn process so it doesn't outlive
 *      the app.
 *
 * The v0.9.0 pivot removed the pop-out-editor, pop-out-debug,
 * and pop-out-pane BrowserWindows (the cOde(n) app is now a
 * single window; editing + debugging happens in VSCode).
 * The detachedWindows map is gone.
 *
 * v0.9.x: the "Open in VSCode" flow no longer asks the user to
 * pick a repo folder on first launch. The location is the
 * standard per-user appData dir (Windows:
 * `C:\Users\<user>\AppData\Roaming\coden-electron\`), the file
 * is the exact `solutions/<id>.py` for the current challenge,
 * and the workspace files (so F5 works) are staged on first
 * launch from the bundled resources.
 */

import { app, BrowserWindow, dialog, ipcMain, shell } from 'electron';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { startServer, ServerHandle } from './server-process';
import { initAutoUpdater, runAutoCheckOnLaunch } from './updater';


let mainWindow: BrowserWindow | null = null;
let server: ServerHandle | null = null;


/**
 * Workspace files copied into the per-user dir on first launch.
 * Order matters only for the log output — they're all
 * independent at copy time. The source must live in
 * `process.resourcesPath/bundled-workspace/<name>/` in packaged
 * mode (it's there because `electron-builder.json` declares
 * it as an extraResource); in dev, the staging step in
 * `build_app.py` puts the same files at
 * `<repo>/bundled-workspace/<name>/` and we read them from
 * there instead.
 */
const WORKSPACE_DIRS = [
  '.vscode',
  'tools',
  'server',
  'code_n',
  'challenges',
] as const;


/** Heuristic: does this folder look like a cOde(n) source repo?
 *  Used by the dev fallback to know whether to bother copying
 *  workspace files from a source-tree staging area. In
 *  packaged mode, we copy from the bundled resource, not from
 *  the dev tree, so this is a dev-only check. */
function resolveDevRepoRoot(): string {
  // In dev, this file is at electron/dist/main.js; the repo root
  // is three parents up. In the packaged app this returns the
  // install dir, which is NOT where the user's source lives —
  // we never use it for workspace files in packaged mode.
  return path.resolve(__dirname, '..', '..', '..');
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
 *  symlink-as-symlink — the user's workspace needs real
 *  files for VSCode to handle them properly). */
function copyDirSync(src: string, dst: string): void {
  fs.cpSync(src, dst, { recursive: true, dereference: true });
}


/**
 * Copy the bundled workspace files (``.vscode``, ``tools``,
 * ``server``, ``code_n``, ``challenges``) into the user's
 * per-user appData dir if they're missing. Idempotent —
 * each dir is copied only if it doesn't already exist in
 * the destination, so subsequent launches are a no-op
 * (just one ``existsSync`` per dir). Player data
 * (``solutions/``, ``progress.json``) is never touched.
 *
 * The .vscode/ dir in particular is hand-tuned for the
 * bundled case — its ``settings.json`` points Python at the
 * system ``python`` on PATH instead of the dev repo's
 * ``.venv/Scripts/python.exe``. So the launch config
 * (``tools/run_solution.py`` under debugpy) works in the
 * packaged app without any venv.
 */
function ensureWorkspaceFiles(codenHome: string): void {
  const bundled = resolveBundledWorkspaceRoot();
  if (!bundled) {
    // Dev mode without a staging step (e.g. someone running
    // `npm start` in electron/ without first running
    // `build_app.py`). Log and bail; the user can still edit
    // files in VSCode, but F5 won't have a launch config to
    // work against.
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
      // — the user might have edited tools/ or added their own
      // .vscode tweaks. To force a refresh, the user can delete
      // the dir and relaunch.
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


/** Sanity-check the challenge id the renderer passed us.
 *  Rejects empty strings, path separators, and ``..`` so a
 *  buggy renderer can't escape the solutions dir. */
function isValidChallengeId(id: unknown): id is string {
  if (typeof id !== 'string' || id.length === 0) return false;
  if (id.length > 128) return false; // challenge ids are short
  if (/[\\/]/.test(id)) return false; // no path separators
  if (id.includes('..')) return false; // no traversal
  return /^[A-Za-z0-9_]+$/.test(id);
}


/** Open the player's ``solutions/<id>.py`` file in VSCode.
 *  Returns a small result object so the renderer can show a
 *  precise error message on failure. */
async function openSolutionFile(
  codenHome: string,
  challengeId: string,
): Promise<{ ok: boolean; filePath?: string; error?: string }> {
  ensureWorkspaceFiles(codenHome);
  const filePath = path.join(codenHome, 'solutions', `${challengeId}.py`);
  if (!fs.existsSync(filePath)) {
    return {
      ok: false,
      filePath,
      error:
        `Solution file not found: ${filePath}. ` +
        'Pick the challenge in cOde(n) first to create its starter, ' +
        'then click "Open in VSCode" again.',
    };
  }
  try {
    const errMsg = await shell.openPath(filePath);
    if (errMsg) {
      // shell.openPath returns a non-empty string on failure
      // (e.g. no app associated with .py). Surface that to the
      // user verbatim.
      return { ok: false, filePath, error: errMsg };
    }
    return { ok: true, filePath };
  } catch (e) {
    const message = e instanceof Error ? e.message : String(e);
    return { ok: false, filePath, error: message };
  }
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

  // Stage the per-user VSCode workspace files (.vscode/, tools/,
  // server/, code_n/, challenges/) into codenHome if they're
  // missing. Idempotent — no-op on subsequent launches. We do
  // this BEFORE starting the server so that if the player
  // clicks "Open in VSCode" right after install, the workspace
  // is already set up.
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

  // Open the player's solutions/<id>.py in VSCode. Called by
  // the renderer's "Open in VSCode" button (in the transport
  // bar + the VSCode tab). Routes through ``shell.openPath``
  // — on Windows, that invokes the OS file-association
  // handler; VSCode (when installed + associated with .py)
  // opens the file in its currently-active window. The
  // renderer's prior call to ``/api/vscode/active`` writes
  // ``solutions/.vscode-active`` so the F5 launch config
  // (in the workspace we just staged) defaults to the right
  // challenge.
  ipcMain.handle('open-in-vscode', async (_evt, payload: unknown) => {
    const challengeId =
      payload && typeof payload === 'object' && 'challengeId' in payload
        ? (payload as { challengeId: unknown }).challengeId
        : undefined;
    if (!isValidChallengeId(challengeId)) {
      return { ok: false, error: 'Invalid challenge id' };
    }
    return openSolutionFile(codenHome, challengeId);
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
