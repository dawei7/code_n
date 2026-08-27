const { app, safeStorage } = require('electron');
const fs = require('node:fs');
const path = require('node:path');

const projectRoot = path.resolve(__dirname, '..');
const codenHome = path.resolve(process.env.CODEN_HOME || path.join(projectRoot, '.coden-data'));

app.setPath('userData', path.join(app.getPath('appData'), 'coden-electron'));

app.whenReady().then(() => {
  if (!safeStorage.isEncryptionAvailable()) {
    console.error('Electron secure-storage decryption is unavailable.');
    app.exit(1);
    return;
  }

  const credentialPath = path.join(codenHome, 'leetcode-session.bin');
  if (!fs.existsSync(credentialPath)) {
    console.error('No leetcode-session.bin found at', credentialPath);
    app.exit(1);
    return;
  }

  const encrypted = fs.readFileSync(credentialPath);
  const credentials = JSON.parse(safeStorage.decryptString(encrypted));
  console.log('Decrypted credentials successfully!');
  console.log('Session length:', credentials.session?.length);
  console.log('CSRF length:', credentials.csrfToken?.length);
  console.log('CF Clearance length:', credentials.cloudflareClearance?.length);

  const parts = [
    `LEETCODE_SESSION=${credentials.session}`,
    `csrftoken=${credentials.csrfToken}`,
  ];
  if (credentials.cloudflareClearance) {
    parts.push(`cf_clearance=${credentials.cloudflareClearance}`);
  }

  const cookieFile = path.join(projectRoot, 'dsa', 'leetcode', '_local', '.leetcode_cookie');
  fs.mkdirSync(path.dirname(cookieFile), { recursive: true });
  fs.writeFileSync(cookieFile, parts.join('; ') + '\n', 'utf-8');
  console.log('Written to', cookieFile);
  app.exit(0);
});
