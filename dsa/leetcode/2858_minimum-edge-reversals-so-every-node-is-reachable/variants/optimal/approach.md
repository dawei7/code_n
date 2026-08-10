## General

**Ignore direction only to expose the tree.** If all edges were bidirectional, the graph would be a tree. Therefore, between any proposed starting node and every other node there is exactly one undirected path. To make all nodes reachable from a chosen root, every edge on that rooted tree must point from parent to child. The task is not choosing among alternative routes; it is counting which of those uniquely positioned edges face the wrong way.

Computing that count independently for all $n$ roots would repeat almost all work. The solution instead computes the answer for root `0` once, then changes the root across one edge at a time. This technique is called rerooting.

**Encoding direction with a sign.** For every original directed edge `x -> y`, the adjacency list receives two records: from `x` to `y` it stores `(y, 1)`, and from `y` to `x` it stores `(x, -1)`. The sign describes how the original arrow looks when traversing that adjacency entry. A `1` means the arrow already follows the traversal direction. A `-1` means traversal goes against the original arrow.

**First DFS: establish `ans[0]`.** Root the undirected tree at node `0`. The first depth-first search walks from every parent toward every child. If its adjacency sign `k` is positive, the corresponding original edge already points outward from `0`, so it needs no reversal. If `k < 0`, the original edge points from child toward parent, which blocks travel from root `0`; that edge must be reversed. The expression `int(k < 0)` is `1` exactly in this latter case, so adding it for all tree edges produces the minimum reversal count for root `0`.

This count is minimal because each wrongly oriented edge separates an entire child-side subtree from the root. Reversing some different edge cannot cross that cut, so every wrong edge is individually necessary. Reversing all of them is also sufficient because then every parent-to-child step is directed outward.

**Second DFS: move the root across one edge.** Suppose the current root is `i` and `j` is its child in the traversal. All edges other than the one between `i` and `j` keep the same required orientation when the root moves from `i` to `j`: within each side of that cut, parent-child relationships do not change. Only the connecting edge flips its desired direction.

If the stored sign from `i` to `j` is `1`, the original edge is `i -> j`. It was correct for root `i`, but root `j` needs `j -> i`, so moving the root adds one required reversal. Hence `ans[j] = ans[i] + 1`.

If the sign is `-1`, the original edge is `j -> i`. Root `i` had to reverse it, while root `j` can use it as-is. Moving the root removes one reversal, so `ans[j] = ans[i] - 1`.

Both cases are exactly the compact assignment `ans[j] = ans[i] + k`. The second DFS propagates this relation over every edge, giving the answer for every possible root in constant work per node.

**Trace the first example.** Original edges are `2 -> 0`, `2 -> 1`, and `1 -> 3`. With root `0`, the first traversal crosses `0` to `2` against `2 -> 0`, so the base count is at least one; the other outward steps can be oriented consistently, yielding `ans[0] = 1`. Rerooting over the same edge from `0` to `2` uses sign `-1`, so `ans[2] = 1 - 1 = 0`. Moving from `2` to `1` follows original `2 -> 1`, so `ans[1] = 0 + 1 = 1`. Moving from `1` to `3` follows `1 -> 3`, giving `ans[3] = 2`.

## Complexity detail

Building the signed adjacency list stores two entries per one of the $n-1$ edges and takes $O(n)$ time. Each DFS visits every node once and examines every adjacency entry once, so the two traversals together remain $O(n)$. The answer array and adjacency list require $O(n)$ space.

The exact implementation uses recursive Python functions. Its recursion stack can reach $O(n)$ on a chain-shaped tree, so total auxiliary space remains $O(n)$. More importantly, the legal constraint permits `n = 100000`, far beyond Python's usual recursion limit. Without an external recursion-limit adjustment, the checked-in implementation can raise `RecursionError` on a sufficiently deep valid tree. This is a genuine robustness defect, not a change to the asymptotic bound. An iterative traversal would preserve the same rerooting mathematics safely.

## Alternatives and edge cases

- **Iterative two-pass rerooting:** Build a parent and order array with an explicit stack, compute `ans[0]` during that traversal, and then process nodes in parent-before-child order using `ans[child] = ans[parent] + sign`. This avoids the recursion-limit defect while keeping $O(n)$ time and space.
- **Independent search from every root:** Recounting wrong arrows for each start node costs $O(n^2)$ time and discards the one-edge rerooting relationship.
- **Direction-sign convention:** The formulas depend on storing `+1` in the original arrow direction and `-1` in the reverse adjacency direction. Reversing that convention requires reversing both count and transition formulas.
- **Two-node tree:** The answers are necessarily `[0,1]` or `[1,0]`; crossing the sole edge changes the count by exactly one.
- **Already outward from one node:** That node receives answer zero. Rerooting still correctly measures how many arrows become wrong for other starts.
- **Tree guarantee:** The parent check `j != fa` is sufficient only because the underlying graph is a tree. A general graph would require a visited set and would not have one uniquely required orientation per edge.
- **Independent answers:** Each `answer[i]` is computed for its own optimal reversal plan. The reroot formula does not claim one fixed set of reversals works for all starts simultaneously.
