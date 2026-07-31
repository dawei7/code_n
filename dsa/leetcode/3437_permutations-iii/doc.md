# Permutations III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3437 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/permutations-iii/) |

## Problem Description

### Goal

For a positive integer $n$, consider permutations containing every integer from $1$ through $n$ exactly once. A permutation is valid when each adjacent pair contains one odd value and one even value; equivalently, the parity must alternate at every position.

Return every valid permutation in lexicographically increasing order. The order of two permutations is determined by the first position at which they differ, with the permutation containing the smaller value at that position appearing first.

### Function Contract

**Inputs**

- `n`: An integer from $1$ through $10$, inclusive.

**Return value**

Return all permutations of $[1,2,\ldots,n]$ whose adjacent values have opposite parity, sorted lexicographically.

### Examples

**Example 1**

- Input: `n = 4`
- Output: `[[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3],[4,3,2,1]]`

**Example 2**

- Input: `n = 2`
- Output: `[[1,2],[2,1]]`

**Example 3**

- Input: `n = 3`
- Output: `[[1,2,3],[3,2,1]]`
