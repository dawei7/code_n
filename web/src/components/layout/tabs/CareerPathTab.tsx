import { useEffect, useRef } from 'react';
import { useAppStore } from '../../../store/useAppStore';

interface CareerPathTabProps {
  onSelectCodenTab: () => void;
}

interface CategoryNode {
  id: string;
  label: string;
}

const CATEGORY_NODES: CategoryNode[] = [
  { id: 'neetcode_arrays', label: 'Arrays & Hashing' },
  { id: 'neetcode_two_pointers', label: 'Two Pointers' },
  { id: 'neetcode_sliding_window', label: 'Sliding Window' },
  { id: 'neetcode_stack', label: 'Stack' },
  { id: 'neetcode_binary_search', label: 'Binary Search' },
  { id: 'neetcode_linked_list', label: 'Linked List' },
  { id: 'neetcode_trees', label: 'Trees' },
  { id: 'neetcode_heap', label: 'Heap / Priority Queue' },
  { id: 'neetcode_backtracking', label: 'Backtracking' },
  { id: 'neetcode_tries', label: 'Tries' },
  { id: 'neetcode_graphs', label: 'Graphs' },
  { id: 'neetcode_advanced_graphs', label: 'Advanced Graphs' },
  { id: 'neetcode_dp1', label: '1-D Dynamic Programming' },
  { id: 'neetcode_dp2', label: '2-D Dynamic Programming' },
  { id: 'neetcode_greedy', label: 'Greedy' },
  { id: 'neetcode_intervals', label: 'Intervals' },
  { id: 'neetcode_math', label: 'Math & Geometry' },
  { id: 'neetcode_bit', label: 'Bit Manipulation' },
];

const CATEGORY_ICONS: Record<string, string> = {
  neetcode_arrays: '[]',
  neetcode_two_pointers: '<>',
  neetcode_sliding_window: '##',
  neetcode_stack: '::',
  neetcode_binary_search: '/2',
  neetcode_linked_list: '->',
  neetcode_trees: 'T',
  neetcode_heap: '^',
  neetcode_backtracking: '*',
  neetcode_tries: 'Tr',
  neetcode_graphs: 'G',
  neetcode_advanced_graphs: 'G+',
  neetcode_dp1: 'D1',
  neetcode_dp2: 'D2',
  neetcode_greedy: '$',
  neetcode_intervals: '..',
  neetcode_math: '#',
  neetcode_bit: '01',
};

export function CareerPathTab({ onSelectCodenTab }: CareerPathTabProps) {
  const challenges = useAppStore((s) => s.challenges);
  const selectChallenge = useAppStore((s) => s.selectChallenge);
  const currentChallengeId = useAppStore((s) => s.currentDetail?.id ?? null);
  const completed = useAppStore((s) => s.progress?.completed ?? []);
  const activeSet = useAppStore((s) => s.activeSet);
  const selectedNodeRef = useRef<HTMLButtonElement | null>(null);

  useEffect(() => {
    if (!currentChallengeId) return;
    const timeout = window.setTimeout(() => {
      selectedNodeRef.current?.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
        inline: 'center',
      });
    }, 50);
    return () => window.clearTimeout(timeout);
  }, [currentChallengeId]);

  const getCategoryChallenges = (catId: string) => {
    return challenges.filter((c) => c.category === catId);
  };

  const handleNodeClick = (challengeId: string) => {
    selectChallenge(challengeId);
    onSelectCodenTab();
  };

  return (
    <div className="space-y-4 flex flex-col h-full overflow-hidden">
      <div className="flex items-center justify-between bg-coden-surface border border-slate-300 dark:border-coden-border p-4 rounded-lg shrink-0 shadow-sm">
        <div className="flex items-center gap-3 min-w-0">
          <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded border border-slate-300 bg-slate-50 text-sky-700 dark:border-coden-border dark:bg-coden-bg dark:text-coden-accent font-mono text-xs">
            MAP
          </span>
          <div className="min-w-0">
            <h3 className="text-sm font-bold text-coden-text leading-tight truncate">
              {activeSet === 'neetcode' ? 'NeetCode 250 Interview Roadmap' : 'GeeksforGeeks Roadmap'}
            </h3>
            <p className="text-[11px] text-slate-600 dark:text-coden-muted font-mono truncate">
              Solve challenges sequentially within each topic to progress
            </p>
          </div>
        </div>
      </div>

      <div className="flex-grow overflow-y-auto pr-1 space-y-4 scrollbar-thin">
        {CATEGORY_NODES.map((node) => {
          const catChallenges = getCategoryChallenges(node.id);
          const total = catChallenges.length;
          if (total === 0) return null;

          const verifiedCount = catChallenges.filter((c) => completed.includes(c.id)).length;
          const progressPercent = total > 0 ? (verifiedCount / total) * 100 : 0;
          const icon = CATEGORY_ICONS[node.id] || '[]';

          return (
            <div
              key={node.id}
              className="p-4 bg-coden-surface border border-slate-300 dark:border-coden-border rounded-lg flex flex-col justify-between transition-all shadow-sm"
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-200 dark:border-coden-border pb-3">
                <div className="flex items-center gap-2 min-w-0">
                  <span className="flex h-7 min-w-7 items-center justify-center rounded border border-slate-300 bg-slate-50 px-1.5 font-mono text-[10px] text-sky-700 dark:border-coden-border dark:bg-coden-bg dark:text-coden-accent">
                    {icon}
                  </span>
                  <span className="text-sm font-bold text-coden-text tracking-wide truncate">
                    {node.label}
                  </span>
                </div>
                <div className="flex items-center gap-3 shrink-0">
                  <div className="w-32 h-1.5 bg-slate-100 dark:bg-coden-bg rounded-full overflow-hidden border border-slate-300 dark:border-coden-border shrink-0">
                    <div
                      className={`h-full transition-all duration-300 ${
                        verifiedCount === total ? 'bg-emerald-500' : 'bg-coden-accent'
                      }`}
                      style={{ width: `${progressPercent}%` }}
                    />
                  </div>
                  <span className="text-[10px] text-slate-600 dark:text-coden-muted font-mono shrink-0">
                    {verifiedCount} / {total} solved
                  </span>
                </div>
              </div>

              <div className="flex flex-wrap items-center gap-2 mt-4">
                {catChallenges.map((challenge, idx) => {
                  const isSelected = challenge.id === currentChallengeId;
                  const isDone = completed.includes(challenge.id);
                  const isLocked =
                    activeSet === 'neetcode' &&
                    idx > 0 &&
                    !completed.includes(catChallenges[idx - 1].id);

                  let cardStyle =
                    'bg-white border-slate-300 text-slate-950 hover:border-sky-500 hover:bg-sky-50 dark:bg-coden-inner dark:border-coden-border dark:text-coden-text dark:hover:border-coden-accent dark:hover:bg-coden-surface';
                  let statusLabel = '';

                  if (isLocked) {
                    cardStyle =
                      'bg-slate-50 border-slate-300 cursor-not-allowed text-slate-600 dark:bg-coden-bg dark:border-coden-border dark:text-coden-muted dark:opacity-80';
                    statusLabel = 'locked';
                  } else if (isDone) {
                    cardStyle =
                      'bg-emerald-50 border-emerald-300 hover:border-emerald-400 hover:bg-emerald-100 text-slate-950 dark:bg-emerald-950/35 dark:border-emerald-800/80 dark:hover:border-emerald-600 dark:hover:bg-emerald-950/50 dark:text-coden-text';
                    statusLabel = 'done';
                  } else {
                    cardStyle =
                      'bg-white border-slate-300 hover:border-sky-500 hover:bg-sky-50 text-slate-950 dark:bg-coden-inner dark:border-coden-border dark:hover:border-coden-accent dark:hover:bg-coden-surface dark:text-coden-text';
                    statusLabel = 'solve';
                  }

                  let diffLabel = 'Easy';
                  let diffColor = 'text-emerald-600 dark:text-emerald-500';
                  if (challenge.difficulty <= 3) {
                    diffLabel = 'Easy';
                    diffColor = 'text-emerald-600 dark:text-emerald-500';
                  } else if (challenge.difficulty <= 7) {
                    diffLabel = 'Medium';
                    diffColor = 'text-amber-600 dark:text-amber-500';
                  } else {
                    diffLabel = 'Hard';
                    diffColor = 'text-rose-600 dark:text-rose-500';
                  }

                  return (
                    <div key={challenge.id} className="flex items-center gap-2 shrink-0">
                      {idx > 0 && (
                        <span className="text-slate-600 dark:text-coden-muted/60 font-mono text-xs select-none">
                          -&gt;
                        </span>
                      )}
                      <button
                        ref={isSelected ? selectedNodeRef : undefined}
                        type="button"
                        onClick={() => !isLocked && handleNodeClick(challenge.id)}
                        disabled={isLocked}
                        className={`px-3 py-2 rounded-lg border flex flex-col text-left transition-all text-xs max-w-[200px] disabled:opacity-100 ${
                          isSelected ? 'ring-2 ring-coden-accent ring-offset-2 ring-offset-coden-surface' : ''
                        } ${cardStyle}`}
                      >
                        <div className="flex items-center justify-between gap-2 w-full min-w-0">
                          <span
                            className="font-bold truncate leading-tight max-w-[140px] block"
                            title={challenge.name}
                          >
                            {challenge.name}
                          </span>
                          <span className="text-[9px] uppercase tracking-wide text-slate-500 dark:text-coden-muted shrink-0">
                            {statusLabel}
                          </span>
                        </div>
                        <div className="flex items-center justify-between gap-3 mt-1.5 w-full text-[9px] font-mono text-slate-600 dark:text-coden-muted">
                          <span className={diffColor}>{diffLabel}</span>
                          {challenge.leetcode_url && !isLocked && (
                            <a
                              href={challenge.leetcode_url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-slate-500 hover:text-sky-700 dark:text-coden-muted dark:hover:text-coden-accent text-[10px]"
                              onClick={(e) => e.stopPropagation()}
                              title="Open on LeetCode"
                            >
                              ↗
                            </a>
                          )}
                        </div>
                      </button>
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
