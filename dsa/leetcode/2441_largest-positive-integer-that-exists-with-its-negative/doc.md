# Largest Positive Integer That Exists With Its Negative

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2441 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Largest Positive Integer That Exists With Its Negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/) |

## Problem Description

### Goal

You are given an integer array `nums` that contains no zeros. A positive integer $k$ qualifies when both $k$ and its additive inverse $-k$ occur somewhere in the array. Occurrences may appear in either order, and repeated copies do not create a different candidate.

Among all qualifying positive integers, find and return the largest one. If the array contains no positive value together with its negative counterpart, return `-1` instead.

### Function Contract

**Inputs**

- `nums`: A list of $n$ nonzero integers, where $1 \le n \le 1000$ and $-1000 \le \texttt{nums[i]} \le 1000$.

**Return value**

- The largest positive integer $k$ for which both $k$ and $-k$ occur, or `-1` if none exists.

### Examples

**Example 1**

- Input: `nums = [-1, 2, -3, 3]`
- Output: `3`
- Explanation: Only 3 has its negative counterpart.

**Example 2**

- Input: `nums = [-1, 10, 6, 7, -7, 1]`
- Output: `7`
- Explanation: Both 1 and 7 qualify, so return the larger value.

**Example 3**

- Input: `nums = [-10, 8, 6, 7, -2, -3]`
- Output: `-1`
- Explanation: No positive value has its negative counterpart.
