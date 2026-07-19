# Subsequence of Size K With the Largest Even Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2098 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. Among all subsequences containing exactly `k` elements, find the largest possible sum that is even.

A subsequence is formed by deleting any number of elements without changing the relative order of those retained. Because only the sum matters, choosing a set of positions also determines a valid subsequence in their original order. Return the largest even sum, or `-1` when no size-$k$ subsequence has an even sum.

### Function Contract

Let $n$ be the length of `nums`.

**Inputs**

- `nums`: a list of $n$ integers, where $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.
- `k`: the required subsequence length, where $1 \le k \le n$.

**Return value**

Return the largest even sum obtainable from exactly `k` elements, or `-1` if no such choice exists.

### Examples

**Example 1**

- Input: `nums = [4,1,5,3,1]`, `k = 3`
- Output: `12`
- Explanation: The subsequence `[4,5,3]` has the largest even sum, $4 + 5 + 3 = 12$.

**Example 2**

- Input: `nums = [4,6,2]`, `k = 3`
- Output: `12`
- Explanation: All three values are selected.

**Example 3**

- Input: `nums = [1,3,5]`, `k = 1`
- Output: `-1`
- Explanation: Every possible one-element sum is odd.
