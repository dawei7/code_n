# Campus Bikes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1057 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/campus-bikes/) |

## Problem Description

### Goal

A campus is represented by the X-Y plane. There are $W$ workers and $B$ bikes, where $W \le B$. Array `workers` gives the position of every worker, and `bikes` gives the position of every bike. Every worker and bike location is unique.

Assign one bike to each worker by repeatedly examining the workers and bikes that are still available. Choose the worker-bike pair having the shortest **Manhattan distance**. If several pairs have that same shortest distance, choose the pair with the smallest worker index; if a tie remains, choose the smallest bike index. Assign that bike to that worker and continue until no worker is available.

For points $(x_1,y_1)$ and $(x_2,y_2)$, their Manhattan distance is

$$
\lvert x_1-x_2 \rvert + \lvert y_1-y_2 \rvert.
$$

Return an array `answer` of length $W$ in which `answer[i]` is the 0-indexed bike assigned to worker `i`.

### Function Contract

**Inputs**

- `workers`: an array of $W$ coordinate pairs, where $1 \le W \le 1000$.
- `bikes`: an array of $B$ coordinate pairs, where $W \le B \le 1000$.
- Each coordinate is an integer in $[0,999]$, and all worker and bike locations are unique.
- Let $D$ be the greatest possible Manhattan distance between two allowed locations; here $D=1998$.

**Return value**

- An integer array of length $W$ mapping each worker index to its assigned bike index.

### Examples

**Example 1**

- Input: `workers = [[0, 0], [2, 1]], bikes = [[1, 2], [3, 3]]`
- Output: `[1, 0]`
- Explanation: Worker 1 and bike 0 form the uniquely closest pair. After they are assigned, worker 0 receives bike 1.

**Example 2**

- Input: `workers = [[0, 0], [1, 1], [2, 0]], bikes = [[1, 0], [2, 2], [2, 1]]`
- Output: `[0, 2, 1]`
- Explanation: Worker 0 first receives bike 0. Workers 1 and 2 are equally far from bike 2, so the smaller worker index gives that bike to worker 1; worker 2 then receives bike 1.
