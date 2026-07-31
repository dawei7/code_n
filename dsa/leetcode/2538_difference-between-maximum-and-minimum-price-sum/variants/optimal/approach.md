
## General

Because every price is positive, the minimum price sum among paths starting at a chosen root is always the root's own price: extending a path can only increase its sum. The required cost is therefore the greatest price sum of a simple path after removing the price of one endpoint. The remaining task is to examine all endpoint pairs without starting a traversal from every possible root.

Root the tree temporarily at node 0. Build a parent array and traversal order iteratively, then process nodes in reverse order so every child's states are ready before its parent.

**Two downward-path states**

For each node `u`, maintain two best downward paths within its processed subtree:

- `with_endpoint[u]` is the maximum complete sum of a path starting at `u`;
- `without_endpoint[u]` is the maximum sum of such a path after removing the price of its descendant endpoint.

The one-node path initializes these states to `price[u]` and zero. Extending through a child adds `price[u]` to the corresponding child state.

**Joining different branches**

Before merging a child's states into the current best states at `u`, join that child branch with the best path formed from `u` and previously processed branches. Exactly one endpoint must be removed, giving the two candidates:

- `with_endpoint[u] + without_endpoint[child]`;
- `without_endpoint[u] + with_endpoint[child]`.

The paths meet only at their lowest common ancestor `u`, whose price occurs in the `u` state and is therefore counted once. Processing a child before updating the stored states also guarantees that the two joined sides come from different branches.

Every simple path has a unique lowest common ancestor in the temporary rooting. When the second of its two branches is processed there, one of these joins considers its full sum with either endpoint removed. Ancestor-to-descendant paths are included because the one-node state at the ancestor acts as one side. Taking the maximum over all joins therefore considers every legal root/path choice.

## Complexity detail

Constructing the adjacency lists and parent order takes $O(n)$ time. Each undirected edge is examined a constant number of times during traversal and dynamic programming, so the total time is $O(n)$. The adjacency lists, parent order, and two state arrays use $O(n)$ space.

## Alternatives and edge cases

- **Traverse from every root:** Computing the maximum root-to-node sum independently for all roots is correct but takes $O(n^2)$ time on a chain.
- **Weighted diameter alone:** Keeping only a complete downward sum cannot represent removing either endpoint; the second state is necessary to preserve both endpoint choices during a merge.
- **Recursive tree DP:** The same recurrence is concise recursively, but a legal chain can contain $10^5$ nodes and overflow the language's call stack; iterative postorder avoids that risk.
- **Single node:** Its only path starts and ends at the same node, so the maximum and minimum sums coincide and the answer is zero.
- **Positive prices:** The reduction of the minimum rooted path to the one-node path depends on every node price being positive.
- **Large result:** A path may contain $10^5$ prices of up to $10^5$, so fixed-width languages need a 64-bit result.
