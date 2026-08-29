import { useState, useRef, useEffect } from 'react';
import { useAppStore } from '../store/useAppStore';
import { APP_THEMES, getTheme } from '../lib/themes';

export function ThemePicker() {
  const themeId = useAppStore((state) => state.themeId);
  const setThemeId = useAppStore((state) => state.setThemeId);
  const [open, setOpen] = useState(false);
  const rootRef = useRef<HTMLDivElement>(null);

  const activeTheme = getTheme(themeId);

  useEffect(() => {
    if (!open) return;
    const closeOutside = (event: PointerEvent) => {
      if (!rootRef.current?.contains(event.target as Node)) {
        setOpen(false);
      }
    };
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setOpen(false);
      }
    };
    document.addEventListener('pointerdown', closeOutside);
    window.addEventListener('keydown', closeOnEscape);
    return () => {
      document.removeEventListener('pointerdown', closeOutside);
      window.removeEventListener('keydown', closeOnEscape);
    };
  }, [open]);

  return (
    <div ref={rootRef} className="relative">
      <button
        type="button"
        onClick={() => setOpen((prev) => !prev)}
        className="flex h-7 items-center gap-1.5 rounded border border-coden-border bg-coden-bg px-2 text-xs font-medium text-coden-muted hover:bg-coden-surface hover:text-coden-text focus-visible:border-coden-accent focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-coden-accent/40 transition-colors"
        title={`Theme: ${activeTheme.name}`}
        aria-label="Choose visual theme"
        aria-expanded={open}
      >
        <span className="flex items-center -space-x-1">
          <span
            className="h-2.5 w-2.5 rounded-full border border-black/20"
            style={{ backgroundColor: activeTheme.colors.bg }}
          />
          <span
            className="h-2.5 w-2.5 rounded-full border border-black/20"
            style={{ backgroundColor: activeTheme.colors.surface }}
          />
          <span
            className="h-2.5 w-2.5 rounded-full border border-black/20"
            style={{ backgroundColor: activeTheme.colors.accent }}
          />
        </span>
        <span className="hidden sm:inline">{activeTheme.name}</span>
      </button>

      {open && (
        <div
          role="dialog"
          aria-label="Theme choices"
          className="absolute right-0 top-full z-[200] mt-2 w-80 select-none rounded-xl border border-coden-border bg-coden-surface p-4 text-coden-text shadow-2xl animate-in fade-in zoom-in-95 duration-150"
        >
          {/* Header */}
          <div className="flex items-start justify-between gap-3 border-b border-coden-border pb-3 mb-3">
            <div>
              <div className="text-sm font-bold text-coden-text flex items-center gap-1.5">
                <span>🎨</span> Visual Themes
              </div>
              <div className="mt-0.5 text-xs text-coden-muted">
                7 curated, harmonious palettes crafted for coding & reading
              </div>
            </div>
            <button
              type="button"
              onClick={() => setOpen(false)}
              className="flex h-6 w-6 items-center justify-center rounded-lg text-coden-muted hover:bg-coden-surface-elevated hover:text-coden-text transition-colors"
              aria-label="Close theme choices"
            >
              ×
            </button>
          </div>

          {/* Theme List */}
          <div className="space-y-2">
            {APP_THEMES.map((theme) => {
              const isSelected = theme.id === themeId;
              return (
                <button
                  key={theme.id}
                  type="button"
                  onClick={() => {
                    setThemeId(theme.id);
                    setOpen(false);
                  }}
                  className={`w-full text-left rounded-lg p-2.5 border transition-all ${
                    isSelected
                      ? 'border-coden-accent bg-coden-accent/10 shadow-sm ring-1 ring-coden-accent'
                      : 'border-coden-border bg-coden-surface hover:bg-coden-surface-elevated hover:border-coden-border/80'
                  }`}
                >
                  <div className="flex items-center justify-between gap-2">
                    <div className="flex items-center gap-2">
                      {/* 4-Color Swatch Preview */}
                      <div
                        className="flex items-center gap-1 p-1 rounded border shadow-inner"
                        style={{
                          backgroundColor: theme.colors.bg,
                          borderColor: theme.colors.border,
                        }}
                      >
                        <span
                          className="h-3.5 w-3.5 rounded-full"
                          style={{ backgroundColor: theme.colors.surface }}
                          title="Surface"
                        />
                        <span
                          className="h-3.5 w-3.5 rounded-full"
                          style={{ backgroundColor: theme.colors.accent }}
                          title="Accent"
                        />
                        <span
                          className="h-3.5 w-3.5 rounded-full"
                          style={{ backgroundColor: theme.colors.text }}
                          title="Text"
                        />
                      </div>

                      <div>
                        <div className="text-xs font-bold text-coden-text flex items-center gap-1.5">
                          {theme.name}
                          <span
                            className={`rounded px-1.5 py-0.2 text-[10px] font-semibold ${
                              theme.mode === 'dark'
                                ? 'bg-zinc-800 text-zinc-300'
                                : 'bg-amber-100 text-amber-900'
                            }`}
                          >
                            {theme.mode === 'dark' ? 'Dark ☾' : 'Light ☀'}
                          </span>
                        </div>
                        <div className="text-[11px] text-coden-muted leading-tight mt-0.5">
                          {theme.subtitle}
                        </div>
                      </div>
                    </div>

                    {isSelected && (
                      <span className="flex h-5 w-5 items-center justify-center rounded-full bg-coden-accent text-[11px] font-bold text-coden-accentContrast">
                        ✓
                      </span>
                    )}
                  </div>
                </button>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
