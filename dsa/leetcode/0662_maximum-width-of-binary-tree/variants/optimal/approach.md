## General

**Width must count invisible gaps**

The width of a level is not simply the number of non-null nodes on that level. It includes null positions between the leftmost and rightmost real nodes as those positions would appear in a complete binary tree.

Therefore, the algorithm needs a horizontal position for each real node, even though it does not enqueue null placeholders. Assigning complete-tree indices provides those positions compactly.

**Virtual complete-tree indexing**

The root receives index one. For a node with index `i`:

- its left child receives `2 * i`;
- its right child receives `2 * i + 1`.

The exact source writes these as `i << 1` and `i << 1 | 1`. Left shift by one multiplies a nonnegative integer by two. Bitwise OR with one sets the low bit, producing the odd right-child index.

These are virtual positions. A missing child is not stored, but its reserved index still creates a gap between real descendants on the same level.

For example, if the leftmost node on a level has index four and the rightmost has index seven, the width is `7 - 4 + 1 = 4`. Indices five and six count even if one or both represent missing nodes.

**Use breadth-first search to isolate levels**

The queue stores pairs `(node, virtual_index)`. It begins with the root at index one.

At the start of each outer iteration, the queue contains exactly the real nodes of one level, ordered from left to right. Because their indices also increase left to right:

- `q[0][1]` is the leftmost real position;
- `q[-1][1]` is the rightmost real position.

The current width is therefore:

`q[-1][1] - q[0][1] + 1`.

The maximum seen so far is updated before removing any current-level nodes.

**Why the queue length is captured**

The inner loop runs `range(len(q))`. Python evaluates `len(q)` when creating the range, so it captures the number of nodes currently on the level.

While those nodes are removed, their children are appended to the same queue. Processing exactly the captured count prevents the loop from continuing into the next level. Afterward, all current nodes are gone and the queue contains exactly the next level.

**Preserve left-to-right order**

Current-level nodes are removed from the front in left-to-right order. For each parent, the left child is appended before the right child. Parents themselves are processed left to right.

Consequently, children enter the queue in increasing virtual-index order. This justifies using the first and last queue entries as level boundaries without sorting.

**A gap example**

Imagine the leftmost path of a level descends through left children while the rightmost path descends through right children. Only two real nodes may remain, but their virtual indices can be far apart. The subtraction counts every complete-tree slot between them, matching the definition.

Enqueuing only real nodes keeps memory proportional to the actual tree, while indices retain the information that null placeholders would have contributed.

**Why the indexing is correct**

In a complete-tree layout, index one is the root, and the formulas `2i` and `2i + 1` assign consecutive left and right positions under every parent. By induction on depth, every real node receives exactly the position it would occupy if all missing nodes were filled with placeholders.

At a fixed level, complete-tree positions are consecutive integers. The number of positions from left boundary `L` through right boundary `R` inclusive is `R - L + 1`. Thus the computed width is exactly the required width for that level.

Breadth-first processing evaluates every nonempty level once, and `ans` retains the largest exact width. The returned value is therefore the maximum width of the tree.

**Why node values are irrelevant**

Only tree shape affects width. The traversal never reads `root.val`, so negative values, duplicates, and magnitudes have no influence.

## Complexity detail

Let `N` be the number of real tree nodes and `W` the maximum number of real nodes stored across a level frontier.

Each real node is enqueued once and dequeued once. Every visit performs constant structural work, so standard running time is `O(N)`.

The queue contains real nodes from at most one current frontier and children being assembled for the next. Its size is `O(W)` and at most `O(N)`. Stored indices and scalar variables do not change that bound, so auxiliary space is `O(N)` in the worst case.

In a very deep sparse tree, unnormalized virtual indices can contain `O(H)` bits, where `H` is height. Python handles arbitrary-size integers safely, but arithmetic is no longer literally constant-time in bit complexity. Normalizing indices per level avoids this practical growth while preserving all width differences.

## Alternatives and edge cases

- **Normalize each level's indices:** Subtract the first index of the level from every index before generating children. Width differences remain unchanged, and numbers stay bounded relative to the current width.

- **Depth-first traversal:** Record the first virtual index seen at each depth and compare every later index against it. This also takes `O(N)` time and `O(H)` recursion plus depth-map space.

- **Enqueue null placeholders:** It makes gaps explicit but can cause the queue to grow exponentially with height. Virtual indices preserve the same information without storing nulls.

- **Count only queue nodes:** This returns the number of real nodes, not the defined width when gaps lie between endpoints.

- **Ordinary node depth without position:** Depth groups levels but cannot measure horizontal gaps. Both depth and complete-tree position are needed.

- **Single-node tree:** The first and last indices are both one, producing width one.

- **Completely one-sided tree:** Each level has one real node, so every width is one even though its virtual index grows.

- **Sparse outer branches:** Two nodes can create a large width despite few real nodes. The endpoint subtraction handles this case.

- **Missing nodes outside the endpoints:** They do not count. Only positions between the leftmost and rightmost real nodes are included, exactly as subtraction specifies.

- **Nonempty-root guarantee:** The source guarantees at least one node. The exact initialization would otherwise enqueue `None` and later try to access its children.

- **Large virtual indices:** Python avoids overflow, but level normalization is advisable in fixed-width languages and for strict bit-cost efficiency.

- **Using `2i + 1` for the left child:** Swapping formulas would reverse or distort positions. The exact left-even, right-odd convention must remain consistent.

- **Updating width after processing:** That can also work if level boundaries are saved first. The exact source updates before mutation, when the queue endpoints directly represent the whole level.
