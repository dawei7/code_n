## General
A complete tree fills every level except possibly the last, whose nodes occupy a left prefix. At any nonempty root, this
guarantees that one child subtree is perfect and can be counted from its height without visiting its nodes.

Measure each child's height by repeatedly following left links:

- If the heights are equal at `h`, the left subtree is perfect with $2^h - 1$ nodes. The root and that subtree contribute
  $2^h$, and only the right subtree remains unresolved.
- If the left height is larger, the right subtree is perfect at its smaller height. The root and that subtree contribute
  `2 ** right_height`, and only the left subtree remains unresolved.

The candidate accumulates the perfect contribution and advances `root` to the unresolved child in a loop. For the
six-node tree `[1,2,3,4,5,6]`, equal child heights first contribute four nodes and move to the right child. Its unequal
child heights then contribute one node and move left, where the final node contributes one, totaling six.

Equal child heights mean the last level has reached the right subtree, so completeness forces the left subtree to be
full. Unequal heights mean the last level has not reached the right subtree's bottom level, so that right subtree is
perfect one level shorter. In either case the added power of two counts exactly the current root and one perfect child,
while completeness is preserved in the remaining child. Repeating until `root` is null partitions every node into
disjoint counted pieces, so the accumulated total is exact.

## Complexity detail
The tree height is $O(\log n)$. At each of at most $O(\log n)$ loop iterations, two left-spine measurements take
$O(\log n)$ time, giving $O(\log^2 n)$ total time. The loop, height counters, and accumulated count use $O(1)$ auxiliary
space.

## Alternatives and edge cases
- **Recursive decomposition:** It performs the same height comparisons and time bound but uses $O(\log n)$ call-stack
  space.
- **Plain DFS or BFS:** It works for arbitrary binary trees but visits all $n$ nodes.
- **Whole-tree perfect assumption:** Treating every complete tree as perfect overcounts a partially filled final level.
- **Last-level binary search:** Testing bit paths to candidate positions also gives $O(\log^2 n)$ time.
- **Empty or singleton tree:** The loop returns zero for `null` and counts one nonempty root correctly.
- **Exact powers:** Integer shifts avoid floating-point rounding when adding a perfect subtree.
