## General

Entering an unsafe cell costs one health; entering a safe cell costs zero. The starting cell's value also reduces health, which is why `dist[0][0] = grid[0][0]`. The problem becomes finding the minimum total cell cost along any path from the upper-left to lower-right.

`dist[x][y]` stores the best cost discovered for a cell. It begins at infinity except at the start. The deque initially contains the start.

For each popped cell, the source tries four directions produced by consecutive pairs of `(-1,0,1,0,-1)`. A neighbor is relaxed when the current distance plus its binary cell value is smaller than the recorded distance. The new cell is appended to the deque.

Repeated relaxation is correct as a label-correcting shortest-path method: whenever a better cost is found, the neighbor is processed again so the improvement can propagate. All costs are nonnegative, and finite grid state ensures the process eventually reaches shortest distances.

After convergence, `dist[-1][-1]` is the minimum number of unsafe cells paid along a path, including endpoints. Health remaining is `health - cost`. It must be at least one, so the condition is strictly `cost < health`, not less than or equal.

For an unsafe starting cell, one health is lost immediately. Example three counts that cost, then uses the central safe cell to keep total loss below five.

**Exact source is not 0-1 BFS.** A true 0-1 BFS pushes zero-cost relaxations to the front with `appendleft` and one-cost relaxations to the back. This source calls `append` for both. It is a FIFO queue relaxation algorithm, similar to SPFA, even though the manifest and editorial label the intended method 0-1 BFS.

The distinction affects complexity, not the relaxation equation's result. Cells can be enqueued multiple times when later improvements arrive. The source also has no in-queue flag, so duplicate queued coordinates can coexist.

No health-based pruning occurs during traversal. Even paths already costing at least health are explored, although they cannot yield a valid final walk. This preserves correctness but may add work.

The grid is not modified. Cycles are harmless because only strict distance improvements enqueue a cell.

## Complexity detail

Let $V=mn$ and $E=O(mn)$ grid edges. The distance table and deque use $O(mn)$ space.

For genuine 0-1 BFS, time would be $O(V+E)=O(mn)$. The exact FIFO label-correcting source does not have that guarantee; in the general worst case it can require $O(VE)=O((mn)^2)$ relaxation work, though the small binary grid often behaves much better.

Thus the manifest's $O(mn)$ time describes the intended 0-1 BFS algorithm, not the precise queue discipline in this file.

## Alternatives and edge cases

- **True 0-1 BFS:** Use `appendleft` for a neighbor with value zero and `append` for value one. This provides the advertised linear bound.
- **Dijkstra:** A min-heap gives $O(mn\log(mn))$ worst-case time and straightforward shortest-path guarantees.
- **Ordinary BFS with visited cells:** It minimizes steps, not unsafe-cell count, and can reject a longer but healthier path.
- **DFS over all paths:** Cycles and exponentially many routes make direct enumeration unsuitable.
- **Cost equal to health:** Remaining health is zero, so the answer is false.
- **Unsafe destination:** Its one cost must be included before checking positivity.
- **Safe zero-cost cycles:** Strict improvement prevents endless equal-distance enqueueing.
- **One row or column:** The algorithm follows the only corridor and sums its unsafe cells.
- **Several optimal paths:** Only their shared minimum cost matters.
- **Start unsafe:** `dist[0][0]` correctly begins at one.
- **Missing `pairwise` import:** Standalone execution requires the itertools import if absent from the harness.
- **No early exit:** FIFO order does not guarantee the first destination pop is final, so computing until the deque empties is appropriate.
- **Why step count is irrelevant:** Safe cells can make a longer route cost less health than a short route. The distance metric is accumulated cell values, not number of moves.
- **Relaxing back toward the start:** Cyclic movement can propose the start again, but its existing minimal cost cannot be improved by adding nonnegative cell costs, so it is not re-enqueued.
- **Destination unreachable geometrically:** A rectangular grid with four-direction movement and no blocked cells is always connected; failure comes only from insufficient health.
- **Health pruning opportunity:** A relaxation with cost at least health cannot belong to a successful path because later costs are nonnegative. The source does not use this optional optimization.
- **Zero-weight ordering defect:** Appending a zero-cost neighbor at the back may delay it behind higher-cost work and cause later reprocessing. `appendleft` is the precise change that restores 0-1 BFS ordering.
- **Distance versus remaining health:** Minimizing cost maximizes final health because initial health is constant. This equivalence justifies solving a shortest-path problem.
- **Starting-cell convention:** The source charges `grid[0][0]` before any move. This matches examples and the notion that occupying an unsafe start reduces health.
