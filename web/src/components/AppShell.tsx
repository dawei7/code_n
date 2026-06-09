/**
 * AppShell.tsx — top-level layout.
 *
 *   +-------------------------------------------+
 *   | header  logo  ........ Layout: 4 ▾       |
 *   +-------------------------------------------+
 *   | transport  challenge  Run  step ctrls ... |
 *   +-------------------------------------------+
 *   |                                           |
 *   |  LayoutRoot (the pane tree)               |
 *   |                                           |
 *   +-------------------------------------------+
 *   | aside | (main)                            |
 *   +-------------------------------------------+
 *
 * The aside (ChallengeList) stays as a fixed global rail — it's
 * a navigation surface, not analysis content. The pane tree
 * lives in the main area only.
 */
import { useEffect } from 'react';
import { useAppStore } from '../store/useAppStore';
import { useStepPlayer } from '../hooks/useStepPlayer';
import { useKeyboardShortcuts } from '../hooks/useKeyboardShortcuts';
import { ChallengeList } from './ChallengeList';
import { LayoutRoot } from './layout/LayoutRoot';
import { useLayoutStore } from '../store/useLayoutStore';
import { StepControls } from './StepControls';
import { allLeaves } from './layout/tree-ops';


export function AppShell() {
  const loadChallenges = useAppStore((s) => s.loadChallenges);
  const loadProgress = useAppStore((s) => s.loadProgress);

  useEffect(() => {
    loadChallenges();
    loadProgress();
  }, [loadChallenges, loadProgress]);

  // When a detached BrowserWindow closes, clear the corresponding
  // "detached" flag in the layout store so the placeholder goes
  // away. Uses the shared electronAPI type from types/electron.d.ts.
  useEffect(() => {
    const api = window.electronAPI;
    if (!api?.onPaneWindowClosed) return;
    const unsubscribe = api.onPaneWindowClosed((paneId) => {
      useLayoutStore.getState().markDetached(paneId, false);
    });
    return unsubscribe;
  }, []);

  useStepPlayer();
  useKeyboardShortcuts();

  return (
    <div className="h-full flex flex-col bg-coden-bg text-coden-text">
      <TopHeader />
      <TransportBar />
      <div className="flex-1 flex overflow-hidden">
        <aside className="w-64 border-r border-coden-border bg-coden-surface shrink-0 overflow-y-auto">
          <ChallengeList />
        </aside>
        <main className="flex-1 overflow-hidden">
          <LayoutRoot />
        </main>
      </div>
    </div>
  );
}


/** Top bar: brand on the left, Layout dropdown on the right. */
function TopHeader() {
  const challenges = useAppStore((s) => s.challenges);
  const applyPreset = useLayoutStore((s) => s.applyPreset);
  const replaceTree = useLayoutStore((s) => s.replaceTree);
  const tree = useLayoutStore((s) => s.tree);
  const leafCount = allLeaves(tree).length;

  return (
    <header className="h-10 flex items-center justify-between px-4 border-b border-coden-border bg-coden-surface shrink-0">
      <div className="flex items-center gap-3">
        <span className="text-lg">⚙️</span>
        <h1 className="text-base font-semibold tracking-tight">cOde(n)</h1>
        {challenges.length > 0 && (
          <span className="text-xs text-coden-muted font-mono">
            {challenges.length} challenges
          </span>
        )}
      </div>
      <div className="flex items-center gap-2 text-xs">
        <span className="text-coden-muted font-mono">{leafCount} panes</span>
        <label className="text-coden-muted">Layout</label>
        <select
          value={String(leafCount)}
          onChange={(e) => {
            const n = Number(e.target.value);
            if (n === 2 || n === 3 || n === 4) applyPreset(n);
          }}
          className="bg-coden-bg border border-coden-border rounded px-2 py-1 font-mono text-coden-text"
          title="Choose 2, 3, or 4 regions"
        >
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
        </select>
        <button
          type="button"
          onClick={() => applyPreset(4)}
          className="px-2 py-1 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border"
          title="Reset the layout to the 4-pane default"
        >
          Reset
        </button>
        <button
          type="button"
          onClick={() => {
            // Snap all splits back to equal sizes.
            const equalize = (n: import('./layout/tree-ops').LayoutNode): import('./layout/tree-ops').LayoutNode => {
              if (n.kind === 'leaf') return n;
              return {
                ...n,
                sizes: Array.from({ length: n.children.length }, () => 1 / n.children.length),
                children: n.children.map(equalize),
              };
            };
            replaceTree(equalize(tree));
          }}
          className="px-2 py-1 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border"
          title="Reset all splitters to equal sizes"
        >
          ⇔ Equalize
        </button>
      </div>
    </header>
  );
}


/**
 * TransportBar — challenge title, Run, Reset, n/seed, step controls.
 * Carved out of the old ChallengeView so it lives at the same level
 * as the pane tree (the panes never own the transport).
 */
function TransportBar() {
  const detail = useAppStore((s) => s.currentDetail);
  const isRunning = useAppStore((s) => s.isRunning);
  const run = useAppStore((s) => s.run);
  const reset = useAppStore((s) => s.reset);
  const runResult = useAppStore((s) => s.runResult);
  const saveSolution = useAppStore((s) => s.saveSolution);
  const n = useAppStore((s) => s.n);
  const setN = useAppStore((s) => s.setN);
  const seed = useAppStore((s) => s.seed);
  const setSeed = useAppStore((s) => s.setSeed);

  async function handlePopOut() {
    const api = (window as Window).electronAPI;
    if (api?.popOutEditor) {
      await api.popOutEditor();
    } else {
      window.open(window.location.pathname + '?view=editor', '_blank');
    }
  }

  return (
    <div className="h-12 px-4 py-2 border-b border-coden-border bg-coden-surface shrink-0 flex items-center gap-3 overflow-x-auto">
      <div className="min-w-0">
        {detail ? (
          <>
            <h2 className="text-sm font-semibold truncate leading-tight">{detail.name}</h2>
            <div className="text-[10px] text-coden-muted font-mono truncate leading-tight">
              {detail.id} · {detail.category} · difficulty {detail.difficulty}/10
            </div>
          </>
        ) : (
          <div className="text-sm text-coden-muted">Pick a challenge →</div>
        )}
      </div>

      <div className="flex items-center gap-1 ml-2 shrink-0">
        <button
          type="button"
          onClick={run}
          disabled={isRunning || !detail}
          className="px-3 py-1.5 text-sm font-semibold rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isRunning ? 'Running…' : '▶ Run'}
        </button>
        <button
          type="button"
          onClick={reset}
          disabled={isRunning}
          className="px-2 py-1.5 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50"
        >
          Reset
        </button>
        <button
          type="button"
          onClick={saveSolution}
          disabled={!detail}
          className="px-2 py-1.5 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50"
          title="Save (Ctrl/Cmd+S)"
        >
          💾
        </button>
        <button
          type="button"
          onClick={handlePopOut}
          className="px-2 py-1.5 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border"
          title="Open the standalone editor in a separate window"
        >
          ⧉
        </button>
      </div>

      {detail && (
        <div className="flex items-center gap-1 text-xs shrink-0">
          <label className="text-coden-muted">n</label>
          <input
            type="number"
            min={2}
            max={detail.max_n}
            value={n}
            onChange={(e) => setN(Math.max(2, Math.min(detail.max_n, Number(e.target.value) || 16)))}
            className="w-16 bg-coden-bg border border-coden-border rounded px-2 py-1 font-mono text-coden-text"
          />
          <label className="text-coden-muted ml-1">seed</label>
          <input
            type="number"
            value={seed ?? ''}
            onChange={(e) => setSeed(e.target.value === '' ? null : Number(e.target.value))}
            className="w-16 bg-coden-bg border border-coden-border rounded px-2 py-1 font-mono text-coden-text"
          />
        </div>
      )}

      <div className="flex-1 min-w-0">
        <StepControls />
      </div>

      {runResult && detail && (
        <div className="text-xs text-coden-muted font-mono shrink-0">
          n=<span className="text-coden-text">{runResult.n}</span>
          <span className="mx-1 text-coden-muted">|</span>
          req:{' '}
          <span className="text-coden-text">{detail.required_complexity}</span>
          <span className="mx-1 text-coden-muted">|</span>
          ops:{' '}
          <span className="text-coden-text">{runResult.stats.total.toLocaleString()}</span>
        </div>
      )}
    </div>
  );
}
