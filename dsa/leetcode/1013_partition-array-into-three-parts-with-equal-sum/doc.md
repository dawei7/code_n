# Partition Array Into Three Parts With Equal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1013 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/) |

## Problem Description

### Goal

You are given an integer array `arr`. Determine whether it can be partitioned, without reordering any elements, into exactly three non-empty contiguous parts whose sums are equal.

Formally, return `true` when there are indices `i` and `j` with `i + 1 < j` such that the sum from index `0` through `i`, the sum from `i + 1` through `j - 1`, and the sum from `j` through the final index are all the same. Otherwise, return `false`.

### Function Contract

**Inputs**

- `arr`: an integer array of length $N$, where $3\le N\le5\cdot10^4$ and $-10^4\le\texttt{arr[i]}\le10^4$.

**Return value**

- `True` if three non-empty contiguous equal-sum parts exist; otherwise `False`.

### Examples

**Example 1**

- Input: `arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]`
- Output: `True`
- Explanation: The three sums are `0 + 2 + 1`, `-6 + 6 - 7 + 9 + 1`, and `2 + 0 + 1`, each equal to `3`.

**Example 2**

- Input: `arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]`
- Output: `False`

**Example 3**

- Input: `arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]`
- Output: `True`
- Explanation: The three contiguous parts each sum to `6`.
