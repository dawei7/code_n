# Number of Boomerangs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 447 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-boomerangs/) |

## Problem Description
### Goal
Given unique points in the two-dimensional plane, a boomerang is an ordered triple of distinct indices `(i, j, k)` where the Euclidean distance from pivot point `i` to point `j` equals the distance from `i` to point `k`.

Return the number of boomerangs. Order matters: swapping the two equidistant endpoint indices produces a different triple, while changing the pivot defines another candidate. Compare exact squared distances to avoid floating-point error. Collinearity is not required, and each occurrence of an equal distance around a pivot can pair with every other occurrence at that distance.

### Function Contract
**Inputs**

- `points`: a list of distinct two-dimensional integer coordinates

**Return value**

- Return the number of ordered boomerangs; swapping `j` and `k` creates a different triple.

### Examples
**Example 1**

- Input: `points = [[0, 0], [1, 0], [2, 0]]`
- Output: `2`

**Example 2**

- Input: `points = [[1, 1], [2, 2], [3, 3]]`
- Output: `2`

**Example 3**

- Input: `points = [[0, 0], [1, 0], [0, 1]]`
- Output: `2`
