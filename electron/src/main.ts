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
import { spawn, spawnSync } from 'node:child_process';
import { startServer, ServerHandle } from './server-process';
import { initAutoUpdater, runAutoCheckOnLaunch } from './updater';


let mainWindow: BrowserWindow | null = null;
let server: ServerHandle | null = null;


// --- Diagnostic log file -------------------------------------------
// We write every console.log/warn/error to a small log file
// in the user's userData dir so the user can see the main
// process's output without having to run the app from a
// terminal. The file is overwritten on each launch; size
// is bounded by the number of clicks.
//
// Why: the v0.9.6 fix added detailed per-click logging
// (``openInVSCode: target=...; code CLI=...``) so we can
// tell which version of the main process is running and
// which strategy was taken. The packaged app is a GUI
// subsystem binary on Windows, so its stdout isn't easily
// visible to the user. The log file is.
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
  // In dev, this file is at electron/dist/electron/src/main.js; the repo root
  // is four parents up. In the packaged app this returns the
  // install dir, which is NOT where the user's source lives —
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
 *  precise error message on failure.
 *
 *  Tries strategies in order:
 *    1. (Windows only) ``shell.openExternal('vscode://file/<path>')``
 *       — uses VSCode's own URL handler, which is registered at
 *       install time on every Windows machine. Atomic, no
 *       process-group bookkeeping, no ``.cmd`` wrapper race.
 *    2. ``code <file> -n`` via the ``code`` CLI (if on PATH
 *       or in the standard install location). The ``-n``
 *       forces a NEW VSCode window so the file isn't added
 *       to a stale window with the wrong workspace. On Windows
 *       we launch through ``cmd.exe /c start ""`` so the
 *       wrapping ``cmd.exe`` returns immediately and the
 *       spawned ``Code.exe`` is properly detached.
 *    3. ``shell.openPath(filePath)`` — uses the OS file
 *       association. Works when the user has associated
 *       ``.py`` with VSCode.
 *
 *  If all strategies fail (VSCode not installed at all), we
 *  return a clear error so the renderer can tell the user. */
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

  // Strategy 1 (Windows only): the ``vscode://file/<path>`` URL.
  // VSCode registers this handler on install regardless of any
  // ``Add to PATH`` choice. Using ``shell.openExternal`` here is
  // atomic and side-steps the Windows ``.cmd`` + detached-spawn
  // race described below (the wrapping ``cmd.exe`` can exit
  // before ``Code.exe`` actually launches, so ``spawn`` reports
  // success while nothing visible happens).
  if (process.platform === 'win32') {
    try {
      const fileUrl = 'antigravity-ide://file/' + pathToVscodeUrl(filePath);
      await shell.openExternal(fileUrl);
      console.log(`[coden-electron] openInVSCode: vscode:// URL OK for ${fileUrl}`);
      return { ok: true, filePath };
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      console.warn(
        `[coden-electron] vscode:// URL failed for ${filePath}: ${message}; ` +
        'falling back to code CLI',
      );
    }
  }

  // Strategy 2: the ``code`` CLI (if installed). The ``-n``
  // flag forces a fresh window so the file isn't added to
  // a stale window with the wrong workspace.
  //
  // On Windows, ``code`` is a ``.cmd`` batch wrapper. Node's
  // ``spawn`` cannot invoke ``.cmd`` files natively (it would
  // fail with ENOENT). We also can't just rely on
  // ``detached: true``: the wrapping ``cmd.exe`` exits as soon
  // as it hands off to ``Code.exe``, and on some Windows builds
  // the new process group is reaped before the GUI process is
  // fully initialised — so the spawn "succeeds" but VSCode
  // never appears. The reliable Windows pattern is to launch
  // through ``cmd.exe /c start ""`` (the Windows builtin that
  // returns immediately after spawning the child). On macOS /
  // Linux a plain detached spawn is fine.
  const codeExe = findCodeCli();
  console.log(
    `[coden-electron] openInVSCode: target=${filePath}; ` +
    `code CLI=${codeExe ?? '(not found)'}`,
  );
  if (codeExe) {
    let spawnError: Error | null = null;
    try {
      let child: ReturnType<typeof spawn>;
      if (process.platform === 'win32') {
        child = spawn(
          'cmd.exe',
          ['/d', '/s', '/c', 'start', '""', `"${codeExe}"`, `"${filePath}"`, '-n'],
          {
            detached: true,
            stdio: 'ignore',
            windowsHide: true,
            // The command line above is already a single properly-
            // quoted Windows command — do NOT let Node re-tokenise
            // it through the shell, or the embedded quotes break.
            shell: false,
          },
        );
      } else {
        child = spawn(codeExe, [filePath, '-n'], {
          detached: true,
          stdio: 'ignore',
          windowsHide: true,
        });
      }
      child.on('error', (err) => {
        spawnError = err;
        console.warn(
          `[coden-electron] code CLI spawn error for ${filePath}: ` +
          `${err.message}; falling back to shell.openPath`,
        );
      });
      child.unref();
      if (!spawnError) {
        console.log(`[coden-electron] openInVSCode: spawned code CLI for ${filePath}`);
        return { ok: true, filePath };
      }
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      console.warn(
        `[coden-electron] code CLI failed for ${filePath}: ${message}; ` +
        'falling back to shell.openPath',
      );
    }
  }

  // Strategy 3: file association. The most common path
  // when the ``code`` CLI isn't installed.
  try {
    const errMsg = await shell.openPath(filePath);
    if (!errMsg) {
      console.log(`[coden-electron] openInVSCode: shell.openPath OK for ${filePath}`);
      return { ok: true, filePath };
    }
    console.warn(
      `[coden-electron] shell.openPath failed for ${filePath}: ${errMsg}; ` +
      'falling back to vscode:// URL',
    );
  } catch (e) {
    const message = e instanceof Error ? e.message : String(e);
    console.warn(
      `[coden-electron] shell.openPath threw for ${filePath}: ${message}; ` +
      'falling back to vscode:// URL',
    );
  }

  // Final fallback: vscode:// URL. Always works if VSCode is
  // installed (the URL handler is registered on install). On
  // Windows this is now strategy 1 and we shouldn't reach here
  // unless both the code CLI and shell.openPath failed; on
  // macOS / Linux it's the catch-all after file association.
  try {
    const fileUrl = 'antigravity-ide://file/' + pathToVscodeUrl(filePath);
    await shell.openExternal(fileUrl);
    console.log(`[coden-electron] openInVSCode: vscode:// URL OK for ${fileUrl}`);
    return { ok: true, filePath };
  } catch (e) {
    const message = e instanceof Error ? e.message : String(e);
    console.error(
      `[coden-electron] openInVSCode: all strategies failed for ${filePath}; ` +
      `last error: ${message}`,
    );
    return {
      ok: false,
      filePath,
      error:
        `Could not open the file in VSCode. ` +
        'Is VSCode installed? (Last error: ' + message + ')',
    };
  }
}


/** Find the ``code`` (or ``code.cmd``) CLI. Checks PATH
 *  first, then the two standard Windows install locations:
 *  per-user (``%LOCALAPPDATA%\Programs\Microsoft VS Code\``)
 *  and per-machine (``C:\Program Files\Microsoft VS Code\``).
 *  Returns the absolute path or null.
 *
 *  Note: on Windows, the CLI is a ``.cmd`` batch wrapper,
 *  not a native binary. We always return the full path
 *  (including the ``.cmd`` extension) so the caller can
 *  spawn it with ``shell: true`` to let the OS resolve
 *  the extension. */
function findCodeCli(): string | null {
  // PATH — prefer ``code.cmd`` (the real Windows entry
  // point) over the bare ``code`` name, which Windows'
  // ``where`` may resolve to the extensionless file.
  const fromPath = findOnPath('antigravity-ide.cmd') ?? findOnPath('antigravity-ide');
  if (fromPath) return fromPath;
  if (process.platform === 'win32') {
    const candidates = [
      // Per-user install (default for the user installer)
      path.join(
        process.env.LOCALAPPDATA ?? '',
        'Programs', 'Antigravity IDE', 'bin', 'antigravity-ide.cmd',
      ),
      // Per-machine install (default for the system MSI)
      path.join(
        process.env.ProgramFiles ?? 'C:\\Program Files',
        'Antigravity IDE', 'bin', 'antigravity-ide.cmd',
      ),
      // Fallback: the VSCode app itself (Code.exe). We
      // accept this last because it's the GUI launcher,
      // not a CLI wrapper; spawning it with a file arg
      // works but loses the ``-n`` flag's "new window"
      // semantic.
      path.join(
        process.env.LOCALAPPDATA ?? '',
        'Programs', 'Antigravity IDE', 'Antigravity IDE.exe',
      ),
      path.join(
        process.env.ProgramFiles ?? 'C:\\Program Files',
        'Antigravity IDE', 'Antigravity IDE.exe',
      ),
    ];
    for (const c of candidates) {
      if (fs.existsSync(c)) return c;
    }
  }
  return null;
}


/** Look up an executable on PATH. Node's ``which`` does
 *  this, but isn't available on Windows by default. We use
 *  ``child_process.spawnSync`` with the platform's shell
 *  command (``where`` on Windows, ``which`` elsewhere). */
function findOnPath(name: string): string | null {
  try {
    const cmd = process.platform === 'win32' ? 'where' : 'which';
    const result = spawnSync(cmd, [name], { encoding: 'utf-8' });
    if (result.status === 0 && result.stdout) {
      const first = result.stdout.split(/\r?\n/)[0]?.trim();
      if (first) return first;
    }
  } catch {
    // PATH lookup failed; not a hard error
  }
  return null;
}


/** Convert an absolute file path to the path portion of a
 *  ``vscode://file/<...>`` URL. Backslashes become forward
 *  slashes; each path segment is ``encodeURIComponent``'d
 *  so Windows drive letters (``C:`` → ``C%3A``) and other
 *  special characters are correctly escaped. The leading
 *  ``/`` (which separates the URL resource from the path)
 *  is added by the caller. */
function pathToVscodeUrl(p: string): string {
  const fwd = p.replace(/\\/g, '/');
  return fwd.split('/').map(encodeURIComponent).join('/');
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
