/**
 * Server process management for the Electron desktop wrapper.
 *
 * Two spawn modes:
 *
 *   1. **Bundled** (production) — when electron-builder packages the
 *      PyInstaller output into ``extraResources``, the bundled
 *      ``coden-server.exe`` lives at
 *      ``process.resourcesPath/coden-server/coden-server.exe``. We
 *      spawn it directly. Its stdout uses the same uvicorn logging
 *      format as dev, so the port-parsing + health-polling code
 *      below is identical.
 *
 *   2. **Dev** (no bundled server) — fall back to spawning
 *      ``python -m uvicorn`` from the repo's venv. Used when you
 *      run ``npm start`` in electron/ without first running
 *      ``build_app.py`` (which produces the PyInstaller bundle).
 *
 * The same ``startServer()`` function picks one based on which
 * artifact is present on disk.
 */

import { spawn, ChildProcess } from 'node:child_process';
import * as os from 'node:os';
import * as path from 'node:path';
import * as fs from 'node:fs';


/** How long to wait for the server to log its port, then for /api/health. */
const PORT_TIMEOUT_MS = 60_000;
const HEALTH_TIMEOUT_MS = 20_000;
const HEALTH_POLL_INTERVAL_MS = 100;

export interface ServerHandle {
  process: ChildProcess;
  port: number;
  kill(): void;
  /** Where the server actually lives on disk (for diagnostics). */
  source: 'bundled' | 'dev-venv';
}


function bundledServerPath(): string | null {
  // electron-builder puts extraResources at process.resourcesPath.
  // In dev, process.resourcesPath is the electron/ directory, not
  // the packaging output, so the check naturally fails.
  if (!process.resourcesPath) return null;
  const exeName = process.platform === 'win32' ? 'coden-server.exe' : 'coden-server';
  const candidate = path.join(process.resourcesPath, 'coden-server', exeName);
  return fs.existsSync(candidate) ? candidate : null;
}


function findPythonExe(repoRoot: string): string {
  const candidates = process.platform === 'win32'
    ? [path.join(repoRoot, '.venv', 'Scripts', 'python.exe')]
    : [
        path.join(repoRoot, '.venv', 'bin', 'python'),
        path.join(repoRoot, '.venv', 'bin', 'python3'),
      ];
  for (const candidate of candidates) {
    if (fs.existsSync(candidate)) return candidate;
  }
  throw new Error(
    `Python venv not found. Looked in: ${candidates.join(', ')}. ` +
    `Run: cd "${repoRoot}" && python -m venv .venv && ` +
    `.venv/Scripts/pip install -r requirements.txt`,
  );
}


function findDebugPythonExe(repoRoot: string): string | null {
  try {
    return findPythonExe(repoRoot);
  } catch {
    // Packaged installs may not have the dev venv. Fall through to
    // a system Python; the debug route will report a clear debugpy
    // install error if that interpreter is missing the module.
  }
  const names = process.platform === 'win32' ? ['python.exe', 'python3.exe', 'py.exe'] : ['python3', 'python'];
  for (const name of names) {
    const found = findOnPath(name);
    if (found) return found;
  }
  return null;
}


function findOnPath(name: string): string | null {
  const pathValue = process.env.PATH ?? '';
  const pathExt = process.platform === 'win32'
    ? (process.env.PATHEXT ?? '.EXE;.CMD;.BAT').split(';')
    : [''];
  for (const dir of pathValue.split(path.delimiter)) {
    if (!dir) continue;
    for (const ext of pathExt) {
      const lowerName = name.toLowerCase();
      const lowerExt = ext.toLowerCase();
      const candidateName = lowerExt && lowerName.endsWith(lowerExt) ? name : name + ext;
      const candidate = path.join(dir, candidateName);
      if (fs.existsSync(candidate)) return candidate;
    }
  }
  return null;
}


/**
 * Spawn the FastAPI server (bundled or dev) and wait until it's
 * ready to accept requests. On any failure, the child process is
 * killed before the error is thrown so the caller doesn't have to
 * clean up.
 *
 * @param repoRoot    In dev, used as cwd + CODEN_HOME. In production
 *                    (bundled), ignored — the caller passes a
 *                    writable ``userData`` dir via ``codenHome``.
 * @param codenHome   Directory where ``progress.json`` and
 *                    ``solutions/`` live. Required for the bundled
 *                    case (the exe's install dir is read-only on
 *                    Windows). In dev, defaults to ``repoRoot``.
 */
export async function startServer(
  repoRoot: string,
  codenHome: string = repoRoot,
): Promise<ServerHandle> {
  // The bundled server writes the bound port to a temp file
  // (path from CODEN_PORT_FILE env var). We poll for it; this is
  // more reliable than parsing stdout when the parent is a Windows
  // GUI-subsystem app.
  const portFile = path.join(os.tmpdir(), `coden-server-port-${process.pid}.txt`);

  // --- Choose the spawn target ---
  const bundled = bundledServerPath();
  let child: ChildProcess;
  let source: 'bundled' | 'dev-venv';

  if (bundled) {
    source = 'bundled';
    // In production, the React build lives at extraResources/web-dist.
    // Tell the server where to find it via CODEN_WEB_DIST.
    const webDist = path.join(process.resourcesPath, 'web-dist');
    // Algorithm reference docs live at extraResources/docs; the
    // server reads them via CODEN_DOCS_DIR. (In dev, the server
    // falls back to <repo>/docs automatically.)
    const docsDir = path.join(process.resourcesPath, 'docs');
    const debugPython = findDebugPythonExe(repoRoot);
    child = spawn(bundled, [], {
      env: {
        ...process.env,
        CODEN_HOME: codenHome,
        CODEN_PORT_FILE: portFile,
        CODEN_WEB_DIST: webDist,
        CODEN_DOCS_DIR: docsDir,
        ...(debugPython ? { CODEN_DEBUG_PYTHON: debugPython } : {}),
      },
      stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true,
    });
  } else {
    source = 'dev-venv';
    const pythonExe = findPythonExe(repoRoot);
    child = spawn(
      pythonExe,
      [
        '-m', 'server.run_server',
      ],
      {
        cwd: repoRoot,
        env: {
          ...process.env,
          CODEN_HOME: codenHome,
          CODEN_PORT_FILE: portFile,
          CODEN_DEBUG_PYTHON: pythonExe,
        },
        stdio: ['ignore', 'pipe', 'pipe'],
        windowsHide: true,
      },
    );
  }

  // If the server exits before we can parse the port, surface that
  // error. Holder object so the closure can mutate without
  // TypeScript's flow analysis narrowing it to `never`.
  const exited: { code: number | null | undefined } = { code: undefined };
  child.on('exit', (code) => {
    exited.code = code;
  });

  // Stream stdout (for diagnostics) and poll the port file. The
  // port file is the canonical signal; stdout is best-effort.
  let stdoutBuffer = '';
  let stderrBuffer = '';
  child.stdout?.on('data', (chunk: Buffer) => {
    stdoutBuffer += chunk.toString();
    process.stdout.write(`[server] ${chunk.toString()}`);
  });
  child.stderr?.on('data', (chunk: Buffer) => {
    stderrBuffer += chunk.toString();
    process.stderr.write(`[server] ${chunk.toString()}`);
  });

  // Wait for the port file to appear.
  const port = await new Promise<number>((resolve, reject) => {
    const timer = setTimeout(() => {
      reject(new Error(
        `Timeout (${PORT_TIMEOUT_MS}ms) waiting for server to write ${portFile}. ` +
        `Last stdout: ${stdoutBuffer.slice(-500)}\n` +
        `Last stderr: ${stderrBuffer.slice(-1000)}`,
      ));
    }, PORT_TIMEOUT_MS);

    const poll = setInterval(() => {
      if (exited.code !== undefined) {
        clearTimeout(timer);
        clearInterval(poll);
        reject(new Error(`server exited with code ${exited.code} before writing the port file`));
        return;
      }
      try {
        if (fs.existsSync(portFile)) {
          const content = fs.readFileSync(portFile, 'utf-8').trim();
          const parsed = Number(content);
          if (Number.isFinite(parsed) && parsed > 0) {
            clearTimeout(timer);
            clearInterval(poll);
            resolve(parsed);
          }
        }
      } catch {
        // file may not be fully written yet; retry
      }
    }, HEALTH_POLL_INTERVAL_MS);
  });

  // Clean up the port file once we've consumed it.
  try {
    fs.unlinkSync(portFile);
  } catch {
    // best-effort; the OS will clean up /tmp eventually
  }

  // Now wait for /api/health to return 200.
  const healthUrl = `http://127.0.0.1:${port}/api/health`;
  const deadline = Date.now() + HEALTH_TIMEOUT_MS;
  while (Date.now() < deadline) {
    if (exited.code !== undefined) {
      throw new Error(`server exited with code ${exited.code} before becoming healthy`);
    }
    try {
      const res = await fetch(healthUrl);
      if (res.ok) {
        return {
          process: child,
          port,
          source,
          kill() {
            try {
              child.kill();
            } catch {
              // already dead
            }
          },
        };
      }
    } catch {
      // server not yet listening; retry
    }
    await new Promise((r) => setTimeout(r, HEALTH_POLL_INTERVAL_MS));
  }

  child.kill();
  throw new Error(`Server didn't become healthy within ${HEALTH_TIMEOUT_MS}ms at ${healthUrl}`);
}
