/**
 * ComplexityTab — required vs achieved complexity, operation
 * budget, and the per-algorithm best/avg/worst notes. Extracted
 * from the left column of the original ChallengeView.
 */
import { ComplexityAnalysis } from '../../ComplexityAnalysis';


export function ComplexityTab() {
  return (
    <div className="h-full overflow-y-auto">
      <ComplexityAnalysis />
    </div>
  );
}
