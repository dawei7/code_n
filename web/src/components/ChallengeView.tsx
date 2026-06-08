import { useAppStore } from '../store/useAppStore';
import { StepControls } from './StepControls';
import { StatusBanner } from './StatusBanner';
import { OpLog } from './OpLog';
import { LocalsPanel } from './LocalsPanel';
import { ComplexityAnalysis } from './ComplexityAnalysis';
import { CodePanel } from './CodePanel';


declare global {
  interface Window {
    electronAPI?: {
      popOutEditor(): Promise<boolean>;
    };
  }
}


/**
 * ChallengeView — the main window's analysis surface.
 *
 * Layout (no embedded editor — the editor lives in a pop-out
 * BrowserWindow so it can be moved to a second monitor):
 *
 *   +--- 4 cols ---+--- 5 cols ---+--- 3 cols ---+
 *   | description  | step controls | op log      |
 *   | status       | locals        |  + CSV      |
 *   | complexity   |  inspector    |             |
 *   |  analysis    |               |             |
 *   +--------------+---------------+-------------+
 *
 * The top header has the Run and Open editor buttons (replacing
 * the old embedded Monaco).
 */
export function ChallengeView() {
  const detail = useAppStore((s) => s.currentDetail);
  const isRunning = useAppStore((s) => s.isRunning);
  const runResult = useAppStore((s) => s.runResult);
  const run = useAppStore((s) => s.run);

  if (!detail) {
    return (
      <div className="h-full flex items-center justify-center text-coden-muted">
        <div className="text-center">
          <div className="text-4xl mb-2">⚙️</div>
          <div className="text-lg">Pick a challenge from the left rail.</div>
        </div>
      </div>
    );
  }

  async function handleOpenEditor() {
    const api = window.electronAPI;
    if (api?.popOutEditor) {
      await api.popOutEditor();
    } else {
      // Dev / browser fallback.
      window.open(window.location.pathname + '?view=editor', '_blank');
    }
  }

  return (
    <div className="h-full flex flex-col">
      {/* Header strip with the action buttons */}
      <div className="px-4 py-2 border-b border-coden-border bg-coden-surface shrink-0 flex items-center gap-4">
        <div className="flex-1 min-w-0">
          <h2 className="text-lg font-semibold truncate">{detail.name}</h2>
          <div className="text-xs text-coden-muted font-mono truncate">
            {detail.id} · {detail.category} · difficulty {detail.difficulty}/10
          </div>
        </div>
        <button
          type="button"
          onClick={run}
          disabled={isRunning}
          className="px-4 py-1.5 text-sm font-semibold rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isRunning ? 'Running…' : '▶ Run'}
        </button>
        <button
          type="button"
          onClick={handleOpenEditor}
          className="px-3 py-1.5 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border"
          title="Open the code editor in a separate window (drag to a second monitor)"
        >
          ⧉ Open editor
        </button>
        {runResult && (
          <div className="text-xs text-coden-muted font-mono">
            n=<span className="text-coden-text">{runResult.n}</span>
            <span className="mx-2 text-coden-muted">|</span>
            req:{' '}
            <span className="text-coden-text">{detail.required_complexity}</span>
            <span className="mx-2 text-coden-muted">|</span>
            ops:{' '}
            <span className="text-coden-text">{runResult.stats.total.toLocaleString()}</span>
          </div>
        )}
      </div>

      <div className="flex-1 grid grid-cols-12 gap-3 p-3 overflow-hidden">
        {/* Left column: description + status + complexity analysis */}
        <div className="col-span-4 flex flex-col gap-3 overflow-y-auto">
          <div className="bg-coden-surface border border-coden-border rounded p-3 text-sm shrink-0">
            <div className="text-xs uppercase text-coden-muted font-semibold mb-1">
              Description
            </div>
            <div className="whitespace-pre-wrap">{detail.description}</div>
          </div>
          <StatusBanner />
          <div className="flex-1 min-h-0">
            <ComplexityAnalysis />
          </div>
        </div>

        {/* Center column: step controls + locals inspector */}
        <div className="col-span-5 flex flex-col gap-2 overflow-hidden">
          <StepControls />
          <div className="flex-1 bg-coden-surface border border-coden-border rounded p-3 overflow-hidden flex flex-col min-h-0">
            <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0">
              Locals at this step
            </div>
            <LocalsPanel />
          </div>
        </div>

        {/* Right column: op log (top) + code view (bottom) */}
        <div className="col-span-3 flex flex-col gap-3 overflow-hidden">
          <div className="flex-1 min-h-0 bg-coden-surface border border-coden-border rounded p-3 overflow-hidden flex flex-col">
            <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0">
              Stats &amp; ops
            </div>
            <OpLog />
          </div>
          <div className="flex-1 min-h-0 overflow-hidden">
            <CodePanel />
          </div>
        </div>
      </div>
    </div>
  );
}
