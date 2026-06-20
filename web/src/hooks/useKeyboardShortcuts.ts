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

      switch (e.key) {
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
