## General

The restriction is a maximum-weight matching condition: once the edge from a node to its parent is chosen, no edge from that node to a child may be chosen. This creates two natural values for every rooted subtree.

Let `parent_edge_free[u]` be the best score in node `u`'s subtree when the edge from `u` to its parent is not chosen. Let `parent_edge_chosen[u]` be the best score when that parent edge is already chosen.

**Build the no-child-edge baseline.** If no edge from `u` to a child is selected, every child `v` uses `parent_edge_free[v]`. Their sum is the baseline. When `u`'s parent edge is chosen, this baseline is the only legal option, so it is exactly `parent_edge_chosen[u]`.

**Add at most one child gain.** When `u` is free, it may remain unmatched or choose one edge `(u, v)` of weight `w`. Choosing that edge replaces `parent_edge_free[v]` in the baseline with `w + parent_edge_chosen[v]`. Therefore add the greatest nonnegative gain:

`w + parent_edge_chosen[v] - parent_edge_free[v]`.

No two child edges can both be selected because they share `u`. These choices cover every legal matching in the subtree, and each transition combines optimal child states, so induction from the leaves proves both state values. The root has no parent edge; its free state is the answer.

**Process without recursion.** Build child lists, traverse from the root to obtain an order, and evaluate nodes in reverse order. This guarantees children are ready before parents without risking recursion depth on a long chain.

## Complexity detail

Each node and edge is added to the child structure, traversal order, and dynamic-programming transitions a constant number of times. The time is $O(n)$ and the child lists, order, and two state arrays use $O(n)$ space.

## Alternatives and edge cases

- **Recursive tree DP:** The same two transitions are concise recursively, but a chain of length $10^5$ can exceed Python's recursion limit.
- **Recompute baselines per child:** Summing all child states separately for every candidate child is correct but can take $O(n^2)$ time on a star.
- **All negative weights:** The nonnegative-gain choice leaves every edge unselected and returns zero.
- **Single node:** There are no selectable edges, so the answer is zero.
- **Parent identifiers:** A parent index is not guaranteed to be numerically smaller than its child; derive traversal order from the tree.
- **Wide node:** At most one incident child edge may be chosen, regardless of how many positive weights it has.
