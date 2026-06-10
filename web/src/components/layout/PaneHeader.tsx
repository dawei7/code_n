/**
 * PaneHeader.tsx — the tab bar + per-pane controls.
 *
 * Per-pane controls:
 *   - ⧉ Detach: pops the pane out into a new BrowserWindow.
 *   - ↩ Reattach (only when detached): bring the pane's content
 *     back into the main window.
 *
 * The whole header carries `data-pane-id` so drag-to-another-pane
 * (TabBar's pointerup) can find its target.
 *
 * Pane creation is a header-preset decision (Layout dropdown),
 * not a per-pane action. There is no "+ New pane" or empty-pane
 * × button.
 */
import { TabBar } from './TabBar';
import type { LeafNode } from './tree-ops';


interface PaneHeaderProps {
  paneId: string;
  leaf: LeafNode;
  detached: boolean;
  onDetach: () => void;
  onReattach: () => void;
}


export function PaneHeader({ paneId, leaf, detached, onDetach, onReattach }: PaneHeaderProps) {
  const isEmpty = leaf.tabIds.length === 0;

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
              disabled={!leaf.activeTabId || isEmpty}
              className="text-xs px-2 py-0.5 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border disabled:opacity-30"
              title="Pop this pane out into its own window"
            >
              ⧉
            </button>
          )}
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
