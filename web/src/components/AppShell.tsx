/**
 * AppShell.tsx — top-level layout.
 *
 *   +-------------------------------------------+
 *   | header  logo  ........ Layout: 4 ▾       |
 *   +-------------------------------------------+
 *   | transport  challenge  result summary     |
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
 *   - a compact case/runtime result line (when
 *     a run is available)
 *
 * No editor pop-out, no AI mode toggle, no external IDE handoff.
 * Debugging now happens inside the cOde(n) editor.
 */
import { useEffect, useMemo, useState } from 'react';
import { useAppStore } from '../store/useAppStore';
import { useKeyboardShortcuts } from '../hooks/useKeyboardShortcuts';
import { useUpdater } from '../hooks/useUpdater';
import { usePaneFontZoom } from '../hooks/usePaneFontZoom';
import { ChallengeList } from './ChallengeList';
import { UpdateToast } from './UpdateToast';
import { TabBar } from './TabBar';
import { Workspace } from './Workspace';
import { ProfileModal } from './ProfileModal';
import { InfoModal } from './InfoModal';
import { EloGuideModal } from './EloGuideModal';
import { BrandWordmark } from './BrandWordmark';
import { EulerWordmark } from './EulerWordmark';
import { getAlgorithmSetsForMode, challengesForAlgorithmSet } from '../lib/algorithmSets';
import { collectSetChallengeIds, filterCustomProblemSetsForMode } from '../lib/customProblemSets';
import { ThemePicker } from './ThemePicker';
import { getTheme, applyThemeToDocument } from '../lib/themes';

export function AppShell() {
  const loadChallenges = useAppStore((s) => s.loadChallenges);
  const loadProgress = useAppStore((s) => s.loadProgress);
  const loadProfiles = useAppStore((s) => s.loadProfiles);
  const challenges = useAppStore((s) => s.challenges);
  const baseFontSize = useAppStore((s) => s.baseFontSize);
  const themeId = useAppStore((s) => s.themeId);
  const [showProfileModal, setShowProfileModal] = useState(false);
  const [showInfoModal, setShowInfoModal] = useState(false);
  const [showEloGuide, setShowEloGuide] = useState(false);

  const sidebarWidth = useAppStore((s) => s.sidebarWidth);
  const setSidebarWidth = useAppStore((s) => s.setSidebarWidth);
  const sidebarPosition = useAppStore((s) => s.sidebarPosition);
  const sidebarCollapsed = useAppStore((s) => s.sidebarCollapsed);
  const sidebarFontScale = useAppStore((s) => s.paneFontScales.sidebar ?? 1);

  usePaneFontZoom();

  useEffect(() => {
    document.documentElement.style.fontSize = `${baseFontSize}px`;
  }, [baseFontSize]);

  useEffect(() => {
    const selected = getTheme(themeId);
    applyThemeToDocument(selected);
  }, [themeId]);

  useEffect(() => {
    let cancelled = false;
    void (async () => {
      await Promise.all([loadProgress(), loadProfiles()]);
      if (!cancelled) await loadChallenges();
    })();
    return () => {
      cancelled = true;
    };
  }, [loadChallenges, loadProgress, loadProfiles]);

  useKeyboardShortcuts();

  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    const startX = e.clientX;
    const startWidth = sidebarWidth;

    const handleMouseMove = (moveEvent: MouseEvent) => {
      const deltaX = moveEvent.clientX - startX;
      const newWidth = sidebarPosition === 'left' 
        ? startWidth + deltaX 
        : startWidth - deltaX;
      setSidebarWidth(Math.max(160, Math.min(600, newWidth)));
    };

    const handleMouseUp = () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
      const finalWidth = useAppStore.getState().sidebarWidth;
      void useAppStore.getState().saveSidebarWidthToBackend(finalWidth);
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
  };

  const handleDoubleClick = () => {
    setSidebarWidth(256);
    void useAppStore.getState().saveSidebarWidthToBackend(256);
  };

  return (
    <div className="h-full flex flex-col bg-coden-bg text-coden-text">
      <TopHeader
        onOpenProfiles={() => setShowProfileModal(true)}
        onOpenInfo={() => setShowInfoModal(true)}
        onOpenEloGuide={() => setShowEloGuide(true)}
      />
      <div className="flex-1 flex overflow-hidden">
        {!sidebarCollapsed && sidebarPosition === 'left' && (
          <aside 
            style={{ width: `${sidebarWidth}px` }}
            className="border-r border-coden-border bg-coden-surface shrink-0 overflow-y-auto"
          >
            <div data-font-scope="sidebar" style={{ zoom: sidebarFontScale }} className="h-full">
              <ChallengeList />
            </div>
          </aside>
        )}
        
        {!sidebarCollapsed && sidebarPosition === 'left' && (
          <div
            onMouseDown={handleMouseDown}
            onDoubleClick={handleDoubleClick}
            className="w-1 hover:w-1.5 active:w-1.5 bg-coden-border hover:bg-coden-accent active:bg-coden-accent cursor-col-resize shrink-0 transition-colors z-20"
            title="Drag to resize, double-click to reset"
          />
        )}

        <main className="flex-1 flex flex-col min-w-0 bg-coden-bg">
          <TabBar />
          <TransportBar />
          <Workspace />
        </main>

        {!sidebarCollapsed && sidebarPosition === 'right' && (
          <div
            onMouseDown={handleMouseDown}
            onDoubleClick={handleDoubleClick}
            className="w-1 hover:w-1.5 active:w-1.5 bg-coden-border hover:bg-coden-accent active:bg-coden-accent cursor-col-resize shrink-0 transition-colors z-20"
            title="Drag to resize, double-click to reset"
          />
        )}

        {!sidebarCollapsed && sidebarPosition === 'right' && (
          <aside 
            style={{ width: `${sidebarWidth}px` }}
            className="border-l border-coden-border bg-coden-surface shrink-0 overflow-y-auto"
          >
            <div data-font-scope="sidebar" style={{ zoom: sidebarFontScale }} className="h-full">
              <ChallengeList />
            </div>
          </aside>
        )}
      </div>
      <UpdateToast />
      {showProfileModal && <ProfileModal onClose={() => setShowProfileModal(false)} />}
      {showInfoModal && <InfoModal onClose={() => setShowInfoModal(false)} />}
      {showEloGuide && <EloGuideModal challenges={challenges} onClose={() => setShowEloGuide(false)} />}
    </div>
  );
}


function TopHeader({
  onOpenProfiles,
  onOpenInfo,
  onOpenEloGuide,
}: {
  onOpenProfiles: () => void;
  onOpenInfo: () => void;
  onOpenEloGuide: () => void;
}) {
  const challenges = useAppStore((s) => s.challenges);
  const updater = useUpdater();
  const theme = useAppStore((s) => s.theme);
  const toggleTheme = useAppStore((s) => s.toggleTheme);
  const cheaterMode = useAppStore((s) => s.cheaterMode);
  const setCheaterMode = useAppStore((s) => s.setCheaterMode);
  const increaseFontSize = useAppStore((s) => s.increaseFontSize);
  const decreaseFontSize = useAppStore((s) => s.decreaseFontSize);
  const activeProfile = useAppStore((s) => s.activeProfile);
  const activeSet = useAppStore((s) => s.activeSet);
  const setActiveSet = useAppStore((s) => s.setActiveSet);
  const activeCustomSetId = useAppStore((s) => s.activeCustomSetId);
  const setActiveCustomSet = useAppStore((s) => s.setActiveCustomSet);
  const customProblemSets = useAppStore((s) => s.customProblemSets);
  const appMode = useAppStore((s) => s.appMode);
  const setAppMode = useAppStore((s) => s.setAppMode);
  const modeCustomSets = useMemo(
    () => filterCustomProblemSetsForMode(customProblemSets, appMode),
    [customProblemSets, appMode],
  );
  const selectedCustomSet = modeCustomSets.find((set) => set.id === activeCustomSetId) ?? null;
  const modeChallenges = useMemo(
    () => challenges.filter((c) => (appMode === 'euler' ? c.dataset === 'euler' || c.id.startsWith('euler_') : c.dataset !== 'euler' && !c.id.startsWith('euler_'))),
    [challenges, appMode],
  );
  const visibleChallengeCount = useMemo(
    () => {
      if (activeSet !== 'custom') return challengesForAlgorithmSet(challenges, activeSet).length;
      if (!selectedCustomSet) return 0;
      const challengeIds = collectSetChallengeIds(selectedCustomSet);
      return modeChallenges.filter((challenge) => challengeIds.has(challenge.id)).length;
    },
    [challenges, activeSet, selectedCustomSet, modeChallenges],
  );
  const activeSetSelectorValue = activeSet === 'custom'
    ? activeCustomSetId ? `custom:${activeCustomSetId}` : 'custom'
    : activeSet;

  const sidebarCollapsed = useAppStore((s) => s.sidebarCollapsed);
  const setSidebarCollapsed = useAppStore((s) => s.setSidebarCollapsed);
  const sidebarPosition = useAppStore((s) => s.sidebarPosition);
  const setSidebarPosition = useAppStore((s) => s.setSidebarPosition);

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
          title={appMode === 'euler' ? "About Euler" : "About cOde(n)"}
          aria-label={appMode === 'euler' ? "About Euler" : "About cOde(n)"}
        >
          {appMode === 'euler' ? <EulerWordmark /> : <BrandWordmark />}
        </button>

        {/* Subtle Android-style toggle switch without text */}
        <button
          type="button"
          onClick={() => {
            const nextMode = appMode === 'coden' ? 'euler' : 'coden';
            setAppMode(nextMode);
            if (activeSet !== 'custom') {
              setActiveSet(nextMode === 'euler' ? 'euler_level' : 'leetcode');
            }
          }}
          className={`relative inline-flex h-4 w-7 shrink-0 cursor-pointer items-center rounded-full p-0.5 transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-coden-accent ml-1.5 ${
            appMode === 'euler'
              ? 'bg-blue-600 dark:bg-blue-500'
              : 'bg-slate-300 dark:bg-slate-700'
          }`}
          title={appMode === 'euler' ? "Switch to cOde(n) (LeetCode)" : "Switch to Project Euler"}
          aria-label={appMode === 'euler' ? "Switch to cOde(n) (LeetCode)" : "Switch to Project Euler"}
        >
          <span
            className={`pointer-events-none inline-block h-3 w-3 rounded-full bg-white shadow-xs ring-0 transition-transform duration-200 ease-in-out ${
              appMode === 'euler' ? 'translate-x-3' : 'translate-x-0'
            }`}
          />
        </button>


        {challenges.length > 0 && (
          <span className="text-[11px] text-slate-500 font-mono shrink-0">
            {visibleChallengeCount} challenges
          </span>
        )}
        <div className="ml-2 flex items-center gap-1 rounded bg-coden-bg border border-coden-border px-2 py-0.5 max-w-[300px]">
          <span className="text-coden-muted text-[10.5px] font-medium truncate max-w-[110px]">
            {activeProfile}
          </span>
          <span className="text-coden-muted/60 text-[10.5px]">·</span>
          <select
            value={activeSetSelectorValue}
            onChange={(event) => {
              const value = event.target.value;
              if (value === 'custom') {
                void setActiveCustomSet(null);
              } else if (value.startsWith('custom:')) {
                void setActiveCustomSet(value.slice('custom:'.length));
              } else {
                void setActiveSet(value as typeof activeSet);
              }
            }}
            className="bg-transparent text-coden-text text-[10.5px] font-medium outline-none cursor-pointer max-w-[145px]"
            title="Select algorithm set"
            aria-label="Select algorithm set"
          >
            {Array.from(new Set(getAlgorithmSetsForMode(appMode).map((s) => s.category)))
              .filter((category) => category !== 'Personal')
              .map((category) => (
                <optgroup
                  key={category}
                  label={category}
                  className="bg-coden-surface text-coden-text font-bold"
                >
                  {getAlgorithmSetsForMode(appMode).filter((s) => s.category === category).map((setOption) => (
                  <option
                    key={setOption.id}
                    value={setOption.id}
                    className="bg-coden-surface text-coden-text font-normal"
                  >
                    {setOption.label}{setOption.hasCareerPath ? ' · Career' : ''}
                  </option>
                  ))}
                </optgroup>
              ))}
            <optgroup
              label="Personal"
              className="bg-coden-surface text-coden-text font-bold"
            >
              {modeCustomSets.length > 0
                ? modeCustomSets.map((set) => (
                  <option
                    key={set.id}
                    value={`custom:${set.id}`}
                    className="bg-coden-surface text-coden-text font-normal"
                  >
                    {set.name || 'Untitled Personal root'}{set.career_mode ? ' · Career' : ''}
                  </option>
                ))
                : (
                  <option
                    value="custom"
                    className="bg-coden-surface text-coden-text font-normal"
                  >
                    {appMode === 'euler' ? 'Create a Euler Personal root…' : 'Create a Personal root…'}
                  </option>
                )}
            </optgroup>
          </select>
        </div>
        <button
          type="button"
          role="switch"
          aria-checked={cheaterMode}
          onClick={() => setCheaterMode(!cheaterMode)}
          className={[
            'inline-flex h-7 shrink-0 items-center gap-2 rounded-full border px-2.5 text-[10.5px] font-bold shadow-sm transition-all',
            cheaterMode
              ? 'border-rose-500 bg-rose-500/20 text-rose-700 ring-1 ring-rose-500/50 hover:bg-rose-500/30 dark:text-rose-200'
              : 'border-emerald-500/80 bg-coden-bg text-coden-muted hover:bg-emerald-500/10 hover:text-emerald-700 dark:hover:text-emerald-300',
          ].join(' ')}
          title={cheaterMode
            ? 'Cheater Mode is on: all reference solutions are visible. Career progression remains unchanged.'
            : 'Turn on Cheater Mode to reveal all reference solutions without changing Career progression.'}
        >
          <span>Cheater Mode 😉</span>
          <span
            aria-hidden="true"
            className={[
              'rounded-full px-1.5 py-0.5 font-mono text-[9px] tracking-wide',
              cheaterMode
                ? 'bg-rose-500 text-white'
                : 'bg-emerald-500/15 text-emerald-700 dark:text-emerald-300',
            ].join(' ')}
          >
            {cheaterMode ? 'ON' : 'OFF'}
          </span>
        </button>
        {(activeSet === 'elo' || activeSet === 'elo_buckets') && (
          <button
            type="button"
            onClick={onOpenEloGuide}
            className="inline-flex h-6 shrink-0 items-center gap-1 rounded border border-coden-border bg-coden-bg px-2 text-[10px] font-semibold text-coden-muted transition-colors hover:border-coden-accent hover:text-coden-accent"
            title="Understand Elo ratings and interview practice targets"
            aria-label="Open Elo difficulty and interview practice guide"
          >
            <span aria-hidden="true" className="font-serif font-bold">i</span>
            Elo guide
          </button>
        )}
        <div className="ml-2 flex items-center gap-1 rounded bg-coden-bg border border-coden-border px-1 py-0.5 shrink-0">
          <button
            type="button"
            onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
            className="px-2 py-0.5 rounded text-[10.5px] font-medium text-coden-muted hover:text-coden-text hover:bg-coden-surface transition-colors"
            title="Toggle Sidebar (Show / Hide)"
            aria-label={sidebarCollapsed ? "Show Sidebar" : "Hide Sidebar"}
          >
            {sidebarCollapsed ? 'Show Sidebar' : 'Hide Sidebar'}
          </button>
          <span className="text-coden-muted/40 text-[10.5px]">|</span>
          <button
            type="button"
            onClick={() => setSidebarPosition(sidebarPosition === 'left' ? 'right' : 'left')}
            className="px-2 py-0.5 rounded text-[10.5px] font-medium text-coden-muted hover:text-coden-text hover:bg-coden-surface transition-colors"
            title="Toggle Sidebar position (Left / Right)"
            aria-label={sidebarPosition === 'left' ? "Move Sidebar to Right" : "Move Sidebar to Left"}
          >
            Position: {sidebarPosition === 'left' ? 'Left' : 'Right'}
          </button>
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
        <ThemePicker />
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
 * TransportBar — challenge identity and compact result line.
 *
 * Carved out of the old ChallengeView so it lives at the
 * same level as the pane tree (the panes never own the
 * transport).
 */
function TransportBar() {
  const detail = useAppStore((s) => s.currentDetail);
  const runResult = useAppStore((s) => s.runResult);
  const eloDisplay = detail
    ? detail.elo_rating !== null
      ? `Elo ${Math.round(detail.elo_rating)}`
      : detail.estimated_elo_rating !== null
        ? `Est. Elo ${Math.round(detail.estimated_elo_rating)}`
        : ''
    : '';
  const difficultyDisplay = detail
    ? [
        detail.difficulty_label,
        eloDisplay,
        `Freq ${detail.frequency === null ? '—' : `${detail.frequency.toFixed(1)}%`}`,
      ].filter(Boolean).join(' · ')
    : '';

  return (
    <div className="min-h-12 px-3 py-2 border-b border-coden-border bg-coden-surface shrink-0 flex items-center gap-3 overflow-x-auto">
      <div className="min-w-[220px] max-w-[380px]">
        {detail ? (
          <>
            <h2 className="text-sm font-semibold truncate leading-tight">{detail.name}</h2>
            <div className="text-xs text-coden-muted font-mono truncate leading-tight">
              {detail.id} · {detail.category} · {difficultyDisplay}
            </div>
          </>
        ) : (
          <div className="text-sm text-coden-muted">Pick a challenge →</div>
        )}
      </div>

      {runResult && detail && (
        <div className="ml-auto text-xs text-coden-muted font-mono shrink-0">
          {runResult.mode === 'real_test' && (
            <span
              className="mr-2 px-1.5 py-0.5 rounded bg-coden-accent/20 text-coden-accent font-semibold"
              title="Full run: visible, custom, and hidden cases"
            >
              FULL RUN
            </span>
          )}
          cases=<span className="text-coden-text">{runResult.case_results?.length || runResult.selected_case_ids?.length || 1}</span>
          <span className="mx-1 text-coden-muted">|</span>
          req:{' '}
          <span className="text-coden-text">{detail.required_complexity}</span>
          <span className="mx-1 text-coden-muted">|</span>
          time:{' '}
          <span className="text-coden-text">{formatRuntimeMs(runResult.runtime_user_ms)}</span>
        </div>
      )}
    </div>
  );
}

function formatRuntimeMs(value: number | null | undefined): string {
  if (value === null || value === undefined) return '—';
  if (value < 10) return `${value.toFixed(2)}ms`;
  if (value < 100) return `${value.toFixed(1)}ms`;
  return `${Math.round(value).toLocaleString()}ms`;
}
