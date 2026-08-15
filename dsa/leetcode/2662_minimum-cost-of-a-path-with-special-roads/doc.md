# Minimum Cost of a Path With Special Roads

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2662 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/) |

## Problem Description

### Goal

Your initial position in a two-dimensional coordinate space is `start = [startX, startY]`, and the destination is `target = [targetX, targetY]`. Traveling normally between two positions $(x_1,y_1)$ and $(x_2,y_2)$ costs their Manhattan distance,

$$
\lvert x_2-x_1 \rvert + \lvert y_2-y_1 \rvert.
$$

You are also given directed special roads. An entry `specialRoads[i] = [x1, y1, x2, y2, cost]` permits travel from `(x1, y1)` to `(x2, y2)` for exactly `cost`; it does not grant the reverse trip. Each special road may be used any number of times. Ordinary Manhattan travel remains available between any two positions, including the start or end of a special road.

Return the minimum total cost needed to reach `target` from `start` using any combination of ordinary movement and special roads.

### Function Contract

**Inputs**

- `start`: Two integers giving the initial coordinates, with `1 <= start[0] <= target[0] <= 100000` and `1 <= start[1] <= target[1] <= 100000`.
- `target`: Two integers giving the destination coordinates.
- `specialRoads`: Between 1 and 200 entries `[x1, y1, x2, y2, cost]`. Every endpoint lies inside the coordinate bounds from `start` through `target`, and `1 <= cost <= 100000`.

**Return value**

- Return the least possible travel cost as an integer.

### Examples

#### Example 1

- **Input:** `start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]`
- **Output:** `5`
- **Explanation:** Move normally to `(1,2)`, take the first road, move to `(3,4)`, and take the second road. The costs are `1 + 2 + 1 + 1`.

#### Example 2

- **Input:** `start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]`
- **Output:** `7`
- **Explanation:** Direct Manhattan travel is optimal. The inexpensive first road points from the target back toward the start, so it cannot help.

#### Example 3

- **Input:** `start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]`
- **Output:** `8`
- **Explanation:** Pay `1` to reach `(1,2)`, pay `4` for the road to `(7,4)`, then pay `3` to reach the target normally.
