import { useAppStore } from '../store/useAppStore';
import type { ChallengeSummary } from '../types/api';


/**
 * ChallengeList — left rail with one row per challenge.
 *
 * MVP behavior: sort_01 is enabled (the engine runner + visualizer
 * work end-to-end for it). All other challenges show their name +
 * category but the row is dimmed and clicking it shows a "Coming
 * in the next sprint" placeholder.
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
              const enabled = c.id === 'sort_01';
              const isCurrent = c.id === currentId;
              const isDone = completed.includes(c.id);
              return (
                <li key={c.id}>
                  <button
                    type="button"
                    disabled={!enabled}
                    onClick={() => selectChallenge(c.id)}
                    className={[
                      'w-full text-left px-2 py-1.5 rounded text-sm font-mono',
                      'flex items-center gap-2',
                      enabled ? 'hover:bg-coden-border' : 'opacity-40 cursor-not-allowed',
                      isCurrent ? 'bg-coden-border text-white' : 'text-coden-text',
                    ].join(' ')}
                  >
                    {isDone && <span className="text-coden-accent">✓</span>}
                    <span className="flex-1 truncate">{c.id}</span>
                    <span className="text-xs text-coden-muted">
                      {c.required_complexity}
                    </span>
                  </button>
                </li>
              );
            })}
          </ul>
        </div>
      ))}
      <div className="px-2 py-3 text-xs text-coden-muted border-t border-coden-border">
        Only <span className="font-mono text-coden-accent">sort_01</span> is
        wired up in the MVP. Other challenges are listed for reference.
      </div>
    </div>
  );
}
