# Shortest Distance from All Buildings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 317 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-from-all-buildings/) |

## Problem Description
### Goal
Given a rectangular grid, `0` marks empty land, `1` marks a building, and `2` marks an obstacle. Choose one empty cell as a gathering location. Travel uses horizontal or vertical steps through empty land; routes cannot pass through buildings, obstacles, or outside the grid.

For each candidate that can reach every building, sum its shortest path distance to all buildings. Return the smallest such total, or `-1` when no empty cell reaches them all. The destination building cell supplies the final step but cannot be crossed to reach another building. Return only the distance total, not the chosen location or paths.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix where `0` is empty land, `1` is a building, and `2` is an obstacle

**Return value**

The minimum total distance from one valid empty cell to all buildings, or `-1` if no such cell exists.

### Examples
**Example 1**

- Input: `grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]`
- Output: `7`

**Example 2**

- Input: `grid = [[1,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1]]`
- Output: `-1`

### Required Complexity

- **Time:** $O(bmn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Reverse the search direction**

Running a separate shortest-path search from every empty candidate repeats almost the same grid exploration up to `mn` times. Instead, run one breadth-first search from each of the `b` buildings. An unweighted four-direction grid is exactly the setting in which BFS discovers every reachable empty cell at its shortest distance from that source.

Maintain two matrices. `distance_sum[r][c]` accumulates the BFS distance contributed by each building that reaches `(r, c)`. `reach_count[r][c]` records how many buildings have reached it. A BFS may enter only cells whose grid value is zero; a building is the source of its own search but never a corridor for another path.

**Distance layers contribute exactly once**

Start a building at distance zero. Whenever BFS first enters an empty neighbor, add the neighbor's layer distance to its accumulated sum, increment its reach count, mark it visited for this building, and enqueue it. Per-building visitation is essential: without it, different paths from the same building would add that building more than once.

In the first sample, the central empty cell receives distances from the two top buildings and the lower building. Obstacles change the reachable paths, but they require no special distance logic because they are never enqueued.

**Reach counts separate finite partial answers from valid answers**

After all building searches, consider only empty cells whose reach count equals the total number of buildings. For such a cell, every added term is a shortest distance from one distinct building, so its accumulated value is exactly the required total distance. Taking the minimum therefore chooses the best valid land cell.

If a cell has a smaller partial sum but was not reached by every building, it is not a candidate at all. If no empty cell has the full reach count, disconnected regions or obstacles prevent a common meeting point and the answer is `-1`.

#### Complexity detail

Let the grid have `m` rows, `n` columns, and `b` buildings. Each building's BFS visits at most `mn` cells, for $O(bmn)$ time. The two accumulation matrices, one visited matrix, and the BFS queue each require $O(mn)$ space.

#### Alternatives and edge cases

- **BFS from every empty cell:** can take $O((mn)^2)$ time when many candidates must explore most of the grid.
- **Manhattan distance without BFS:** is invalid because obstacles and non-traversable buildings can force detours or disconnect regions.
- **Multi-source BFS from all buildings together:** finds distance to the nearest building, not the sum of independent distances to every building.
- A grid with no empty land returns `-1`. An empty cell reached by only some buildings must be rejected even if its partial distance sum is small.

</details>
