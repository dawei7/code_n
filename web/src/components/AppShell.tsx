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
 *   - Run / Reset / Open in VSCode buttons
 *   - n + seed inputs
 *   - a compact "n=… | req: … | ops: …" result line (when
 *     a run is available)
 *
 * No editor pop-out, no AI mode toggle, no debug pop-out,
 * no step controls. The "Open in VSCode" button writes the
 * active challenge id to solutions/.vscode-active and calls
 * Electron's shell.openPath(repoRoot).
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
  const progress = useAppStore((s) => s.progress);

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
    <header className="h-10 flex items-center justify-between px-4 border-b border-coden-border bg-coden-surface shrink-0 select-none">
      <div className="flex items-center gap-2">
        <button
          onClick={onOpenProfiles}
          className="text-base p-1 hover:bg-slate-800 rounded transition-all cursor-pointer flex items-center justify-center h-7 w-7"
          title="Open Settings"
        >
          ⚙️
        </button>
        <button
          onClick={onOpenInfo}
          className="text-base p-1 hover:bg-slate-800 rounded transition-all cursor-pointer flex items-center justify-center h-7 w-7"
          title="Open System Documentation & Help"
        >
          ℹ️
        </button>
        <h1 className="text-sm font-bold tracking-tight text-white ml-1">cOde(n)</h1>
        {challenges.length > 0 && (
          <span className="text-[11px] text-slate-500 font-mono">
            {challenges.length} challenges
          </span>
        )}
        <span className="ml-3 px-2 py-0.5 rounded bg-slate-950 border border-slate-850 text-slate-400 text-[10.5px] font-medium select-none">
          👤 User: {activeProfile} ({progress?.active_set === 'neetcode' ? 'NeetCode 250' : 'GeeksforGeeks'})
        </span>
        {updater.state.appVersion && (
          <span
            className="text-[10px] text-slate-500 font-mono"
            title={`Currently running v${updater.state.appVersion.current} on the '${updater.state.appVersion.channel}' channel`}
          >
            v{updater.state.appVersion.current}
          </span>
        )}
      </div>
      <div className="flex items-center gap-2 text-xs">
        <div className="flex items-center rounded border border-coden-border bg-coden-bg overflow-hidden mr-2">
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
          {language === 'en' ? '🇩🇪 DE' : '🇬🇧 EN'}
        </button>
        <button
          type="button"
          onClick={toggleTheme}
          className="px-2 py-1 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border"
          title={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
        >
          {theme === 'dark' ? '☀️ Light' : '🌙 Dark'}
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
 * TransportBar — challenge title, mode toggle, Run, Reset,
 * Open in VSCode, n/seed inputs, compact result line.
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
  const openInVSCode = useAppStore((s) => s.openInVSCode);

  async function handleOpenInVSCode() {
    if (!detail) return;
    // The store action handles: handoff-file write, on-demand
    // starter creation, the IPC call, the v0.9.2-vs-v0.9.3
    // boolean vs object return shape, and shared error state
    // (so VSCodeTab sees the same error the TransportBar set).
    await openInVSCode(detail);
  }

  return (
    <div className="h-12 px-4 py-2 border-b border-coden-border bg-coden-surface shrink-0 flex items-center gap-3 overflow-x-auto">
      <div className="min-w-0">
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
          onClick={() => void run()}
          disabled={isRunning || !detail}
          className="px-3 py-1.5 text-sm font-semibold rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
          title="Run the solution from solutions/<id>.py (re-reads the file on every click)"
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
          onClick={() => void handleOpenInVSCode()}
          disabled={!detail}
          className="px-2 py-1.5 text-sm rounded border border-coden-accent text-coden-accent hover:bg-coden-accent hover:text-coden-bg disabled:opacity-50 disabled:cursor-not-allowed"
          title="Open solutions/<id>.py in Antigravity (writes the active challenge id to solutions/.vscode-active first)"
        >
          {'</>'} Antigravity
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
