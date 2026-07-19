## General
**Reject blocked endpoints immediately:** A path cannot start or finish on a cell containing 1. This also handles the one-cell grid, whose answer is one only when its sole cell is open.

**Search by increasing path length:** Put `(0, 0, 1)` in a FIFO queue. Removing the front state processes the smallest unprocessed distance. For each cell, inspect all eight offsets except `(0, 0)` and enqueue every in-bounds open neighbor with distance increased by one.

**Mark on enqueue:** Change an open cell to 1 as soon as it enters the queue. The first discovery is already along a shortest path in this unweighted graph, so a later discovery cannot improve its distance. Early marking prevents duplicate queue entries.

Breadth-first search visits cells in nondecreasing path length. Therefore, when the destination is removed, its stored distance is the minimum possible. If the queue empties first, every open cell reachable from the start has been explored and no clear path exists.

## Complexity detail
The matrix has $n^2$ cells. Each is enqueued at most once and checks eight constant-count neighbors, giving $O(n^2)$ time. The queue can hold $O(n^2)$ cells in the worst case. Reusing `grid` for visited marks avoids a separate visited matrix but does mutate the supplied working copy.

## Alternatives and edge cases
- **Dijkstra with a heap:** It is correct, but every edge has unit weight, so heap ordering adds unnecessary logarithmic overhead.
- **List queue with `pop(0)`:** It preserves BFS correctness but repeatedly shifts the remaining queue and scales worse than a deque.
- **Depth-first search:** The first found path need not be shortest and exhaustive simple-path search can be exponential.
- **Blocked start or destination:** Return `-1` without searching.
- **Single open cell:** Return 1 because the start and destination are the same visited cell.
- **Corner movement:** Diagonal neighbors are valid even when the two orthogonal cells beside the corner are blocked.
- **No route:** Exhaustion of the queue yields `-1`.
