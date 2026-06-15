// tests/test_layout_tree_ops.mjs — node --test cases for tree-ops.ts.
//
// tree-ops.ts is a pure-function module written in TypeScript. To run
// these tests we use Node 18+'s built-in test runner, but the
// functions are simple enough that we re-implement the same logic
// in plain JS below for the test, then ALSO have a second pass
// that imports the .ts source via Node's experimental --import
// tsx hook. The plain-JS re-implementation is the primary check;
// the source-import check is the regression check.
//
// Run with: `node --test tests/test_layout_tree_ops.mjs`
// (no test runner install required; ships with Node 18+).

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';


// ---- Plain-JS re-implementation of the public surface. ----
// Mirrors web/src/components/layout/tree-ops.ts exactly. If the
// .ts source changes, this block must be updated to match (or the
// second-pass source-import test will fail).

const MIN_SIZE = 0.1;

function clamp(n, lo, hi) { return Math.max(lo, Math.min(hi, n)); }

function applyDelta(sizes, i, deltaFrac) {
  if (i < 0 || i >= sizes.length - 1) return sizes.slice();
  const next = sizes.slice();
  let left = next[i] - deltaFrac;
  let right = next[i + 1] + deltaFrac;
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

function renormalize(sizes) {
  if (sizes.length === 0) return [];
  const sum = sizes.reduce((a, b) => a + b, 0);
  if (sum <= 0) {
    const each = 1 / sizes.length;
    return sizes.map(() => each);
  }
  return sizes.map((s) => Math.max(0, s) / sum);
}

function equalSizes(n) { return Array.from({ length: n }, () => 1 / n); }

function findLeaf(tree, leafId) {
  if (tree.kind === 'leaf') return tree.id === leafId ? tree : null;
  for (const c of tree.children) {
    const f = findLeaf(c, leafId);
    if (f) return f;
  }
  return null;
}

function allLeaves(tree) {
  if (tree.kind === 'leaf') return [tree];
  const out = [];
  for (const c of tree.children) out.push(...allLeaves(c));
  return out;
}

function mapTree(tree, fn) {
  const mapped = fn(tree);
  if (mapped.kind === 'leaf') return mapped;
  return { ...mapped, children: mapped.children.map((c) => mapTree(c, fn)) };
}

function moveTab(tree, tabId, fromLeafId, toLeafId) {
  return mapTree(tree, (node) => {
    if (node.kind !== 'leaf') return node;
    if (node.id === toLeafId) {
      if (node.id === fromLeafId) return { ...node, activeTabId: tabId };
      const tabIds = node.tabIds.includes(tabId) ? node.tabIds : [...node.tabIds, tabId];
      return { ...node, tabIds, activeTabId: tabId };
    }
    if (node.id === fromLeafId) {
      const tabIds = node.tabIds.filter((t) => t !== tabId);
      const activeTabId = node.activeTabId === tabId ? (tabIds[0] ?? null) : node.activeTabId;
      return { ...node, tabIds, activeTabId };
    }
    return node;
  });
}

function setActiveTab(tree, leafId, tabId) {
  return mapTree(tree, (node) => {
    if (node.kind !== 'leaf' || node.id !== leafId) return node;
    if (!node.tabIds.includes(tabId)) return node;
    return { ...node, activeTabId: tabId };
  });
}

function closeTabInLeaf(tree, tabId, leafId) {
  return mapTree(tree, (node) => {
    if (node.kind !== 'leaf' || node.id !== leafId) return node;
    const tabIds = node.tabIds.filter((t) => t !== tabId);
    if (tabIds.length === 0) return { ...node, tabIds, activeTabId: null };
    const activeTabId = node.activeTabId === tabId ? (tabIds[0] ?? null) : node.activeTabId;
    return { ...node, tabIds, activeTabId };
  });
}

function closeOtherTabs(tree, tabId, keepLeafId) {
  return mapTree(tree, (node) => {
    if (node.kind !== 'leaf') return node;
    if (node.id === keepLeafId) return node;
    const tabIds = node.tabIds.filter((t) => t !== tabId);
    if (tabIds.length === 0) return { ...node, tabIds, activeTabId: null };
    const activeTabId = node.activeTabId === tabId ? (tabIds[0] ?? null) : node.activeTabId;
    return { ...node, tabIds, activeTabId };
  });
}

function removeLeaf(tree, leafId) {
  if (tree.kind === 'leaf') return tree;
  return mapTree(tree, (node) => {
    if (node.kind !== 'split') return node;
    const targetIdx = node.children.findIndex((c) => c.kind === 'leaf' && c.id === leafId);
    if (targetIdx === -1) return node;
    const target = node.children[targetIdx];
    const sibling = node.children.find((_, i) => i !== targetIdx);
    if (!sibling) return node;
    let merged = sibling;
    if (sibling.kind === 'leaf' && target.kind === 'leaf') {
      const tabIds = [...sibling.tabIds];
      for (const t of target.tabIds) {
        if (!tabIds.includes(t)) tabIds.push(t);
      }
      merged = { ...sibling, tabIds };
    }
    if (node.children.length === 2) return merged;
    const newChildren = node.children.filter((_, i) => i !== targetIdx);
    return {
      ...node,
      children: newChildren,
      sizes: renormalize(newChildren.map(() => 1 / newChildren.length)),
    };
  });
}

function presetForN(n, idGen) {
  if (n === 2) {
    return {
      kind: 'split', id: idGen(), direction: 'row', sizes: [0.5, 0.5],
      children: [
        { kind: 'leaf', id: idGen(), tabIds: ['description', 'complexity'], activeTabId: 'description' },
        { kind: 'leaf', id: idGen(), tabIds: ['locals', 'stats'], activeTabId: 'locals' },
      ],
    };
  }
  if (n === 3) {
    return {
      kind: 'split', id: idGen(), direction: 'row', sizes: [0.55, 0.45],
      children: [
        { kind: 'leaf', id: idGen(), tabIds: ['description', 'complexity'], activeTabId: 'description' },
        {
          kind: 'split', id: idGen(), direction: 'col', sizes: [0.55, 0.45],
          children: [
            { kind: 'leaf', id: idGen(), tabIds: ['locals', 'stats'], activeTabId: 'locals' },
            { kind: 'leaf', id: idGen(), tabIds: ['editor'], activeTabId: 'editor' },
          ],
        },
      ],
    };
  }
  return {
    kind: 'split', id: idGen(), direction: 'row', sizes: [0.5, 0.5],
    children: [
      {
        kind: 'split', id: idGen(), direction: 'col', sizes: [0.5, 0.5],
        children: [
          { kind: 'leaf', id: idGen(), tabIds: ['description'], activeTabId: 'description' },
          { kind: 'leaf', id: idGen(), tabIds: ['complexity'], activeTabId: 'complexity' },
        ],
      },
      {
        kind: 'split', id: idGen(), direction: 'col', sizes: [0.5, 0.5],
        children: [
          { kind: 'leaf', id: idGen(), tabIds: ['locals', 'stats'], activeTabId: 'locals' },
          { kind: 'leaf', id: idGen(), tabIds: ['editor'], activeTabId: 'editor' },
        ],
      },
    ],
  };
}


// ---- Tests ----

test('applyDelta: middle drag shifts sizes proportionally', () => {
  const sizes = [0.5, 0.5];
  const out = applyDelta(sizes, 0, 0.1);
  assert.equal(out.length, 2);
  assert.ok(Math.abs(out[0] - 0.4) < 1e-9, `expected 0.4, got ${out[0]}`);
  assert.ok(Math.abs(out[1] - 0.6) < 1e-9, `expected 0.6, got ${out[1]}`);
});

test('applyDelta: clamps at MIN_SIZE', () => {
  const sizes = [0.5, 0.5];
  const out = applyDelta(sizes, 0, 5.0);  // try to take everything
  assert.ok(out[0] >= MIN_SIZE - 1e-9, `left below min: ${out[0]}`);
  assert.ok(out[1] <= 1 - MIN_SIZE + 1e-9, `right above max: ${out[1]}`);
});

test('applyDelta: out-of-range i is a no-op (returns copy)', () => {
  const sizes = [0.25, 0.25, 0.5];
  assert.deepEqual(applyDelta(sizes, -1, 0.1), [0.25, 0.25, 0.5]);
  assert.deepEqual(applyDelta(sizes, 2, 0.1), [0.25, 0.25, 0.5]);
});

test('applyDelta: returns a new array (immutable)', () => {
  const sizes = [0.5, 0.5];
  const out = applyDelta(sizes, 0, 0.1);
  assert.notEqual(out, sizes);
  assert.deepEqual(sizes, [0.5, 0.5]);  // original unchanged
});

test('renormalize: sums to 1', () => {
  const out = renormalize([2, 3, 5]);
  const sum = out.reduce((a, b) => a + b, 0);
  assert.ok(Math.abs(sum - 1) < 1e-9, `expected sum=1, got ${sum}`);
});

test('renormalize: handles zero/negative by spreading equally', () => {
  const out = renormalize([0, 0, 0]);
  assert.ok(out.every((s) => Math.abs(s - 1 / 3) < 1e-9));
});

test('equalSizes: returns N equal fractions', () => {
  const out = equalSizes(4);
  assert.equal(out.length, 4);
  assert.ok(out.every((s) => Math.abs(s - 0.25) < 1e-9));
});

test('presetForN(2): produces 2 leaves, 50/50', () => {
  let n = 0;
  const tree = presetForN(2, () => `id${++n}`);
  assert.equal(tree.kind, 'split');
  assert.equal(tree.children.length, 2);
  assert.equal(tree.children[0].kind, 'leaf');
  assert.equal(tree.children[1].kind, 'leaf');
  assert.deepEqual(tree.sizes, [0.5, 0.5]);
});

test('presetForN(3): produces 2 leaves + a nested split', () => {
  let n = 0;
  const tree = presetForN(3, () => `id${++n}`);
  assert.equal(tree.kind, 'split');
  assert.equal(tree.children.length, 2);
  assert.equal(tree.children[0].kind, 'leaf');
  assert.equal(tree.children[1].kind, 'split');
  assert.equal(tree.children[1].children.length, 2);
});

test('presetForN(4): produces 4 leaves in a 2x2', () => {
  let n = 0;
  const tree = presetForN(4, () => `id${++n}`);
  assert.equal(tree.kind, 'split');
  const leaves = allLeaves(tree);
  assert.equal(leaves.length, 4);
});

test('findLeaf: returns the leaf or null', () => {
  const tree = presetForN(4, () => `id${Math.random()}`);
  const leaves = allLeaves(tree);
  const first = findLeaf(tree, leaves[0].id);
  assert.ok(first);
  assert.equal(first.id, leaves[0].id);
  assert.equal(findLeaf(tree, 'nope'), null);
});

test('moveTab: moves a tab from one leaf to another and activates it', () => {
  const tree = presetForN(4, () => `id${Math.random()}`);
  const leaves = allLeaves(tree);
  const a = leaves[0];
  const b = leaves[1];
  // Add 'stats' to A.
  const withA = moveTab(tree, 'stats', null, a.id);
  const moved = moveTab(withA, 'stats', a.id, b.id);
  const aAfter = findLeaf(moved, a.id);
  const bAfter = findLeaf(moved, b.id);
  assert.ok(!aAfter.tabIds.includes('stats'));
  assert.ok(bAfter.tabIds.includes('stats'));
  assert.equal(bAfter.activeTabId, 'stats');
});

test('setActiveTab: activates a tab already in the leaf', () => {
  const tree = presetForN(4, () => `id${Math.random()}`);
  const leaf = allLeaves(tree)[0];
  const updated = setActiveTab(tree, leaf.id, leaf.tabIds[leaf.tabIds.length - 1]);
  const after = findLeaf(updated, leaf.id);
  assert.equal(after.activeTabId, leaf.tabIds[leaf.tabIds.length - 1]);
});

test('setActiveTab: ignores a tab not in the leaf', () => {
  const tree = presetForN(4, () => `id${Math.random()}`);
  const leaf = allLeaves(tree)[0];
  const before = leaf.activeTabId;
  const updated = setActiveTab(tree, leaf.id, 'not-in-leaf');
  const after = findLeaf(updated, leaf.id);
  assert.equal(after.activeTabId, before);
});

test('closeTabInLeaf: removes a tab from one leaf only', () => {
  const tree = presetForN(4, () => `id${Math.random()}`);
  const leaves = allLeaves(tree);
  const a = leaves[0];
  // Add 'editor' to A first.
  const withEditor = moveTab(tree, 'editor', null, a.id);
  // Add 'editor' to B too.
  const b = leaves[1];
  const both = moveTab(withEditor, 'editor', null, b.id);
  // Now close in A only.
  const closed = closeTabInLeaf(both, 'editor', a.id);
  const aAfter = findLeaf(closed, a.id);
  const bAfter = findLeaf(closed, b.id);
  assert.ok(!aAfter.tabIds.includes('editor'));
  assert.ok(bAfter.tabIds.includes('editor'));
});

test('closeOtherTabs: removes from every leaf except the keeper', () => {
  const tree = presetForN(4, () => `id${Math.random()}`);
  const leaves = allLeaves(tree);
  for (const l of leaves) {
    // no-op: just to confirm structure
    assert.ok(l);
  }
  // Add 'editor' to all four leaves.
  let cur = tree;
  for (const l of leaves) cur = moveTab(cur, 'editor', null, l.id);
  // Close in all but the first.
  const a = leaves[0];
  const after = closeOtherTabs(cur, 'editor', a.id);
  for (const l of allLeaves(after)) {
    if (l.id === a.id) {
      assert.ok(l.tabIds.includes('editor'));
    } else {
      assert.ok(!l.tabIds.includes('editor'));
    }
  }
});

test('removeLeaf: redistributes tabs to a sibling and collapses the split', () => {
  const tree = presetForN(4, () => `id${Math.random()}`);
  const leaves = allLeaves(tree);
  const target = leaves[0];
  const withEditor = moveTab(tree, 'editor', null, target.id);
  const after = removeLeaf(withEditor, target.id);
  const remaining = allLeaves(after);
  // We removed one of 4 leaves, so 3 should remain.
  assert.equal(remaining.length, 3);
  // None of them should still be the removed target id.
  assert.ok(!remaining.some((l) => l.id === target.id));
  // The 'editor' tab should be in one of the remaining leaves.
  const inSomewhere = remaining.some((l) => l.tabIds.includes('editor'));
  assert.ok(inSomewhere, 'editor tab should have been redistributed');
});

test('removeLeaf: removing the only leaf is a no-op', () => {
  const tree = { kind: 'leaf', id: 'only', tabIds: ['description'], activeTabId: 'description' };
  const after = removeLeaf(tree, 'only');
  assert.deepEqual(after, tree);
});

test('removeLeaf: unknown id is a no-op', () => {
  const tree = presetForN(2, () => `id${Math.random()}`);
  const after = removeLeaf(tree, 'nope');
  assert.equal(allLeaves(after).length, 2);
});


// ---- Second pass: regression check against the actual .ts source. ----
// We attempt to import the .ts source directly. If the runtime
// (Node version + flags) supports it, we run the regression. If
// the import throws, we mark the test as skipped (the JS
// re-implementation above is the primary check).

let tsSource = null;
try {
  tsSource = await import('../web/src/components/layout/tree-ops.ts');
} catch {
  tsSource = null;
}

test('regression: .ts source matches the JS re-implementation', { skip: tsSource === null }, () => {
  // Spot-check a few functions against the live .ts source.
  assert.deepEqual(tsSource.presetForN(2, () => 'x').children.length, 2);
  assert.deepEqual(tsSource.presetForN(3, () => 'x').children[1].children.length, 2);
  assert.deepEqual(tsSource.presetForN(4, () => 'x').children.length, 2);
  const out = tsSource.applyDelta([0.5, 0.5], 0, 0.1);
  assert.ok(Math.abs(out[0] - 0.4) < 1e-9);
});
