# Shortest Path in Binary Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1091 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/shortest-path-in-binary-matrix/) |

## Problem Description

### Goal

Given an $n\times n$ binary matrix `grid`, find a clear path from the top-left cell `(0, 0)` to the bottom-right cell `(n - 1, n - 1)`. Every visited cell must contain `0`.

Consecutive path cells must be different and 8-directionally connected: they may share either an edge or a corner. The path length is its number of visited cells, including both endpoints. Return the length of the shortest clear path, or `-1` when no clear path exists.

### Function Contract

**Inputs**

- `grid`: an $n\times n$ matrix containing only 0 and 1, where $1 \le n \le 100$.

**Return value**

- The minimum number of cells on a clear path from `(0, 0)` to `(n - 1, n - 1)`, or `-1` if no such path exists.

### Examples

**Example 1**

- Input: `grid = [[0, 1], [1, 0]]`
- Output: `2`

The two open cells touch at a corner, so the diagonal is a valid two-cell path.

**Example 2**

- Input: `grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]`
- Output: `-1`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Reject blocked endpoints immediately:** A path cannot start or finish on a cell containing 1. This also handles the one-cell grid, whose answer is one only when its sole cell is open.

**Search by increasing path length:** Put `(0, 0, 1)` in a FIFO queue. Removing the front state processes the smallest unprocessed distance. For each cell, inspect all eight offsets except `(0, 0)` and enqueue every in-bounds open neighbor with distance increased by one.

**Mark on enqueue:** Change an open cell to 1 as soon as it enters the queue. The first discovery is already along a shortest path in this unweighted graph, so a later discovery cannot improve its distance. Early marking prevents duplicate queue entries.

Breadth-first search visits cells in nondecreasing path length. Therefore, when the destination is removed, its stored distance is the minimum possible. If the queue empties first, every open cell reachable from the start has been explored and no clear path exists.

#### Complexity detail

The matrix has $n^2$ cells. Each is enqueued at most once and checks eight constant-count neighbors, giving $O(n^2)$ time. The queue can hold $O(n^2)$ cells in the worst case. Reusing `grid` for visited marks avoids a separate visited matrix but does mutate the supplied working copy.

#### Alternatives and edge cases

- **Dijkstra with a heap:** It is correct, but every edge has unit weight, so heap ordering adds unnecessary logarithmic overhead.
- **List queue with `pop(0)`:** It preserves BFS correctness but repeatedly shifts the remaining queue and scales worse than a deque.
- **Depth-first search:** The first found path need not be shortest and exhaustive simple-path search can be exponential.
- **Blocked start or destination:** Return `-1` without searching.
- **Single open cell:** Return 1 because the start and destination are the same visited cell.
- **Corner movement:** Diagonal neighbors are valid even when the two orthogonal cells beside the corner are blocked.
- **No route:** Exhaustion of the queue yields `-1`.

</details>
