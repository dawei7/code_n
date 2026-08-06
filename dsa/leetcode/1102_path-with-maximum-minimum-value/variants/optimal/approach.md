## General
**Use the endpoints as an absolute upper bound.** Every path contains both corners, so its score is at most `endpoint_cap = min(grid[0][0], grid[-1][-1])`. If the matrix-wide minimum already meets that cap, every cell can support it and any cardinal corner-to-corner route achieves the best possible score immediately. This handles dense legal maximum grids without unnecessary heap work.

**Treat path quality as a bottleneck.** Reaching a neighbor from a path with `score` produces `candidate = min(score, grid[next_row][next_column])`. A max-priority heap orders frontier states by this candidate, so the next removed state has the greatest path minimum currently available.

**Keep only improving states.** `best_score[row][column]` stores the strongest bottleneck discovered for each cell. Push a neighbor only when the new candidate improves that value, and discard a popped entry when a newer, stronger score has superseded it. This avoids the protected implementation's unconditional duplicate heap entries while preserving every potentially optimal route.

**Return when the destination is popped.** The heap removes scores from strongest to weakest, and extending a path can only preserve or reduce its bottleneck. Consequently, a current entry equal to the destination's recorded best score cannot later be improved; returning it is safe.

The shortcut returns only when it reaches the endpoint upper bound, so it is optimal. Otherwise the relaxation is Dijkstra's greedy proof with `min` replacing addition and a max-priority heap replacing a min-priority heap. Every discarded state is dominated by a stronger path already recorded for the same cell, while every improving state remains available for extension. The first current destination entry is therefore the maximum achievable path minimum.

## Complexity detail
There are $V=mn$ cells and at most four adjacency edges per cell. Scanning for the global minimum costs $O(V)$. Each improving relaxation adds a heap state, and heap insertion and removal cost $O(\log V)$, giving $O(V \log V)$ total time because the grid has $O(V)$ edges. The heap and best-score matrix use $O(V)$ space.

## Alternatives and edge cases
- **Descending cells plus union-find:** Activate cells from highest to lowest value and join active neighbors until the two corners connect; this also takes $O(V \log V)$ time.
- **Binary search with reachability:** Test whether cells at least a threshold connect the corners, yielding $O(V \log U)$ time for value range $U$.
- **Test every integer threshold:** It is correct but pseudopolynomial and can take $O(UV)$ time when values are large.
- **Unconditional heap pushes:** Pushing every unvisited neighbor remains mathematically correct, but duplicate states can exhaust cOde(n)'s execution-step allowance on a legal $100 \times 100$ grid.
- **Single cell:** The endpoint cap and matrix minimum are that cell's value, so it is returned directly.
- **No diagonal movement:** A high-valued diagonal alone does not form a path; only four cardinal directions are allowed.
