import { lazy, Suspense, useEffect } from 'react';
import { AppShell } from './components/AppShell';
import { ErrorBoundary } from './components/ErrorBoundary';
import { mountBroadcastSync } from './lib/broadcastSync';


// Both Monaco-bearing components are lazy-loaded so the main
// bundle doesn't pay the ~1.5MB Monaco cost. The main shell
// never loads Monaco unless the user opens an editor tab.
const EditorView = lazy(() =>
  import('./components/EditorView').then((m) => ({ default: m.EditorView })),
);
const DetachedPaneHost = lazy(() =>
  import('./components/DetachedPaneHost').then((m) => ({ default: m.DetachedPaneHost })),
);
// The popped-out debug window. It hosts the same DebugSurface
// as the in-window DebugTab, but reads its state from the
// shared zustand store (via mountBroadcastSync) and posts
// commands back to the main window on the coden-debug-cmd
// BroadcastChannel. See DetachedDebugHost.tsx.
const DetachedDebugHost = lazy(() =>
  import('./components/DetachedDebugHost').then((m) => ({ default: m.DetachedDebugHost })),
);


/**
 * Top-level React entry.
 *
 * Routes by URL query:
 *   - `?view=editor`     → EditorView (the legacy pop-out Monaco
 *     editor — intentionally decoupled, no BroadcastChannel sync)
 *   - `?view=pane&paneId=...&tabId=...` → DetachedPaneHost
 *     (a single tab in its own BrowserWindow; sync via channel)
 *   - `?view=debug&sessionId=...` → DetachedDebugHost
 *     (the popped-out debug window; pure view + command sender;
 *     the main window owns the WS and forwards commands)
 *   - default            → AppShell (the main window)
 *
 * The BroadcastChannel sync is mounted in AppShell,
 * DetachedPaneHost, and DetachedDebugHost, but NOT in
 * EditorView (the legacy editor stays decoupled per the plan).
 *
 * ErrorBoundary wraps everything: a render error in any
 * child surfaces as a visible red card with the message +
 * stack, instead of an invisible black-screen failure.
 */
export default function App() {
  return (
    <ErrorBoundary>
      <RoutedApp />
    </ErrorBoundary>
  );
}


function RoutedApp() {
  const params = new URLSearchParams(window.location.search);
  if (params.get('view') === 'editor') {
    return (
      <Suspense fallback={<div className="h-full flex items-center justify-center text-coden-muted">Loading editor…</div>}>
        <EditorView />
      </Suspense>
    );
  }
  if (params.get('view') === 'pane') {
    return (
      <Suspense fallback={<div className="h-full flex items-center justify-center text-coden-muted">Loading…</div>}>
        <DetachedPaneHost />
      </Suspense>
    );
  }
  if (params.get('view') === 'debug') {
    return (
      <Suspense fallback={<div className="h-full flex items-center justify-center text-coden-muted">Loading debug…</div>}>
        <DetachedDebugHost />
      </Suspense>
    );
  }
  // Default: main shell. Mount the broadcast sync once.
  return <AppWithSync />;
}


function AppWithSync() {
  useEffect(() => {
    const teardown = mountBroadcastSync();
    return teardown;
  }, []);
  return <AppShell />;
}
