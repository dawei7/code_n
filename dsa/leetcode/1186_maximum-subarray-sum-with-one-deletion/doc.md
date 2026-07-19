# Maximum Subarray Sum with One Deletion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1186 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) |

## Problem Description

### Goal

Given an integer array `arr`, choose a non-empty subarray—that is, a contiguous range of its elements. From the chosen subarray, you may optionally delete at most one element, and you want the sum of the elements that remain to be as large as possible.

Return that maximum sum. Deletion is optional, so an unchanged subarray is allowed. If an element is deleted, at least one element must still remain; deleting the only element of a length-one subarray to obtain an empty result is forbidden.

### Function Contract

**Inputs**

- `arr`: A list of $n$ integers, where $1\le n\le10^5$ and $-10^4\le\texttt{arr[i]}\le10^4$.

**Return value**

- The maximum sum obtainable from a non-empty subarray after deleting zero or one of its elements.

### Examples

**Example 1**

- Input: `arr = [1,-2,0,3]`
- Output: `4`

Choose the entire subarray and delete `-2`; the remaining elements sum to `1 + 0 + 3 = 4`.

**Example 2**

- Input: `arr = [1,-2,-2,3]`
- Output: `3`

Choosing the one-element subarray `[3]` is better than connecting the separated positive values.

**Example 3**

- Input: `arr = [-1,-1,-1,-1]`
- Output: `-1`

The result cannot be empty, so deleting the only value from a one-element choice cannot produce zero.
