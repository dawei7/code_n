# K-th Nearest Obstacle Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3275 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [K-th Nearest Obstacle Queries](https://leetcode.com/problems/k-th-nearest-obstacle-queries/) |

## Problem Description

### Goal

An infinite two-dimensional plane initially contains no obstacles. Each entry `queries[i] = [x, y]` adds one obstacle at the coordinate $(x, y)$; every queried coordinate is unique, so no obstacle is built twice. Its distance from the origin is the Manhattan distance $lvert x \rvert + \lvert y \rvert$.

After every addition, report the distance of the $k$th nearest obstacle among all obstacles built so far. Equal distances occupy separate positions because they belong to separate obstacles. If fewer than $k$ obstacles exist after a query, report `-1` for that position. Return all reports in query order.

### Function Contract

**Inputs**

- `queries`: A nonempty list of distinct coordinate pairs `[x, y]`, with $-10^9 \le x, y \le 10^9$.
- `k`: The requested one-based nearest rank, with $1 \le k \le 10^5$.

Let $n$ be the number of queries, where $1 \le n \le 2 \cdot 10^5$.

**Return value**

Return a list of $n$ integers. Entry $i$ is the $k$th smallest obstacle distance after processing `queries[i]`, or `-1` when fewer than $k$ obstacles have been added.

### Examples

#### Example 1

- **Input:** `queries = [[1, 2], [3, 4], [2, 3], [-3, 0]], k = 2`
- **Output:** `[-1, 7, 5, 3]`
- **Explanation:** The sorted distance prefixes are `[3]`, `[3, 7]`, `[3, 5, 7]`, and `[3, 3, 5, 7]`.

#### Example 2

- **Input:** `queries = [[5, 5], [4, 4], [3, 3]], k = 1`
- **Output:** `[10, 8, 6]`
- **Explanation:** Each new obstacle becomes the nearest one.

#### Example 3

- **Input:** `queries = [[1, 0], [0, 1], [-1, 0]], k = 2`
- **Output:** `[-1, 1, 1]`
- **Explanation:** Distinct obstacles at the same distance count separately toward the requested rank.
