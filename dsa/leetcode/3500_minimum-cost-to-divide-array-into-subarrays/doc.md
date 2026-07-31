# Minimum Cost to Divide Array Into Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3500 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/) |

## Problem Description

### Goal

You are given equally sized integer arrays `nums` and `cost`, together with an integer `k`. Divide both arrays at the same boundaries so that `nums` becomes one or more non-empty contiguous subarrays covering every element in order. Number the resulting subarrays from $1$ in their left-to-right order.

If the $i$th subarray spans indices $l$ through $r$, its cost is the sum of `nums` from index $0$ through $r$, plus $k i$, multiplied by the sum of `cost` from $l$ through $r$. Add this value for every chosen subarray. Return the minimum total over all valid divisions; the number of subarrays is part of the choice rather than an input requirement.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.
- `cost`: A list of $n$ positive integers whose indices align with `nums`.
- `k`: A positive integer used in the order-dependent term of each subarray.

The constraints are $1 \le n \le 1000$ and $1 \le \texttt{nums[i]}, \texttt{cost[i]}, k \le 1000$.

**Return value**

Return the minimum possible total cost as an integer.

### Examples

**Example 1**

- Input: `nums = [3,1,4], cost = [4,6,6], k = 1`
- Output: `110`
- Explanation: Divide after index $1$. The first subarray costs `(3 + 1 + 1 * 1) * (4 + 6) = 50`, and the second costs `(3 + 1 + 4 + 1 * 2) * 6 = 60`.

**Example 2**

- Input: `nums = [4,8,5,1,14,2,2,12,1], cost = [7,2,8,4,2,2,1,1,2], k = 7`
- Output: `985`
- Explanation: One optimal division is `[4,8,5,1]`, `[14,2,2]`, and `[12,1]`, whose respective costs are `525`, `250`, and `210`.

**Example 3**

- Input: `nums = [2], cost = [3], k = 5`
- Output: `21`
- Explanation: The only subarray has cost `(2 + 5 * 1) * 3 = 21`.
