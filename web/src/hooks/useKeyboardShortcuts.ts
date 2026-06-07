/**
 * useKeyboardShortcuts — global key handler for the app.
 *
 * Wired up at the AppShell level. Skips events that originate
 * inside Monaco's textarea so the editor keeps its own shortcuts
 * (cut/copy/paste, multi-cursor, etc.) intact.
 */
import { useEffect } from 'react';
import { useAppStore } from '../store/useAppStore';


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
