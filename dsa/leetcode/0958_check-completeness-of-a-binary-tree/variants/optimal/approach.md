## General

**Completeness is a level-order no-gap rule**

In a complete binary tree, nodes fill positions from left to right with no missing position before a later real node.

Level-order traversal lists tree positions in exactly this order. If missing children are included as `None` placeholders, the sequence for a complete tree has a simple form:

- zero or more real nodes;
- followed only by `None` values.

The moment a `None` appears, no later queue entry may be a real node.

**Why the queue stores missing children**

The queue starts with the root. Whenever a real node is removed, both `node.left` and `node.right` are appended, even when one is `None`.

Ordinary BFS often skips missing children. That would lose the positional gaps that distinguish complete and incomplete trees.

For example, if a node has a right child but no left child, skipping the missing left pointer would make the right child appear to occupy the next normal position. Enqueuing `None` preserves evidence of the forbidden gap.

**Stop at the first gap**

The loop removes queue entries from the left.

If the entry is real, its two child positions are appended and traversal continues.

If the entry is `None`, the loop breaks. This is the first absent position in level-order layout. The tree is complete exactly when every remaining queued position is also absent.

The final expression:

`all(node is None for node in q)`

checks that no real node occurs after this gap.

**A complete example**

For level order `[1, 2, 3, 4, 5, 6]`:

- Root one appends two and three.
- Two appends four and five.
- Three appends six and `None`.
- Leaves append their missing children.

The first `None` appears only after all real nodes have been processed. Every remaining queue entry is also `None`, so the method returns true.

The last level need not be full. It only needs to occupy the leftmost positions, which is exactly what the no-real-node-after-gap rule captures.

**An incomplete example**

For tree `[1, 2, 3, 4, 5, None, 7]`, processing node three appends `None` for its left child and node seven for its right child.

When that first `None` eventually reaches the front, seven remains later in the queue. The final `all` test sees a real node and returns false.

This represents a last-level node to the right of an empty position.

**Why breaking early is safe**

After the first missing position, the algorithm no longer needs to expand nodes. It only needs to know whether any queued entry is real.

If all are `None`, expanding them would do nothing because missing nodes have no children. If a real entry exists, its mere presence proves incompleteness, regardless of descendants.

Therefore, stopping and inspecting the queue is equivalent to continuing a full placeholder traversal but avoids an infinite expansion of missing children.


Breadth-first order corresponds to the array-index layout of a binary tree: for every occupied position, its left and right child positions follow in level order.

If the tree is complete, occupied positions form a prefix of this layout. Hence after the first missing position, no real node can remain, and the method returns true.

If the method returns true, every real queued node occurred before every missing position. Thus occupied positions form a left-filled prefix at each level, all earlier levels are full, and the tree is complete.

The two directions prove equivalence.

## Complexity detail

Let `N` be the number of real nodes.

Every real node is removed at most once and appends two child references. The final generator scans at most `O(N)` queued placeholders and nodes. Total time is `O(N)`.

The queue can contain `O(N)` references at the widest level, so auxiliary space is `O(N)`.

The algorithm does not allocate tree nodes or modify the tree.

## Alternatives and edge cases

- **Continue BFS after a gap with a flag:** Set `seen_null` and reject any later real node. This is equivalent and may be easier to recognize.
- **Heap-style indices:** Assign root index one and children indices `2i` and `2i + 1`; completeness holds when maximum index equals node count. Large indices can grow on sparse deep trees.
- **Recursive node counting:** Compare subtree heights and shapes, but completeness conditions are more intricate than the level-order gap rule.
- **Single node:** Its children are missing, so all entries after the first gap are `None` and the result is true.
- **Right child without left child:** The queued right node follows a `None` left position and causes false.
- **Partially filled last level:** Valid only when nodes occupy a contiguous left prefix.
- **Missing position above the last level:** Any descendant later in BFS makes the tree incomplete.
- **Queueing both children:** Omitting `None` children destroys gap information.
- **Nonempty-root contract:** The input contains at least one node, but the same logic would also regard an empty tree as complete if supported.
- **No mutation:** The method is safe when callers retain the original tree.
