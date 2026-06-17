/**
 * VSCodeTab — the "how to use VSCode with cOde(n)" reference.
 *
 * Replaces the in-app editor + in-app debug surface. The
 * player edits and debugs in VSCode; this tab is the
 * "click here for the setup details" surface.
 *
 * The tab shows:
 *   - The user's cOde(n) source folder (so they know where
 *     "Open in VSCode" is pointing) + a "Change" button to
 *     repoint at a different repo.
 *   - A big "Open in VSCode" button (calls Electron's
 *     shell.openPath via the openInVSCode IPC, or the
 *     vscode:// URL fallback in dev).
 *   - The 3-step "how to debug a challenge" walkthrough.
 *   - The current active-challenge id (so the user can
 *     see what the F5 default will be).
 */
import { useEffect, useState } from 'react';
import { useAppStore } from '../../../store/useAppStore';
import { writeActiveChallenge } from '../../../api/vscode';


export function VSCodeTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const [opening, setOpening] = useState(false);
  const [lastError, setLastError] = useState<string | null>(null);
  const [repoPath, setRepoPath] = useState<string | null>(null);
  const [changingRepo, setChangingRepo] = useState(false);

  // On mount, fetch the user-chosen repo path. The main
  // process stores this in app.getPath('userData')/repo-path.json
  // after the first "Open in VSCode" click (where the picker
  // is shown if nothing is set yet). null = "not set yet",
  // which the UI surfaces as a prompt to click "Open in VSCode".
  useEffect(() => {
    const api = window.electronAPI;
    if (api?.getRepoPath) {
      void api.getRepoPath().then(setRepoPath);
    }
  }, []);

  async function refreshRepoPath() {
    const api = window.electronAPI;
    if (api?.getRepoPath) {
      const p = await api.getRepoPath();
      setRepoPath(p);
    }
  }

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
          // Two failure modes: (a) VSCode isn't installed,
          // (b) the user cancelled the repo-path picker on
          // first run. Distinguish by re-checking the path.
          const p = await api.getRepoPath?.();
          if (!p) {
            setLastError(
              'No repo path set. Click "Change" to pick the folder where ' +
              'you cloned the cOde(n) repository.',
            );
          } else {
            setLastError('VSCode did not respond. Is it installed and on PATH?');
          }
        } else {
          // Refresh the path — the picker may have just set
          // it for the first time.
          await refreshRepoPath();
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

  async function handleChangeRepo() {
    setChangingRepo(true);
    try {
      const api = window.electronAPI;
      if (api?.setRepoPath) {
        const newPath = await api.setRepoPath();
        if (newPath) {
          setRepoPath(newPath);
        } else {
          setLastError(
            'Picked folder does not look like a cOde(n) source clone ' +
            '(missing .vscode/ or solutions/ or tools/run_solution.py).',
          );
        }
      }
    } finally {
      setChangingRepo(false);
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

      {/* Repo path card. Shows the currently-configured path
          (set on first "Open in VSCode" click) so the user
          can see where the project will open. The "Change"
          button pops a folder picker to repoint at a
          different clone. */}
      <div className="border border-coden-border bg-coden-bg rounded p-3 text-xs space-y-2">
        <div className="flex items-start justify-between gap-2">
          <div className="min-w-0 flex-1">
            <div className="text-coden-muted uppercase tracking-wider font-semibold text-[10px] mb-1">
              Your cOde(n) source folder
            </div>
            {repoPath ? (
              <div className="font-mono text-coden-text break-all">
                {repoPath}
              </div>
            ) : (
              <div className="text-coden-muted italic">
                Not set yet — click "Open in VSCode" below and pick your
                cOde(n) source clone (the one with .vscode/, solutions/,
                and tools/ subfolders).
              </div>
            )}
          </div>
          <button
            type="button"
            onClick={() => void handleChangeRepo()}
            disabled={changingRepo}
            className="px-2 py-1 text-xs rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50 shrink-0"
            title="Pick a different cOde(n) source folder"
          >
            {changingRepo ? '…' : 'Change'}
          </button>
        </div>
      </div>

      <button
        type="button"
        onClick={() => void handleOpenInVSCode()}
        disabled={opening}
        className="w-full px-4 py-3 text-sm font-semibold rounded border border-coden-accent bg-coden-accent/10 text-coden-accent hover:bg-coden-accent hover:text-coden-bg disabled:opacity-50 disabled:cursor-not-allowed"
        title={repoPath
          ? `Open ${repoPath} in VSCode`
          : 'Pick your cOde(n) source folder, then open it in VSCode'}
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
            above. VSCode opens your cOde(n) source folder (set on
            first click).
          </li>
          <li>
            Open{' '}
            <span className="font-mono text-coden-text">
              solutions/{detail?.id ?? '<id>'}.py
            </span>{' '}
            in VSCode. A starter is already there; replace the{' '}
            <span className="font-mono text-coden-muted"># Write your code here.</span>
            {' '}body with your implementation.
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
          <li><span className="text-coden-accent">solutions/&lt;id&gt;.py</span> — the 264 starter templates</li>
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
