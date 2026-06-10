/**
 * Pane.tsx — leaf wrapper. Renders PaneHeader + PaneContent.
 * Holds the detach/reattach click handlers.
 */
import { useLayoutStore } from '../../store/useLayoutStore';
import { PaneHeader } from './PaneHeader';
import { PaneContent } from './PaneContent';
import { BUILTIN_TABS } from './tabs/registry';
import type { LeafNode } from './tree-ops';


interface PaneProps {
  leaf: LeafNode;
}


export function Pane({ leaf }: PaneProps) {
  const detachedPanes = useLayoutStore((s) => s.detachedPanes);
  const markDetached = useLayoutStore((s) => s.markDetached);
  const moveTab = useLayoutStore((s) => s.moveTab);
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

  const onAddTab = (tabId: string) => {
    // fromLeafId=null means "add without removing from any source"
    moveTab(tabId, null, leaf.id);
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
      {/* The body scrolls vertically. overflow-x-hidden keeps long
          lines / wide tables from triggering a horizontal scrollbar
          on the pane itself (inner content can still scroll its own
          X axis if it wants to). min-h-0 is what lets flex children
          actually shrink past their content height — without it the
          scrollbar would never appear. */}
      <div className="flex-1 min-h-0 overflow-y-auto overflow-x-auto">
        {isDetached ? (
          <div className="h-full flex items-center justify-center text-coden-muted text-xs">
            (detached — reattach to view here)
          </div>
        ) : isEmpty ? (
          <div
            data-pane-id={leaf.id}
            className="h-full flex flex-col items-center justify-center text-coden-muted gap-3 select-none p-4"
          >
            <div className="text-sm">Empty pane</div>
            <div className="text-[10px] text-coden-muted/70">
              Click a tab to add it, or drag one here from another pane.
            </div>
            <div className="flex flex-wrap gap-2 justify-center max-w-md">
              {BUILTIN_TABS.map((def) => (
                <button
                  key={def.id}
                  type="button"
                  onClick={() => onAddTab(def.id)}
                  className="px-3 py-1.5 text-xs font-mono rounded border border-coden-border bg-coden-surface text-coden-text hover:border-coden-accent hover:text-coden-accent"
                  title={`Add ${def.label} to this pane`}
                >
                  <span aria-hidden="true" className="mr-1.5">{def.icon}</span>
                  {def.label}
                </button>
              ))}
            </div>
          </div>
        ) : (
          <PaneContent tabId={leaf.activeTabId} />
        )}
      </div>
    </div>
  );
}
