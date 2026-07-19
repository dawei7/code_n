## General
**Represent every downward path as a prefix difference**

During depth-first traversal, let `current_sum` be the sum from the root through the current node. A downward path ending here has target sum exactly when an earlier ancestor prefix equals `current_sum - targetSum`. Seed frequency zero with one occurrence so paths beginning at the root are included.

**Count active ancestor prefixes**

Maintain a frequency map containing only prefixes on the current root-to-node recursion path. At each node, add the frequency of `current_sum - targetSum` to the answer, then increment `current_sum` before exploring both children.

**Backtrack before visiting another branch**

After both child calls return, decrement the current prefix frequency. Otherwise a prefix from the completed left branch could incorrectly combine with a node in the right branch even though those nodes do not form a downward ancestor path.

**Why every valid path is counted once**

Every downward path has one ending node and one prefix immediately before its starting node. When DFS visits that endpoint, the starting prefix is active and contributes exactly once through the frequency lookup. Nonancestor prefixes have already been removed or have not yet been visited, so no invalid cross-branch path contributes.

## Complexity detail
The app reconstructs and traverses each of `n` nodes once. Hash-map work is average constant time per node, so total time is $O(n)$. The reconstructed nodes, active prefix counts, and recursion stack use $O(n)$ space in the worst case.

## Alternatives and edge cases
- **Start a sum search at every node:** explores every downward path directly and takes $O(n^2)$ time on a skewed tree.
- **Store complete root-to-node value lists:** can recompute suffix sums but uses repeated linear work per node.
- **Negative values:** invalidate sliding-window reasoning but are handled by prefix differences.
- **Zero values:** repeated equal prefix sums must retain frequencies, not just membership.
- **Empty tree:** contains no nonempty paths.
- **Paths need not start at the root:** the earlier-prefix subtraction captures every starting depth.
