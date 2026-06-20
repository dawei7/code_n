import { useState, useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';
import type { ChallengeSummary } from '../types/api';

/**
 * ChallengeList — left rail with one row per challenge.
 *
 * Each row shows the human title (e.g. "Bubble Sort") as the
 * primary label, full-width. The complexity class sits in a
 * tooltip / on a second line below the title for narrow panes.
 * The machine id is intentionally NOT shown in the rail (it
 * is in the detail panel header and URL slug for power users).
 * The engine runner and verifier handle every spec the
 * registry exposes, so all challenges are clickable.
 */
export function ChallengeList() {
  const challenges = useAppStore((s) => s.challenges);
  const currentId = useAppStore((s) => s.currentDetail?.id ?? null);
  const selectChallenge = useAppStore((s) => s.selectChallenge);
  const completed = useAppStore((s) => s.progress?.completed ?? []);

  const [searchQuery, setSearchQuery] = useState('');
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  const toggleCategory = (category: string) => {
    setExpanded((prev) => ({ ...prev, [category]: !prev[category] }));
  };

  const filteredChallenges = useMemo(() => {
    if (!searchQuery.trim()) return challenges;
    const lowerQ = searchQuery.toLowerCase();
    return challenges.filter(c => 
      c.name.toLowerCase().includes(lowerQ) || 
      c.id.toLowerCase().includes(lowerQ) ||
      c.category.toLowerCase().includes(lowerQ)
    );
  }, [challenges, searchQuery]);

  // Group by category
  const grouped = useMemo(() => {
    return filteredChallenges.reduce<Record<string, ChallengeSummary[]>>((acc, c) => {
      (acc[c.category] ??= []).push(c);
      return acc;
    }, {});
  }, [filteredChallenges]);

  return (
    <div className="flex flex-col h-full overflow-hidden">
      <div className="p-3 shrink-0 border-b border-coden-border bg-coden-surface">
        <input 
          type="text" 
          placeholder="Search algorithms..." 
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full bg-[#1e1e1e] border border-coden-border rounded px-3 py-1.5 text-sm text-coden-text placeholder-coden-muted focus:outline-none focus:border-coden-accent transition-colors"
        />
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
                <span>{category} <span className="ml-1 opacity-60">({items.length})</span></span>
                <span 
                  className="transform transition-transform duration-200 group-hover:text-coden-accent text-[10px]" 
                  style={{ transform: isCollapsed ? 'rotate(-90deg)' : 'rotate(0deg)' }}
                >
                  ▼
                </span>
              </button>
              
              {!isCollapsed && (
                <ul className="mt-1 space-y-0.5">
                  {items.map((c) => {
                    const isCurrent = c.id === currentId;
                    const isDone = completed.includes(c.id);
                    return (
                      <li key={c.id}>
                        <button
                          type="button"
                          onClick={() => selectChallenge(c.id)}
                          className={[
                            'w-full text-left px-2 py-1.5 rounded text-sm',
                            'flex items-center gap-2',
                            'hover:bg-coden-border transition-colors duration-150',
                            isCurrent ? 'bg-coden-border text-white' : 'text-coden-text',
                          ].join(' ')}
                          title={`${c.name} · ${c.required_complexity} · ${c.id}`}
                        >
                          {isDone ? (
                            <span className="text-coden-accent shrink-0 text-xs" aria-label="completed">✓</span>
                          ) : (
                            <span className="w-3 shrink-0" aria-hidden="true" />
                          )}
                          <div className="flex-1 min-w-0">
                            <div className="truncate">{c.name}</div>
                            <div className="text-[11px] text-coden-muted font-mono truncate mt-0.5 opacity-80">
                              {c.required_complexity}
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
            <span className="text-2xl">🔍</span>
            <span className="text-sm">No algorithms found</span>
          </div>
        )}
      </div>
    </div>
  );
}
