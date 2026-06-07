import { useAppStore } from '../store/useAppStore';
import { Editor } from './Editor';
import { Toolbar } from './Toolbar';
import { Visualizer } from './Visualizer';
import { StepControls } from './StepControls';
import { StatusBanner } from './StatusBanner';
import { OpLog } from './OpLog';
import { LocalsPanel } from './LocalsPanel';


/**
 * ChallengeView — the main panel for one challenge.
 *
 * Three-column layout: description + editor (left), visualizer
 * + step controls (center), op log + locals (right).
 */
export function ChallengeView() {
  const detail = useAppStore((s) => s.currentDetail);

  if (!detail) {
    return (
      <div className="h-full flex items-center justify-center text-coden-muted">
        <div className="text-center">
          <div className="text-4xl mb-2">⚙️</div>
          <div className="text-lg">Pick a challenge from the left rail.</div>
        </div>
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col">
      {/* Header strip */}
      <div className="px-4 py-2 border-b border-coden-border bg-coden-surface shrink-0">
        <div className="flex items-baseline justify-between">
          <div>
            <h2 className="text-lg font-semibold">{detail.name}</h2>
            <div className="text-xs text-coden-muted font-mono">
              {detail.id} · {detail.category} · difficulty {detail.difficulty}/10
            </div>
          </div>
          <div className="text-xs text-coden-muted">
            Required: <span className="font-mono text-coden-text">{detail.required_complexity}</span>
          </div>
        </div>
      </div>

      <div className="flex-1 grid grid-cols-12 gap-3 p-3 overflow-hidden">
        {/* Left column: description + editor + status */}
        <div className="col-span-4 flex flex-col gap-3 overflow-hidden">
          <div className="bg-coden-surface border border-coden-border rounded p-3 overflow-y-auto max-h-40 text-sm">
            <div className="text-xs uppercase text-coden-muted font-semibold mb-1">
              Description
            </div>
            <div className="whitespace-pre-wrap">{detail.description}</div>
          </div>
          <StatusBanner />
          <div className="flex-1 flex flex-col min-h-0">
            <Toolbar />
            <div className="flex-1 min-h-0 mt-2">
              <Editor />
            </div>
          </div>
        </div>

        {/* Center column: visualizer + step controls */}
        <div className="col-span-5 flex flex-col gap-2 overflow-hidden">
          <div className="flex-1 bg-coden-surface border border-coden-border rounded p-3 overflow-hidden">
            <Visualizer />
          </div>
          <StepControls />
        </div>

        {/* Right column: op log + locals */}
        <div className="col-span-3 flex flex-col gap-3 overflow-hidden">
          <div className="bg-coden-surface border border-coden-border rounded p-3 overflow-hidden flex flex-col min-h-0">
            <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0">
              Stats &amp; ops
            </div>
            <OpLog />
          </div>
          <div className="bg-coden-surface border border-coden-border rounded p-3 overflow-hidden flex flex-col min-h-0">
            <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0">
              Locals at step
            </div>
            <LocalsPanel />
          </div>
        </div>
      </div>
    </div>
  );
}
