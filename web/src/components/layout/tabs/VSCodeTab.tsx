/**
 * VSCodeTab — the "how to use VSCode with cOde(n)" reference.
 *
 * Replaces the in-app editor + in-app debug surface. The
 * player edits and debugs in VSCode; this tab is the
 * "click here for the setup details" surface.
 *
 * The tab shows:
 *   - The path of the current challenge's solution file
 *     (so the user knows which file will open in VSCode).
 *   - A big "Open in VSCode" button (calls the openInVSCode
 *     IPC, which opens the exact solutions/<id>.py file in
 *     the player's VSCode).
 *   - The 3-step "how to debug a challenge" walkthrough.
 *   - The current active-challenge id (so the user can see
 *     what the F5 default will be).
 *
 * v0.9.x: the previous "Your cOde(n) source folder" card +
 * "Change" button were removed. The location of the player's
 * workspace is now a standard per-user path (app.getPath('userData'))
 * set up automatically on first launch — no user picking.
 */
import { useAppStore } from '../../../store/useAppStore';


export function VSCodeTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const open = useAppStore((s) => s.openInVSCode);
  const opening = useAppStore((s) => s.vscodeOpening);
  const lastError = useAppStore((s) => s.vscodeLastError);
  const lastOpenedPath = useAppStore((s) => s.vscodeLastOpenedPath);
  const clearVSCodeError = useAppStore((s) => s.clearVSCodeError);

  async function handleOpenInVSCode() {
    clearVSCodeError();
    await open(detail);
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

      {/* Current file card. Shows the path of the file that
          "Open in VSCode" will open, so the user knows what
          they're about to edit. The path lives in the standard
          per-user appData dir; cOde(n) sets the whole thing up
          automatically on first launch. */}
      <div className="border border-coden-border bg-coden-bg rounded p-3 text-xs space-y-2">
        <div className="text-coden-muted uppercase tracking-wider font-semibold text-[10px] mb-1">
          Current solution file
        </div>
        {detail ? (
          <div className="font-mono text-coden-text break-all">
            solutions/{detail.id}.py
          </div>
        ) : (
          <div className="text-coden-muted italic">
            Pick a challenge to see its file path.
          </div>
        )}
        {lastOpenedPath && (
          <div className="text-[10px] text-coden-muted mt-2 break-all">
            Last opened: <span className="font-mono text-coden-text">{lastOpenedPath}</span>
          </div>
        )}
      </div>

      <button
        type="button"
        onClick={() => void handleOpenInVSCode()}
        disabled={opening || !detail}
        className="w-full px-4 py-3 text-sm font-semibold rounded border border-coden-accent bg-coden-accent/10 text-coden-accent hover:bg-coden-accent hover:text-coden-bg disabled:opacity-50 disabled:cursor-not-allowed"
        title={detail
          ? `Open solutions/${detail.id}.py in VSCode`
          : 'Pick a challenge first'}
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
            above. VSCode opens the current solution file
            (<span className="font-mono text-coden-text">solutions/{detail?.id ?? '<id>'}.py</span>).
          </li>
          <li>
            Edit the file. A starter is already there; replace the{' '}
            <span className="font-mono text-coden-muted"># Write your code here.</span>
            {' '}body with your implementation.
          </li>
          <li>
            Press{' '}
            <span className="font-mono text-coden-text">F5</span> → pick{' '}
            <span className="font-mono text-coden-text">Run current challenge (debug)</span>
            {' '}→ enter the challenge id (or leave blank to use the active
            one), n, and seed. The verdict prints in the integrated terminal.
          </li>
          <li>
            Set a breakpoint in your code, then step with F10 (over) / F11 (in)
            / Shift+F11 (out).
          </li>
        </ol>
        <p className="text-[11px] text-coden-muted mt-2">
          F5 in VSCode requires Python on your <span className="font-mono">PATH</span>.
          If you don't have it, just use cOde(n)'s{' '}
          <span className="font-mono text-coden-accent">▶ Run</span> button — it
          works regardless.
        </p>
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
          Where everything lives
        </h3>
        <p className="text-xs text-coden-text mb-2">
          Your workspace is set up automatically in the standard
          per-user appData folder. On Windows that's typically:
        </p>
        <pre className="text-[11px] font-mono text-coden-text bg-coden-bg border border-coden-border rounded p-2 overflow-x-auto whitespace-pre">
{`C:\\Users\\<you>\\AppData\\Roaming\\coden-electron\\
├── solutions/         # your code (the source of truth)
├── .vscode/           # launch.json, tasks.json, settings.json
├── tools/             # tools/run_solution.py (F5 entry point)
├── server/, code_n/, challenges/   # engine source (for F5 to import)
└── progress.json      # your per-challenge best ops`}
        </pre>
        <p className="text-[11px] text-coden-muted mt-2">
          cOde(n) copies the engine files into this folder on first
          launch. The folder is per-user — you don't pick a location
          and you don't have to point VSCode at anything.
        </p>
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
