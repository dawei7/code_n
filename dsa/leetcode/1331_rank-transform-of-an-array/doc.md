# Rank Transform of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1331 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/) |

## Problem Description
### Goal
Given an integer array `arr`, replace every element by a positive integer rank that represents its order among the array's distinct values.

Ranks start at 1. A larger original value must receive a larger rank, equal values must receive the same rank, and the assigned ranks must be as small as possible. Consequently, the smallest distinct value has rank 1 and each next distinct value has the next integer rank.

Return ranks in the original element order. An empty input produces an empty output.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $0\le n\le10^5$ and $-10^9\le\texttt{arr[i]}\le10^9$.

**Return value**

An array of length $n$ in which each value is replaced by one plus the number of distinct input values smaller than it.

### Examples
**Example 1**

- Input: `arr = [40,10,20,30]`
- Output: `[4,1,2,3]`

**Example 2**

- Input: `arr = [100,100,100]`
- Output: `[1,1,1]`
- Explanation: Equal elements share the smallest possible rank.

**Example 3**

- Input: `arr = [37,12,28,9,100,56,80,5,12]`
- Output: `[5,3,4,2,8,6,7,1,3]`
