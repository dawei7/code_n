## General

Choosing an edge an even number of times has no effect, while choosing it an odd number of times has the same effect as choosing it once. A shortest sequence therefore corresponds to a subset of the tree's edges. For every node, the parity of selected incident edges must equal whether `start` and `target` differ at that node.

Root the tree at node `0`. Record each node's parent, the edge leading to that parent, and a traversal order. Then process every non-root node in reverse traversal order, so all of its descendants have already been settled.

At such a node `v`, every child edge has already received its final decision. Only the parent edge can still alter `v`:

- If `v` still has the wrong color, its parent edge must be selected. Mark that edge and toggle the parent's remaining need.
- If `v` is already correct, its parent edge must not be selected, because selecting it would make `v` wrong again.

Thus each non-root decision is forced. After all of them, no undecided edge remains incident to the root. A remaining mismatch at the root makes the transformation impossible; otherwise the forced edge subset is valid.

This also proves minimality. Any valid sequence has the same forced parent-edge decision at the first processed node, then at the next, and so on. Consequently, a feasible tree has exactly one selected-edge subset. Repeating an edge would add two cancelling operations, so the unique subset is the minimum-length sequence. Store its membership in an array indexed by the original edge order and enumerate that array from left to right to produce increasing indices without a separate sort.

Equivalently, the node mismatches form a parity vector over $\mathrm{GF}(2)$. Every edge contributes `1` at both endpoints. A connected tree's edge-incidence vectors generate exactly the even-parity node vectors, and the bottom-up procedure constructs their unique representation.

## Complexity detail

Let $N=n$. Building the adjacency list, rooting the tree, processing nodes in reverse order, and enumerating selected edges each take $O(N)$ time because a tree has $N-1$ edges. The adjacency list, traversal arrays, mismatch state, and selected-edge flags use $O(N)$ auxiliary space.

The benchmark defines size as $N$. Its path requires every edge to be selected, forcing a full traversal and a full output scan. The slower control repeatedly searches all edges to find the lone remaining edge incident to the next leaf, giving $O(N^2)$ work.

## Alternatives and edge cases

- **Queue-based leaf peeling:** Maintaining current degrees and a queue of leaves makes the same forced decisions without choosing a root explicitly; it also runs in $O(N)$ time and space.
- **Generic Gaussian elimination:** The incident-edge parity equations can be solved as a linear system over $\mathrm{GF}(2)$, but a general eliminator ignores the tree structure and is far more expensive.
- **Enumerate edge subsets:** Trying all $2^{N-1}$ subsets gives a direct oracle for tiny trees but is infeasible for the legal limit.
- **Repeated leaf searches:** Removing one leaf at a time while rescanning every edge is correct but takes $O(N^2)$ time on a path.
- **Already matching strings:** No edge is selected, so return `[]`.
- **Odd number of mismatched nodes:** Each operation toggles two endpoints, preserving total mismatch parity; an odd mismatch count is impossible and leaves the root unresolved.
- **Increasing output order:** Traversal order is unrelated to edge indices. Record boolean membership and enumerate indices afterward.
- **Deep path:** Use an iterative traversal rather than recursive DFS so a legal $10^5$-node path cannot overflow the Python call stack.
- **Repeated edge operations:** Toggling one edge twice cancels, so repetitions can never belong to a minimum-length sequence.
