import { ipcMain, safeStorage } from 'electron';
import * as fs from 'node:fs';
import * as path from 'node:path';

import type {
  LeetCodeCredentialInput,
  LeetCodeSessionStatus,
  LeetCodeSubmissionResult,
} from '../../web/src/types/electron';


const CREDENTIAL_FILENAME = 'leetcode-session.bin';


function normalize(input: LeetCodeCredentialInput): LeetCodeCredentialInput {
  return {
    session: input.session.trim(),
    csrfToken: input.csrfToken.trim(),
    cloudflareClearance: (input.cloudflareClearance || '').trim(),
  };
}


function readCredentials(filePath: string): LeetCodeCredentialInput | null {
  if (!fs.existsSync(filePath) || !safeStorage.isEncryptionAvailable()) return null;
  try {
    return JSON.parse(safeStorage.decryptString(fs.readFileSync(filePath))) as LeetCodeCredentialInput;
  } catch {
    return null;
  }
}


async function callBridge<T>(
  port: number,
  bridgeToken: string,
  route: string,
  credentials: LeetCodeCredentialInput,
): Promise<T> {
  const response = await fetch(`http://127.0.0.1:${port}/api/leetcode${route}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Coden-Desktop-Token': bridgeToken,
    },
    body: JSON.stringify({
      credentials: {
        session: credentials.session,
        csrf_token: credentials.csrfToken,
        cloudflare_clearance: credentials.cloudflareClearance || '',
      },
    }),
  });
  if (!response.ok) {
    let message = `Request failed (${response.status}).`;
    try {
      const payload = await response.json() as { detail?: string };
      if (payload.detail) message = payload.detail;
    } catch {
      // Keep the status-only message.
    }
    throw new Error(message);
  }
  return response.json() as Promise<T>;
}


export function initLeetCodeIntegration(options: {
  serverPort: number;
  codenHome: string;
  bridgeToken: string;
}): void {
  const credentialPath = path.join(options.codenHome, CREDENTIAL_FILENAME);
  const configuredStatus = (): LeetCodeSessionStatus => ({
    configured: Boolean(readCredentials(credentialPath)),
    secureStorageAvailable: safeStorage.isEncryptionAvailable(),
    state: readCredentials(credentialPath) ? 'unchecked' : 'missing',
    message: readCredentials(credentialPath)
      ? 'Session is saved securely; verify it before submitting.'
      : 'No LeetCode session is configured.',
  });

  for (const channel of ['leetcode:credentials-save', 'leetcode:credentials-clear', 'leetcode:session-status', 'leetcode:submit']) {
    ipcMain.removeHandler(channel);
  }

  ipcMain.handle('leetcode:credentials-save', async (_event, raw: LeetCodeCredentialInput): Promise<LeetCodeSessionStatus> => {
    if (!safeStorage.isEncryptionAvailable()) {
      return { configured: false, secureStorageAvailable: false, state: 'unavailable', message: 'OS-backed credential encryption is unavailable.' };
    }
    const credentials = normalize(raw);
    if (!credentials.session || !credentials.csrfToken) {
      throw new Error('LEETCODE_SESSION and csrftoken are required.');
    }
    fs.mkdirSync(options.codenHome, { recursive: true });
    fs.writeFileSync(credentialPath, safeStorage.encryptString(JSON.stringify(credentials)));
    return configuredStatus();
  });

  ipcMain.handle('leetcode:credentials-clear', async (): Promise<LeetCodeSessionStatus> => {
    try { fs.rmSync(credentialPath, { force: true }); } catch { /* best effort */ }
    return configuredStatus();
  });

  ipcMain.handle('leetcode:session-status', async (): Promise<LeetCodeSessionStatus> => {
    const credentials = readCredentials(credentialPath);
    if (!credentials) return configuredStatus();
    try {
      const status = await callBridge<Omit<LeetCodeSessionStatus, 'configured' | 'secureStorageAvailable'>>(
        options.serverPort,
        options.bridgeToken,
        '/internal/session/status',
        credentials,
      );
      return { ...status, configured: true, secureStorageAvailable: true };
    } catch (error) {
      return {
        configured: true,
        secureStorageAvailable: true,
        state: 'unreachable',
        message: error instanceof Error ? error.message : String(error),
      };
    }
  });

  ipcMain.handle('leetcode:submit', async (_event, challengeId: string): Promise<LeetCodeSubmissionResult> => {
    const credentials = readCredentials(credentialPath);
    if (!credentials) throw new Error('Configure and verify your LeetCode session first.');
    return callBridge<LeetCodeSubmissionResult>(
      options.serverPort,
      options.bridgeToken,
      `/internal/submissions/${encodeURIComponent(challengeId)}`,
      credentials,
    );
  });
}
