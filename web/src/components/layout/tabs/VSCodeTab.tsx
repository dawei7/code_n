/**
 * VSCodeTab — the "how to use VSCode with cOde(n)" reference.
 *
 * Replaces the in-app editor + in-app debug surface. The
 * player edits and debugs in VSCode; this tab is the
 * "click here for the setup details" surface.
 *
 * The tab shows:
 *   - A big "Open in VSCode" button (calls Electron's
 *     shell.openPath via the openInVSCode IPC, or the
 *     vscode:// URL fallback in dev).
 *   - The repo root (so the user knows where to look).
 *   - A 3-step "how to debug a challenge" walkthrough.
 *   - The current active-challenge id (so the user can
 *     see what the F5 default will be).
 */
import { useState } from 'react';
import { useAppStore } from '../../../store/useAppStore';
import { writeActiveChallenge } from '../../../api/vscode';


export function VSCodeTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const [opening, setOpening] = useState(false);
  const [lastError, setLastError] = useState<string | null>(null);

  async function handleOpenInVSCode() {
    setOpening(true);
    setLastError(null);
    try {
      // Write the active-challenge handoff file FIRST so when
      // VSCode opens and the user presses F5, the launch
      // config defaults to the right challenge. Even if the
      // IPC fails afterwards, the handoff is in place.
      if (detail) {
        try {
          await writeActiveChallenge(detail.id);
        } catch {
          // ignore — the Open below is the user-visible action
        }
      }
      const api = window.electronAPI;
      if (api?.openInVSCode) {
        const ok = await api.openInVSCode();
        if (!ok) {
          setLastError('VSCode did not respond. Is it installed and on PATH?');
        }
      } else {
        // Dev / browser fallback: open the vscode:// protocol URL.
        // The user must have VSCode installed for this to work;
        // the protocol handler is registered on install.
        const path = window.location.host || '127.0.0.1:5173';
        window.open(`vscode://vscode-oss/${encodeURIComponent(path)}`, '_blank');
      }
    } catch (e) {
      setLastError(e instanceof Error ? e.message : String(e));
    } finally {
      setOpening(false);
    }
  }

  return (
    <div className="h-full overflow-y-auto p-4 space-y-4">
      <header>
        <h2 className="text-base font-semibold text-coden-text">
          Edit &amp; debug in VSCode
        </h2>
        <p className="text-xs text-coden-muted mt-1">
          cOde(n) shows the verdict + complexity analysis. The actual
          editing and debugging happens in VSCode — it has breakpoints,
          locals, watch, and call stack out of the box.
        </p>
      </header>

      <button
        type="button"
        onClick={() => void handleOpenInVSCode()}
        disabled={opening}
        className="w-full px-4 py-3 text-sm font-semibold rounded border border-coden-accent bg-coden-accent/10 text-coden-accent hover:bg-coden-accent hover:text-coden-bg disabled:opacity-50 disabled:cursor-not-allowed"
        title="Open the project in VSCode (or the vscode:// handler if you're in a browser)"
      >
        {opening ? 'Opening…' : '</> Open in VSCode'}
      </button>

      {lastError && (
        <div className="border border-rose-500/40 bg-rose-500/10 rounded p-3 text-xs text-rose-300">
          {lastError}
        </div>
      )}

      <section>
        <h3 className="text-xs uppercase text-coden-muted font-semibold mb-2">
          How to debug a challenge
        </h3>
        <ol className="text-xs text-coden-text space-y-2 list-decimal list-inside">
          <li>
            Click <span className="font-mono text-coden-accent">Open in VSCode</span>{' '}
            above. VSCode opens the project at the repo root.
          </li>
          <li>
            Open{' '}
            <span className="font-mono text-coden-text">
              solutions/{detail?.id ?? '<id>'}.py
            </span>{' '}
            in VSCode.
          </li>
          <li>
            Press{' '}
            <span className="font-mono text-coden-text">F5</span> → pick{' '}
            <span className="font-mono text-coden-text">Run current challenge (debug)</span>
            {' '}→ enter the challenge id (or leave blank to use the active
            one), n, and seed.
          </li>
          <li>
            Set a breakpoint in your code, then step with F10 (over) / F11 (in)
            / Shift+F11 (out). The verdict prints in the integrated terminal.
          </li>
        </ol>
      </section>

      <section>
        <h3 className="text-xs uppercase text-coden-muted font-semibold mb-2">
          The source of truth is on disk
        </h3>
        <p className="text-xs text-coden-text">
          The file{' '}
          <span className="font-mono text-coden-text">
            solutions/{detail?.id ?? '<id>'}.py
          </span>{' '}
          is what cOde(n) runs. When you click <span className="font-mono text-coden-accent">▶ Run</span>
          {' '}in cOde(n), it re-reads the file from disk — so VSCode edits
          are picked up automatically. No "Save" button needed.
        </p>
      </section>

      <section>
        <h3 className="text-xs uppercase text-coden-muted font-semibold mb-2">
          What's in the repo
        </h3>
        <ul className="text-xs text-coden-text space-y-1.5 list-disc list-inside font-mono">
          <li><span className="text-coden-accent">tools/run_solution.py</span> — the F5 entry point</li>
          <li><span className="text-coden-accent">.vscode/launch.json</span> — the debug config</li>
          <li><span className="text-coden-accent">.vscode/tasks.json</span> — non-debug tasks + tests</li>
          <li><span className="text-coden-accent">.vscode/settings.json</span> — Python interpreter + file excludes</li>
          <li><span className="text-coden-accent">.vscode/extensions.json</span> — recommended extensions</li>
          <li><span className="text-coden-accent">solutions/.vscode-active</span> — the active-challenge handoff (gitignored)</li>
        </ul>
      </section>

      <section>
        <h3 className="text-xs uppercase text-coden-muted font-semibold mb-2">
          Why VSCode, not the in-app editor?
        </h3>
        <p className="text-xs text-coden-text">
          cOde(n) is a results panel: it shows the verdict, the AST op
          count, the ±5% tolerance band, and the return value. VSCode is
          a world-class code editor with first-class Python debugging —
          using it for the editing + debugging loop means cOde(n) stays
          small and focused, and you get the same tooling you already
          use for everything else.
        </p>
      </section>
    </div>
  );
}
