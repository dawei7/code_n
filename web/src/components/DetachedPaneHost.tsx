/**
 * DetachedPaneHost.tsx — the renderer for `?view=pane&paneId=...&tabId=...`.
 *
 * This is what shows in a BrowserWindow that the main window
 * opened via `electronAPI.popOutPane(paneId, tabId)`. It mounts
 * a minimal chrome (the tab's label + a "Reattach" button that
 * closes the window) and renders the tab's content. Cross-window
 * state sync happens via BroadcastChannel (see lib/broadcastSync.ts).
 *
 * The host is intentionally decoupled from the layout store: the
 * detached window doesn't know about the main window's tree, and
 * the main window doesn't know about the detached window's UI
 * beyond "this paneId is detached". Each side renders its own
 * pane for the same tabId.
 */
import { useEffect, useMemo } from 'react';
import { mountBroadcastSync } from '../lib/broadcastSync';
import { PaneContent } from './layout/PaneContent';
import { getTab } from './layout/tabs/registry';


export function DetachedPaneHost() {
  // Read paneId + tabId from the URL.
  const params = useMemo(
    () => new URLSearchParams(window.location.search),
    [],
  );
  const paneId = params.get('paneId') ?? 'detached';
  const tabId = params.get('tabId') ?? 'description';

  // Mount the broadcast sync so this window receives state from
  // the main window and can save (e.g. editor) back to the server.
  useEffect(() => {
    const teardown = mountBroadcastSync();
    return teardown;
  }, []);

  const def = getTab(tabId);

  function handleReattach() {
    // Tell the main window to mark this pane as no longer detached.
    const api = window.electronAPI;
    // The IPC 'pane-window-closed' fires when this window closes;
    // the main window's handler will clear the detached flag.
    // We just need to close the window.
    if (typeof window !== 'undefined' && 'close' in window) {
      window.close();
    }
    void api; // (referenced for type narrowing)
  }

  return (
    <div className="h-full flex flex-col bg-coden-bg text-coden-text">
      <div className="h-10 flex items-center justify-between px-4 border-b border-coden-border bg-coden-surface shrink-0">
        <div className="flex items-center gap-2 text-sm">
          <span className="text-lg">⚙️</span>
          <span className="font-semibold">cOde(n)</span>
          <span className="text-xs text-coden-muted font-mono">
            detached pane · {paneId.slice(0, 8)}…
          </span>
          {def && (
            <span className="text-xs text-coden-muted font-mono">
              · {def.icon} {def.label}
            </span>
          )}
        </div>
        <button
          type="button"
          onClick={handleReattach}
          className="text-xs px-2 py-1 rounded border border-coden-border text-coden-accent hover:bg-coden-border"
          title="Close this window; the pane reappears in the main window"
        >
          ↩ Reattach
        </button>
      </div>
      <div className="flex-1 min-h-0 overflow-hidden">
        <PaneContent tabId={tabId} />
      </div>
    </div>
  );
}
