# Maximize Subarray Sum After Removing All Occurrences of One Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3410 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Divide and Conquer, Dynamic Programming, Segment Tree, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/) |

## Problem Description

### Goal

You are given an integer array `nums`. You may perform the following operation at most once: choose any integer $x$ whose complete removal would leave the array non-empty, then remove every occurrence of $x$ from the array. The retained elements close their gaps and form the resulting array in their original relative order.

For every possible resulting array, including the unchanged array when no operation is performed, consider the sum of its maximum-sum non-empty contiguous subarray. Return the greatest such sum.

### Function Contract

**Inputs**

- `nums`: The integer array on which the optional removal is performed.

The constraints are $1\le\lvert\texttt{nums}\rvert\le10^5$ and $-10^6\le\texttt{nums[i]}\le10^6$.

**Return value**

- The maximum non-empty subarray sum obtainable after at most one legal operation.

### Examples

**Example 1**

- Input: `nums = [-3, 2, -2, -1, 3, -2, 3]`
- Output: `7`

Removing every `-2` produces `[-3, 2, -1, 3, 3]`. Its subarray `[2, -1, 3, 3]` has sum 7, which is optimal.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `10`

It is optimal to skip the operation and use the complete array.
