/** Fast development launcher for Vite + Electron + the local API server. */

import { spawn, spawnSync } from 'node:child_process';
import net from 'node:net';


const isWindows = process.platform === 'win32';
const npmCommand = isWindows ? 'npm.cmd' : 'npm';
const checkOnly = process.argv.includes('--check');
const children = new Set();
let stopping = false;


function availablePort() {
  return new Promise((resolve, reject) => {
    const server = net.createServer();
    server.unref();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      const port = typeof address === 'object' && address ? address.port : 0;
      server.close((error) => error ? reject(error) : resolve(port));
    });
  });
}


function launch(args, env) {
  const child = spawn(npmCommand, args, {
    cwd: process.cwd(),
    env,
    stdio: 'inherit',
    shell: isWindows,
    windowsHide: true,
  });
  children.add(child);
  child.once('exit', () => children.delete(child));
  return child;
}


function stopTree(child) {
  if (!child?.pid || child.exitCode !== null || child.signalCode !== null) return;
  if (isWindows) {
    spawnSync('taskkill', ['/PID', String(child.pid), '/T', '/F'], {
      stdio: 'ignore',
      windowsHide: true,
    });
  } else {
    child.kill('SIGTERM');
  }
}


function stopAll() {
  if (stopping) return;
  stopping = true;
  for (const child of children) stopTree(child);
}


async function waitForUrl(url, child, timeoutMs = 15_000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    if (child.exitCode !== null || child.signalCode !== null) {
      throw new Error(`Vite exited before ${url} became ready`);
    }
    try {
      const response = await fetch(url);
      if (response.ok) return;
    } catch {
      // Vite is still starting.
    }
    await new Promise((resolve) => setTimeout(resolve, 50));
  }
  throw new Error(`Timed out waiting for Vite at ${url}`);
}


async function main() {
  const [webPort, apiPort] = await Promise.all([availablePort(), availablePort()]);
  const webUrl = `http://127.0.0.1:${webPort}`;
  const env = {
    ...process.env,
    CODEN_DEV_WEB_URL: webUrl,
    CODEN_DEV_API_PORT: String(apiPort),
  };

  const vite = launch(
    ['run', 'dev', '--prefix', 'web', '--', '--host', '127.0.0.1', '--port', String(webPort), '--strictPort'],
    env,
  );
  await waitForUrl(webUrl, vite);
  console.log(`[coden-dev] Vite ready at ${webUrl}; API port reserved at ${apiPort}`);

  if (checkOnly) {
    stopTree(vite);
    return;
  }

  const electron = launch(['run', 'dev', '--prefix', 'electron'], env);
  const exitCode = await new Promise((resolve) => {
    electron.once('exit', (code) => resolve(code ?? 0));
  });
  stopTree(vite);
  process.exitCode = exitCode;
}


process.once('SIGINT', () => {
  stopAll();
  process.exitCode = 130;
});
process.once('SIGTERM', () => {
  stopAll();
  process.exitCode = 143;
});
process.once('exit', stopAll);

main().catch((error) => {
  console.error(`[coden-dev] ${error instanceof Error ? error.message : String(error)}`);
  stopAll();
  process.exitCode = 1;
});
