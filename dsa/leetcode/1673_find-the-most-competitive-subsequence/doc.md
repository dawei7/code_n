# Find the Most Competitive Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1673 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-most-competitive-subsequence/) |

## Problem Description
### Goal
Choose exactly $k$ elements from `nums` while preserving their original relative order. Elements not chosen may be erased from any positions, so the result is a subsequence rather than necessarily a contiguous subarray.

Among all length-$k$ subsequences, return the most competitive one: compare two candidates from left to right, and at the first index where they differ, the candidate with the smaller value is more competitive. Equal values do not decide the order, so comparison continues to the next position.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$ whose values may repeat.
- `k`: the required positive subsequence length, with $1 \le k \le n$.

**Return value**

Return the lexicographically smallest subsequence of `nums` containing exactly $k$ elements.

### Examples
**Example 1**

- Input: `nums = [3,5,2,6], k = 2`
- Output: `[2,6]`

**Example 2**

- Input: `nums = [2,4,3,3,5,4,9,6], k = 4`
- Output: `[2,3,3,4]`
