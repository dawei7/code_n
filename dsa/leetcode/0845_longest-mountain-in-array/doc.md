# Longest Mountain in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 845 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Dynamic Programming, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-mountain-in-array/) |

## Problem Description
### Goal
An array is a mountain when it has at least three elements and contains an interior peak. Every element before that peak must be strictly increasing toward it, and every element after the peak must be strictly decreasing away from it. Consequently, neither side may be empty, and equal adjacent values cannot occur inside a mountain.

Given an integer array `arr`, find the maximum length among all contiguous subarrays that satisfy this mountain definition. Return `0` when no mountain subarray exists.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $1 \leq n \leq 10^4$ and $0 \leq \texttt{arr[i]} \leq 10^4$.

**Return value**

Return the length of the longest subarray that is strictly increasing to one interior peak and then strictly decreasing. Return `0` if no such subarray exists.

### Examples
**Example 1**

- Input: `arr = [2,1,4,7,3,2,5]`
- Output: `5`

The subarray `[1,4,7,3,2]` is the longest mountain.

**Example 2**

- Input: `arr = [2,2,2]`
- Output: `0`

Equal adjacent values cannot form either strict side of a mountain.

**Example 3**

- Input: `arr = [0,1,0]`
- Output: `3`

The entire array rises to `1` and then falls.
