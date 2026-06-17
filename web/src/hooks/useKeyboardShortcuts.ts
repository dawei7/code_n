/**
 * useKeyboardShortcuts — global key handler for the app.
 *
 * Wired up at the AppShell level. The v0.9.0 pivot removed
 * the in-app editor + step player, so the shortcut set is
 * much smaller:
 *   - Ctrl/Cmd+Alt+Arrow: move the active tab to the next/prev
 *     pane (the layout-management power shortcut).
 *   - R (or Ctrl/Cmd+R ignored to avoid browser refresh):
 *     Run the challenge.
 *   - Ctrl/Cmd+R: browser refresh (not intercepted).
 *
 * The Monaco `isInsideMonaco` check stays as a no-op (the
 * in-app editor is gone) but is kept so the hook is
 * future-proof if a Monaco-bearing tab ever comes back.
 */
import { useEffect } from 'react';
import { useAppStore } from '../store/useAppStore';
import { useLayoutStore } from '../store/useLayoutStore';
import { allLeaves } from '../components/layout/tree-ops';


function isInsideMonaco(target: EventTarget | null): boolean {
  if (!(target instanceof HTMLElement)) return false;
  return Boolean(target.closest('.monaco-editor'));
}


export function useKeyboardShortcuts(): void {
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      // Monaco check kept for future-proofing (in case an
      // editor tab ever returns). Currently a no-op.
      if (isInsideMonaco(e.target)) return;

      const s = useAppStore.getState();
      const l = useLayoutStore.getState();

      // Ctrl/Cmd+Alt+Arrow: move the active tab of the first leaf
      // with an active tab to the next/previous leaf. Useful for
      // power users who want keyboard-only tab management.
      if ((e.ctrlKey || e.metaKey) && e.altKey && (e.key === 'ArrowRight' || e.key === 'ArrowLeft')) {
        e.preventDefault();
        const leaves = allLeaves(l.tree);
        const fromIdx = leaves.findIndex((leaf) => leaf.activeTabId);
        if (fromIdx === -1) return;
        const fromLeaf = leaves[fromIdx]!;
        if (!fromLeaf.activeTabId) return;
        const toIdx = e.key === 'ArrowRight'
          ? (fromIdx + 1) % leaves.length
          : (fromIdx - 1 + leaves.length) % leaves.length;
        const toLeaf = leaves[toIdx];
        if (!toLeaf) return;
        l.moveTab(fromLeaf.activeTabId, fromLeaf.id, toLeaf.id);
        return;
      }

      switch (e.key) {
        case 'r':
        case 'R':
          if (e.ctrlKey || e.metaKey) return;  // browser refresh
          e.preventDefault();
          void s.run();
          break;
        case 'F5':
          // F5 = Run, mirroring the in-app Run button. This is
          // the same shortcut VSCode uses for "Start Debugging",
          // so the muscle memory transfers when the player
          // opens the project in VSCode.
          e.preventDefault();
          void s.run();
          break;
      }
    }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);
}
