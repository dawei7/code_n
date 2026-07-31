# Closest Equal Element Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3488 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-equal-element-queries/) |

## Problem Description

### Goal

The array `nums` is circular: index 0 follows index $n-1$, and travel is allowed in either direction. Each entry of `queries` is an index into this array.

For a queried index `i`, consider every other index `j` satisfying `nums[j] = nums[i]`. Find the minimum number of circular steps between `i` and any such `j`. The queried index itself is not a candidate.

Return one distance per query. If the queried value occurs nowhere else in the array, return `-1` for that query.

### Function Contract

**Inputs**

- `nums`: A circular array of positive integers.
- `queries`: A list of valid indices into `nums`.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. The constraints are $1\le q\le n\le10^5$, $1\le\texttt{nums[i]}\le10^6$, and $0\le\texttt{queries[i]}<n$.

For indices $i$ and $j$, their circular distance is

$$
\min\bigl(\lvert i-j\rvert,\ n-\lvert i-j\rvert\bigr).
$$

**Return value**

Return a list of length $q$. Its entry for each query is the smallest circular distance to another equal-valued index, or `-1` if no such index exists.

### Examples

**Example 1**

- Input: `nums = [1, 3, 1, 4, 1, 3, 2]`, `queries = [0, 3, 5]`
- Output: `[2, -1, 3]`

Index 0 reaches another 1 at index 2 in two steps. The 4 at index 3 is unique. From index 5, wrapping through indices 6 and 0 reaches the other 3 at index 1 in three steps.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`, `queries = [0, 1, 2, 3]`
- Output: `[-1, -1, -1, -1]`

Every value occurs once.

**Example 3**

- Input: `nums = [5, 1, 2, 3, 5]`, `queries = [0, 4]`
- Output: `[1, 1]`

The two copies of 5 are adjacent across the circular boundary.
