import { useEffect } from 'react';
import { useAppStore } from '../store/useAppStore';
import { useStepPlayer } from '../hooks/useStepPlayer';
import { useKeyboardShortcuts } from '../hooks/useKeyboardShortcuts';
import { ChallengeList } from './ChallengeList';
import { ChallengeView } from './ChallengeView';


/**
 * AppShell — the top-level layout. A header, a left rail with
 * the challenge list, and the main challenge view on the right.
 */
export function AppShell() {
  const loadChallenges = useAppStore((s) => s.loadChallenges);
  const loadProgress = useAppStore((s) => s.loadProgress);
  const challenges = useAppStore((s) => s.challenges);

  useEffect(() => {
    loadChallenges();
    loadProgress();
  }, [loadChallenges, loadProgress]);

  useStepPlayer();
  useKeyboardShortcuts();

  return (
    <div className="h-full flex flex-col bg-coden-bg text-coden-text">
      {/* Header */}
      <header className="h-12 flex items-center justify-between px-4 border-b border-coden-border bg-coden-surface shrink-0">
        <div className="flex items-center gap-3">
          <span className="text-xl">⚙️</span>
          <h1 className="text-lg font-semibold tracking-tight">cOde(n)</h1>
          <span className="text-xs text-coden-muted font-mono">web rebuild</span>
        </div>
        <div className="text-xs text-coden-muted">
          {challenges.length > 0 && `${challenges.length} challenges`}
        </div>
      </header>

      {/* Main layout */}
      <div className="flex-1 flex overflow-hidden">
        <aside className="w-64 border-r border-coden-border bg-coden-surface shrink-0 overflow-y-auto">
          <ChallengeList />
        </aside>
        <main className="flex-1 overflow-hidden">
          <ChallengeView />
        </main>
      </div>
    </div>
  );
}
