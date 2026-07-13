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
import { useEffect, useMemo, useRef, useState } from 'react';
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
import { ALGORITHM_SETS, challengesForAlgorithmSet } from '../lib/algorithmSets';
import {
  ACCENT_PRESETS,
  DEFAULT_ACCENT_COLORS,
  accentContrastRatio,
  bestAccentTextColor,
  colorToHex,
  formatCssColor,
  normalizeAccentColors,
  parseCssColor,
} from '../lib/accentColors';
import type { RgbaColor, ThemeMode } from '../lib/accentColors';


export function AppShell() {
  const loadChallenges = useAppStore((s) => s.loadChallenges);
  const loadProgress = useAppStore((s) => s.loadProgress);
  const loadProfiles = useAppStore((s) => s.loadProfiles);
  const baseFontSize = useAppStore((s) => s.baseFontSize);
  const theme = useAppStore((s) => s.theme);
  const [showProfileModal, setShowProfileModal] = useState(false);
  const [showInfoModal, setShowInfoModal] = useState(false);

  const sidebarWidth = useAppStore((s) => s.sidebarWidth);
  const setSidebarWidth = useAppStore((s) => s.setSidebarWidth);
  const sidebarPosition = useAppStore((s) => s.sidebarPosition);
  const sidebarCollapsed = useAppStore((s) => s.sidebarCollapsed);
  const sidebarFontScale = useAppStore((s) => s.paneFontScales.sidebar ?? 1);
  const accentColors = useAppStore((s) => s.accentColors);

  usePaneFontZoom();

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
    const colors = normalizeAccentColors(accentColors);
    const accent = colors[theme];
    document.documentElement.style.setProperty('--coden-accent', accent);
    document.documentElement.style.setProperty('--coden-accent-contrast', bestAccentTextColor(accent, theme));
  }, [accentColors, theme]);

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
      <TopHeader onOpenProfiles={() => setShowProfileModal(true)} onOpenInfo={() => setShowInfoModal(true)} />
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
  const visibleChallengeCount = useMemo(
    () => challengesForAlgorithmSet(challenges, activeSet).length,
    [challenges, activeSet],
  );

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
          title="About cOde(n)"
          aria-label="About cOde(n)"
        >
          cOde(n)
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
            value={activeSet}
            onChange={(event) => void setActiveSet(event.target.value as typeof activeSet)}
            className="bg-transparent text-coden-text text-[10.5px] font-medium outline-none cursor-pointer max-w-[145px]"
            title="Select algorithm set"
            aria-label="Select algorithm set"
          >
            {Array.from(new Set(ALGORITHM_SETS.map((s) => s.category))).map((category) => (
              <optgroup
                key={category}
                label={category}
                className="bg-coden-surface text-coden-text font-bold"
              >
                {ALGORITHM_SETS.filter((s) => s.category === category).map((setOption) => (
                  <option
                    key={setOption.id}
                    value={setOption.id}
                    className="bg-coden-surface text-coden-text font-normal"
                  >
                    {setOption.label}
                  </option>
                ))}
              </optgroup>
            ))}
          </select>
        </div>
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
        <AccentColorPicker />
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


function AccentColorPicker() {
  const theme = useAppStore((state) => state.theme);
  const savedColors = useAppStore((state) => state.accentColors);
  const saveAccentColors = useAppStore((state) => state.saveAccentColors);
  const rootRef = useRef<HTMLDivElement>(null);
  const normalizedSaved = normalizeAccentColors(savedColors);
  const [open, setOpen] = useState(false);
  const [editingTheme, setEditingTheme] = useState<ThemeMode>(theme);
  const [draft, setDraft] = useState(normalizedSaved);
  const [colorInput, setColorInput] = useState(normalizedSaved[theme]);
  const [error, setError] = useState('');
  const [saving, setSaving] = useState(false);

  const beginEditing = () => {
    const next = normalizeAccentColors(savedColors);
    setDraft(next);
    setEditingTheme(theme);
    setColorInput(next[theme]);
    setError('');
    setOpen(true);
  };

  useEffect(() => {
    if (!open) return;
    const closeOutside = (event: PointerEvent) => {
      if (!rootRef.current?.contains(event.target as Node)) setOpen(false);
    };
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setOpen(false);
    };
    document.addEventListener('pointerdown', closeOutside);
    window.addEventListener('keydown', closeOnEscape);
    return () => {
      document.removeEventListener('pointerdown', closeOutside);
      window.removeEventListener('keydown', closeOnEscape);
    };
  }, [open]);

  const parsed = parseCssColor(colorInput) ?? parseCssColor(draft[editingTheme])!;
  const selectedColor = draft[editingTheme];
  const contrast = accentContrastRatio(selectedColor, editingTheme);
  const contrastTone = contrast >= 4.5 ? 'Strong' : contrast >= 3 ? 'Usable' : 'Low';
  const previewText = bestAccentTextColor(selectedColor, editingTheme);

  const applyColor = (color: RgbaColor) => {
    const formatted = formatCssColor(color);
    setDraft((current) => ({ ...current, [editingTheme]: formatted }));
    setColorInput(formatted);
    setError('');
  };

  const changeInput = (value: string) => {
    setColorInput(value);
    const color = parseCssColor(value);
    if (!color) {
      setError('Use HEX (#RRGGBB or #RRGGBBAA) or rgba(r, g, b, a).');
      return;
    }
    setDraft((current) => ({ ...current, [editingTheme]: formatCssColor(color) }));
    setError('');
  };

  const switchEditingTheme = (nextTheme: ThemeMode) => {
    setEditingTheme(nextTheme);
    setColorInput(draft[nextTheme]);
    setError('');
  };

  const save = async () => {
    if (error || !parseCssColor(colorInput)) return;
    setSaving(true);
    try {
      await saveAccentColors(draft);
      setOpen(false);
    } catch (saveError) {
      setError(saveError instanceof Error ? saveError.message : 'Could not save the accent color.');
    } finally {
      setSaving(false);
    }
  };

  return (
    <div ref={rootRef} className="relative mr-1">
      <button
        type="button"
        onClick={() => open ? setOpen(false) : beginEditing()}
        className="flex h-7 w-7 items-center justify-center rounded border border-coden-border bg-coden-bg hover:bg-coden-surface focus-visible:border-coden-accent focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-coden-accent/40"
        title="Choose global accent color"
        aria-label="Choose global accent color"
        aria-expanded={open}
      >
        <span className="h-3.5 w-3.5 rounded-full border border-coden-text/20 shadow-sm" style={{ backgroundColor: normalizedSaved[theme] }} />
      </button>

      {open && (
        <div role="dialog" aria-label="Accent color settings" className="absolute right-0 top-full z-[200] mt-2 w-80 select-text rounded-lg border border-coden-border bg-coden-surface p-4 text-coden-text shadow-2xl">
          <div className="flex items-start justify-between gap-3">
            <div>
              <div className="text-sm font-bold">Accent color</div>
              <div className="mt-0.5 text-[10px] leading-relaxed text-coden-muted">Saved separately for dark and light mode.</div>
            </div>
            <button type="button" onClick={() => setOpen(false)} className="flex h-6 w-6 items-center justify-center rounded text-coden-muted hover:bg-coden-inner hover:text-coden-text" aria-label="Cancel color changes">×</button>
          </div>

          <div className="mt-3 grid grid-cols-2 rounded-md border border-coden-border bg-coden-bg p-1">
            {(['dark', 'light'] as ThemeMode[]).map((mode) => (
              <button key={mode} type="button" onClick={() => switchEditingTheme(mode)} className={`rounded px-3 py-1.5 text-[11px] font-bold capitalize transition-colors ${editingTheme === mode ? 'bg-coden-accent text-coden-accentContrast' : 'text-coden-muted hover:text-coden-text'}`}>
                {mode}
              </button>
            ))}
          </div>

          <div className="mt-3 grid grid-cols-[72px_minmax(0,1fr)] gap-3">
            <label className="group relative flex h-[72px] cursor-pointer items-center justify-center overflow-hidden rounded-md border border-coden-border bg-coden-bg" title="Open the color palette">
              <span className="h-11 w-11 rounded-full border-4 border-coden-surface shadow" style={{ backgroundColor: selectedColor }} />
              <input
                type="color"
                value={colorToHex(parsed)}
                onChange={(event) => {
                  const rgb = parseCssColor(event.target.value)!;
                  applyColor({ ...rgb, a: parsed.a });
                }}
                className="absolute inset-0 cursor-pointer opacity-0"
                aria-label={`Choose ${editingTheme} accent from color palette`}
              />
            </label>
            <div>
              <label className="text-[10px] font-bold uppercase tracking-wider text-coden-muted" htmlFor="accent-color-value">HEX or RGBA</label>
              <input
                id="accent-color-value"
                value={colorInput}
                onChange={(event) => changeInput(event.target.value)}
                spellCheck={false}
                className={`mt-1 h-8 w-full rounded border bg-coden-bg px-2 font-mono text-[11px] outline-none ${error ? 'border-rose-500' : 'border-coden-border focus:border-coden-accent'}`}
              />
              <div className="mt-2 flex items-center gap-2">
                <span className="w-11 text-[10px] text-coden-muted">Alpha</span>
                <input
                  type="range"
                  min="0"
                  max="100"
                  value={Math.round(parsed.a * 100)}
                  onChange={(event) => applyColor({ ...parsed, a: Number(event.target.value) / 100 })}
                  className="min-w-0 flex-1 accent-[var(--coden-accent)]"
                  aria-label="Accent opacity"
                />
                <span className="w-8 text-right font-mono text-[10px] text-coden-muted">{Math.round(parsed.a * 100)}%</span>
              </div>
            </div>
          </div>

          <div className="mt-3">
            <div className="mb-1.5 text-[10px] font-bold uppercase tracking-wider text-coden-muted">Palette</div>
            <div className="grid grid-cols-12 gap-1">
              {ACCENT_PRESETS.map((preset) => (
                <button key={preset} type="button" onClick={() => applyColor({ ...parseCssColor(preset)!, a: parsed.a })} className="h-5 rounded-sm border border-coden-text/15 transition hover:scale-110" style={{ backgroundColor: preset }} title={preset} aria-label={`Use ${preset}`} />
              ))}
            </div>
          </div>

          <div className="mt-3 grid grid-cols-[1fr_auto] items-center gap-3 rounded-md border border-coden-border bg-coden-bg p-2.5">
            <div>
              <div className="text-[10px] font-bold uppercase tracking-wider text-coden-muted">Contrast</div>
              <div className={`mt-0.5 text-xs font-bold ${contrast >= 3 ? 'text-emerald-400' : 'text-amber-400'}`}>{contrast.toFixed(2)}:1 · {contrastTone}</div>
              <div className="mt-0.5 text-[9px] text-coden-muted">Against the {editingTheme} background</div>
            </div>
            <div className="flex h-11 w-20 items-center justify-center rounded font-bold shadow-inner" style={{ backgroundColor: selectedColor, color: previewText }}>Aa</div>
          </div>

          {error && <div className="mt-2 text-[10px] leading-relaxed text-rose-400">{error}</div>}

          <div className="mt-4 flex items-center justify-between gap-2">
            <button
              type="button"
              onClick={() => applyColor(parseCssColor(DEFAULT_ACCENT_COLORS[editingTheme])!)}
              className="rounded border border-coden-border px-2.5 py-1.5 text-[10px] font-bold text-coden-muted hover:bg-coden-inner hover:text-coden-text"
            >
              Reset to Teal
            </button>
            <div className="flex items-center gap-2">
              <button type="button" onClick={() => setOpen(false)} className="rounded border border-coden-border px-3 py-1.5 text-[10px] font-bold text-coden-muted hover:bg-coden-inner hover:text-coden-text">Cancel</button>
              <button type="button" onClick={() => void save()} disabled={Boolean(error) || saving} className="rounded bg-coden-accent px-3 py-1.5 text-[10px] font-bold text-coden-accentContrast hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-50">{saving ? 'Saving…' : 'Save'}</button>
            </div>
          </div>
        </div>
      )}
    </div>
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
  const difficultyDisplay = detail
    ? `${detail.difficulty_label}${
      detail.elo_rating !== null
        ? ` · Elo ${Math.round(detail.elo_rating)}`
        : detail.difficulty_estimate !== null
          ? ` · Estimated ${detail.difficulty_estimate}/10`
          : ''
    }`
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
