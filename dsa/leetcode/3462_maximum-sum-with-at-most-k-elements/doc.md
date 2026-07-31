# Maximum Sum With at Most K Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3462 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/) |

## Problem Description
### Goal
Choose at most `k` cells from the $n\times m$ integer matrix `grid` and maximize the sum of their values. Every chosen cell contributes independently; adjacency and positions within a row impose no restrictions.

Row `i` has its own capacity `limits[i]`: no more than that many cells may be chosen from the row. The global count across all rows must also not exceed `k`. Matrix entries are nonnegative, and `k` never exceeds the sum of the row capacities, so an optimal selection may always use exactly `k` cells without decreasing its sum.

### Function Contract
**Inputs**

- `grid`: An $n\times m$ matrix of nonnegative integers.
- `limits`: A length-$n$ list where `limits[i]` is the maximum number of selections permitted from row `i`.
- `k`: The maximum total number of selected cells.

The constraints are $1 \le n,m \le 500$, $0 \le \texttt{grid[i][j]} \le 10^5$, $0 \le \texttt{limits[i]} \le m$, and

$$
0 \le k \le \min\left(nm,\sum_{i=0}^{n-1}\texttt{limits[i]}\right).
$$

**Return value**

Return the maximum sum obtainable under both the row capacities and the global selection limit.

### Examples
**Example 1**

- Input: `grid = [[1, 2], [3, 4]], limits = [1, 2], k = 2`
- Output: `7`

Both selected values, `4` and `3`, may come from the second row because its capacity is two.

**Example 2**

- Input: `grid = [[5, 3, 7], [8, 2, 6]], limits = [2, 2], k = 3`
- Output: `21`

Select `7` from the first row and `8` and `6` from the second row.

**Example 3**

- Input: `grid = [[10]], limits = [1], k = 1`
- Output: `10`
