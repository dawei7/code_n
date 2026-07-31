# Maximize Y-Sum by Picking a Triplet of Distinct X-Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3572 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/) |

## Problem Description

### Goal

Two integer arrays `x` and `y` describe paired values at the same indices. Choose three distinct indices such that their three corresponding `x` values are pairwise distinct.

Among every valid triplet, maximize the sum of the three associated `y` values. If the array contains fewer than three distinct values in `x`, no qualifying triplet exists and the answer is `-1`.

### Function Contract

**Inputs**

- `x`: An integer array of length $n$, where $3\le n\le10^5$ and $1\le\texttt{x[i]}\le10^6$.
- `y`: An integer array of the same length, where $1\le\texttt{y[i]}\le10^6$.

Let $u$ be the number of distinct values in `x`.

**Return value**

Return the largest possible sum `y[i] + y[j] + y[k]` over three indices whose `x` values are pairwise distinct, or `-1` when $u<3$.

### Examples

**Example 1**

- Input: `x = [1,2,1,3,2], y = [5,3,4,6,2]`
- Output: `14`
- Explanation: The best representatives for `x` values `1`, `2`, and `3` contribute `5`, `3`, and `6`.

**Example 2**

- Input: `x = [1,2,1,2], y = [4,5,6,7]`
- Output: `-1`
- Explanation: Only two distinct `x` values occur.

---
