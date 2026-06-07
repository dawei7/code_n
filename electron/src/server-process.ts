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
import * as path from 'node:path';
import * as fs from 'node:fs';


/** How long to wait for the server to log its port line, then for /api/health. */
const PORT_TIMEOUT_MS = 10_000;
const HEALTH_TIMEOUT_MS = 10_000;
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
  // --- Choose the spawn target ---
  const bundled = bundledServerPath();
  let child: ChildProcess;
  let source: 'bundled' | 'dev-venv';

  if (bundled) {
    source = 'bundled';
    child = spawn(bundled, [], {
      env: { ...process.env, CODEN_HOME: codenHome },
      stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true,
    });
  } else {
    source = 'dev-venv';
    const pythonExe = findPythonExe(repoRoot);
    child = spawn(
      pythonExe,
      [
        '-m', 'uvicorn',
        'server.app.main:app',
        '--host', '127.0.0.1',
        '--port', '0',  // pick a free port; we read it from stdout
      ],
      {
        cwd: repoRoot,
        env: { ...process.env, CODEN_HOME: codenHome },
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

  // Stream stdout and wait for the "Uvicorn running on http://127.0.0.1:PORT" line.
  const port = await new Promise<number>((resolve, reject) => {
    let buffer = '';
    const onData = (chunk: Buffer) => {
      buffer += chunk.toString();
      const match = buffer.match(/Uvicorn running on https?:\/\/127\.0\.0\.1:(\d+)/);
      if (match) {
        child.stdout?.off('data', onData);
        resolve(Number(match[1]));
      }
    };
    child.stdout?.on('data', onData);
    child.stderr?.on('data', (chunk) => {
      // Forward stderr to the parent process so the developer
      // can see it in the Electron terminal.
      process.stderr.write(`[server] ${chunk.toString()}`);
    });

    const timer = setTimeout(() => {
      child.stdout?.off('data', onData);
      reject(new Error(
        `Timeout (${PORT_TIMEOUT_MS}ms) waiting for server to print its port. ` +
        `Last stdout: ${buffer.slice(-200)}`,
      ));
    }, PORT_TIMEOUT_MS);

    const interval = setInterval(() => {
      if (exited.code !== undefined) {
        clearTimeout(timer);
        clearInterval(interval);
        reject(new Error(`server exited with code ${exited.code} before printing a port`));
      }
    }, 100);
  });

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
