/**
 * LocalsTab — the JSON locals view at the current trace frame.
 * Wrapped in the "Locals at this step" card chrome that used to
 * live in the center column of the original ChallengeView.
 */
import { LocalsPanel } from '../../LocalsPanel';


export function LocalsTab() {
  return (
    <div className="h-full bg-coden-surface border border-coden-border rounded p-3 overflow-hidden flex flex-col min-h-0">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0">
        Locals at this step
      </div>
      <div className="flex-1 min-h-0 overflow-hidden">
        <LocalsPanel />
      </div>
    </div>
  );
}
