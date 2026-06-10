/**
 * StatsTab — op log + the read/compare/swap/write stats grid.
 * Extracted from the right column of the original ChallengeView.
 */
import { OpLog } from '../../OpLog';


export function StatsTab() {
  return (
    <div className="h-full bg-coden-surface border border-coden-border rounded p-3 flex flex-col min-h-0">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0">
        Stats &amp; ops
      </div>
      {/* OpLog owns its own scrollbar (overflow-y-auto inside).
          Don't wrap it in overflow-hidden here — that would clip
          OpLog's scrollbar and break scrolling. */}
      <div className="flex-1 min-h-0 overflow-auto">
        <OpLog />
      </div>
    </div>
  );
}
