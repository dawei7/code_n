import { useState, useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';
import type { ChallengeSummary } from '../types/api';

const CATEGORY_DISPLAY_NAMES: Record<string, string> = {
  neetcode_arrays: 'Arrays & Hashing',
  neetcode_two_pointers: 'Two Pointers',
  neetcode_sliding_window: 'Sliding Window',
  neetcode_stack: 'Stack',
  neetcode_binary_search: 'Binary Search',
  neetcode_linked_list: 'Linked List',
  neetcode_trees: 'Trees',
  neetcode_heap: 'Heap / Priority Queue',
  neetcode_backtracking: 'Backtracking',
  neetcode_tries: 'Tries',
  neetcode_graphs: 'Graphs',
  neetcode_advanced_graphs: 'Advanced Graphs',
  neetcode_dp1: '1-D Dynamic',
  neetcode_dp2: '2-D Dynamic',
  neetcode_greedy: 'Greedy',
  neetcode_intervals: 'Intervals',
  neetcode_math: 'Math & Geometry',
  neetcode_bit: 'Bit Manipulation',
};

function formatCategory(category: string): string {
  if (category in CATEGORY_DISPLAY_NAMES) {
    return CATEGORY_DISPLAY_NAMES[category];
  }
  const cleaned = category.replace(/^(leetcode|neetcode|gfg)_/i, '');
  return cleaned.replace(/_/g, ' ');
}

function formatChallengeTitle(challenge: ChallengeSummary, activeSet: string): string {
  if (activeSet !== 'leetcode') return challenge.name;
  const match = /^lc_(\d+)$/.exec(challenge.id);
  return match ? `${match[1]}. ${challenge.name}` : challenge.name;
}

/**
 * ChallengeList — left rail with one row per challenge.
 *
 * Each row shows the human title (e.g. "Bubble Sort") as the
 * primary label, full-width. The complexity class sits in a
 * tooltip / on a second line below the title for narrow panes.
 * LeetCode rows prefix the human title with their numeric problem id;
 * other datasets keep showing only the human title. The internal machine
 * id remains available in the detail panel header and tooltip.
 * The engine runner and verifier handle every spec the
 * registry exposes, so all challenges are clickable.
 */
export function ChallengeList() {
  const challenges = useAppStore((s) => s.challenges);
  const currentId = useAppStore((s) => s.currentDetail?.id ?? null);
  const selectChallenge = useAppStore((s) => s.selectChallenge);
  const completed = useAppStore((s) => s.progress?.completed ?? []);
  const unlockedLeetcode = useAppStore((s) => s.progress?.unlocked_leetcode ?? []);
  const activeSet = useAppStore((s) => s.activeSet);

  const [searchQuery, setSearchQuery] = useState('');
  const [difficultyFilter, setDifficultyFilter] = useState('all');
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  const toggleCategory = (category: string) => {
    setExpanded((prev) => ({ ...prev, [category]: !prev[category] }));
  };

  const filteredChallenges = useMemo(() => {
    const isLockedSet = activeSet === 'neetcode';
    let baseList = isLockedSet
      ? challenges.filter(c => c.unlocked)
      : challenges;

    if (activeSet === 'leetcode' && difficultyFilter !== 'all') {
      const selectedDifficulty = Number(difficultyFilter);
      baseList = baseList.filter((challenge) => challenge.difficulty === selectedDifficulty);
    }

    if (!searchQuery.trim()) return baseList;
    const lowerQ = searchQuery.toLowerCase();
    return baseList.filter(c => 
      c.name.toLowerCase().includes(lowerQ) || 
      c.id.toLowerCase().includes(lowerQ) ||
      c.category.toLowerCase().includes(lowerQ) ||
      c.categories.some((category) => category.toLowerCase().includes(lowerQ)) ||
      c.difficulty.toString() === lowerQ ||
      `difficulty ${c.difficulty}`.includes(lowerQ) ||
      c.difficulty_label.toLowerCase().includes(lowerQ)
    );
  }, [challenges, searchQuery, activeSet, difficultyFilter]);

  // Group by category
  const grouped = useMemo(() => {
    const result = filteredChallenges.reduce<Record<string, ChallengeSummary[]>>((acc, c) => {
      const categories = c.categories.length > 0 ? c.categories : [c.category];
      for (const category of new Set(categories)) {
        (acc[category] ??= []).push(c);
      }
      return acc;
    }, {});

    if (activeSet === 'leetcode') {
      for (const items of Object.values(result)) {
        items.sort((left, right) => {
          const difficultyOrder = left.difficulty - right.difficulty;
          if (difficultyOrder !== 0) return difficultyOrder;

          const leftId = Number(left.id.replace(/^lc_/, ''));
          const rightId = Number(right.id.replace(/^lc_/, ''));
          return leftId - rightId;
        });
      }
    }
    return result;
  }, [filteredChallenges, activeSet]);

  return (
    <div className="flex flex-col h-full overflow-hidden">
      <div className="p-3 shrink-0 border-b border-coden-border bg-coden-surface">
        <input 
          type="text" 
          placeholder="Search challenges"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full bg-coden-bg border border-coden-border rounded px-3 py-1.5 text-sm text-coden-text placeholder-coden-muted focus:outline-none focus:border-coden-accent transition-colors"
        />
        {activeSet === 'leetcode' && (
          <select
            aria-label="Filter by difficulty"
            value={difficultyFilter}
            onChange={(event) => {
              setDifficultyFilter(event.target.value);
              setExpanded({});
            }}
            className="mt-2 w-full bg-coden-bg border border-coden-border rounded px-3 py-1.5 text-sm text-coden-text focus:outline-none focus:border-coden-accent transition-colors"
          >
            <option value="all">All difficulty levels</option>
            <optgroup label="Easy">
              <option value="1">Level 1 — Easy</option>
              <option value="2">Level 2 — Easy</option>
              <option value="3">Level 3 — Easy</option>
            </optgroup>
            <optgroup label="Medium">
              <option value="4">Level 4 — Medium</option>
              <option value="5">Level 5 — Medium</option>
              <option value="6">Level 6 — Medium</option>
            </optgroup>
            <optgroup label="Hard">
              <option value="7">Level 7 — Hard</option>
              <option value="8">Level 8 — Hard</option>
              <option value="9">Level 9 — Hard</option>
              <option value="10">Level 10 — Hard</option>
            </optgroup>
          </select>
        )}
        <div className="mt-2 text-[11px] font-mono text-coden-muted">
          {filteredChallenges.length} of {challenges.length} unique challenges
        </div>
      </div>
      
      <div className="flex-1 overflow-y-auto p-2 scrollbar-hide">
        {Object.entries(grouped).map(([category, items]) => {
          // If searching, always expand to show results. Otherwise respect expanded state.
          const isCollapsed = !searchQuery.trim() && !expanded[category];
          
          return (
            <div key={category} className="mb-3">
              <button 
                onClick={() => toggleCategory(category)}
                className="w-full flex items-center justify-between px-2 py-1.5 text-xs uppercase tracking-wider text-coden-muted font-semibold hover:text-coden-text transition-colors group select-none"
              >
                <span>{formatCategory(category)} <span className="ml-1 opacity-60">({items.length})</span></span>
                <span 
                  className="transform transition-transform duration-200 group-hover:text-coden-accent text-[10px]" 
                  style={{ transform: isCollapsed ? 'rotate(-90deg)' : 'rotate(0deg)' }}
                >
                  ▾
                </span>
              </button>
              
              {!isCollapsed && (
                <ul className="mt-1 space-y-0.5">
                  {items.map((c) => {
                    const isCurrent = c.id === currentId;
                    const isDone = completed.includes(c.id);
                    const isLeetcodeVerified = unlockedLeetcode.includes(c.id);
                    const isLocked = !c.unlocked;
                    const displayTitle = formatChallengeTitle(c, activeSet);

                    let statusIndicator = <span className="w-3 shrink-0" />;
                    if (isLocked) {
                      statusIndicator = <span className="text-coden-muted shrink-0 text-xs" title="Locked in Career Mode">◆</span>;
                    } else if (isDone && isLeetcodeVerified) {
                      statusIndicator = <span className="text-green-400 shrink-0 text-xs font-bold" title="Verified on LeetCode">●</span>;
                    } else if (isDone) {
                      statusIndicator = <span className="text-yellow-500 shrink-0 text-xs font-bold" title="Completed locally, LeetCode pending">●</span>;
                    }

                    return (
                      <li key={c.id}>
                        <button
                          type="button"
                          onClick={() => !isLocked && selectChallenge(c.id)}
                          disabled={isLocked}
                          className={[
                            'w-full text-left px-2 py-1.5 rounded text-sm',
                            'flex items-center gap-2',
                            isLocked
                              ? 'opacity-40 cursor-not-allowed'
                              : 'hover:bg-coden-border transition-colors duration-150',
                            isCurrent
                              ? 'bg-sky-100 text-slate-950 ring-1 ring-sky-300 shadow-inner dark:bg-coden-border dark:text-coden-text dark:ring-0'
                              : 'text-coden-text',
                          ].join(' ')}
                          title={isLocked ? "Locked in Career Mode (complete parent nodes first)" : `${c.name} · ${c.required_complexity} · ${c.id}`}
                        >
                          {statusIndicator}
                          <div className="flex-1 min-w-0">
                            <div className="truncate">{displayTitle}</div>
                            <div
                              className={[
                                'text-[11px] font-mono truncate mt-0.5',
                                isCurrent
                                  ? 'text-slate-600 dark:text-coden-muted'
                                  : 'text-coden-muted opacity-80',
                              ].join(' ')}
                            >
                              {activeSet === 'leetcode'
                                ? `Difficulty ${c.difficulty}/10 · ${c.difficulty_label}`
                                : c.required_complexity}
                            </div>
                          </div>
                        </button>
                      </li>
                    );
                  })}
                </ul>
              )}
            </div>
          );
        })}
        
        {Object.keys(grouped).length === 0 && (
          <div className="flex flex-col items-center justify-center p-8 text-coden-muted space-y-2">
            <span className="text-sm">No algorithms found</span>
            <span className="text-xs">Try a name, id, or category.</span>
          </div>
        )}
      </div>
    </div>
  );
}
