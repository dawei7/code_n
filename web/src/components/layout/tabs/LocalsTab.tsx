/**
 * LocalsTab — the JSON locals view at the current trace frame.
 * Wrapped in the "Locals at this step" card chrome that used to
 * live in the center column of the original ChallengeView.
 */
import { LocalsPanel } from '../../LocalsPanel';


export function LocalsTab() {
  return (
    <div className="h-full bg-coden-surface border border-coden-border rounded p-3 flex flex-col min-h-0">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0">
        Locals at this step
      </div>
      {/* The LocalsPanel owns its own vertical scrollbar (the JSON
          view needs to be vertically scrollable when locals are
          many). Letting this wrapper be overflow-visible instead
          of overflow-hidden lets the LocalsPanel's overflow-auto
          actually take effect. */}
      <div className="flex-1 min-h-0 overflow-auto">
        <LocalsPanel />
      </div>
    </div>
  );
}
