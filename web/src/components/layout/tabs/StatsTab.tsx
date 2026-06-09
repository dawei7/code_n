/**
 * StatsTab — op log + the read/compare/swap/write stats grid.
 * Extracted from the right column of the original ChallengeView.
 */
import { OpLog } from '../../OpLog';


export function StatsTab() {
  return (
    <div className="h-full bg-coden-surface border border-coden-border rounded p-3 overflow-hidden flex flex-col">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0">
        Stats &amp; ops
      </div>
      <OpLog />
    </div>
  );
}
