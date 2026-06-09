/**
 * useKeyboardShortcuts — global key handler for the app.
 *
 * Wired up at the AppShell level. Skips events that originate
 * inside Monaco's textarea so the editor keeps its own shortcuts
 * (cut/copy/paste, multi-cursor, etc.) intact.
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
      // Don't hijack keys that belong to the editor.
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
        case ' ':
          e.preventDefault();
          if (s.runResult) {
            s.isPlaying ? s.pause() : s.play();
          } else {
            s.run();
          }
          break;
        case 'ArrowRight':
          e.preventDefault();
          s.step(e.shiftKey ? 10 : 1);
          break;
        case 'ArrowLeft':
          e.preventDefault();
          s.step(e.shiftKey ? -10 : -1);
          break;
        case 'Home':
          e.preventDefault();
          s.step('first');
          break;
        case 'End':
          e.preventDefault();
          s.step('last');
          break;
        case 'r':
        case 'R':
          if (e.ctrlKey || e.metaKey) return;  // browser refresh
          e.preventDefault();
          s.run();
          break;
        case 's':
        case 'S':
          if (e.ctrlKey || e.metaKey) {
            e.preventDefault();
            s.saveSolution();
          }
          break;
        case 'Escape':
          s.pause();
          break;
      }
    }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);
}
