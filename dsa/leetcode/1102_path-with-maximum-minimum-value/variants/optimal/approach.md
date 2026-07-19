## General
**Treat path quality as a bottleneck.** Reaching a neighbor from a path with score `score` produces `candidate = min(score, grid[next_row][next_col])`. A max-heap orders frontier states by this candidate, so the next removed state has the greatest path minimum currently available.

**Finalize the strongest score first.** Start with the top-left value. When a cell is popped for the first time, no later frontier state can offer it a larger bottleneck: every later state has a score no greater than the current heap maximum, and extending a path can only preserve or reduce its minimum. Mark that cell visited and push each unvisited neighbor with the updated candidate.

**Return when the destination is popped.** The same finalization argument applies to the bottom-right cell. Its first popped score is at least every unprocessed path's frontier score, so no alternative path can improve it.

This is Dijkstra's greedy proof with `min` replacing additive edge relaxation and a max-heap replacing a min-heap. The bottleneck of a path never increases when extended, which is the monotonic property needed for permanent finalization.

## Complexity detail
There are $V=mn$ cells and at most four adjacency edges per cell. Heap insertion and removal cost $O(\log V)$, giving $O(V \log V)$ time. The heap and visited matrix each store at most $O(V)$ states.

## Alternatives and edge cases
- **Descending cells plus union-find:** Activate cells from highest to lowest value and join active neighbors until the two corners connect; this also takes $O(V \log V)$ time.
- **Binary search with reachability:** Test whether cells at least a threshold connect the corners, yielding $O(V \log U)$ time for value range $U$.
- **Test every integer threshold:** It is correct but pseudopolynomial and can take $O(UV)$ time when values are large.
- **Single cell:** The path contains only that cell, so its value is the answer.
- **Low endpoint:** The answer can never exceed either corner value because every path includes both endpoints.
- **No diagonal movement:** A high-valued diagonal alone does not form a path; only four cardinal directions are allowed.
