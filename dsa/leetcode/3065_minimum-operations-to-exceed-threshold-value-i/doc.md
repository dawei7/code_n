# Minimum Operations to Exceed Threshold Value I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3065 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `nums` and an integer threshold `k`. One operation removes one occurrence of the smallest value currently present in the array.

Find the minimum number of operations required until every remaining array element is greater than or equal to `k`. The input guarantees that at least one original element already meets the threshold, so completing the process never requires removing the entire array.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$.
- `k`: The inclusive lower bound that every remaining value must meet.

The constraints are $1 \le n \le 50$, $1 \le \texttt{nums[i]} \le 10^9$, and $1 \le k \le 10^9$. At least one index $i$ satisfies $\texttt{nums[i]} \ge k$.

**Return value**

Return the minimum number of smallest-element removals needed so that every remaining value is at least `k`.

### Examples

#### Example 1

- **Input:** `nums = [2, 11, 10, 1, 3], k = 10`
- **Output:** `3`
- **Explanation:** Removing `1`, `2`, and `3` leaves `[11, 10]`, whose values both meet the threshold.

#### Example 2

- **Input:** `nums = [1, 1, 2, 4, 9], k = 1`
- **Output:** `0`
- **Explanation:** Every value is already at least `1`.

#### Example 3

- **Input:** `nums = [1, 1, 2, 4, 9], k = 9`
- **Output:** `4`
- **Explanation:** The four values below `9` must be removed, leaving the single value `9`.
