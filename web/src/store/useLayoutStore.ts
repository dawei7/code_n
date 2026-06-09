/**
 * useLayoutStore.ts — the pane tree + tab registry + persistence.
 *
 * The layout state is the single source of truth for what tabs
 * live in which panes and how big each pane is. Persisted to
 * `localStorage` key `coden:layout:v1`. The store's actions
 * delegate to pure functions in components/layout/tree-ops.ts
 * (which are unit-tested via tests/test_layout_tree_ops.mjs).
 *
 * Why a separate store from useAppStore? The two evolve on
 * different cadences: useAppStore is the engine state (challenges,
 * runs, op log); useLayoutStore is the UI state (pane geometry,
 * tab assignment). Keeping them apart means the layout doesn't
 * have to be persisted on every Run and the engine state
 * doesn't have to be re-broadcast on every splitter drag.
 */
import { create } from 'zustand';
import {
  type LayoutNode,
  allLeaves,
  applyDelta,
  closeOtherTabs as closeOtherTabsOp,
  closeTabInLeaf as closeTabInLeafOp,
  equalSizes,
  moveTab as moveTabOp,
  presetForN,
  removeLeaf as removeLeafOp,
  setActiveTab as setActiveTabOp,
} from '../components/layout/tree-ops';


/** Bumped on breaking schema changes; see `migrate()` below. */
const SCHEMA_VERSION = 1;
const STORAGE_KEY = 'coden:layout:v1';


/** Re-derive the reverse index from the tree. O(leaves * tabs). */
function buildTabLocations(tree: LayoutNode): Map<string, Set<string>> {
  const m = new Map<string, Set<string>>();
  for (const leaf of allLeaves(tree)) {
    for (const t of leaf.tabIds) {
      let set = m.get(t);
      if (!set) {
        set = new Set();
        m.set(t, set);
      }
      set.add(leaf.id);
    }
  }
  return m;
}


/** Counter-based id generator. Stable across reloads within a session. */
let nextId = 1;
function newId(prefix: string): string {
  return `${prefix}-${nextId++}`;
}


/** Pick a default tree (4-pane 2x2) for fresh installs. */
function defaultTree(): LayoutNode {
  return presetForN(4, () => newId('n'));
}


/**
 * Read persisted layout from localStorage. Returns null on
 * any failure (corrupt JSON, schema mismatch, private mode).
 * Migrations go here.
 */
function loadFromStorage(): {
  tree: LayoutNode;
  detachedPanes: Record<string, true>;
} | null {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (parsed?.schemaVersion !== SCHEMA_VERSION) return null;
    if (!parsed?.tree || parsed.tree.kind !== 'split') return null;
    if (allLeaves(parsed.tree).length < 1) return null;
    // Sanity: every active tab must exist in its leaf's tabIds.
    for (const leaf of allLeaves(parsed.tree)) {
      if (leaf.activeTabId && !leaf.tabIds.includes(leaf.activeTabId)) {
        leaf.activeTabId = leaf.tabIds[0] ?? null;
      }
    }
    return {
      tree: parsed.tree,
      detachedPanes: parsed.detachedPanes ?? {},
    };
  } catch {
    return null;
  }
}


function saveToStorage(payload: { tree: LayoutNode; detachedPanes: Record<string, true> }): void {
  try {
    localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify({ ...payload, schemaVersion: SCHEMA_VERSION }),
    );
  } catch {
    // private mode / quota — fail silently
  }
}


/** Debounced wrapper around saveToStorage. */
let saveTimer: ReturnType<typeof setTimeout> | null = null;
function schedulePersist(payload: { tree: LayoutNode; detachedPanes: Record<string, true> }): void {
  if (saveTimer !== null) clearTimeout(saveTimer);
  saveTimer = setTimeout(() => saveToStorage(payload), 300);
}


export interface LayoutState {
  tree: LayoutNode;
  detachedPanes: Record<string, true>;

  // --- Actions ---
  applyPreset(n: 2 | 3 | 4): void;
  setActiveTab(leafId: string, tabId: string): void;
  moveTab(tabId: string, fromLeafId: string | null, toLeafId: string): void;
  closeTabInLeaf(tabId: string, leafId: string): void;
  closeOtherTabs(tabId: string, keepLeafId: string | null): void;
  closeTabEverywhere(tabId: string): void;
  removeLeaf(leafId: string): void;
  /** Adjust a split's sizes by a delta fraction on child i. */
  resizeSplit(splitId: string, i: number, deltaFrac: number): void;
  /** Reset a split to equal sizes. */
  resetSplit(splitId: string): void;
  /** Mark a leaf as detached (its content is now in a BrowserWindow)
   *  or as re-attached (back in the main window). The leaf is still
   *  in the tree; the caller can render a "Detached" placeholder. */
  markDetached(paneId: string, detached: boolean): void;
  /** Replace the entire tree (used by the layout dropdown). */
  replaceTree(tree: LayoutNode): void;
}


const persisted = loadFromStorage();


export const useLayoutStore = create<LayoutState>((set) => {
  const initialTree = persisted?.tree ?? defaultTree();

  function commit(updater: (s: LayoutState) => Partial<LayoutState>): void {
    set((s) => {
      const next = updater(s);
      const merged = { ...s, ...next };
      schedulePersist({ tree: merged.tree, detachedPanes: merged.detachedPanes });
      return next;
    });
  }

  return {
    tree: initialTree,
    detachedPanes: persisted?.detachedPanes ?? {},

    applyPreset(n) {
      commit(() => ({ tree: presetForN(n, () => newId('n')) }));
    },

    setActiveTab(leafId, tabId) {
      commit((s) => ({ tree: setActiveTabOp(s.tree, leafId, tabId) }));
    },

    moveTab(tabId, fromLeafId, toLeafId) {
      commit((s) => ({ tree: moveTabOp(s.tree, tabId, fromLeafId, toLeafId) }));
    },

    closeTabInLeaf(tabId, leafId) {
      commit((s) => ({ tree: closeTabInLeafOp(s.tree, tabId, leafId) }));
    },

    closeOtherTabs(tabId, keepLeafId) {
      commit((s) => ({ tree: closeOtherTabsOp(s.tree, tabId, keepLeafId) }));
    },

    closeTabEverywhere(tabId) {
      commit((s) => ({ tree: closeOtherTabsOp(s.tree, tabId, null) }));
    },

    removeLeaf(leafId) {
      commit((s) => {
        const tree = removeLeafOp(s.tree, leafId);
        const { [leafId]: _removed, ...detachedPanes } = s.detachedPanes;
        void _removed;
        return { tree, detachedPanes };
      });
    },

    resizeSplit(splitId, i, deltaFrac) {
      commit((s) => {
        // Walk the tree to find the split; apply delta locally.
        const apply = (node: LayoutNode): LayoutNode => {
          if (node.kind === 'leaf') return node;
          if (node.id === splitId) {
            return { ...node, sizes: applyDelta(node.sizes, i, deltaFrac) };
          }
          return { ...node, children: node.children.map(apply) };
        };
        return { tree: apply(s.tree) };
      });
    },

    resetSplit(splitId) {
      commit((s) => {
        const apply = (node: LayoutNode): LayoutNode => {
          if (node.kind === 'leaf') return node;
          if (node.id === splitId) {
            return { ...node, sizes: equalSizes(node.children.length) };
          }
          return { ...node, children: node.children.map(apply) };
        };
        return { tree: apply(s.tree) };
      });
    },

    markDetached(paneId, detached) {
      commit((s) => {
        const { [paneId]: _, ...rest } = s.detachedPanes;
        void _;
        return {
          detachedPanes: detached ? { ...rest, [paneId]: true } : rest,
        };
      });
    },

    replaceTree(tree) {
      commit(() => ({ tree }));
    },
  };
});


/** Helper: the reverse index, recomputed from the current tree. */
export function useTabLocations(): Map<string, Set<string>> {
  return useLayoutStore((s) => buildTabLocations(s.tree));
}
