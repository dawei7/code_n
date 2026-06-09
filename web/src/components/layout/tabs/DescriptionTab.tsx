/**
 * DescriptionTab — challenge description text + the pass/fail
 * status banner. Extracted from the left column of the original
 * ChallengeView 3-column grid.
 */
import { useAppStore } from '../../../store/useAppStore';
import { StatusBanner } from '../../StatusBanner';


export function DescriptionTab() {
  const detail = useAppStore((s) => s.currentDetail);

  if (!detail) {
    return (
      <div className="h-full flex items-center justify-center text-xs text-coden-muted">
        Pick a challenge from the left rail.
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col gap-3 overflow-y-auto">
      <div className="bg-coden-surface border border-coden-border rounded p-3 text-sm shrink-0">
        <div className="text-xs uppercase text-coden-muted font-semibold mb-1">
          Description
        </div>
        <div className="whitespace-pre-wrap">{detail.description}</div>
      </div>
      <StatusBanner />
    </div>
  );
}
