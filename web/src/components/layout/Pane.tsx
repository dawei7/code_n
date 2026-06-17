/**
 * Pane.tsx — leaf wrapper. Renders PaneHeader + PaneContent.
 *
 * The v0.9.0 pivot removed detached BrowserWindows (the
 * pop-out editor, the pop-out debug surface, the pop-out
 * pane host). The detach / reattach handlers + the
 * `detachedPanes` state are gone — the layout store still
 * has the field for backwards compatibility with persisted
 * state, but the only leaf state is "in the main window"
 * from now on.
 */
import { PaneHeader } from './PaneHeader';
import { PaneContent } from './PaneContent';
import { BUILTIN_TABS } from './tabs/registry';
import { useLayoutStore } from '../../store/useLayoutStore';
import type { LeafNode } from './tree-ops';


interface PaneProps {
  leaf: LeafNode;
}


export function Pane({ leaf }: PaneProps) {
  const moveTab = useLayoutStore((s) => s.moveTab);
  const isEmpty = leaf.tabIds.length === 0;

  const onAddTab = (tabId: string) => {
    // fromLeafId=null means "add without removing from any source"
    moveTab(tabId, null, leaf.id);
  };

  return (
    <div className="flex flex-col w-full h-full min-w-0 min-h-0 bg-coden-bg">
      <PaneHeader paneId={leaf.id} leaf={leaf} />
      {/* The body scrolls vertically. overflow-x-hidden keeps long
          lines / wide tables from triggering a horizontal scrollbar
          on the pane itself (inner content can still scroll its own
          X axis if it wants to). min-h-0 is what lets flex children
          actually shrink past their content height — without it the
          scrollbar would never appear. */}
      <div className="flex-1 min-h-0 overflow-y-auto overflow-x-auto">
        {isEmpty ? (
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
                  className="px-2 py-1.5 text-xs font-mono rounded border border-coden-border bg-coden-surface text-coden-text hover:border-coden-accent hover:text-coden-accent"
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
