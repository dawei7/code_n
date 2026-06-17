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
import { useUpdater } from '../hooks/useUpdater';
import { useDebugSession } from '../hooks/useDebugSession';
import { ChallengeList } from './ChallengeList';
import { LayoutRoot } from './layout/LayoutRoot';
import { useLayoutStore } from '../store/useLayoutStore';
import { StepControls } from './StepControls';
import { allLeaves } from './layout/tree-ops';
import { UpdateToast } from './UpdateToast';


export function AppShell() {
  const loadChallenges = useAppStore((s) => s.loadChallenges);
  const loadProgress = useAppStore((s) => s.loadProgress);
  const aiMode = useAppStore((s) => s.aiMode);

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

  // Add/remove the AI Report tab from the layout based on
  // `aiMode`. When AI is on, add it to the first leaf that
  // has the locals tab (so it sits next to the other analysis
  // surfaces); when AI is off, close it from every leaf.
  useEffect(() => {
    const layout = useLayoutStore.getState();
    const leaves = allLeaves(layout.tree);
    if (aiMode) {
      const target = leaves.find((l) => l.tabIds.includes('locals')) ?? leaves[0];
      if (target && !target.tabIds.includes('aiReport')) {
        layout.moveTab('aiReport', null, target.id);
      }
    } else {
      for (const l of leaves) {
        if (l.tabIds.includes('aiReport')) {
          layout.closeTabInLeaf('aiReport', l.id);
        }
      }
    }
  }, [aiMode]);

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
      <UpdateToast />
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
  const updater = useUpdater();
  const aiMode = useAppStore((s) => s.aiMode);
  const setAiMode = useAppStore((s) => s.setAiMode);

  // Tooltip describing the last update action for the "Check for
  // updates" button. Changes when the state changes.
  const updateButtonTitle = (() => {
    switch (updater.state.status.state) {
      case 'idle': return 'Check for cOde(n) updates';
      case 'checking': return 'Checking for updates…';
      case 'available': return `Update v${updater.state.status.version} available; downloading…`;
      case 'downloading': return `Downloading v${updater.state.status.version}…`;
      case 'downloaded': return `v${updater.state.status.version} ready — click Restart below`;
      case 'not-available': return 'You are on the latest version';
      case 'error': return `Update error: ${updater.state.status.message ?? 'unknown'}`;
    }
  })();

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
        {updater.state.appVersion && (
          <span
            className="text-[10px] text-coden-muted font-mono"
            title={`Currently running v${updater.state.appVersion.current} on the '${updater.state.appVersion.channel}' channel`}
          >
            v{updater.state.appVersion.current}
          </span>
        )}
      </div>
      <div className="flex items-center gap-2 text-xs">
        <span className="text-coden-muted font-mono">{leafCount} panes</span>
        <label
          className="flex items-center gap-1 cursor-pointer text-coden-muted hover:text-coden-text"
          title="Show the AI Report tab and enable Ollama-powered hints (requires local Ollama running)"
        >
          <input
            type="checkbox"
            checked={aiMode}
            onChange={(e) => setAiMode(e.target.checked)}
            className="accent-coden-accent"
          />
          AI
        </label>
        <label className="text-coden-muted">Layout</label>
        <select
          value={leafCount}
          onChange={(e) => {
            const n = Number(e.target.value);
            if (n >= 1 && n <= 6) applyPreset(n as 1 | 2 | 3 | 4 | 5 | 6);
          }}
          className="bg-coden-bg border border-coden-border rounded px-2 py-1 font-mono text-coden-text"
          title="Choose 1, 2, 3, 4, 5, or 6 panes"
        >
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
        </select>
        <button
          type="button"
          onClick={() => {
            // Snap all splits back to equal sizes (1/N each child).
            // Tree structure is preserved — only sizes change.
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
          className="px-2 py-1 rounded border border-coden-accent text-coden-accent hover:bg-coden-accent hover:text-coden-bg"
          title="Resize ALL panes to be equal (1/N). Use this to fix any pane that's been squished."
        >
          ⇔ Equal sizes
        </button>
        <button
          type="button"
          onClick={() => applyPreset(4)}
          className="px-2 py-1 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border"
          title="Reset the whole layout to the 4-pane default (clears your arrangement)"
        >
          ↺ Reset layout
        </button>
        <button
          type="button"
          onClick={() => void updater.checkNow()}
          disabled={updater.state.checking || updater.state.status.state === 'downloading'}
          className="px-2 py-1 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border disabled:opacity-50 disabled:cursor-not-allowed"
          title={updateButtonTitle}
        >
          {updater.state.checking ? 'Checking…' : '↻ Check for updates'}
        </button>
      </div>
    </header>
  );
}


/**
 * TransportBar — challenge title, mode toggle, Run, Reset, n/seed,
 * step controls. Carved out of the old ChallengeView so it lives
 * at the same level as the pane tree (the panes never own the
 * transport).
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
  const mode = useAppStore((s) => s.mode);
  const setMode = useAppStore((s) => s.setMode);
  const aiMode = useAppStore((s) => s.aiMode);
  const source = useAppStore((s) => s.source);
  const breakpoints = useAppStore((s) => s.breakpoints);
  const debugStatus = useAppStore((s) => s.debugStatus);
  const debugSession = useDebugSession();

  /**
   * Unified Run handler. If the user has set any breakpoints
   * in the editor gutter, this starts a debug session (the
   * session auto-pops-out into its own window the first time
   * a breakpoint is hit; see useDebugSession). Otherwise it
   * runs the challenge normally and renders the trace in
   * the 4-pane layout.
   *
   * Real-test mode forces the regular path: debug sessions
   * are exploratory and don't make sense with a server-picked
   * seed.
   */
  function handleRun() {
    if (!detail) return;
    if (
      breakpoints.size > 0 &&
      mode === 'practice' &&
      (debugStatus === 'idle' || debugStatus === 'exited' || debugStatus === 'error')
    ) {
      void debugSession.start({
        challengeId: detail.id,
        source: source || '',
        n,
        seed,
      });
      return;
    }
    void run();
  }

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

      {/* Mode toggle: practice (user picks n/seed) vs real_test
          (server picks n/seed, fresh every run). */}
      <div className="flex items-center text-xs shrink-0">
        <div
          className="inline-flex rounded border border-coden-border overflow-hidden"
          title="Practice: you pick n + seed. Real test: server picks both, fresh every run."
        >
          <button
            type="button"
            onClick={() => setMode('practice')}
            className={[
              'px-2 py-1 font-semibold',
              mode === 'practice'
                ? 'bg-coden-accent text-coden-bg'
                : 'text-coden-muted hover:text-coden-text hover:bg-coden-border',
            ].join(' ')}
          >
            Practice
          </button>
          <button
            type="button"
            onClick={() => setMode('real_test')}
            className={[
              'px-2 py-1 font-semibold border-l border-coden-border',
              mode === 'real_test'
                ? 'bg-coden-accent text-coden-bg'
                : 'text-coden-muted hover:text-coden-text hover:bg-coden-border',
            ].join(' ')}
          >
            Real test
          </button>
        </div>
      </div>

      <div className="flex items-center gap-1 ml-2 shrink-0">
        <button
          type="button"
          onClick={handleRun}
          disabled={isRunning || !detail}
          className="px-3 py-1.5 text-sm font-semibold rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
          title={
            breakpoints.size > 0
              ? `Run with debug (${breakpoints.size} breakpoint${breakpoints.size === 1 ? '' : 's'})`
              : 'Run the challenge'
          }
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
        {aiMode && runResult && (
          <button
            type="button"
            onClick={() => {
              // Open the AI Report tab in the first leaf that
              // has it; if it isn't in any leaf (e.g. AI was
              // turned on but the tab was never added), do
              // nothing here — the user can drag it from the
              // tab pool. The effect above adds it on toggle.
              const layout = useLayoutStore.getState();
              const leaves = allLeaves(layout.tree);
              const target = leaves.find((l) => l.tabIds.includes('aiReport'));
              if (target) {
                layout.setActiveTab(target.id, 'aiReport');
              }
            }}
            className="px-2 py-1.5 text-sm rounded border border-coden-accent text-coden-accent hover:bg-coden-accent hover:text-coden-bg"
            title="Open the AI Report tab"
          >
            🤖 Hint
          </button>
        )}
      </div>

      {detail && (
        <div
          className="flex items-center gap-1 text-xs shrink-0"
          title={
            mode === 'real_test'
              ? 'Server picks n + seed for the real test'
              : 'Pick the input size and a seed'
          }
        >
          <label className="text-coden-muted">n</label>
          <input
            type="number"
            min={2}
            max={detail.max_n}
            value={n}
            disabled={mode === 'real_test'}
            onChange={(e) => setN(Math.max(2, Math.min(detail.max_n, Number(e.target.value) || 16)))}
            className="w-16 bg-coden-bg border border-coden-border rounded px-2 py-1 font-mono text-coden-text disabled:opacity-50 disabled:cursor-not-allowed"
          />
          <label className="text-coden-muted ml-1">seed</label>
          <input
            type="number"
            value={seed ?? ''}
            disabled={mode === 'real_test'}
            onChange={(e) => setSeed(e.target.value === '' ? null : Number(e.target.value))}
            className="w-16 bg-coden-bg border border-coden-border rounded px-2 py-1 font-mono text-coden-text disabled:opacity-50 disabled:cursor-not-allowed"
          />
        </div>
      )}

      <div className="flex-1 min-w-0">
        <StepControls />
      </div>

      {runResult && detail && (
        <div className="text-xs text-coden-muted font-mono shrink-0">
          {runResult.mode === 'real_test' && (
            <span
              className="mr-2 px-1.5 py-0.5 rounded bg-coden-accent/20 text-coden-accent font-semibold"
              title="Real test: server picked n + seed"
            >
              REAL TEST
            </span>
          )}
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
