# Minimum Incompatibility

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1681 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming, Bit Manipulation, Bitmask |
| Official Link | [minimum-incompatibility](https://leetcode.com/problems/minimum-incompatibility/) |

## Problem Description & Examples
### Goal
Split the array into `k` groups of equal size. No group may contain duplicate values, and a group's incompatibility is its maximum minus minimum. Minimize the sum of group incompatibilities.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `k`: the number of groups.

**Return value**

Return the minimum total incompatibility, or `-1` if no valid partition exists.

### Examples
**Example 1**

- Input: `nums = [1,2,1,4], k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [6,3,8,1,3,1,2,2], k = 4`
- Output: `6`

**Example 3**

- Input: `nums = [5,3,3,6,3,3], k = 3`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Use bitmask dynamic programming. Precompute every subset of size `n / k` that contains unique values and its incompatibility. Then let `dp[mask]` be the minimum cost to fill the selected indices in `mask`; transition by adding one valid subset disjoint from `mask`, usually anchored on the first unused index to reduce duplicate transitions.

---

## Complexity Analysis
- **Time Complexity**: `O(3^n)` in the common subset-DP formulation
- **Space Complexity**: `O(2^n)`
