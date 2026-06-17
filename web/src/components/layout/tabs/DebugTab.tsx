/**
 * DebugTab — the in-window debug surface. A thin wrapper that
 * renders the shared ``DebugSurface`` component.
 *
 * The actual debug-surface JSX (status bar, source with
 * clickable gutter, locals, controls) lives in
 * ``web/src/components/DebugSurface.tsx`` so it can be reused
 * in the popped-out debug window (``DetachedDebugHost``).
 *
 * The hook that owns the WS is mounted in ``AppShell``; the
 * detached window talks to the same hook indirectly through
 * the ``coden-debug-cmd`` BroadcastChannel.
 */
import { DebugSurface } from '../../DebugSurface';


/** Stable component identity so React doesn't remount on re-render. */
export function DebugTab() {
  return <DebugSurface commandTarget="local" />;
}
