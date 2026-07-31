const { app, safeStorage } = require('electron');
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

const projectRoot = path.resolve(__dirname, '..', '..');
const rawTargets = process.argv.slice(2);
const codenHome = path.resolve(process.env.CODEN_HOME || path.join(projectRoot, '.coden-data'));
const candidateSource = process.env.CODEN_LEETCODE_CANDIDATE_SOURCE || '';
// Match the development app's Chromium profile because safeStorage's key is
// held there, while cOde(n) deliberately stores the encrypted credential blob
// in the separate repository-local CODEN_HOME.
app.setPath('userData', path.join(app.getPath('appData'), 'coden-electron'));

async function main() {
  if (!rawTargets.length || rawTargets.some((value) => !/^lc_\d+(?::[a-z][a-z0-9_-]*)?$/.test(value))) {
    throw new Error(
      'Pass canonical challenge ids, optionally with a variant, for example lc_44 or lc_1502:simplified.',
    );
  }
  if (candidateSource && rawTargets.length !== 1) {
    throw new Error('A staged replacement source can be verified for only one challenge at a time.');
  }
  const targets = rawTargets.map((value) => {
    const [challengeId, variantId = ''] = value.split(':', 2);
    return { challengeId, variantId };
  });
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
  for (const [index, { challengeId, variantId }] of targets.entries()) {
    if (index > 0) await new Promise((resolve) => setTimeout(resolve, 10_000));
    const verifierArgs = [verifier, challengeId];
    if (variantId) verifierArgs.push('--variant', variantId);
    if (candidateSource) verifierArgs.push('--candidate-source', candidateSource);
    verifierArgs.push('--confirm-submit');
    const child = spawnSync(python, verifierArgs, {
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
    if (child.status === 0 && !variantId && !candidateSource) {
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
