# Maximum Unique Subarray Sum After Deletion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3487 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/) |

## Problem Description

### Goal

You are given an integer array `nums`. Delete any number of its elements while leaving at least one element. The retained elements preserve their relative order.

After the deletions, select a subarray whose elements are all unique and whose sum is as large as possible. Because arbitrary elements may be deleted first, every desired collection of retained indices can be made contiguous by deleting the unwanted indices between them.

Return the maximum sum obtainable by this process. The final selected subarray must be non-empty.

### Function Contract

**Inputs**

- `nums`: A non-empty list of integers.

The length $n$ satisfies $1\le n\le100$, and each element satisfies $-100\le\texttt{nums[i]}\le100$.

**Return value**

Return the maximum sum of a non-empty, all-unique subarray after deleting any number of original elements.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 5]`
- **Output:** `15`

All elements are already distinct and positive, so no deletion improves the complete array.

#### Example 2

- **Input:** `nums = [1, 1, 0, 1, 1]`
- **Output:** `1`

Delete all but one copy of 1; retaining zero would not increase the sum.

#### Example 3

- **Input:** `nums = [1, 2, -1, -2, 1, 0, -1]`
- **Output:** `3`

One copy each of 1 and 2 produces the maximum sum.

#### Example 4

- **Input:** `nums = [-5, -1, -3]`
- **Output:** `-1`

With no positive or zero value available, the non-empty requirement forces retaining the greatest negative element.
