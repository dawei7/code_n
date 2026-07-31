# Maximum K to Sort a Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3644 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-k-to-sort-a-permutation/) |

## Problem Description
### Goal

You are given a permutation `nums` containing every integer from $0$ through $n-1$ exactly once. Choose one non-negative integer `k`. You may then perform any number of swaps, but a pair of current values may be exchanged only when their bitwise AND equals `k`.

Determine the maximum `k` for which the permitted swaps can transform the permutation into non-decreasing order, which for this value range is `[0, 1, ..., n - 1]`. Return `0` when the input is already sorted.

### Function Contract
**Inputs**

- `nums`: A permutation of all integers in $[0,n-1]$, where $1\le n\le 10^5$.

**Return value**

Return the greatest non-negative `k` that permits enough valid swaps to sort the permutation, or `0` if no swaps are needed.

### Examples
**Example 1**

- Input: `nums = [0,3,2,1]`
- Output: `1`
- Explanation: The misplaced values are 3 and 1, whose bitwise AND is 1. They may be swapped directly.

**Example 2**

- Input: `nums = [0,1,3,2]`
- Output: `2`
- Explanation: Swapping 3 and 2 is allowed because `3 & 2 = 2`.

**Example 3**

- Input: `nums = [3,2,1,0]`
- Output: `0`
- Explanation: The bitwise AND of all misplaced values is 0, and no positive value can permit every necessary movement.
