/**
 * LayoutRoot.tsx — top of the layout tree. Reads the tree from
 * the layout store and dispatches to SplitPane (which recurses).
 *
 * Narrow-window auto-collapse: if the main area is < 720px wide,
 * replace the tree with a single leaf (the first leaf of the
 * current tree, with all tabs merged in). Below ~720px a 2x2
 * grid is unusable. The collapse is one-way per session — when
 * the window grows back, the user can pick a layout preset from
 * the header to restore. (Restoring automatically is tricky
 * because we'd need to remember the previous tree shape.)
 */
import { useEffect, useRef } from 'react';
import { useLayoutStore } from '../../store/useLayoutStore';
import { useAppStore } from '../../store/useAppStore';
import { SplitPane } from './SplitPane';
import { allLeaves, type LayoutNode } from './tree-ops';


const NARROW_WIDTH = 720;


function collapseToSingleLeaf(tree: LayoutNode): LayoutNode {
  const leaves = allLeaves(tree);
  if (leaves.length === 0) return tree;
  const first = leaves[0]!;
  const seen = new Set<string>();
  const tabIds: string[] = [];
  for (const l of leaves) {
    for (const t of l.tabIds) {
      if (!seen.has(t)) { seen.add(t); tabIds.push(t); }
    }
  }
  return {
    kind: 'leaf',
    id: first.id,
    tabIds,
    activeTabId: first.activeTabId ?? tabIds[0] ?? null,
  };
}


export function LayoutRoot() {
  const tree = useLayoutStore((s) => s.tree);
  const replaceTree = useLayoutStore((s) => s.replaceTree);
  const challenges = useAppStore((s) => s.challenges);
  const loadChallenges = useAppStore((s) => s.loadChallenges);
  const containerRef = useRef<HTMLDivElement | null>(null);
  const collapsedRef = useRef(false);

  // Make sure challenges are loaded (in case the LayoutRoot mounts
  // before AppShell's effect did).
  useEffect(() => {
    if (challenges.length === 0) {
      void loadChallenges();
    }
  }, [challenges.length, loadChallenges]);

  // Narrow-window observer: collapse to a single leaf when the
  // container width drops below NARROW_WIDTH. We only collapse
  // once per session — if the user widens the window we leave
  // the single-leaf layout alone (the preset dropdown restores).
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;
    const ro = new ResizeObserver((entries) => {
      const w = entries[0]?.contentRect.width ?? Infinity;
      if (w < NARROW_WIDTH && !collapsedRef.current && tree.kind === 'split') {
        collapsedRef.current = true;
        replaceTree(collapseToSingleLeaf(tree));
      }
    });
    ro.observe(el);
    return () => ro.disconnect();
  }, [tree, replaceTree]);

  return (
    <div ref={containerRef} className="w-full h-full min-w-0 min-h-0">
      <SplitPane node={tree} />
    </div>
  );
}
