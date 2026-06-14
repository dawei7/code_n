/**
 * UpdateToast — floating bottom-right pill that surfaces
 * auto-update progress and the "Restart to install" action.
 *
 * Renders nothing in dev mode (no `window.electronAPI`). Only
 * shown when:
 *   - state === 'available'   (download is about to start)
 *   - state === 'downloading' (progress bar)
 *   - state === 'downloaded'  (Restart button)
 *
 * Hidden for: 'idle', 'checking' (too brief to be useful),
 * 'not-available' (no need to nag), 'error' (logged, surfaced
 * via the "Check for updates" button tooltip).
 */

import { useUpdater } from '../hooks/useUpdater';


function formatBytes(n: number | undefined): string {
  if (n == null) return '';
  if (n < 1024) return `${n} B`;
  if (n < 1024 * 1024) return `${(n / 1024).toFixed(0)} KB`;
  return `${(n / (1024 * 1024)).toFixed(1)} MB`;
}


export function UpdateToast() {
  const { state, install } = useUpdater();
  const s = state.status;
  const version = s.version ? ` v${s.version}` : '';
  const isElectron = typeof window !== 'undefined' && !!window.electronAPI;
  if (!isElectron) return null;

  // --- Available: a newer version is found, about to start
  // downloading (autoDownload=true means this is usually brief). ---
  if (s.state === 'available') {
    return (
      <div
        role="status"
        className="fixed bottom-4 right-4 z-50 max-w-sm bg-coden-surface border border-coden-accent text-coden-text rounded-lg shadow-lg px-4 py-3 text-sm"
      >
        <div className="flex items-center gap-2">
          <span aria-hidden>↓</span>
          <div>
            <div className="font-semibold">Update available{version}</div>
            <div className="text-xs text-coden-muted">Downloading in the background…</div>
          </div>
        </div>
      </div>
    );
  }

  // --- Downloading: progress bar. ---
  if (s.state === 'downloading') {
    const pct = Math.round((s.progress ?? 0) * 100);
    return (
      <div
        role="status"
        className="fixed bottom-4 right-4 z-50 max-w-sm bg-coden-surface border border-coden-accent text-coden-text rounded-lg shadow-lg px-4 py-3 text-sm"
      >
        <div className="flex items-center justify-between gap-2 mb-1">
          <span className="font-semibold">Downloading update{version}…</span>
          <span className="text-xs font-mono text-coden-muted">
            {pct}%
            {s.total != null ? ` (${formatBytes(s.transferred)} / ${formatBytes(s.total)})` : ''}
          </span>
        </div>
        <div className="h-1.5 bg-coden-border rounded overflow-hidden">
          <div
            className="h-full bg-coden-accent transition-all"
            style={{ width: `${pct}%` }}
          />
        </div>
      </div>
    );
  }

  // --- Downloaded: ask the user to restart. ---
  if (s.state === 'downloaded') {
    return (
      <div
        role="status"
        className="fixed bottom-4 right-4 z-50 max-w-sm bg-emerald-900/40 border border-emerald-600 text-emerald-100 rounded-lg shadow-lg px-4 py-3 text-sm"
      >
        <div className="flex items-center gap-3">
          <div className="flex-1">
            <div className="font-semibold">Update{version} ready</div>
            <div className="text-xs text-emerald-200/80">
              Restart cOde(n) to install.
            </div>
          </div>
          <button
            type="button"
            onClick={install}
            className="px-3 py-1.5 text-sm rounded bg-emerald-600 text-white hover:bg-emerald-500 font-medium"
          >
            Restart
          </button>
        </div>
      </div>
    );
  }

  // Everything else (idle / checking / not-available / error) is
  // surfaced via the "Check for updates" button's title-tooltip,
  // not as a toast.
  return null;
}
