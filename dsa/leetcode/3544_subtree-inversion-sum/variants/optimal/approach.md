## General

Root the tree at `0`. The effect of all decisions above a node is summarized by two facts: whether an odd number of ancestor inversions currently flips its sign, and the distance to the nearest inverted ancestor. Distances at least `k` are equivalent because inversion is allowed in all of them, so cap the distance at `k`.

For each node, build two arrays indexed by capped distance. `even[d]` is the best subtree sum when ancestor inversions preserve the current signs, while `odd[d]` is the best sum when they reverse every current sign. If `d < k`, the node cannot be inverted; keep its inherited sign and add each child's state at `d + 1`. If `d = k`, compare that same no-inversion result with inverting the node. Inversion toggles the node's sign and the parity passed to every child, and each child is then distance `1` from this newly inverted node.

Children are independent once parity and distance are fixed, so their optimal contributions add. Inductively, each state examines every legal choice at its root and combines optimal solutions for all child subtrees. The larger choice at distance `k` is therefore optimal. At the overall root there is no close inverted ancestor and parity is even, so the answer is the root's `even[k]` state.

Build parent links and traversal order iteratively, then process that order backward. This avoids recursion failure on a 50,000-node chain. Once a child's arrays have been merged into its parent they are released, limiting live storage in common tree shapes while preserving the $O(nk)$ worst-case bound.

## Complexity detail

Each parent-child edge contributes to both parity arrays at every one of the $k+1$ capped distances, so the total time is $O(nk)$. The adjacency list, rooted order, and dynamic-programming arrays require $O(nk)$ space in the worst case. Since $k \le 50$, the state dimension is tightly bounded.

## Alternatives and edge cases

- **Top-down memoization:** Uses the same parity-and-distance recurrence, but recursive calls can overflow on a path of length 50,000 and cached Python states add substantial overhead.
- **Remember the exact last inverted ancestor:** This is correct but creates up to quadratic state on a deep tree; capping distance at `k` merges behaviorally identical states.
- **Greedily flip negative subtree sums:** Nested inversions change descendant signs, and the spacing rule couples decisions on one ancestor chain, so local subtree sums are insufficient.
- **Independent branches:** Inverted nodes with neither one ancestral to the other impose no spacing restriction and are optimized separately.
- **`k = 1`:** Parent and child inversions are both allowed because their distance is exactly the minimum; their overlapping effects may cancel below the child.
- **Large `k`:** A root-to-leaf path may contain few inverted nodes, but different branches can still each contain a choice.
- **Zero values:** Their own sign is irrelevant, yet inversion at that node may still improve descendants.
- **All positive values:** Choosing no inversion preserves the original sum and is always considered.
