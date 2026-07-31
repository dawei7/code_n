## General

**Each added edge flips exactly two degree parities**

Only nodes with odd degree need attention. Adding an edge toggles the parity of both endpoints, so one edge can repair two odd nodes and two edges can repair at most four. The handshaking lemma also guarantees that the number of odd-degree nodes is even. Consequently, only counts `0`, `2`, and `4` can succeed; any larger count is immediately impossible.

Build an adjacency set for every node while computing the degrees. The sets make every test for an existing edge an expected $O(1)$ operation and prevent considering a forbidden duplicate.

**Resolve each feasible odd-count case completely**

With no odd nodes, adding nothing already satisfies the goal.

For two odd nodes `a` and `b`, one missing edge between them repairs both. If that edge already exists, two edges must pass through a third node `middle`: add `(a, middle)` and `(b, middle)`. Such a node is valid exactly when it differs from both endpoints and is adjacent to neither. Scanning all nodes tests every possible intermediate choice.

For four odd nodes, every one of the two new edges must pair two of them; involving an even-degree node would create another odd degree that the remaining edge cannot eliminate. Four labeled nodes have exactly three distinct pairings. Test all three and accept when both edges in any pairing are absent.

These cases are exhaustive because adding an edge changes only its two endpoints. Every accepted construction toggles each original odd node exactly once and leaves all other degrees even.

## Complexity detail

Let $m = \lvert\texttt{edges}\rvert$. Building the adjacency sets and collecting odd-degree nodes takes $O(n+m)$ time. The two-odd case scans at most $n$ candidate intermediates, while the four-odd case checks only three pairings. The total time is therefore $O(n+m)$. The adjacency sets store both directions of every edge and the node array, requiring $O(n+m)$ auxiliary space.

## Alternatives and edge cases

- **Scan the edge list for every adjacency query:** This avoids adjacency sets but can take $O(nm)$ time when the two odd nodes are adjacent and every possible intermediate must be checked.
- **Adjacency matrix:** Constant-time edge queries are convenient, but an $n \times n$ matrix requires $O(n^2)$ space and is infeasible for $n=10^5$.
- **Already-even graph:** Zero additions are permitted, so an empty odd-node list returns `True` immediately.
- **More than four odd nodes:** Two edges toggle at most four odd endpoints, making repair impossible regardless of graph connectivity.
- **Two odd nodes that are already adjacent:** A second copy of their edge is forbidden; success depends on finding a third node adjacent to neither.
- **Four odd nodes:** All three pairings must be considered because existing edges can block one or two pairings while leaving another valid.
