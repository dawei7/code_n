# Minimum Number of Increasing Subsequence to Be Removed

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3231 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/) |

## Problem Description

### Goal

You are given an integer array `nums`. In one operation, choose a strictly increasing subsequence of the current array and remove every chosen element. The chosen positions need not be contiguous, but their values must increase strictly in their existing left-to-right order.

Repeat this operation until the array becomes empty. Return the minimum possible number of removals. Elements not selected in an operation retain their relative order, and equal values cannot belong to the same removed subsequence because the increase must be strict.

### Function Contract

**Inputs**

- `nums`: An integer array with $1 \leq \lvert\texttt{nums}\rvert \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^5$.

**Return value**

Return the minimum number of strictly increasing subsequences whose removal empties the array.

### Examples

**Example 1**

- Input: `nums = [5, 3, 1, 4, 2]`
- Output: `3`
- Explanation: Remove `[1, 2]`, `[3, 4]`, and `[5]`.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `1`
- Explanation: The whole array is already strictly increasing.

**Example 3**

- Input: `nums = [5, 4, 3, 2, 1]`
- Output: `5`
- Explanation: No increasing subsequence can contain two elements.
