# Find the Largest Almost Missing Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3471 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. Consider every contiguous subarray whose length is exactly `k`. An integer is **almost missing** when it appears in exactly one of those subarrays. A value is counted once for a particular subarray even if that subarray contains the value at multiple positions; the condition concerns how many distinct size-`k` subarrays contain it.

Return the largest almost missing integer. If every value occurs in either zero or at least two size-`k` subarrays, return `-1`. The full range of valid window positions must be considered, including the special cases in which each window has one element or the only window covers the entire array.

### Function Contract

**Inputs**

- `nums`: The integer array to examine.
- `k`: The exact length of every considered subarray.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\le n\le50$, $0\le\texttt{nums[i]}\le50$, and $1\le k\le n$.

**Return value**

Return the largest value contained in exactly one size-`k` subarray, or `-1` if no such value exists.

### Examples

#### Example 1

- **Input:** `nums = [3,9,2,1,7], k = 3`
- **Output:** `7`

The value `7` occurs only in `[2,1,7]`. Although `3` also belongs to exactly one window, `7` is larger.

#### Example 2

- **Input:** `nums = [3,9,7,2,1,7], k = 4`
- **Output:** `3`

Only `3` occurs in one size-four subarray. The repeated value `7` is present in all three windows.

#### Example 3

- **Input:** `nums = [0,0], k = 1`
- **Output:** `-1`

Each singleton window contains one zero, so zero appears in two distinct windows.
