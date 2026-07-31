# XOR After Range Multiplication Queries I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3653 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Simulation, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/xor-after-range-multiplication-queries-i/) |

## Problem Description
### Goal

You are given an integer array `nums` and an ordered list of queries. A query `[l, r, k, v]` visits indices

$$
l,\ l+k,\ l+2k,\ \ldots
$$

through the last such index not exceeding `r`. At every visited index `i`, replace the current value with `nums[i] * v` modulo $10^9+7$. Queries are processed sequentially, so a later multiplication sees the value produced by all earlier applicable queries.

After every query has been applied, return the bitwise XOR of all final array values.

### Function Contract
**Inputs**

- `nums`: An array of $n$ positive integers, where $1\le n\le1000$ and each initial value is at most $10^9$.
- `queries`: Between 1 and 1000 rows `[l, r, k, v]`, where $0\le l\le r<n$, $1\le k\le n$, and $1\le v\le10^5$.

**Return value**

Return the bitwise XOR of all entries after applying every modular multiplication in query order.

### Examples
**Example 1**

- Input: `nums = [1,1,1]`, `queries = [[0,2,1,4]]`
- Output: `4`
- Explanation: All three values become 4, and `4 ^ 4 ^ 4` equals 4.

**Example 2**

- Input: `nums = [2,3,1,5,4]`, `queries = [[1,4,2,3],[0,2,1,2]]`
- Output: `31`
- Explanation: The queries produce `[4,18,2,15,4]`, whose XOR is 31.
