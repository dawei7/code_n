/**
 * Server process management for the Electron dev launcher.
 *
 * Spawns ``uvicorn`` as a child process, parses the port from
 * stdout, polls ``/api/health`` until the server is ready, and
 * exposes a ``kill()`` method that the main process calls on
 * Electron quit so the uvicorn process doesn't outlive the app.
 *
 * The Electron dev launcher is a stopgap until the full
 * PyInstaller `coden-server.exe` + electron-builder NSIS
 * packaging is implemented (next sprint per the rebuild plan).
 */

import { spawn, ChildProcess } from 'node:child_process';
import * as path from 'node:path';
import * as fs from 'node:fs';


/** How long to wait for uvicorn to log its port line, then for /api/health. */
const PORT_TIMEOUT_MS = 10_000;
const HEALTH_TIMEOUT_MS = 10_000;
const HEALTH_POLL_INTERVAL_MS = 100;

export interface ServerHandle {
  process: ChildProcess;
  port: number;
  kill(): void;
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
 * Spawn uvicorn and wait until the server is ready to accept requests.
 *
 * On any failure, the child process is killed before the error is
 * thrown so the caller doesn't have to clean up.
 */
export async function startServer(repoRoot: string): Promise<ServerHandle> {
  const pythonExe = findPythonExe(repoRoot);

  const child = spawn(
    pythonExe,
    [
      '-m', 'uvicorn',
      'server.app.main:app',
      '--host', '127.0.0.1',
      '--port', '0',  // pick a free port; we read it from stdout
    ],
    {
      cwd: repoRoot,
      env: { ...process.env, CODEN_HOME: repoRoot },
      stdio: ['ignore', 'pipe', 'pipe'],
    },
  );

  // If uvicorn exits before we can parse the port, surface that error.
  // We use a holder object so the closure can mutate the inner value
  // without TypeScript's flow analysis narrowing it to `never`.
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
      // Forward uvicorn's stderr to the parent process so the
      // developer can see it in the Electron terminal.
      process.stderr.write(`[uvicorn] ${chunk.toString()}`);
    });

    const timer = setTimeout(() => {
      child.stdout?.off('data', onData);
      reject(new Error(
        `Timeout (${PORT_TIMEOUT_MS}ms) waiting for uvicorn to print its port. ` +
        `Last stdout: ${buffer.slice(-200)}`,
      ));
    }, PORT_TIMEOUT_MS);

    // Race the timer with the child's exit event.
    const interval = setInterval(() => {
      if (exited) {
        clearTimeout(timer);
        clearInterval(interval);
        reject(new Error(`uvicorn exited with code ${exited.code} before printing a port`));
      }
    }, 100);
  });

  // Now wait for /api/health to return 200.
  const healthUrl = `http://127.0.0.1:${port}/api/health`;
  const deadline = Date.now() + HEALTH_TIMEOUT_MS;
  while (Date.now() < deadline) {
    if (exited) {
      throw new Error(`uvicorn exited with code ${exited.code} before becoming healthy`);
    }
    try {
      const res = await fetch(healthUrl);
      if (res.ok) {
        return {
          process: child,
          port,
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
