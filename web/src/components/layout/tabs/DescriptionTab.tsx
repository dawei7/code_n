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
      <div className="flex items-center justify-center text-xs text-coden-muted p-4">
        Pick a challenge from the left rail.
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-3">
      <div className="bg-coden-surface rounded-lg p-4 text-sm shrink-0 shadow-md">
        <div className="text-xs uppercase text-coden-muted font-semibold mb-1">
          Description
        </div>
        <div className="whitespace-pre-wrap">{detail.description}</div>
      </div>
      <StatusBanner />
    </div>
  );
}
