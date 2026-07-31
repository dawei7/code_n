# Find the Index of Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3109 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-the-index-of-permutation](https://leetcode.com/problems/find-the-index-of-permutation/) |

## Problem Description

### Goal

You are given an array `perm` of length $n$ containing every integer from $1$ through $n$ exactly once. Consider all $n!$ permutations of these integers arranged in lexicographically sorted order. Between two different permutations, the one with the smaller value at their first differing position comes earlier.

Return the zero-based index at which `perm` appears in that ordering. Because the number of preceding permutations can be very large, return the index modulo $10^9+7$.

### Function Contract

**Inputs**

- `perm`: A permutation of `[1, 2, ..., n]`, where $1 \le n \le 10^5$.

**Return value**

- The zero-based lexicographic index of `perm` among all permutations of `[1, 2, ..., n]`, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `perm = [1, 2]`
- Output: `0`
- Explanation: The two permutations are `[1, 2]` and `[2, 1]`, so the input is first.

**Example 2**

- Input: `perm = [3, 1, 2]`
- Output: `4`
- Explanation: In order, the six permutations are `[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, and `[3,2,1]`.
