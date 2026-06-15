/**
 * tree-ops.ts — pure functions for the layout pane tree.
 *
 * The tree is recursive: split nodes have direction + sizes + children;
 * leaf nodes hold a list of tab ids and an active tab id. These helpers
 * are the *only* JS unit-testable seam in the layout code; everything
 * else is React/Zustand glue. Covered by tests/test_layout_tree_ops.mjs
 * via `node --test`.
 *
 * Invariants maintained by every mutator below:
 *   - SplitNode.sizes is normalized to sum to 1.
 *   - Each child size is in [MIN_SIZE, 1 - MIN_SIZE] (so no child
 *     can be made smaller than MIN_SIZE by a drag).
 *   - LeafNode.tabIds is deduplicated; activeTabId (if set) is
 *     present in tabIds.
 */

export type LayoutNode =
  | {
      kind: 'split';
      id: string;
      direction: 'row' | 'col';
      sizes: number[];
      children: LayoutNode[];
    }
  | {
      kind: 'leaf';
      id: string;
      tabIds: string[];
      activeTabId: string | null;
    };


/** Lower bound on a single child's share of a split. */
export const MIN_SIZE = 0.1;


/** Clamp `n` to [lo, hi]. */
function clamp(n: number, lo: number, hi: number): number {
  return Math.max(lo, Math.min(hi, n));
}


/**
 * Adjust sizes[] by shifting deltaFrac from child i to child i+1
 * (negative delta shifts the other way). Clamps each side to
 * [MIN_SIZE, 1 - MIN_SIZE] and renormalizes so the array still
 * sums to 1. Returns a NEW array (immutable).
 */
export function applyDelta(
  sizes: number[],
  i: number,
  deltaFrac: number,
): number[] {
  if (i < 0 || i >= sizes.length - 1) return sizes.slice();
  const next = sizes.slice();
  // Proposed: take `deltaFrac` from i, give to i+1.
  let left = next[i]! - deltaFrac;
  let right = next[i + 1]! + deltaFrac;
  // Clamp both sides.
  const maxLeft = 1 - MIN_SIZE;
  const minLeft = MIN_SIZE;
  const minRight = MIN_SIZE;
  const maxRight = 1 - MIN_SIZE;
  if (left < minLeft) {
    const overshoot = minLeft - left;
    left = minLeft;
    right = clamp(right - overshoot, minRight, maxRight);
  } else if (left > maxLeft) {
    const overshoot = left - maxLeft;
    left = maxLeft;
    right = clamp(right + overshoot, minRight, maxRight);
  }
  if (right < minRight) {
    const overshoot = minRight - right;
    right = minRight;
    left = clamp(left - overshoot, minLeft, maxLeft);
  } else if (right > maxRight) {
    const overshoot = right - maxRight;
    right = maxRight;
    left = clamp(left + overshoot, minLeft, maxLeft);
  }
  next[i] = left;
  next[i + 1] = right;
  return next;
}


/** Find a leaf by id. Returns null if not found. */
export function findLeaf(tree: LayoutNode, leafId: string): LeafNode | null {
  if (tree.kind === 'leaf') return tree.id === leafId ? tree : null;
  for (const child of tree.children) {
    const found = findLeaf(child, leafId);
    if (found) return found;
  }
  return null;
}


/** All leaf nodes in tree order (depth-first). */
export function allLeaves(tree: LayoutNode): LeafNode[] {
  if (tree.kind === 'leaf') return [tree];
  const out: LeafNode[] = [];
  for (const child of tree.children) {
    out.push(...allLeaves(child));
  }
  return out;
}


/** Walk the tree, calling `fn` on every node. */
export function walk(
  tree: LayoutNode,
  fn: (node: LayoutNode, parent: LayoutNode | null) => void,
  parent: LayoutNode | null = null,
): void {
  fn(tree, parent);
  if (tree.kind === 'split') {
    for (const c of tree.children) walk(c, fn, tree);
  }
}


/**
 * Update a single split node's sizes by id. Returns a new tree.
 * If the split id is not found, returns the original tree (no-op).
 */
export function setSizes(
  tree: LayoutNode,
  splitId: string,
  sizes: number[],
): LayoutNode {
  if (tree.kind === 'leaf') return tree;
  if (tree.id === splitId) {
    return { ...tree, sizes: renormalize(sizes) };
  }
  return {
    ...tree,
    children: tree.children.map((c) => setSizes(c, splitId, sizes)),
  };
}


/** Normalize `sizes` to sum to 1; pads/clamps as needed. */
export function renormalize(sizes: number[]): number[] {
  if (sizes.length === 0) return [];
  const sum = sizes.reduce((a, b) => a + b, 0);
  if (sum <= 0) {
    const each = 1 / sizes.length;
    return sizes.map(() => each);
  }
  return sizes.map((s) => Math.max(0, s) / sum);
}


/** Reset a split to equal sizes. */
export function equalSizes(n: number): number[] {
  return Array.from({ length: n }, () => 1 / n);
}


/**
 * Move `tabId` from `fromLeafId` to `toLeafId` (adds it to the
 * target's tabIds and makes it the active tab there; also removes
 * it from the source leaf). If the tab is not in the source leaf,
 * this is treated as "add to target". Returns a new tree.
 */
export function moveTab(
  tree: LayoutNode,
  tabId: string,
  fromLeafId: string | null,
  toLeafId: string,
): LayoutNode {
  return mapTree(tree, (node) => {
    if (node.kind !== 'leaf') return node;
    if (node.id === toLeafId) {
      if (node.id === fromLeafId) {
        // Same leaf; just activate.
        return { ...node, activeTabId: tabId };
      }
      // Add the tab to the target if it isn't there already.
      const tabIds = node.tabIds.includes(tabId)
        ? node.tabIds
        : [...node.tabIds, tabId];
      return { ...node, tabIds, activeTabId: tabId };
    }
    if (node.id === fromLeafId) {
      const tabIds = node.tabIds.filter((t) => t !== tabId);
      const activeTabId =
        node.activeTabId === tabId
          ? (tabIds[0] ?? null)
          : node.activeTabId;
      return { ...node, tabIds, activeTabId };
    }
    return node;
  });
}


/** Set the active tab of a specific leaf. */
export function setActiveTab(
  tree: LayoutNode,
  leafId: string,
  tabId: string,
): LayoutNode {
  return mapTree(tree, (node) => {
    if (node.kind !== 'leaf' || node.id !== leafId) return node;
    if (!node.tabIds.includes(tabId)) return node;
    return { ...node, activeTabId: tabId };
  });
}


/** Remove a tab from one leaf (VSCode "Close" on a tab). */
export function closeTabInLeaf(
  tree: LayoutNode,
  tabId: string,
  leafId: string,
): LayoutNode {
  return mapTree(tree, (node) => {
    if (node.kind !== 'leaf' || node.id !== leafId) return node;
    const tabIds = node.tabIds.filter((t) => t !== tabId);
    if (tabIds.length === 0) {
      return { ...node, tabIds, activeTabId: null };
    }
    const activeTabId =
      node.activeTabId === tabId ? (tabIds[0] ?? null) : node.activeTabId;
    return { ...node, tabIds, activeTabId };
  });
}


/**
 * Remove `tabId` from every leaf except `keepLeafId`. (VSCode
 * "Close others" on a tab.) If `keepLeafId` is null, removes from
 * every leaf (full global remove).
 */
export function closeOtherTabs(
  tree: LayoutNode,
  tabId: string,
  keepLeafId: string | null,
): LayoutNode {
  return mapTree(tree, (node) => {
    if (node.kind !== 'leaf') return node;
    if (node.id === keepLeafId) return node;
    const tabIds = node.tabIds.filter((t) => t !== tabId);
    if (tabIds.length === 0) {
      return { ...node, tabIds, activeTabId: null };
    }
    const activeTabId =
      node.activeTabId === tabId ? (tabIds[0] ?? null) : node.activeTabId;
    return { ...node, tabIds, activeTabId };
  });
}


/**
 * Remove a leaf by id. Its tabs are redistributed to a sibling
 * leaf in the same parent split (the first sibling, by index).
 * If the parent split ends up with a single child, it collapses
 * to that child (and the replacement propagates upward through
 * the tree, collapsing ancestor splits that are now singletons).
 */
export function removeLeaf(tree: LayoutNode, leafId: string): LayoutNode {
  // Edge case: a single-leaf tree cannot have a leaf removed.
  if (tree.kind === 'leaf') return tree;

  // Recursive walker. For each split we visit, check whether the
  // target leaf is one of our direct children. If so, merge its
  // tabs into a sibling and either return the merged sibling (if
  // the split has exactly 2 children) or return a copy with the
  // target removed (if it had 3+). Either return value replaces
  // this split in the parent — and the parent's collapse chain
  // works the same way via mapTree.
  return mapTree(tree, (node) => {
    if (node.kind !== 'split') return node;
    const targetIdx = node.children.findIndex(
      (c) => c.kind === 'leaf' && c.id === leafId,
    );
    if (targetIdx === -1) return node;
    const target = node.children[targetIdx]!;
    // Pick a sibling to absorb the target's tabs.
    const sibling = node.children.find((_, i) => i !== targetIdx);
    if (!sibling) return node;  // shouldn't happen for a real tree
    let merged: LayoutNode = sibling;
    if (sibling.kind === 'leaf' && target.kind === 'leaf') {
      const tabIds = [...sibling.tabIds];
      for (const t of target.tabIds) {
        if (!tabIds.includes(t)) tabIds.push(t);
      }
      merged = { ...sibling, tabIds };
    }
    if (node.children.length === 2) {
      // Collapse this split to the merged sibling. The parent
      // will see this single child and may itself collapse.
      return merged;
    }
    // 3+ children: just drop the target leaf and rebalance sizes.
    const newChildren = node.children.filter((_, i) => i !== targetIdx);
    return {
      ...node,
      children: newChildren,
      sizes: renormalize(newChildren.map(() => 1 / newChildren.length)),
    };
  });
}


/** Type of a leaf node, exported for the registry. */
export interface LeafNode {
  kind: 'leaf';
  id: string;
  tabIds: string[];
  activeTabId: string | null;
}


/** Apply `fn` to every node in the tree, returning a new tree. */
function mapTree(
  tree: LayoutNode,
  fn: (node: LayoutNode) => LayoutNode,
): LayoutNode {
  const mapped = fn(tree);
  if (mapped.kind === 'leaf') return mapped;
  return {
    ...mapped,
    children: mapped.children.map((c) => mapTree(c, fn)),
  };
}


/**
 * Build a default tree for a given number of regions.
 *   - 1 → one leaf with every default tab
 *   - 2 → single split (row) with 2 leaves, 50/50
 *   - 3 → split (row): big-left leaf + right-split (col) with 2 leaves
 *   - 4 → split (row) of 2 split (col)s, each with 2 leaves
 *   - 5 → 2 rows x 3 cols, with one empty picker leaf
 *   - 6 → 2 rows x 3 cols, with one empty picker leaf
 *
 * Each preset's tab assignment is curated so the most useful
 * information is always in view. n=5/6 include one empty leaf
 * as a "drop a tab here" slot — the empty-pane picker still
 * works, but the user CANNOT add NEW panes (that's a header
 * preset decision, not a runtime action).
 */
export function presetForN(
  n: 1 | 2 | 3 | 4 | 5 | 6,
  idGen: () => string,
): LayoutNode {
  if (n === 1) {
    return {
      kind: 'leaf',
      id: idGen(),
      tabIds: ['description', 'complexity', 'locals'],
      activeTabId: 'description',
    };
  }
  if (n === 2) {
    return {
      kind: 'split',
      id: idGen(),
      direction: 'row',
      sizes: [0.5, 0.5],
      children: [
        { kind: 'leaf', id: idGen(), tabIds: ['description', 'complexity'], activeTabId: 'description' },
        { kind: 'leaf', id: idGen(), tabIds: ['locals'], activeTabId: 'locals' },
      ],
    };
  }
  if (n === 3) {
    return {
      kind: 'split',
      id: idGen(),
      direction: 'row',
      sizes: [0.55, 0.45],
      children: [
        { kind: 'leaf', id: idGen(), tabIds: ['description', 'complexity'], activeTabId: 'description' },
        {
          kind: 'split',
          id: idGen(),
          direction: 'col',
          sizes: [0.55, 0.45],
          children: [
            { kind: 'leaf', id: idGen(), tabIds: ['locals'], activeTabId: 'locals' },
            { kind: 'leaf', id: idGen(), tabIds: ['editor'], activeTabId: 'editor' },
          ],
        },
      ],
    };
  }
  if (n === 4) {
    return {
      kind: 'split',
      id: idGen(),
      direction: 'row',
      sizes: [0.5, 0.5],
      children: [
        {
          kind: 'split',
          id: idGen(),
          direction: 'col',
          sizes: [0.5, 0.5],
          children: [
            { kind: 'leaf', id: idGen(), tabIds: ['description'], activeTabId: 'description' },
            { kind: 'leaf', id: idGen(), tabIds: ['complexity'], activeTabId: 'complexity' },
          ],
        },
        {
          kind: 'split',
          id: idGen(),
          direction: 'col',
          sizes: [0.5, 0.5],
          children: [
            { kind: 'leaf', id: idGen(), tabIds: ['locals'], activeTabId: 'locals' },
            { kind: 'leaf', id: idGen(), tabIds: ['editor'], activeTabId: 'editor' },
          ],
        },
      ],
    };
  }
  if (n === 5) {
    // 2 rows x 2 cols.
    return {
      kind: 'split',
      id: idGen(),
      direction: 'row',
      sizes: [0.5, 0.5],
      children: [
        {
          kind: 'split',
          id: idGen(),
          direction: 'col',
          sizes: [0.5, 0.5],
          children: [
            { kind: 'leaf', id: idGen(), tabIds: ['description'], activeTabId: 'description' },
            { kind: 'leaf', id: idGen(), tabIds: ['complexity'], activeTabId: 'complexity' },
          ],
        },
        {
          kind: 'split',
          id: idGen(),
          direction: 'col',
          sizes: [0.5, 0.5],
          children: [
            { kind: 'leaf', id: idGen(), tabIds: ['locals'], activeTabId: 'locals' },
            { kind: 'leaf', id: idGen(), tabIds: ['editor'], activeTabId: 'editor' },
          ],
        },
      ],
    };
  }
  // n === 6: 2 rows x 3 cols.
  return {
    kind: 'split',
    id: idGen(),
    direction: 'row',
    sizes: [0.5, 0.5],
    children: [
      {
        kind: 'split',
        id: idGen(),
        direction: 'col',
        sizes: [0.34, 0.33, 0.33],
        children: [
          { kind: 'leaf', id: idGen(), tabIds: ['description'], activeTabId: 'description' },
          { kind: 'leaf', id: idGen(), tabIds: ['complexity'], activeTabId: 'complexity' },
          { kind: 'leaf', id: idGen(), tabIds: ['locals'], activeTabId: 'locals' },
        ],
      },
      {
        kind: 'split',
        id: idGen(),
        direction: 'col',
        sizes: [0.5, 0.5],
        children: [
          { kind: 'leaf', id: idGen(), tabIds: ['editor'], activeTabId: 'editor' },
          { kind: 'leaf', id: idGen(), tabIds: ['aiReport'], activeTabId: 'aiReport' },
        ],
      },
    ],
  };
}
