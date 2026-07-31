## General

Only changing a `1` to `0` can remove connectivity; changing `0` to `1` adds movement options. First search for a monotone path while replacing each visited nonterminal `1` with `0`. Trying down before right consistently carves one boundary path. A failed branch cannot reach the finish, so erasing its cells does not remove a usable suffix of another complete path.

If the first search finds no path, the unchanged problem is already disconnected and zero flips suffice. Otherwise, restore the two endpoints because the operation may not remove them, then run the same search again.

Any path found on the second pass is internally disjoint from the carved path. One permitted flip cannot touch both disjoint paths, so disconnection is impossible. If no second path exists, the monotone planar structure has internal vertex connectivity one: every start-to-finish route shares an interior bottleneck, and flipping such a cell disconnects the matrix. This is the two-path form of the vertex-cut argument specialized to right-and-down grid paths.

The recursion limit is raised to the maximum possible path length plus a small margin. A monotone path uses at most $m+n-1$ cells even when the matrix contains many more cells.

## Complexity detail

Each search marks a cell before expanding it, so a cell is processed at most once per pass. Two passes take $O(mn)$ time. The recursion follows a monotone path and therefore has depth at most $m+n-1$, using $O(m+n)$ stack space. The grid itself supplies the visited marks.

## Alternatives and edge cases

- **Try every possible flip:** Flipping each interior `1` and recomputing reachability is correct but can require $O((mn)^2)$ time.
- **Forward and backward path counts:** Dynamic programming can identify whether a diagonal layer has one path-carrying cell, but counts must be capped or handled carefully to avoid enormous integers.
- **Already disconnected grid:** No modification is required, so the result is `True`.
- **Single cell or endpoint-only strip:** When no interior cell exists and the endpoint path is present, it cannot be disconnected legally.
- **Changing `0` to `1`:** This can only add paths and therefore never helps achieve disconnection.
- **Endpoint restoration:** Both endpoint cells must be reset between searches because they are forbidden flip targets.
