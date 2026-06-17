/**
 * PaneHeader.tsx — the tab bar.
 *
 * The v0.9.0 pivot removed the per-pane detach / reattach
 * buttons (no detached BrowserWindows exist anymore). The
 * header is just the tab bar now; the rest of the layout
 * controls (number of panes, equal sizes, reset) live in
 * the global TopHeader.
 *
 * The whole header carries `data-pane-id` so drag-to-another-pane
 * (TabBar's pointerup) can find its target.
 */
import { TabBar } from './TabBar';
import type { LeafNode } from './tree-ops';


interface PaneHeaderProps {
  paneId: string;
  leaf: LeafNode;
}


export function PaneHeader({ paneId, leaf }: PaneHeaderProps) {
  return (
    <div
      data-pane-id={paneId}
      className="flex flex-col shrink-0 bg-coden-surface"
    >
      <div className="flex items-stretch">
        <TabBar leaf={leaf} />
      </div>
    </div>
  );
}
