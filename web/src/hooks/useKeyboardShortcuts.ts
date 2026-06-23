/**
 * useKeyboardShortcuts — global key handler for the app.
 *
 * Wired up at the AppShell level. F5 runs the current challenge
 * unless focus is inside Monaco, where the editor owns keyboard
 * input.
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
      if (isInsideMonaco(e.target)) return;

      const s = useAppStore.getState();

      switch (e.key) {
        case 'F5':
          e.preventDefault();
          void s.run();
          break;
      }
    }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);
}
