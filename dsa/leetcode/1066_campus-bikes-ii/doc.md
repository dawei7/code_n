# Campus Bikes II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1066 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/campus-bikes-ii/) |

## Problem Description

### Goal

Workers and bikes occupy unique positions on a two-dimensional grid. Array `workers` lists every worker coordinate, and `bikes` lists every bike coordinate. There are at least as many bikes as workers.

Assign exactly one distinct bike to each worker. The cost of an assignment is the sum, over all workers, of the Manhattan distance between that worker and the assigned bike. Return the minimum possible total cost among all valid one-to-one assignments; bikes not assigned to a worker may remain unused.

For points $(x_1,y_1)$ and $(x_2,y_2)$, Manhattan distance is

$$
\lvert x_1-x_2 \rvert+\lvert y_1-y_2 \rvert.
$$

### Function Contract

**Inputs**

- `workers`: an array of $W$ coordinate pairs, where $1 \le W \le B$.
- `bikes`: an array of $B$ coordinate pairs, where $B \le 10$.
- Every coordinate is an integer from $0$ through $999$, and all worker and bike positions are unique.

**Return value**

- The minimum sum of Manhattan distances after assigning a different bike to every worker.

### Examples

**Example 1**

- Input: `workers = [[0, 0], [2, 1]], bikes = [[1, 2], [3, 3]]`
- Output: `6`
- Explanation: Assigning bike 0 to worker 0 and bike 1 to worker 1 costs `3 + 3`.

**Example 2**

- Input: `workers = [[0, 0], [1, 1], [2, 0]], bikes = [[1, 0], [2, 2], [2, 1]]`
- Output: `4`

**Example 3**

- Input: `workers = [[0, 0]], bikes = [[5, 5]]`
- Output: `10`
