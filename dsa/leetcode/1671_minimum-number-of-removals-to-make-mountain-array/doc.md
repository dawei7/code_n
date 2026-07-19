# Minimum Number of Removals to Make Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1671 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) |

## Problem Description
### Goal
An array is a mountain when it has at least three elements and some interior peak index. Values before that peak must be strictly increasing, and values after it must be strictly decreasing. Both sides must therefore contain at least one element; a purely increasing or purely decreasing sequence is not a mountain.

Given an integer array `nums`, remove as few elements as possible while preserving the relative order of all remaining elements so that they form a mountain array. Return the minimum removal count. The input guarantee ensures that at least one valid mountain subsequence can be retained.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $3 \le n \le 1000$ and values may repeat.

**Return value**

Return the minimum number of elements that must be removed so the remaining subsequence is strictly increasing to one interior peak and strictly decreasing afterward.

### Examples
**Example 1**

- Input: `nums = [1,3,1]`
- Output: `0`

**Example 2**

- Input: `nums = [2,1,1,5,6,2,3,1]`
- Output: `3`
- Explanation: retaining `[1,5,6,3,1]` produces a five-element mountain.
