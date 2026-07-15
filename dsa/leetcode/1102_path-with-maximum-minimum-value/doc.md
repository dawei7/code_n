# Path With Maximum Minimum Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1102 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/path-with-maximum-minimum-value/) |

## Problem Description

### Goal

Given an $m \times n$ integer matrix `grid`, start at the top-left cell `(0, 0)` and reach the bottom-right cell `(m - 1, n - 1)`. Each move goes to a horizontally or vertically adjacent cell; cells may be revisited, although an optimal path never needs a cycle.

The score of a path is the minimum cell value encountered anywhere on it. Among every valid path between the two corners, return the maximum possible score.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ matrix, where $1 \leq m,n \leq 100$ and $0 \leq \texttt{grid[row][col]} \leq 10^9$.

Let $V = mn$ be the number of cells.

**Return value**

The largest achievable minimum cell value over all four-directional paths from the top-left to the bottom-right cell.

### Examples

**Example 1**

- Input: `grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]`
- Output: `4`

**Example 2**

- Input: `grid = [[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]`
- Output: `2`

**Example 3**

- Input: `grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]`
- Output: `3`

### Required Complexity

- **Time:** $O(V \log V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Treat path quality as a bottleneck.** Reaching a neighbor from a path with score `score` produces `candidate = min(score, grid[next_row][next_col])`. A max-heap orders frontier states by this candidate, so the next removed state has the greatest path minimum currently available.

**Finalize the strongest score first.** Start with the top-left value. When a cell is popped for the first time, no later frontier state can offer it a larger bottleneck: every later state has a score no greater than the current heap maximum, and extending a path can only preserve or reduce its minimum. Mark that cell visited and push each unvisited neighbor with the updated candidate.

**Return when the destination is popped.** The same finalization argument applies to the bottom-right cell. Its first popped score is at least every unprocessed path's frontier score, so no alternative path can improve it.

This is Dijkstra's greedy proof with `min` replacing additive edge relaxation and a max-heap replacing a min-heap. The bottleneck of a path never increases when extended, which is the monotonic property needed for permanent finalization.

#### Complexity detail

There are $V=mn$ cells and at most four adjacency edges per cell. Heap insertion and removal cost $O(\log V)$, giving $O(V \log V)$ time. The heap and visited matrix each store at most $O(V)$ states.

#### Alternatives and edge cases

- **Descending cells plus union-find:** Activate cells from highest to lowest value and join active neighbors until the two corners connect; this also takes $O(V \log V)$ time.
- **Binary search with reachability:** Test whether cells at least a threshold connect the corners, yielding $O(V \log U)$ time for value range $U$.
- **Test every integer threshold:** It is correct but pseudopolynomial and can take $O(UV)$ time when values are large.
- **Single cell:** The path contains only that cell, so its value is the answer.
- **Low endpoint:** The answer can never exceed either corner value because every path includes both endpoints.
- **No diagonal movement:** A high-valued diagonal alone does not form a path; only four cardinal directions are allowed.

</details>
