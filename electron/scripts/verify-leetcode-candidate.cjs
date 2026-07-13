const { app, safeStorage } = require('electron');
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

const projectRoot = path.resolve(__dirname, '..', '..');
const challengeIds = process.argv.slice(2);
const codenHome = path.resolve(process.env.CODEN_HOME || path.join(projectRoot, '.coden-data'));
// Match the development app's Chromium profile because safeStorage's key is
// held there, while cOde(n) deliberately stores the encrypted credential blob
// in the separate repository-local CODEN_HOME.
app.setPath('userData', path.join(app.getPath('appData'), 'coden-electron'));

async function main() {
  if (!challengeIds.length || challengeIds.some((value) => !/^lc_\d+$/.test(value))) {
    throw new Error('Pass one or more canonical challenge ids, for example lc_44 lc_45.');
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

  const python = path.join(projectRoot, '.venv', 'Scripts', 'python.exe');
  const verifier = path.join(projectRoot, 'tools', 'verify_leetcode_submission.py');
  for (const [index, challengeId] of challengeIds.entries()) {
    if (index > 0) await new Promise((resolve) => setTimeout(resolve, 10_000));
    const child = spawnSync(python, [verifier, challengeId, '--confirm-submit'], {
      cwd: projectRoot,
      env: {
        ...process.env,
        LEETCODE_SESSION: credentials.session,
        LEETCODE_CSRFTOKEN: credentials.csrfToken,
        LEETCODE_CFCLEARANCE: credentials.cloudflareClearance || '',
      },
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true,
    });

    if (child.stdout) process.stdout.write(child.stdout);
    if (child.stderr) process.stderr.write(child.stderr);
    if (child.error) throw child.error;
    if (child.status === 0) {
      spawnSync(python, ['tools/audit_leetcode_migration.py', '--clear-block', challengeId.slice(3)], {
        cwd: projectRoot,
        stdio: 'ignore',
        windowsHide: true,
      });
    } else {
      process.exitCode = child.status ?? 1;
    }
  }
}

app.whenReady().then(async () => {
  try {
    await main();
    app.exit(process.exitCode || 0);
  } catch (error) {
    console.error(`Verification bridge failed: ${error instanceof Error ? error.message : String(error)}`);
    app.exit(1);
  }
});
