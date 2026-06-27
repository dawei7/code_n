/**
 * AppShell.tsx — top-level layout.
 *
 *   +-------------------------------------------+
 *   | header  logo  ........ Layout: 4 ▾       |
 *   +-------------------------------------------+
 *   | transport  challenge  Run  n/seed ...    |
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
 *
 * The v0.9.0 transport bar is much smaller than the old one:
 *   - challenge title (left)
 *   - practice / real-test toggle
 *   - Run / Reset buttons
 *   - n + seed inputs
 *   - a compact "n=… | req: … | ops: …" result line (when
 *     a run is available)
 *
 * No editor pop-out, no AI mode toggle, no external IDE handoff.
 * Debugging now happens inside the cOde(n) editor.
 */
import { useEffect, useState } from 'react';
import { useAppStore } from '../store/useAppStore';
import { useKeyboardShortcuts } from '../hooks/useKeyboardShortcuts';
import { useUpdater } from '../hooks/useUpdater';
import { ChallengeList } from './ChallengeList';
import { UpdateToast } from './UpdateToast';
import { TabBar } from './TabBar';
import { Workspace } from './Workspace';
import { ProfileModal } from './ProfileModal';
import { InfoModal } from './InfoModal';
import { ALGORITHM_SETS } from '../lib/algorithmSets';


export function AppShell() {
  const loadChallenges = useAppStore((s) => s.loadChallenges);
  const loadProgress = useAppStore((s) => s.loadProgress);
  const loadProfiles = useAppStore((s) => s.loadProfiles);
  const baseFontSize = useAppStore((s) => s.baseFontSize);
  const theme = useAppStore((s) => s.theme);
  const [showProfileModal, setShowProfileModal] = useState(false);
  const [showInfoModal, setShowInfoModal] = useState(false);

  useEffect(() => {
    document.documentElement.style.fontSize = `${baseFontSize}px`;
  }, [baseFontSize]);

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);

  useEffect(() => {
    loadChallenges();
    loadProgress();
    loadProfiles();
  }, [loadChallenges, loadProgress, loadProfiles]);

  useKeyboardShortcuts();

  return (
    <div className="h-full flex flex-col bg-coden-bg text-coden-text">
      <TopHeader onOpenProfiles={() => setShowProfileModal(true)} onOpenInfo={() => setShowInfoModal(true)} />
      <div className="flex-1 flex overflow-hidden">
        <aside className="w-64 border-r border-coden-border bg-coden-surface shrink-0 overflow-y-auto">
          <ChallengeList />
        </aside>
        <main className="flex-1 flex flex-col min-w-0 bg-coden-bg">
          <TabBar />
          <TransportBar />
          <Workspace />
        </main>
      </div>
      <UpdateToast />
      {showProfileModal && <ProfileModal onClose={() => setShowProfileModal(false)} />}
      {showInfoModal && <InfoModal onClose={() => setShowInfoModal(false)} />}
    </div>
  );
}


function TopHeader({ onOpenProfiles, onOpenInfo }: { onOpenProfiles: () => void; onOpenInfo: () => void }) {
  const challenges = useAppStore((s) => s.challenges);
  const updater = useUpdater();
  const theme = useAppStore((s) => s.theme);
  const toggleTheme = useAppStore((s) => s.toggleTheme);
  const language = useAppStore((s) => s.language);
  const setLanguage = useAppStore((s) => s.setLanguage);
  const increaseFontSize = useAppStore((s) => s.increaseFontSize);
  const decreaseFontSize = useAppStore((s) => s.decreaseFontSize);
  const activeProfile = useAppStore((s) => s.activeProfile);
  const activeSet = useAppStore((s) => s.activeSet);
  const setActiveSet = useAppStore((s) => s.setActiveSet);

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
    <header className="h-10 flex items-center justify-between gap-3 px-3 border-b border-coden-border bg-coden-surface shrink-0 select-none">
      <div className="flex items-center gap-2 min-w-0">
        <button
          onClick={onOpenProfiles}
          className="text-sm p-1 hover:bg-coden-border rounded transition-all cursor-pointer flex items-center justify-center h-7 w-7"
          title="Open Settings"
          aria-label="Open Settings"
        >
          ⚙
        </button>
        <button
          onClick={onOpenInfo}
          className="text-sm p-1 hover:bg-coden-border rounded transition-all cursor-pointer flex items-center justify-center h-7 w-7"
          title="Open System Documentation & Help"
          aria-label="Open System Documentation & Help"
        >
          i
        </button>
        <button
          type="button"
          onClick={onOpenInfo}
          className="text-sm font-bold tracking-tight text-coden-text ml-1 shrink-0 hover:text-coden-accent transition-colors"
          title="About cOde(n)"
          aria-label="About cOde(n)"
        >
          cOde(n)
        </button>
        {challenges.length > 0 && (
          <span className="text-[11px] text-slate-500 font-mono shrink-0">
            {challenges.length} challenges
          </span>
        )}
        <div className="ml-2 flex items-center gap-1 rounded bg-coden-bg border border-coden-border px-2 py-0.5 max-w-[300px]">
          <span className="text-coden-muted text-[10.5px] font-medium truncate max-w-[110px]">
            {activeProfile}
          </span>
          <span className="text-coden-muted/60 text-[10.5px]">·</span>
          <select
            value={activeSet}
            onChange={(event) => void setActiveSet(event.target.value as typeof activeSet)}
            className="bg-transparent text-coden-text text-[10.5px] font-medium outline-none cursor-pointer max-w-[145px]"
            title="Select algorithm set"
            aria-label="Select algorithm set"
          >
            {ALGORITHM_SETS.map((setOption) => (
              <option
                key={setOption.id}
                value={setOption.id}
                className="bg-coden-surface text-coden-text"
              >
                {setOption.label}
              </option>
            ))}
          </select>
        </div>
        {updater.state.appVersion && (
          <span
            className="text-[10px] text-slate-500 font-mono"
            title={`Currently running v${updater.state.appVersion.current} on the '${updater.state.appVersion.channel}' channel`}
          >
            v{updater.state.appVersion.current}
          </span>
        )}
      </div>
      <div className="flex items-center gap-1 text-xs shrink-0">
        <div className="flex items-center rounded border border-coden-border bg-coden-bg overflow-hidden mr-1">
          <button
            type="button"
            onClick={decreaseFontSize}
            className="px-2 py-1 text-coden-muted hover:text-coden-text hover:bg-coden-surface border-r border-coden-border transition-colors font-semibold"
            title="Decrease text size"
          >
            A-
          </button>
          <button
            type="button"
            onClick={increaseFontSize}
            className="px-2 py-1 text-coden-muted hover:text-coden-text hover:bg-coden-surface transition-colors font-semibold"
            title="Increase text size"
          >
            A+
          </button>
        </div>
        <button
          type="button"
          onClick={() => setLanguage(language === 'en' ? 'de' : 'en')}
          className="px-2 py-1 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border mr-1"
          title={`Switch to ${language === 'en' ? 'German' : 'English'}`}
        >
          {language === 'en' ? 'DE' : 'EN'}
        </button>
        <button
          type="button"
          onClick={toggleTheme}
          className="h-7 w-7 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border flex items-center justify-center text-sm"
          title={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
          aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
        >
          {theme === 'dark' ? '☀' : '☾'}
        </button>
        <button
          type="button"
          onClick={() => void updater.checkNow()}
          disabled={updater.state.checking || updater.state.status.state === 'downloading'}
          className="px-2 py-1 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border disabled:opacity-50 disabled:cursor-not-allowed"
          title={updateButtonTitle}
        >
          {updater.state.checking ? 'Checking...' : 'Updates'}
        </button>
      </div>
    </header>
  );
}


/**
 * TransportBar — challenge title, mode toggle, Run, Reset,
 * n/seed inputs, compact result line.
 *
 * Carved out of the old ChallengeView so it lives at the
 * same level as the pane tree (the panes never own the
 * transport).
 */
function TransportBar() {
  const detail = useAppStore((s) => s.currentDetail);
  const isRunning = useAppStore((s) => s.isRunning);
  const run = useAppStore((s) => s.run);
  const reset = useAppStore((s) => s.reset);
  const runResult = useAppStore((s) => s.runResult);
  const n = useAppStore((s) => s.n);
  const setN = useAppStore((s) => s.setN);
  const seed = useAppStore((s) => s.seed);
  const setSeed = useAppStore((s) => s.setSeed);
  const mode = useAppStore((s) => s.mode);
  const setMode = useAppStore((s) => s.setMode);

  return (
    <div className="min-h-12 px-3 py-2 border-b border-coden-border bg-coden-surface shrink-0 flex items-center gap-3 overflow-x-auto">
      <div className="min-w-[220px] max-w-[380px]">
        {detail ? (
          <>
            <h2 className="text-sm font-semibold truncate leading-tight">{detail.name}</h2>
            <div className="text-xs text-coden-muted font-mono truncate leading-tight">
              {detail.id} · {detail.category} · difficulty {detail.difficulty}/10
            </div>
          </>
        ) : (
          <div className="text-sm text-coden-muted">Pick a challenge →</div>
        )}
      </div>

      {/* Mode toggle: practice (user picks n/seed) vs real_test
          (server picks n/seed, fresh every run). */}
      <div className="flex items-center text-xs shrink-0 ml-auto">
        <div
          className="inline-flex rounded border border-coden-border overflow-hidden"
          title="Practice: you pick n + seed. Real test: server picks both, fresh every run."
        >
          <button
            type="button"
            onClick={() => setMode('practice')}
            title="Practice mode"
            aria-label="Practice mode"
            className={[
              'h-7 w-8 font-semibold flex items-center justify-center text-sm',
              mode === 'practice'
                ? 'bg-coden-accent text-coden-bg'
                : 'text-coden-muted hover:text-coden-text hover:bg-coden-border',
            ].join(' ')}
          >
            ⚙
          </button>
          <button
            type="button"
            onClick={() => setMode('real_test')}
            title="Real test mode"
            aria-label="Real test mode"
            className={[
              'h-7 w-8 font-semibold border-l border-coden-border flex items-center justify-center text-sm',
              mode === 'real_test'
                ? 'bg-coden-accent text-coden-bg'
                : 'text-coden-muted hover:text-coden-text hover:bg-coden-border',
            ].join(' ')}
          >
            ✓
          </button>
        </div>
      </div>

      <div className="flex items-center gap-1 ml-2 shrink-0">
        <button
          type="button"
          onClick={() => void run()}
          disabled={isRunning || !detail}
          className="coden-transport-run h-8 w-9 text-sm font-semibold rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
          title="Run the solution from solutions/<id>.py (re-reads the file on every click)"
          aria-label="Run solution"
        >
          {isRunning ? 'Running…' : '▶ Run'}
        </button>
        <button
          type="button"
          onClick={reset}
          disabled={isRunning}
          className="coden-transport-reset h-8 w-9 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50 flex items-center justify-center"
          title="Reset current solution"
          aria-label="Reset current solution"
        >
          Reset
        </button>
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
            className="h-7 w-16 bg-coden-bg border border-coden-border rounded px-2 font-mono text-coden-text disabled:opacity-50 disabled:cursor-not-allowed"
          />
          <label className="text-coden-muted ml-1">seed</label>
          <input
            type="number"
            value={seed ?? ''}
            disabled={mode === 'real_test'}
            onChange={(e) => setSeed(e.target.value === '' ? null : Number(e.target.value))}
            className="h-7 w-16 bg-coden-bg border border-coden-border rounded px-2 font-mono text-coden-text disabled:opacity-50 disabled:cursor-not-allowed"
          />
        </div>
      )}

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
          <span className="text-coden-text">{(runResult.user_ast_ops ?? 0).toLocaleString()}</span>
        </div>
      )}
    </div>
  );
}
