## General
**Summarize the ancestor path:** For a node, every possible difference with an ancestor is bounded by the minimum and maximum values already seen from the root to its parent. No other ancestor value can be farther from the node's value than one of those two extremes.

**Carry extrema into each child:** Store triples of `(node, path_min, path_max)` on a depth-first stack. At a visited node, update the answer with `node.val - path_min` and `path_max - node.val`, then form `next_min` and `next_max` including the current value before pushing its children.

Each stack entry receives exactly the extrema of that node's ancestor path. Therefore every candidate difference considered is between a valid ancestor and descendant. Conversely, for every node, its farthest-valued ancestor is represented by one of the carried extrema, so the traversal cannot miss the global maximum.

**Keep traversal iterative:** A valid tree may contain 5000 nodes in one chain. An explicit stack retains the same depth-first state without depending on Python's recursion limit.

## Complexity detail
Every one of the $N$ nodes is pushed and processed once, so the traversal takes $O(N)$ time. The stack contains at most one path plus deferred siblings, bounded by the tree height $H$, for $O(H)$ auxiliary space.

## Alternatives and edge cases
- **Recursive depth-first search:** Pass the same path minimum and maximum through recursive calls for identical asymptotic bounds, but a deeply skewed tree can exceed the language's recursion limit.
- **Rescan each descendant subtree:** Treat every node as an ancestor and search below it for extreme values. This repeats work and takes $O(NH)$ time, which is $O(N^2)$ on a chain.
- **Equal values:** If all node values are identical, every valid difference is zero.
- **Extreme values:** Values `0` and `100000` may produce the maximum possible answer `100000`.
- **Distinct-node rule:** A node is not paired with itself; initializing the path extrema at the root and evaluating descendants respects that requirement.
