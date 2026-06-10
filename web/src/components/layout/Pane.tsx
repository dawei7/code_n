/**
 * Pane.tsx — leaf wrapper. Renders PaneHeader + PaneContent.
 * Holds the detach/reattach click handlers.
 */
import { useLayoutStore } from '../../store/useLayoutStore';
import { PaneHeader } from './PaneHeader';
import { PaneContent } from './PaneContent';
import type { LeafNode } from './tree-ops';


interface PaneProps {
  leaf: LeafNode;
}


export function Pane({ leaf }: PaneProps) {
  const detachedPanes = useLayoutStore((s) => s.detachedPanes);
  const markDetached = useLayoutStore((s) => s.markDetached);
  const isDetached = !!detachedPanes[leaf.id];
  const isEmpty = leaf.tabIds.length === 0;

  const onDetach = () => {
    if (!leaf.activeTabId) return;
    const tabId = leaf.activeTabId;
    // Mark as detached FIRST so the placeholder shows immediately
    // even before the IPC roundtrip returns.
    markDetached(leaf.id, true);
    const api = window.electronAPI;
    if (api?.popOutPane) {
      void api.popOutPane(leaf.id, tabId);
    } else {
      // Dev / browser fallback: open the pane URL in a new tab.
      const port = window.location.port || '5173';
      const host = window.location.hostname || '127.0.0.1';
      const url = `http://${host}:${port}/?view=pane&paneId=${encodeURIComponent(leaf.id)}&tabId=${encodeURIComponent(tabId)}`;
      window.open(url, '_blank');
    }
  };

  const onReattach = () => {
    markDetached(leaf.id, false);
  };

  return (
    <div className="flex flex-col w-full h-full min-w-0 min-h-0 bg-coden-bg">
      <PaneHeader
        paneId={leaf.id}
        leaf={leaf}
        detached={isDetached}
        onDetach={onDetach}
        onReattach={onReattach}
      />
      <div className="flex-1 min-h-0 overflow-hidden">
        {isDetached ? (
          <div className="h-full flex items-center justify-center text-coden-muted text-xs">
            (detached — reattach to view here)
          </div>
        ) : isEmpty ? (
          <div
            data-pane-id={leaf.id}
            className="h-full flex flex-col items-center justify-center text-coden-muted text-xs gap-2 select-none"
          >
            <div className="text-2xl opacity-40">∅</div>
            <div>No tabs in this pane.</div>
            <div className="text-[10px]">
              Drag a tab here from another pane, or right-click a tab → Move to pane.
            </div>
          </div>
        ) : (
          <PaneContent tabId={leaf.activeTabId} />
        )}
      </div>
    </div>
  );
}
