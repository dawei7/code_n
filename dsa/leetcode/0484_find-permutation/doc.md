# Find Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 484 |
| Difficulty | Medium |
| Topics | Array, String, Stack, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/find-permutation/) |

## Problem Description
### Goal
Given a pattern string `s` containing only `I` and `D`, construct a permutation of the integers from `1` through `len(s) + 1`. At pattern position `i`, `I` requires the value at permutation position `i` to be smaller than the next value, while `D` requires it to be larger.

Return the lexicographically smallest permutation satisfying every adjacent comparison. Use each integer in the required range exactly once, preserve the pattern's left-to-right comparison positions, and do not return a merely valid permutation when a smaller valid prefix is possible. A run of consecutive `D` characters may require several values to appear in reverse order.

### Function Contract
**Inputs**

- `s`: a nonempty string containing only `I` and `D`

**Return value**

- The lexicographically smallest permutation whose adjacent comparisons match `s`

### Examples
**Example 1**

- Input: `s = "I"`
- Output: `[1, 2]`

**Example 2**

- Input: `s = "DI"`
- Output: `[2, 1, 3]`

**Example 3**

- Input: `s = "DDIIDI"`
- Output: `[3, 2, 1, 4, 6, 5, 7]`
