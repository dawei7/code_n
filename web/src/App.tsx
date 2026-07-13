import { useEffect } from 'react';
import { AppShell } from './components/AppShell';
import { ErrorBoundary } from './components/ErrorBoundary';
import { mountBroadcastSync } from './lib/broadcastSync';


/**
 * Top-level React entry.
 *
 * The v0.9.0 pivot removed all detached windows (the editor
 * pop-out, the debug pop-out, the detached-pane host). The
 * app is now a single window — the main AppShell. The
 * BroadcastChannel sync is still mounted (dormant) so the
 * architecture isn't ripped out, in case a future pop-out
 * surface ever comes back.
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
  // Single window — no URL routing.
  return <AppWithSync />;
}


function AppWithSync() {
  useEffect(() => {
    const teardown = mountBroadcastSync();
    return teardown;
  }, []);
  return <AppShell />;
}
