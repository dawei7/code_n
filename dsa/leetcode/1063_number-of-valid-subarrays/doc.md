# Number of Valid Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1063 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-valid-subarrays/) |

## Problem Description

### Goal

Given an integer array `nums`, call a non-empty contiguous subarray valid when its leftmost element is less than or equal to every other element contained in that subarray.

Return the total number of valid subarrays. Each choice of left and right boundary is counted separately, and every single-element subarray is valid because it contains no later element that can be smaller than its first value.

### Function Contract

**Inputs**

- `nums`: an integer array of length $N$, where $1 \le N \le 5 \cdot 10^4$.

**Return value**

- The number of non-empty subarrays whose first element is no greater than every subsequent element in that subarray.

### Examples

**Example 1**

- Input: `nums = [1, 4, 2, 5, 3]`
- Output: `11`

**Example 2**

- Input: `nums = [3, 2, 1]`
- Output: `3`
- Explanation: Each start is immediately blocked by a smaller next value, so only the single-element subarrays are valid.

**Example 3**

- Input: `nums = [2, 2, 2]`
- Output: `6`
- Explanation: Equality is allowed, so every subarray is valid.
