/**
 * api/vscode.ts — the cOde(n) → VSCode IPC bridge.
 *
 * The Electron main process exposes a ``writeActiveChallenge``
 * handler that writes the current challenge id to
 * ``solutions/.vscode-active`` (a tiny JSON file). The
 * ``tools/run_solution.py`` script reads that file when
 * no id is passed on the command line, so the next time
 * the user presses F5 in VSCode, the launch config defaults
 * to the challenge that cOde(n) is currently showing.
 *
 * The shape is intentionally minimal — just the id. n and
 * seed are still prompted for in the launch config (they
 * depend on the user's intent for this particular run).
 */
import { apiPost } from './client';


/**
 * Write the active challenge id to the handoff file.
 * Returns ``true`` if the file was written, ``false`` if
 * the server's PUT returned an error. Throws on network
 * failure (the caller should catch).
 */
export function writeActiveChallenge(challengeId: string): Promise<boolean> {
  return apiPost<{ ok: boolean }>('/vscode/active', { challenge_id: challengeId })
    .then((r) => r.ok)
    .catch(() => false);
}
