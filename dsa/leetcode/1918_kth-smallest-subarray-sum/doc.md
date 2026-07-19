# Kth Smallest Subarray Sum

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/kth-smallest-subarray-sum/) |
| Frontend ID | 1918 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an integer array `nums` containing only positive values. Every non-empty contiguous subarray contributes one sum, and equal sums from different subarray positions remain separate entries.

Arrange all $N(N+1)/2$ subarray sums in non-decreasing order and return the value at rank `k`, where ranks are one-based.

The choice concerns values rather than intervals: the function returns only the selected sum, not the subarray that produced it. If several subarrays have the same sum, each occurrence keeps its own place in the ordering.

### Function Contract

**Inputs**

- `nums`: an array of $N$ positive integers, with $1 \le N \le 2 \cdot 10^4$ and $1 \le \texttt{nums[i]} \le 5 \cdot 10^4$.
- `k`: a one-based rank satisfying $1 \le k \le N(N+1)/2$.

**Return value**

- Return the `k`th smallest sum among all non-empty contiguous subarrays of `nums`.

### Examples

**Example 1**

- Input: `nums = [2, 1, 3], k = 4`
- Output: `3`

The sorted subarray sums are `1, 2, 3, 3, 4, 6`, so the fourth value is `3`.

**Example 2**

- Input: `nums = [3, 3, 5, 5], k = 7`
- Output: `10`

The sorted sums are `3, 3, 5, 5, 6, 8, 10, 11, 13, 16`.
