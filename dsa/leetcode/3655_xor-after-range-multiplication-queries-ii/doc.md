# XOR After Range Multiplication Queries II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3655 |
| Difficulty | Hard |
| Topics | Array, Divide and Conquer, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/) |

## Problem Description

### Goal

You are given an integer array `nums` and up to $10^5$ multiplication queries. A query `[l, r, k, v]` visits the arithmetic progression of indices

$$
l,\ l+k,\ l+2k,\ \ldots
$$

through the last visited index not exceeding `r`. Multiply every visited current value by `v` and reduce it modulo $10^9+7$. Apply the complete query sequence and return the bitwise XOR of all final array values.

This version has substantially larger array and query limits than the direct-simulation version, so an implementation must avoid visiting every affected index of every dense query separately.

### Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers, where $1\le n\le10^5$ and each value is at most $10^9$.
- `queries`: Between 1 and $10^5$ rows `[l, r, k, v]`, where $0\le l\le r<n$, $1\le k\le n$, and $1\le v\le10^5$.

**Return value**

Return the XOR of all values after every requested modular multiplication has taken effect.

### Examples

#### Example 1

- **Input:** `nums = [1,1,1]`, `queries = [[0,2,1,4]]`
- **Output:** `4`
- **Explanation:** All entries become 4, and the XOR of three copies of 4 is 4.

#### Example 2

- **Input:** `nums = [2,3,1,5,4]`, `queries = [[1,4,2,3],[0,2,1,2]]`
- **Output:** `31`
- **Explanation:** The final array is `[4,18,2,15,4]`.
