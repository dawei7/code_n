## General

Assign every node two coordinates relative to the root:

- `depth` is its distance downward from the root;
- `offset` is its horizontal column.

The root has `(depth, offset) = (0, 0)`. Moving to a left child adds one to depth and subtracts one from offset. Moving to a right child adds one to depth and adds one to offset.

Vertical order then means:

1. output smaller offsets before larger offsets;
2. within one offset, output smaller depths before larger depths;
3. when both coordinates match, preserve left-to-right tree order.

The exact source gathers coordinates with preorder depth-first search and sorts afterward. The manifest describes breadth-first traversal, but no queue appears in `solution.py`; this explanation follows the DFS and its stable-sort tie handling.

**Grouping nodes by column**

`d` is a `defaultdict(list)` keyed by horizontal offset. At each real node, the DFS appends `(depth, root.val)` to the list for that offset.

The offset recurrence is exact because every left edge moves one column left and every right edge moves one column right. Along any root-to-node path, the final offset is the number of right moves minus the number of left moves. Nodes with the same result belong to the same vertical column even if their paths and depths differ.

Depth is incremented on every edge, so it equals the node's row in the conceptual drawing. Storing both depth and value lets the later phase reorder a column top-to-bottom without losing the returned data.

**Why the DFS visits left before right**

The recursive order is:

1. record the current node;
2. traverse the complete left subtree;
3. traverse the complete right subtree.

This is preorder DFS with left-child priority. The priority matters only when two nodes share both depth and offset. Such nodes must come from different branches. The node reached through the horizontally earlier branch must appear first under the problem's left-to-right tie rule.

When nodes at one fixed depth are viewed in preorder's visitation sequence, left subtrees appear before right subtrees. Therefore, tied nodes are appended to their column list in the required left-to-right order.

DFS alone does not give top-to-bottom column order. A deep node in the left subtree may be appended before a shallower node from the right subtree that shares its column. This is why the stored depth and later sorting are necessary.

**Sorting columns from left to right**

After traversal, `d.items()` contains pairs `(offset, list)`. Calling `sorted(d.items())` orders those pairs by their integer key, from the most negative offset to the most positive.

This produces the required leftmost-to-rightmost column order. Unlike the BFS range optimization in the editorial, the exact source does not track minimum and maximum offsets; it sorts the discovered dictionary keys.

Every column between the minimum and maximum is in fact populated for a connected binary tree, but sorting works without relying on or separately proving that property.

**Sorting one column top to bottom**

For each column list `v`, the source runs

`v.sort(key=lambda x: x[0])`.

The key is only the depth. Values are deliberately not used as a secondary key because this problem does not ask tied nodes to be sorted numerically.

Python's list sort is stable: when two entries have equal keys, it preserves their previous relative order. Since left-before-right DFS appended equal-depth, equal-column nodes in the required horizontal order, the stable depth sort keeps that tie order unchanged.

This combination is essential. An unstable sort could reverse tied nodes, and sorting full tuples would use node value as an unintended secondary key.

After sorting, `[x[1] for x in v]` extracts only node values, and the resulting list is appended to `ans`.

**Tracing the first example**

For `[3,9,20,null,null,15,7]`, coordinates are:

| Value | Depth | Offset |
| --- | --- | --- |
| 3 | 0 | 0 |
| 9 | 1 | -1 |
| 20 | 1 | 1 |
| 15 | 2 | 0 |
| 7 | 2 | 2 |

Sorting offset keys gives -1, 0, 1, and 2. Column 0 sorts by depth as 3 then 15. The result is `[[9],[3,15],[20],[7]]`.

In the second example, nodes 0 and 1 both occupy depth 2 and offset 0. Node 0 lies in the root's left subtree, while node 1 lies in the right subtree. Left-first DFS appends 0 before 1. Sorting by depth keeps their equal-key order, producing central column `[3,0,1]` rather than sorting those values.

**Why every required ordering rule holds**

Every node is visited once and placed under its exact offset, so column membership is complete and exclusive. Sorting dictionary items orders all columns by offset. Sorting each list by depth orders nodes top-to-bottom.

For equal depth and offset, stable sorting retains the DFS insertion order, and left-first traversal matches the required left-to-right order. These three independent properties cover every comparison the output specification requires.

## Complexity detail

Let $N$ be the number of nodes and $h$ the tree height. DFS visits every node once, costing $O(N)$ time.

If there are $C$ distinct columns, sorting dictionary items costs $O(C\log C)$. If column $j$ contains $s_j$ nodes, sorting all column lists costs

$$
\sum_j O(s_j\log s_j),
$$

which is at most $O(N\log N)$. The total exact-source time complexity is therefore $O(N\log N)$ in the worst case.

The dictionary lists store one `(depth, value)` pair per node, using $O(N)$ space. The recursion stack uses $O(h)$ space, and sorting may use temporary memory. The returned lists contain $N$ values. Overall space is $O(N)$.

The manifest's $O(N)$ time bound belongs to breadth-first grouping combined with tracked contiguous column bounds, not to this DFS-plus-sorting implementation.

## Alternatives and edge cases

- **Breadth-first search with minimum and maximum offsets:** BFS naturally visits top-to-bottom and left-to-right. Group values by offset, track the offset range, then emit every column without sorting. This achieves $O(N)$ time and matches the manifest.
- **BFS plus sorted keys:** It avoids per-column depth sorting but still spends $O(C\log C)$ on column keys.
- **DFS sorting full tuples:** Sorting `(depth, value)` would incorrectly order same-position ties by numeric value rather than left-to-right occurrence.
- **DFS without storing depth:** Preorder does not globally visit shallower nodes before deeper nodes, so a column can be out of top-to-bottom order.
- **Right-before-left DFS:** Stable sorting would preserve the wrong horizontal tie order for equal coordinates.
- **Empty tree:** DFS returns immediately, the dictionary stays empty, and the result is `[]`.
- **Single node:** It is stored in offset 0 at depth 0, producing `[[root.val]]`.
- **Only left children:** Every node occupies a new smaller offset, so each output column contains one value.
- **Only right children:** Every node occupies a new larger offset, again producing singleton columns.
- **Several nodes in one column:** Depth sorting places ancestors and shallower cross-branch nodes before deeper nodes.
- **Equal node values:** Ordering depends on coordinates and traversal, not value uniqueness.
- **Negative values:** Values are payload only and do not affect ordering.
- **Same depth and column:** Stable sort plus left-first DFS supplies the required left-to-right tie resolution.
- **Different depth but same column:** Depth is the primary within-column key regardless of DFS visitation time.
- **Recursion depth:** With at most 100 nodes, a skewed tree is normally below Python's recursion limit; an iterative traversal would remove this environment dependency.
