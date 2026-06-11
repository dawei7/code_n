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

  // Group by category
  const grouped = challenges.reduce<Record<string, ChallengeSummary[]>>((acc, c) => {
    (acc[c.category] ??= []).push(c);
    return acc;
  }, {});

  return (
    <div className="p-2">
      {Object.entries(grouped).map(([category, items]) => (
        <div key={category} className="mb-4">
          <div className="px-2 py-1 text-xs uppercase tracking-wider text-coden-muted font-semibold">
            {category}
          </div>
          <ul>
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
                      'hover:bg-coden-border',
                      isCurrent ? 'bg-coden-border text-white' : 'text-coden-text',
                    ].join(' ')}
                    title={`${c.name} · ${c.required_complexity} · ${c.id}`}
                  >
                    {isDone ? (
                      <span className="text-coden-accent shrink-0" aria-label="completed">✓</span>
                    ) : (
                      <span className="w-3 shrink-0" aria-hidden="true" />
                    )}
                    <div className="flex-1 min-w-0">
                      <div className="truncate">{c.name}</div>
                      <div className="text-[10px] text-coden-muted font-mono truncate">
                        {c.required_complexity}
                      </div>
                    </div>
                  </button>
                </li>
              );
            })}
          </ul>
        </div>
      ))}
    </div>
  );
}
