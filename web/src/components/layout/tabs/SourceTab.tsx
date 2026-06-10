/**
 * SourceTab — read-only source view with the active line marked.
 * Was the bottom half of the right column in the original 3-pane
 * layout. Now a first-class tab the user can place in any pane.
 */
import { CodePanel } from '../../CodePanel';


export function SourceTab() {
  return (
    <div className="h-full flex flex-col min-h-0">
      <CodePanel />
    </div>
  );
}
