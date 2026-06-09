/**
 * PaneHeader.tsx — the tab bar + per-pane controls.
 *
 * Per-pane controls:
 *   - ⧉ Detach: pops the current active tab out into a new
 *     BrowserWindow. (Implemented in step 7; for now the button
 *     is rendered but no-op-safe.)
 *   - × Close pane: only if there is more than one leaf in the
 *     tree. Redistributes the leaf's tabs to a sibling.
 *
 * The whole header carries `data-pane-id` so drag-to-another-pane
 * (TabBar's pointerup) can find its target.
 */
import { TabBar } from './TabBar';
import { useLayoutStore } from '../../store/useLayoutStore';
import { allLeaves } from './tree-ops';


interface PaneHeaderProps {
  paneId: string;
  leaf: import('./tree-ops').LayoutNode extends infer T
    ? T extends { kind: 'leaf'; id: string; tabIds: string[]; activeTabId: string | null }
      ? T
      : never
    : never;
  detached: boolean;
  onDetach: () => void;
  onReattach: () => void;
}


export function PaneHeader({ paneId, leaf, detached, onDetach, onReattach }: PaneHeaderProps) {
  const tree = useLayoutStore((s) => s.tree);
  const removeLeaf = useLayoutStore((s) => s.removeLeaf);
  const canClose = allLeaves(tree).length > 1;

  return (
    <div
      data-pane-id={paneId}
      className="flex flex-col shrink-0 bg-coden-surface"
    >
      <div className="flex items-stretch">
        <TabBar leaf={leaf} detached={detached} />
        <div className="flex items-center gap-1 px-2 border-l border-coden-border bg-coden-surface shrink-0">
          {detached ? (
            <button
              type="button"
              onClick={onReattach}
              className="text-xs px-2 py-0.5 rounded border border-coden-border text-coden-accent hover:bg-coden-border"
              title="Reattach this pane back to the main window"
            >
              ↩ Reattach
            </button>
          ) : (
            <button
              type="button"
              onClick={onDetach}
              disabled={!leaf.activeTabId}
              className="text-xs px-2 py-0.5 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border disabled:opacity-30"
              title="Pop this pane out into its own window"
            >
              ⧉
            </button>
          )}
          <button
            type="button"
            onClick={() => canClose && removeLeaf(paneId)}
            disabled={!canClose}
            className="text-xs px-2 py-0.5 rounded text-coden-muted hover:text-rose-300 hover:bg-coden-border disabled:opacity-30"
            title="Close this pane (tabs redistribute to a sibling)"
          >
            ×
          </button>
        </div>
      </div>
      {detached && (
        <div className="px-3 py-2 text-xs text-coden-muted border-b border-coden-border bg-coden-bg">
          This pane is detached. The active tab is showing in a separate window.
        </div>
      )}
    </div>
  );
}
