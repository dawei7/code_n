# Trionic Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3640 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/trionic-array-ii/) |

## Problem Description

### Goal

Given an integer array `nums`, a trionic subarray is a contiguous range `nums[l...r]` for which two interior indices $p$ and $q$ satisfy $l<p<q<r$.

From $l$ through $p$ the values must be strictly increasing; from $p$ through $q$ they must be strictly decreasing; and from $q$ through $r$ they must again be strictly increasing. Each phase therefore contains at least one adjacent comparison.

Return the maximum sum among all trionic subarrays. Values may be negative, so the best range need not be the longest one or the whole array. At least one trionic subarray is guaranteed to exist.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $4 \le n \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the greatest element sum of any contiguous subarray following the strict increasing-decreasing-increasing pattern.

### Examples

#### Example 1

- **Input:** `nums = [0, -2, -1, -3, 0, 2, -1]`
- **Output:** `-4`
- **Explanation:** The range `[-2, -1, -3, 0, 2]` has the three required phases and sum $-4$.

#### Example 2

- **Input:** `nums = [1, 4, 2, 7]`
- **Output:** `14`
- **Explanation:** The entire array increases, decreases, then increases, and its sum is 14.
