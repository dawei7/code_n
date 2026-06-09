import { lazy, Suspense, useEffect } from 'react';
import { AppShell } from './components/AppShell';
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


/**
 * Top-level React entry.
 *
 * Routes by URL query:
 *   - `?view=editor`     → EditorView (the legacy pop-out Monaco
 *     editor — intentionally decoupled, no BroadcastChannel sync)
 *   - `?view=pane&paneId=...&tabId=...` → DetachedPaneHost
 *     (a single tab in its own BrowserWindow; sync via channel)
 *   - default            → AppShell (the main window)
 *
 * The BroadcastChannel sync is mounted in AppShell and
 * DetachedPaneHost, but NOT in EditorView (the legacy editor
 * stays decoupled per the plan).
 */
export default function App() {
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
