# Best Sightseeing Pair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1014 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/best-sightseeing-pair/) |

## Problem Description

### Goal

You are given an integer array `values`, where `values[i]` is the value of sightseeing spot `i`. For two spots at indices `i < j`, their distance is $j-i$.

The pair's score is the sum of both sightseeing values minus that distance, written as `values[i] + values[j] + i - j`. Choose two distinct spots in their array order and return the maximum possible score among all such pairs.

### Function Contract

**Inputs**

- `values`: an array of $N$ sightseeing values, where $2\le N\le5\cdot10^4$ and $1\le\texttt{values[i]}\le1000$.

**Return value**

- The maximum score over all index pairs `i < j`.

### Examples

**Example 1**

- Input: `values = [8, 1, 5, 2, 6]`
- Output: `11`
- Explanation: Indices `0` and `2` score `8 + 5 + 0 - 2 = 11`.

**Example 2**

- Input: `values = [1, 2]`
- Output: `2`
- Explanation: The only pair scores `1 + 2 + 0 - 1 = 2`.

**Example 3**

- Input: `values = [4, 7, 5, 8]`
- Output: `13`
- Explanation: Indices `1` and `3` score `7 + 8 + 1 - 3 = 13`.
