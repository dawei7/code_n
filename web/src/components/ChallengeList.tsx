import { useAppStore } from '../store/useAppStore';
import type { ChallengeSummary } from '../types/api';


/**
 * ChallengeList — left rail with one row per challenge.
 *
 * Each row shows the human title (e.g. "Bubble Sort") as the
 * primary label, with the machine id (e.g. "sort_01") as a small
 * muted prefix so the URL slug is still discoverable. The
 * engine runner and verifier handle every spec the registry
 * exposes, so all challenges are clickable.
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
                    title={`${c.id} — ${c.name}`}
                  >
                    {isDone ? (
                      <span className="text-coden-accent" aria-label="completed">✓</span>
                    ) : (
                      <span className="w-3" aria-hidden="true" />
                    )}
                    <span className="flex-1 truncate">
                      <span className="text-[10px] text-coden-muted font-mono mr-1.5">
                        {c.id}
                      </span>
                      {c.name}
                    </span>
                    <span className="text-[10px] text-coden-muted font-mono">
                      {c.required_complexity}
                    </span>
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
