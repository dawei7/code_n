# Shortest Subarray to be Removed to Make Array Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1574 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/) |

## Problem Description
### Goal

Given an integer array `arr`, remove one contiguous subarray so that the elements left behind are in non-decreasing order. The removed subarray may be empty, which matters when the original array already satisfies the ordering requirement.

Removing a subarray preserves the relative order of every retained element. The retained portion can therefore consist of a prefix, a suffix, or a prefix joined directly to a suffix; either retained side may be empty. Equal adjacent values are allowed because the target order is non-decreasing rather than strictly increasing.

Return the minimum possible number of removed elements. The answer is zero for an already non-decreasing array, while removing all but one element is always sufficient.

### Function Contract
**Inputs**

- `arr`: An integer array of length $N$, where $1 \le N \le 10^5$ and $1 \le \texttt{arr[i]} \le 10^9$.

**Return value**

Return the minimum length of a contiguous subarray whose removal leaves `arr` in non-decreasing order.

### Examples
**Example 1**

- Input: `arr = [1, 2, 3, 10, 4, 2, 3, 5]`
- Output: `3`

**Example 2**

- Input: `arr = [5, 4, 3, 2, 1]`
- Output: `4`

**Example 3**

- Input: `arr = [1, 2, 3]`
- Output: `0`
