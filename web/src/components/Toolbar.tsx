import { useAppStore } from '../store/useAppStore';


/**
 * Toolbar — Run / Reset / Save / Show solution buttons + n/seed inputs.
 *
 * NOTE: kept for reference; superseded by AppShell's TransportBar.
 * The new pane system (see web/src/components/AppShell.tsx) hosts
 * the same controls in its TransportBar. Kept here only because
 * deleting legacy source files is a guarded action in this
 * sandbox; this file is no longer imported anywhere.
 */
export function Toolbar() {
  const detail = useAppStore((s) => s.currentDetail);
  const isRunning = useAppStore((s) => s.isRunning);
  const run = useAppStore((s) => s.run);
  const reset = useAppStore((s) => s.reset);
  const saveSolution = useAppStore((s) => s.saveSolution);
  const setSource = useAppStore((s) => s.setSource);

  const n = useAppStore((s) => s.n);
  const setN = useAppStore((s) => s.setN);
  const seed = useAppStore((s) => s.seed);
  const setSeed = useAppStore((s) => s.setSeed);

  if (!detail) return null;

  async function handlePopOut() {
    const api = window.electronAPI;
    if (api?.popOutEditor) {
      await api.popOutEditor();
    } else {
      // Dev / browser fallback: open the same URL in a new tab.
      // The URL is just a hint; the browser will reuse the same
      // process. Mostly useful for quick testing.
      window.open(window.location.pathname + '?view=editor', '_blank');
    }
  }

  return (
    <div className="flex items-center gap-2 flex-wrap">
      <button
        type="button"
        onClick={run}
        disabled={isRunning}
        className="px-3 py-1.5 text-sm font-medium rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {isRunning ? 'Running…' : '▶ Run'}
      </button>
      <button
        type="button"
        onClick={reset}
        disabled={isRunning}
        className="px-3 py-1.5 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50"
      >
        Reset
      </button>
      <button
        type="button"
        onClick={saveSolution}
        className="px-3 py-1.5 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border"
        title="Save (Ctrl/Cmd+S)"
      >
        💾 Save
      </button>
      <button
        type="button"
        onClick={() => setSource(detail.optimal_source)}
        className="px-3 py-1.5 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border"
        title="Copy the canonical optimal solution into the editor"
      >
        Show solution
      </button>
      <button
        type="button"
        onClick={handlePopOut}
        className="px-3 py-1.5 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border"
        title="Open the editor in a separate window you can drag to a second monitor"
      >
        ⧉ Pop out
      </button>

      <div className="flex items-center gap-1 ml-auto text-xs">
        <label className="text-coden-muted">n</label>
        <input
          type="number"
          min={2}
          max={detail.max_n}
          value={n}
          onChange={(e) => setN(Math.max(2, Math.min(detail.max_n, Number(e.target.value) || 16)))}
          className="w-16 bg-coden-bg border border-coden-border rounded px-2 py-1 font-mono text-coden-text"
        />
        <label className="text-coden-muted ml-2">seed</label>
        <input
          type="number"
          value={seed ?? ''}
          onChange={(e) => setSeed(e.target.value === '' ? null : Number(e.target.value))}
          className="w-20 bg-coden-bg border border-coden-border rounded px-2 py-1 font-mono text-coden-text"
        />
      </div>
    </div>
  );
}
