## General
**Each stack entry carries the sum of one unique root path**

Use a depth-first stack of `(node, sum_through_node)` pairs, initialized with the root value. When pushing a child, add its value to the parent's stored sum. Tree structure gives every node a unique root path, so no path identity or visited set is needed.

**Target equality matters only when the path cannot continue**

Compare with `targetSum` only when a node has neither child. An internal prefix equal to the target is not a qualifying complete path, even if all remaining descendants would change the sum away from it.

Negative node values prevent safe pruning based on whether a running sum has exceeded the target; the traversal should continue until a leaf unless a valid path has already been found.

**Pending sums are exact, not best-so-far summaries**

Every stack pair stores the exact sum of node values along the unique path from the root to that node. Every reachable node is pushed at most once.

**Trace a matching leaf and a nonqualifying prefix**

In the first example, the path `5 -> 4 -> 11 -> 2` reaches a leaf with sum `22`, so the search returns true. A prefix such as `5 -> 4` would not qualify even if its sum matched a target.

**Only a leaf closes a complete path sum**

Each stack state carries the sum from the root through its node, so a leaf comparison evaluates exactly one complete root-to-leaf path. Internal nodes are not accepted even if their partial sum equals the target because their paths have not ended.

Depth-first traversal reaches every leaf unless a valid one has already established the true answer. It therefore returns true exactly when at least one complete path has the required sum.

## Complexity detail
When no path matches, all `n` nodes are processed once, giving $O(n)$ time. Depth-first pending work is bounded by $O(h)$, where `h` is tree height.

## Alternatives and edge cases
- **Recursive remaining-sum DFS:** has the same bounds and is concise, but relies on call-stack depth.
- **Breadth-first search:** is correct but may store $O(w)$ nodes in a wide tree.
- **Check any downward path:** solves a different problem because the path must start at the root and end at a leaf.
- Empty input returns false even when `targetSum` is zero because no root-to-leaf path exists.
- Early success may avoid visiting the remaining tree, but an absent match requires inspecting every reachable leaf.
