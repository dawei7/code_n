# Combinations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 77 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/combinations/) |

## Problem Description
### Goal
Given positive integers `n` and `k`, choose exactly `k` distinct values from the inclusive range `1` through `n`. Each choice defines a combination, so rearranging the same selected values does not create another result.

Return all `C(n, k)` combinations exactly once. Values within a combination and the result collection may appear in any order. When $k = n$, the only answer contains the entire range; when $k = 1$, each range value forms one singleton combination.

### Function Contract
**Inputs**

- `n`: the inclusive upper value, with $1 \le n \le 20$
- `k`: the required combination size, with $1 \le k \le n$

**Return value**

A `List[List[int]]` containing all `C(n,k)` combinations.

### Examples
**Example 1**

- Input: `n = 4, k = 2`
- Output: `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]` in any order

**Example 2**

- Input: `n = 2, k = 1`
- Output: `[[1],[2]]`

**Example 3**

- Input: `n = 3, k = 3`
- Output: `[[1,2,3]]`
