## General
**Reverse the search direction**

Running a separate shortest-path search from every empty candidate repeats almost the same grid exploration up to `mn` times. Instead, run one breadth-first search from each of the `b` buildings. An unweighted four-direction grid is exactly the setting in which BFS discovers every reachable empty cell at its shortest distance from that source.

Maintain two matrices. `distance_sum[r][c]` accumulates the BFS distance contributed by each building that reaches `(r, c)`. `reach_count[r][c]` records how many buildings have reached it. A BFS may enter only cells whose grid value is zero; a building is the source of its own search but never a corridor for another path.

**Distance layers contribute exactly once**

Start a building at distance zero. Whenever BFS first enters an empty neighbor, add the neighbor's layer distance to its accumulated sum, increment its reach count, mark it visited for this building, and enqueue it. Per-building visitation is essential: without it, different paths from the same building would add that building more than once.

In the first sample, the central empty cell receives distances from the two top buildings and the lower building. Obstacles change the reachable paths, but they require no special distance logic because they are never enqueued.

**Reach counts separate finite partial answers from valid answers**

After all building searches, consider only empty cells whose reach count equals the total number of buildings. For such a cell, every added term is a shortest distance from one distinct building, so its accumulated value is exactly the required total distance. Taking the minimum therefore chooses the best valid land cell.

If a cell has a smaller partial sum but was not reached by every building, it is not a candidate at all. If no empty cell has the full reach count, disconnected regions or obstacles prevent a common meeting point and the answer is `-1`.

## Complexity detail
Let the grid have `m` rows, `n` columns, and `b` buildings. Each building's BFS visits at most `mn` cells, for $O(bmn)$ time. The two accumulation matrices, one visited matrix, and the BFS queue each require $O(mn)$ space.

## Alternatives and edge cases
- **BFS from every empty cell:** can take $O((mn)^2)$ time when many candidates must explore most of the grid.
- **Manhattan distance without BFS:** is invalid because obstacles and non-traversable buildings can force detours or disconnect regions.
- **Multi-source BFS from all buildings together:** finds distance to the nearest building, not the sum of independent distances to every building.
- A grid with no empty land returns `-1`. An empty cell reached by only some buildings must be rejected even if its partial distance sum is small.
