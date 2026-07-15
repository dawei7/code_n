# As Far from Land as Possible

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1162 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/as-far-from-land-as-possible/) |

## Problem Description

### Goal

You are given an $n \times n$ grid containing only `0` and `1`. A `0` represents a water cell and a `1` represents a land cell.

Choose a water cell whose distance to its nearest land cell is as large as possible, and return that distance. Distance is Manhattan distance: between cells $(x_0, y_0)$ and $(x_1, y_1)$ it is $\lvert x_0 - x_1 \rvert + \lvert y_0 - y_1 \rvert$. If the grid contains no land or contains no water, return `-1` because no valid water-to-land distance exists.

### Function Contract

**Inputs**

- `grid`: A square $n \times n$ matrix, where $1 \le n \le 100$ and every entry is either `0` for water or `1` for land.

**Return value**

- The maximum, over all water cells, of the Manhattan distance to that cell's nearest land cell; or `-1` when the grid is all water or all land.

### Examples

**Example 1**

- Input: `grid = [[1,0,1],[0,0,0],[1,0,1]]`
- Output: `2`

The central water cell `(1, 1)` is two steps from its nearest land.

**Example 2**

- Input: `grid = [[1,0,0],[0,0,0],[0,0,0]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1,1],[1,1]]`
- Output: `-1`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Start from every land cell at once.** Put all land coordinates into one breadth-first queue and mark them visited. This is a multi-source search: level zero contains every possible nearest-land origin rather than choosing one land cell and repeating a search.

**Expand equal distances together.** Each queue layer reaches the unvisited orthogonal neighbors of the preceding layer. Moving one step up, down, left, or right increases Manhattan distance by exactly one. Therefore, the first time a water cell is reached, the current BFS depth is the length of its shortest path to any land cell—and hence its nearest-land Manhattan distance.

Continue until no cells remain. The last newly reached water layer has the largest of these nearest-land distances, so its depth is the answer. Every cell is marked before it is enqueued, preventing duplicate work from different land sources. Before expansion, reject an empty initial queue (all water) and a queue containing all $n^2$ cells (all land), both of which require `-1`.

#### Complexity detail

The initialization scans all $n^2$ cells. Each cell is then enqueued at most once and checks four neighbors, so the search also costs $O(n^2)$ time. The visited matrix and queue can each hold $O(n^2)$ entries in the worst case, giving $O(n^2)$ auxiliary space.

#### Alternatives and edge cases

- **Search from every water cell:** Scanning all land cells for each water cell is direct but can require $O(n^4)$ time.
- **Run one BFS per land cell:** This repeats most grid exploration and can also become quartic.
- **Two-pass dynamic programming:** Forward and backward distance passes achieve $O(n^2)$ time, but require careful initialization and boundary handling.
- **All water:** With no land source, nearest-land distance is undefined and the result is `-1`.
- **All land:** There is no water cell to choose, so the result is also `-1`.
- **Diagonal cells:** Diagonal movement is not allowed; a diagonal offset of one row and one column contributes distance $2$.

</details>
