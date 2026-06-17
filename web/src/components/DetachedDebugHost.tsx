/**
 * DetachedDebugHost — the renderer for ``?view=debug&sessionId=...``.
 *
 * Lives in its own BrowserWindow. The main window owns the WS;
 * the pop-out is a pure view of the shared zustand store and a
 * pure sender of commands (over the ``coden-debug-cmd``
 * BroadcastChannel). When the user clicks Step / Continue / Stop
 * in this window, the action is posted to the channel and the
 * main window's listener forwards it to the WS.
 *
 * Cross-window state sync happens via the existing
 * ``mountBroadcastSync`` infrastructure; the bulk snapshot
 * carries ``breakpoints`` and the full debug surface state
 * (status, current line, locals, etc.) so this window always
 * shows what's in the main window's store.
 */
import { useEffect, useMemo } from 'react';
import { mountBroadcastSync } from '../lib/broadcastSync';
import { DEBUG_CMD_CHANNEL, type DebugCommand } from '../lib/debugCommands';
import { DebugSurface } from './DebugSurface';


export function DetachedDebugHost() {
  // Read the sessionId from the URL so we can show it in the
  // header. The actual session lifecycle lives in the main
  // window; this is just a label.
  const sessionId = useMemo(
    () => new URLSearchParams(window.location.search).get('sessionId') ?? '',
    [],
  );

  // Mount the snapshot broadcast sync so this window receives
  // the main window's debug state. (The existing
  // mountBroadcastSync is symmetric; both windows call it.)
  useEffect(() => {
    const teardown = mountBroadcastSync();
    return teardown;
  }, []);

  // On mount: tell the main window "I'm alive" so it can
  // decide whether to re-trigger popOutDebug() on the next
  // stopped event (auto-reopen UX). The main window already
  // has the pop-out registered in Electron's detachedWindows
  // map, so this is purely informational.
  //
  // On unmount: tell the main window "the user closed me
  // manually" so it doesn't try to call close() on a
  // destroyed window.
  useEffect(() => {
    if (typeof BroadcastChannel === 'undefined') return;
    const ch = new BroadcastChannel(DEBUG_CMD_CHANNEL);
    ch.postMessage({ kind: 'popout_ready' } satisfies DebugCommand);
    return () => {
      ch.postMessage({ kind: 'popout_closed' } satisfies DebugCommand);
      ch.close();
    };
  }, []);

  return (
    <div className="h-full flex flex-col bg-coden-bg text-coden-text">
      <div className="h-10 flex items-center justify-between px-4 border-b border-coden-border bg-coden-surface shrink-0">
        <div className="flex items-center gap-2 text-sm">
          <span className="text-lg">⚙️</span>
          <span className="font-semibold">cOde(n)</span>
          <span className="text-xs text-coden-muted font-mono">
            🐞 debug session
            {sessionId ? ` · ${sessionId.slice(0, 8)}…` : ''}
          </span>
        </div>
        <button
          type="button"
          onClick={() => window.close()}
          className="text-xs px-2 py-1 rounded border border-coden-border text-coden-accent hover:bg-coden-border"
          title="Close this window. The debug session keeps running in the main window; the next breakpoint will reopen the pop-out."
        >
          ✕ Close
        </button>
      </div>
      <div className="flex-1 min-h-0 overflow-hidden">
        <DebugSurface commandTarget="remote" />
      </div>
    </div>
  );
}
