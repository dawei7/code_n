const { app, safeStorage } = require('electron');
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

const projectRoot = path.resolve(__dirname, '..', '..');
const codenHome = path.resolve(process.env.CODEN_HOME || path.join(projectRoot, '.coden-data'));
app.setPath('userData', path.join(app.getPath('appData'), 'coden-electron'));

async function main() {
  if (process.argv.length !== 2) {
    throw new Error('This bridge does not accept command-line arguments.');
  }
  if (!safeStorage.isEncryptionAvailable()) {
    throw new Error('Electron secure-storage decryption is unavailable.');
  }

  const credentialPath = path.join(codenHome, 'leetcode-session.bin');
  const encrypted = fs.readFileSync(credentialPath);
  const credentials = JSON.parse(safeStorage.decryptString(encrypted));
  if (!credentials.session || !credentials.csrfToken) {
    throw new Error('The stored LeetCode credentials are incomplete.');
  }

  const child = spawnSync(
    path.join(projectRoot, '.venv', 'Scripts', 'python.exe'),
    [path.join(projectRoot, 'tools', 'update_leetcode_metrics.py'), '--refresh-zerotrac'],
    {
      cwd: projectRoot,
      env: {
        ...process.env,
        LEETCODE_COOKIE: '',
        LEETCODE_SESSION: credentials.session,
        LEETCODE_CSRFTOKEN: credentials.csrfToken,
        LEETCODE_CF_CLEARANCE: credentials.cloudflareClearance || '',
      },
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true,
    },
  );

  if (child.stdout) process.stdout.write(child.stdout);
  if (child.stderr) process.stderr.write(child.stderr);
  if (child.error) throw child.error;
  process.exitCode = child.status ?? 1;
}

app.whenReady().then(async () => {
  try {
    await main();
    app.exit(process.exitCode || 0);
  } catch (error) {
    console.error(
      `Authenticated metrics bridge failed: ${error instanceof Error ? error.message : String(error)}`,
    );
    app.exit(1);
  }
});
