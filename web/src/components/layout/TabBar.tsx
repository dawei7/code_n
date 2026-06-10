/**
 * TabBar.tsx — the tab strip at the top of a pane.
 *
 * Each tab is a button. Pointer-driven reorder (not HTML5 DnD —
 * dark-theme friendly, no ghost image, works on touch). On
 * pointerup the target pane is found via
 * event.target.closest('[data-pane-id]') and the moveTab action
 * is dispatched.
 *
 * Right-click on a tab opens a context menu: Close, Close others,
 * Close all (only enabled for closable tabs), Move to pane →.
 *
 * The trailing "+" button opens a popover listing every built-in
 * tab. Clicking a tab there adds it to this pane and activates it.
 * Tabs already present in THIS pane are shown as "Added" (disabled).
 * The same tab can be in multiple panes (e.g. Description in both
 * top-left and bottom-right) — that's by design.
 */
import { useEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { useLayoutStore } from '../../store/useLayoutStore';
import { allLeaves } from './tree-ops';
import { BUILTIN_TABS, getTab } from './tabs/registry';
import type { LeafNode } from './tree-ops';


interface TabBarProps {
  leaf: LeafNode;
  /** When true, the leaf is rendered as a "Detached — Reattach"
   *  placeholder; we still render its tabs read-only. */
  detached?: boolean;
}


interface DragState {
  pointerId: number;
  tabId: string;
  startX: number;
  startY: number;
  currentX: number;
  currentY: number;
  /** Width of the tab being dragged (for ghost sizing). */
  width: number;
}


interface ContextMenuState {
  x: number;
  y: number;
  tabId: string;
}


export function TabBar({ leaf, detached = false }: TabBarProps) {
  const setActiveTab = useLayoutStore((s) => s.setActiveTab);
  const moveTab = useLayoutStore((s) => s.moveTab);
  const closeTabInLeaf = useLayoutStore((s) => s.closeTabInLeaf);
  const closeOtherTabs = useLayoutStore((s) => s.closeOtherTabs);
  const closeTabEverywhere = useLayoutStore((s) => s.closeTabEverywhere);
  const tree = useLayoutStore((s) => s.tree);

  const [drag, setDrag] = useState<DragState | null>(null);
  const [ctxMenu, setCtxMenu] = useState<ContextMenuState | null>(null);
  const [addOpen, setAddOpen] = useState(false);
  const [addPos, setAddPos] = useState<{ left: number; top: number } | null>(null);
  const ctxRef = useRef<HTMLDivElement | null>(null);
  const addButtonRef = useRef<HTMLButtonElement | null>(null);
  const addMenuRef = useRef<HTMLDivElement | null>(null);

  // Close the context menu on any outside click or Escape.
  useEffect(() => {
    if (!ctxMenu) return;
    function onDown(e: MouseEvent) {
      if (ctxRef.current && !ctxRef.current.contains(e.target as Node)) {
        setCtxMenu(null);
      }
    }
    function onKey(e: KeyboardEvent) {
      if (e.key === 'Escape') setCtxMenu(null);
    }
    window.addEventListener('mousedown', onDown);
    window.addEventListener('keydown', onKey);
    return () => {
      window.removeEventListener('mousedown', onDown);
      window.removeEventListener('keydown', onKey);
    };
  }, [ctxMenu]);

  // Close the "+" add-menu on any outside click or Escape. The menu
  // is rendered via a portal, so the outside-click check has to
  // test BOTH the menu element AND the trigger button.
  useEffect(() => {
    if (!addOpen) return;
    function onDown(e: MouseEvent) {
      const target = e.target as Node;
      if (addMenuRef.current?.contains(target)) return;
      if (addButtonRef.current?.contains(target)) return;
      setAddOpen(false);
    }
    function onKey(e: KeyboardEvent) {
      if (e.key === 'Escape') setAddOpen(false);
    }
    // Recompute the menu position on scroll or resize while open.
    function reposition() {
      const btn = addButtonRef.current;
      if (!btn) return;
      const r = btn.getBoundingClientRect();
      setAddPos({ left: r.left, top: r.bottom });
    }
    window.addEventListener('mousedown', onDown);
    window.addEventListener('keydown', onKey);
    window.addEventListener('scroll', reposition, true);
    window.addEventListener('resize', reposition);
    return () => {
      window.removeEventListener('mousedown', onDown);
      window.removeEventListener('keydown', onKey);
      window.removeEventListener('scroll', reposition, true);
      window.removeEventListener('resize', reposition);
    };
  }, [addOpen]);

  const addTabToThisPane = (tabId: string) => {
    if (leaf.tabIds.includes(tabId)) {
      // Already here — just activate it.
      setActiveTab(leaf.id, tabId);
    } else {
      // Use moveTab with fromLeafId=null to add without removing.
      moveTab(tabId, null, leaf.id);
    }
    setAddOpen(false);
  };

  // Drag global handlers — set on pointerdown, removed on pointerup.
  useEffect(() => {
    if (!drag) return;
    function onMove(e: PointerEvent) {
      if (e.pointerId !== drag!.pointerId) return;
      setDrag({ ...drag!, currentX: e.clientX, currentY: e.clientY });
    }
    function onUp(e: PointerEvent) {
      if (e.pointerId !== drag!.pointerId) return;
      // Find the pane under the pointer.
      const target = document.elementFromPoint(e.clientX, e.clientY);
      const paneEl = target?.closest('[data-pane-id]');
      const toPaneId = paneEl?.getAttribute('data-pane-id') ?? null;
      if (toPaneId && toPaneId !== leaf.id) {
        moveTab(drag!.tabId, leaf.id, toPaneId);
      }
      setDrag(null);
    }
    window.addEventListener('pointermove', onMove);
    window.addEventListener('pointerup', onUp);
    return () => {
      window.removeEventListener('pointermove', onMove);
      window.removeEventListener('pointerup', onUp);
    };
  }, [drag, leaf.id, moveTab]);

  const startDrag = (
    e: React.PointerEvent<HTMLButtonElement>,
    tabId: string,
    width: number,
  ) => {
    if (detached) return;
    if (e.button !== 0) return;
    e.preventDefault();
    e.stopPropagation();
    setDrag({
      pointerId: e.pointerId,
      tabId,
      startX: e.clientX,
      startY: e.clientY,
      currentX: e.clientX,
      currentY: e.clientY,
      width,
    });
  };

  const onContextMenu = (
    e: React.MouseEvent<HTMLButtonElement>,
    tabId: string,
  ) => {
    e.preventDefault();
    e.stopPropagation();
    setCtxMenu({ x: e.clientX, y: e.clientY, tabId });
  };

  const onClickTab = (tabId: string) => {
    if (detached) return;
    setActiveTab(leaf.id, tabId);
  };

  const onCloseClick = (
    e: React.MouseEvent<HTMLSpanElement>,
    tabId: string,
  ) => {
    e.stopPropagation();
    e.preventDefault();
    closeTabInLeaf(tabId, leaf.id);
  };

  const allTabs = allLeaves(tree).flatMap((l) => l.tabIds);
  const tabIsGlobal = (id: string) => allTabs.includes(id);

  // The ghost position for the active drag, in pixels.
  const ghost = drag
    ? {
        left: drag.currentX - drag.width / 2,
        top: drag.currentY - 12,
        width: drag.width,
      }
    : null;

  return (
    <div className="flex items-stretch h-7 bg-coden-surface border-b border-coden-border overflow-x-auto">
      {/* The "+" add-tab button. The menu is rendered via a portal
          (see below) so it can escape the pane's `overflow-hidden`
          ancestor and is not clipped at the pane edge. */}
      {!detached && (
        <div className="relative flex items-stretch shrink-0">
          <button
            ref={addButtonRef}
            type="button"
            onClick={() => {
              if (!addOpen && addButtonRef.current) {
                const r = addButtonRef.current.getBoundingClientRect();
                setAddPos({ left: r.left, top: r.bottom });
              }
              setAddOpen((v) => !v);
            }}
            className={[
              'px-2 h-full text-xs font-mono border-r border-coden-border',
              'text-coden-muted hover:text-coden-text hover:bg-coden-bg/50',
            ].join(' ')}
            title="Add a tab to THIS pane (use the ⊞ in the pane header to add a NEW pane)"
            aria-label="Add tab to this pane"
          >
            + Tab
          </button>
        </div>
      )}
      {addOpen && addPos && createPortal(
        <div
          ref={addMenuRef}
          style={{
            position: 'fixed',
            left: addPos.left,
            top: addPos.top,
            zIndex: 1000,
          }}
          className="bg-coden-surface border border-coden-border rounded shadow-xl text-xs font-mono min-w-[180px] py-1"
        >
          {BUILTIN_TABS.map((def) => {
            const already = leaf.tabIds.includes(def.id);
            return (
              <button
                key={def.id}
                type="button"
                disabled={already}
                onClick={() => addTabToThisPane(def.id)}
                className={[
                  'w-full text-left px-3 py-1 flex items-center gap-2',
                  already
                    ? 'text-coden-muted opacity-50 cursor-not-allowed'
                    : 'hover:bg-coden-border cursor-pointer',
                ].join(' ')}
                title={already ? `${def.label} is already in this pane` : `Add ${def.label} to this pane`}
              >
                <span aria-hidden="true">{def.icon}</span>
                <span className="flex-1">{def.label}</span>
                {already && <span className="text-[10px] text-coden-muted">added</span>}
              </button>
            );
          })}
        </div>,
        document.body,
      )}
      {leaf.tabIds.map((tabId) => {
        const def = getTab(tabId);
        if (!def) return null;
        const isActive = leaf.activeTabId === tabId && !detached;
        return (
          <button
            key={tabId}
            type="button"
            data-tab-id={tabId}
            data-active={isActive ? 'true' : 'false'}
            onClick={() => onClickTab(tabId)}
            onContextMenu={(e) => onContextMenu(e, tabId)}
            onPointerDown={(e) =>
              startDrag(e, tabId, e.currentTarget.offsetWidth)
            }
            className={[
              'group flex items-center gap-1.5 px-3 text-xs font-mono whitespace-nowrap',
              'border-r border-coden-border select-none',
              isActive
                ? 'bg-coden-bg text-coden-text'
                : 'bg-coden-surface text-coden-muted hover:text-coden-text hover:bg-coden-bg/50',
              detached ? 'cursor-default' : 'cursor-pointer',
            ].join(' ')}
            title={def.label}
          >
            <span aria-hidden="true">{def.icon}</span>
            <span>{def.label}</span>
            {!detached && (
              <span
                role="button"
                aria-label={`Close ${def.label}`}
                tabIndex={-1}
                onPointerDown={(e) => e.stopPropagation()}
                onClick={(e) => onCloseClick(e, tabId)}
                className="ml-1 text-coden-muted hover:text-coden-text hover:bg-coden-border rounded-sm w-4 h-4 inline-flex items-center justify-center"
              >
                ×
              </span>
            )}
          </button>
        );
      })}

      {/* Drag ghost */}
      {ghost && drag && (
        <div
          aria-hidden="true"
          style={{
            position: 'fixed',
            left: ghost.left,
            top: ghost.top,
            width: ghost.width,
            pointerEvents: 'none',
            zIndex: 50,
            opacity: 0.85,
          }}
          className="flex items-center gap-1.5 px-3 h-7 text-xs font-mono bg-coden-bg border border-coden-accent text-coden-text rounded shadow-lg"
        >
          <span>{getTab(drag.tabId)?.icon}</span>
          <span>{getTab(drag.tabId)?.label}</span>
        </div>
      )}

      {/* Context menu (rendered via portal so it can overflow the
          pane's `overflow-hidden` ancestor at the pane edge). */}
      {ctxMenu && createPortal(
        <div
          ref={ctxRef}
          style={{
            position: 'fixed',
            left: ctxMenu.x,
            top: ctxMenu.y,
            zIndex: 1000,
          }}
          className="bg-coden-surface border border-coden-border rounded shadow-xl text-xs font-mono min-w-[180px] py-1"
        >
          <button
            type="button"
            className="block w-full text-left px-3 py-1 hover:bg-coden-border"
            onClick={() => { closeTabInLeaf(ctxMenu.tabId, leaf.id); setCtxMenu(null); }}
          >
            Close
          </button>
          <button
            type="button"
            className="block w-full text-left px-3 py-1 hover:bg-coden-border"
            onClick={() => { closeOtherTabs(ctxMenu.tabId, leaf.id); setCtxMenu(null); }}
          >
            Close others
          </button>
          {getTab(ctxMenu.tabId)?.closable && tabIsGlobal(ctxMenu.tabId) && (
            <button
              type="button"
              className="block w-full text-left px-3 py-1 hover:bg-coden-border text-rose-300"
              onClick={() => { closeTabEverywhere(ctxMenu.tabId); setCtxMenu(null); }}
            >
              Close all (remove)
            </button>
          )}
          <div className="border-t border-coden-border my-1" />
          <div className="px-3 py-1 text-coden-muted">Move to pane</div>
          {allLeaves(tree)
            .filter((l) => l.id !== leaf.id)
            .map((l) => (
              <button
                key={l.id}
                type="button"
                className="block w-full text-left px-3 py-1 hover:bg-coden-border"
                onClick={() => { moveTab(ctxMenu.tabId, leaf.id, l.id); setCtxMenu(null); }}
              >
                → {l.id.slice(0, 12)}…
                {l.activeTabId ? ` (${l.activeTabId})` : ''}
              </button>
            ))}
        </div>,
        document.body,
      )}
    </div>
  );
}
