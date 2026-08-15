# Minimum Operations to Exceed Threshold Value II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3066 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `nums` and an integer threshold `k`. You may repeatedly transform the array while it contains at least two elements.

In one operation, select the two smallest current values, call them $x$ and $y$, and remove both occurrences. Insert the value `min(x, y) * 2 + max(x, y)` at any array position. The insertion position does not affect which values are present for later operations.

Return the minimum number of operations needed until every current value is greater than or equal to `k`. The input guarantees that this condition can always be reached.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$.
- `k`: The inclusive threshold every final array value must meet.

The constraints are $2 \le n \le 2 \cdot 10^5$, $1 \le \texttt{nums[i]} \le 10^9$, and $1 \le k \le 10^9$. A valid sequence of operations is guaranteed to exist.

**Return value**

Return the minimum number of required two-smallest combination operations.

### Examples

#### Example 1

- **Input:** `nums = [2, 11, 10, 1, 3], k = 10`
- **Output:** `2`
- **Explanation:** Combine `1` and `2` into `4`, then combine `3` and `4` into `10`. The remaining values are `[10, 11, 10]`.

#### Example 2

- **Input:** `nums = [1, 1, 2, 4, 9], k = 20`
- **Output:** `4`
- **Explanation:** The successive arrays can contain `[2, 4, 9, 3]`, then `[7, 4, 9]`, then `[15, 9]`, and finally `[33]`.
