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
  neetcode_arrays: '📊',
  neetcode_two_pointers: '👉👈',
  neetcode_sliding_window: '🪟',
  neetcode_stack: '🥞',
  neetcode_binary_search: '🔍',
  neetcode_linked_list: '🔗',
  neetcode_trees: '🌳',
  neetcode_heap: '🏔️',
  neetcode_backtracking: '🌀',
  neetcode_tries: '🌲',
  neetcode_graphs: '🕸️',
  neetcode_advanced_graphs: '🚀',
  neetcode_dp1: '📈',
  neetcode_dp2: '📊',
  neetcode_greedy: '💰',
  neetcode_intervals: '📅',
  neetcode_math: '🔢',
  neetcode_bit: '💾',
};

export function CareerPathTab({ onSelectCodenTab }: CareerPathTabProps) {
  const challenges = useAppStore((s) => s.challenges);
  const selectChallenge = useAppStore((s) => s.selectChallenge);
  const completed = useAppStore((s) => s.progress?.completed ?? []);
  const activeSet = useAppStore((s) => s.activeSet);

  // Helper to map category IDs to challenges
  const getCategoryChallenges = (catId: string) => {
    return challenges.filter((c) => c.category === catId);
  };

  // Navigation click handler
  const handleNodeClick = (challengeId: string) => {
    selectChallenge(challengeId);
    onSelectCodenTab();
  };

  return (
    <div className="space-y-4 flex flex-col h-full overflow-hidden">
      {/* Roadmap Header Dashboard */}
      <div className="flex items-center justify-between bg-[#0f172a] border border-slate-800/80 p-4 rounded-2xl shrink-0">
        <div className="flex items-center gap-3">
          <span className="text-xl">🗺️</span>
          <div>
            <h3 className="text-sm font-bold text-white leading-tight">
              {activeSet === 'neetcode' ? 'NeetCode 250 Interview Roadmap' : 'GeeksforGeeks Roadmap'}
            </h3>
            <p className="text-[11px] text-slate-400 font-mono">Solve challenges sequentially within each topic to progress</p>
          </div>
        </div>
      </div>

      {/* Categories Roadmap List */}
      <div className="flex-grow overflow-y-auto pr-1 space-y-4 scrollbar-thin">
        {CATEGORY_NODES.map((node) => {
          const catChallenges = getCategoryChallenges(node.id);
          const total = catChallenges.length;
          if (total === 0) return null; // Hide categories with no active challenges

          const verifiedCount = catChallenges.filter((c) => completed.includes(c.id)).length;
          const progressPercent = total > 0 ? (verifiedCount / total) * 100 : 0;
          const icon = CATEGORY_ICONS[node.id] || '📁';

          return (
            <div
              key={node.id}
              className="p-4 bg-[#0f172a] border border-slate-800/80 rounded-2xl flex flex-col justify-between transition-all"
            >
              {/* Category Header */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div className="flex items-center gap-2">
                  <span className="text-base">{icon}</span>
                  <span className="text-sm font-bold text-white tracking-wide">
                    {node.label}
                  </span>
                </div>
                <div className="flex items-center gap-3">
                  {/* Small progress bar */}
                  <div className="w-32 h-1.5 bg-slate-950 rounded-full overflow-hidden border border-slate-900 shrink-0">
                    <div 
                      className={`h-full transition-all duration-300 ${
                        verifiedCount === total ? 'bg-emerald-400' : 'bg-indigo-500'
                      }`}
                      style={{ width: `${progressPercent}%` }}
                    />
                  </div>
                  <span className="text-[10px] text-slate-400 font-mono shrink-0">
                    {verifiedCount} / {total} solved
                  </span>
                </div>
              </div>

              {/* Challenges Flow */}
              <div className="flex flex-wrap items-center gap-2 mt-4">
                {catChallenges.map((c, idx) => {
                  const isDone = completed.includes(c.id);
                  const isLocked = activeSet === 'neetcode' && idx > 0 && !completed.includes(catChallenges[idx - 1].id);

                  let cardStyle = "bg-slate-900/40 border-slate-800 text-slate-300 hover:border-slate-700 hover:bg-slate-900/60";
                  let statusEmoji = "•";

                  if (isLocked) {
                    cardStyle = "bg-slate-950/20 border-slate-900 opacity-40 cursor-not-allowed text-slate-500";
                    statusEmoji = "🔒";
                  } else if (isDone) {
                    cardStyle = "bg-emerald-950/15 border-emerald-500/35 hover:bg-emerald-950/25 text-emerald-100";
                    statusEmoji = "✅";
                  } else {
                    cardStyle = "bg-indigo-950/15 border-indigo-650/40 hover:border-indigo-500 hover:bg-indigo-950/25 text-white";
                    statusEmoji = "▶ Solve";
                  }

                  // Determine difficulty color label
                  let diffLabel = "Easy";
                  let diffColor = "text-emerald-400";
                  if (c.difficulty <= 3) {
                    diffLabel = "Easy";
                    diffColor = "text-emerald-400";
                  } else if (c.difficulty <= 7) {
                    diffLabel = "Medium";
                    diffColor = "text-amber-400";
                  } else {
                    diffLabel = "Hard";
                    diffColor = "text-rose-500";
                  }

                  return (
                    <div key={c.id} className="flex items-center gap-2 shrink-0">
                      {idx > 0 && (
                        <span className="text-slate-700 font-mono text-xs select-none">➔</span>
                      )}
                      <button
                        type="button"
                        onClick={() => !isLocked && handleNodeClick(c.id)}
                        disabled={isLocked}
                        className={`px-3 py-2 rounded-xl border flex flex-col text-left transition-all text-xs max-w-[200px] ${cardStyle}`}
                      >
                        <div className="flex items-center justify-between gap-2 w-full min-w-0">
                          <span className="font-bold truncate leading-tight max-w-[140px] block" title={c.name}>
                            {c.name}
                          </span>
                          <span className="text-[10px] shrink-0">{statusEmoji}</span>
                        </div>
                        <div className="flex items-center justify-between gap-3 mt-1.5 w-full text-[9px] font-mono text-slate-500">
                          <span className={diffColor}>{diffLabel}</span>
                          {c.leetcode_url && !isLocked && (
                            <a
                              href={c.leetcode_url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-slate-500 hover:text-indigo-400 text-[10px]"
                              onClick={(e) => e.stopPropagation()}
                              title="Open on LeetCode"
                            >
                              🔗
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
