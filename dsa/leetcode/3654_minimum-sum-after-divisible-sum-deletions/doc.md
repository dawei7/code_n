# Minimum Sum After Divisible Sum Deletions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3654 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/) |

## Problem Description
### Goal

You are given a positive integer array `nums` and an integer `k`. You may repeatedly delete any contiguous subarray whose element sum is divisible by `k`. After a deletion, the elements on its two sides close the gap, so later deletions may span portions that were not adjacent in the original array.

Perform any number of valid deletions, including none, and return the smallest possible sum of the elements that remain.

### Function Contract
**Inputs**

- `nums`: Between 1 and $10^5$ positive integers, each at most $10^6$.
- `k`: The divisibility modulus, with $1\le k\le10^5$.

**Return value**

Return the minimum sum achievable after repeatedly deleting contiguous subarrays whose sums are multiples of `k`.

### Examples
**Example 1**

- Input: `nums = [1,1,1]`, `k = 2`
- Output: `1`
- Explanation: Delete either adjacent pair of ones, whose sum is 2.

**Example 2**

- Input: `nums = [3,1,4,1,5]`, `k = 3`
- Output: `5`
- Explanation: Delete `[1,4,1]` with sum 6, then delete the remaining leading 3.
