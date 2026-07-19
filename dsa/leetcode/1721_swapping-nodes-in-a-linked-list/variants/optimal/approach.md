## General
**Locate the forward position**

Start `kth_from_start` at `head` and advance it `k - 1` links. It now points to the $k$th node from the beginning. Keep this pointer because it will also establish the exact offset needed to locate the node counted from the end.

**Preserve a gap to find the backward position**

Place a runner at `kth_from_start` and a second pointer, `kth_from_end`, at `head`. Advance both pointers together until the runner reaches the final node. The runner began with exactly $n-k$ links remaining, so the second pointer also advances $n-k$ times and finishes at position $n-k+1$, the $k$th node from the end.

**Exchange values without rewiring links**

Swap the two nodes' `val` fields and return `head`. If the two positional descriptions name the same middle node, swapping its value with itself is harmless. Because no `next` pointer changes, endpoint, adjacent-node, and same-node cases require no structural special handling.

## Complexity detail
The initial advance and synchronized traversal together follow at most a constant number of links per node, taking $O(n)$ time. The algorithm stores only three node references and a loop counter, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Compute the length first:** One full traversal can determine $n$, followed by scans to positions $k$ and $n-k+1$; this is still $O(n)$ time and $O(1)$ space but needs an additional pass.
- **Store every node:** Collecting node references in an array makes both positions directly indexable, but it uses $O(n)$ auxiliary space.
- **Repeated suffix measurement:** Testing candidates by recounting every remaining suffix can locate the node from the end correctly but takes $O(n^2)$ time.
- **Same node:** When $2k=n+1$, both pointers meet at the middle node and the output is unchanged.
- **Endpoint swap:** For `k = 1` or `k = n`, the first and last values exchange.
- **Duplicate values:** Positions, not values, identify the nodes; equal stored values may make the output appear unchanged.
