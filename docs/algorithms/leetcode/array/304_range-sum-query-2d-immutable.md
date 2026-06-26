# Range Sum Query 2D - Immutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_15` |
| Frontend ID | 304 |
| Difficulty | Medium |
| Topics | Array, Design, Matrix, Prefix Sum |
| Official Link | [range-sum-query-2d-immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) |

## Problem Description & Examples
### Goal
Given a 2D matrix `matrix` and a list of queries `queries` where each query is `[row1, col1, row2, col2]`, compute the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

`solve(matrix, queries)` returns a list of sums for each query.

### Function Contract
**Inputs**

- `matrix`: List[List[int]]
- `queries`: List[List[int]] - [r1,c1,r2,c2]

**Return value**

List[int] - sum for each query

### Examples
**Example 1**

- Input: `matrix = [[3, 0], [1, 2]], queries = [[0, 0, 1, 1]]`
- Output: `[6]`

**Example 2**

- Input: `matrix = [[-2, 94], [7, -90]], queries = [[1, 1, 1, 1]]`
- Output: `[-90]`

**Example 3**

- Input: `matrix = [[-66, 45], [95, -84]], queries = [[1, 0, 1, 1]]`
- Output: `[11]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
