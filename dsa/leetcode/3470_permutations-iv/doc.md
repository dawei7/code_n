# Permutations IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3470 |
| Difficulty | Hard |
| Topics | Array, Math, Combinatorics, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/permutations-iv/) |

## Problem Description
### Goal
Given positive integers `n` and `k`, consider permutations of the first $n$ positive integers. A permutation is alternating when every adjacent pair contains one odd value and one even value; equivalently, no two adjacent elements may both be odd or both be even.

Sort all alternating permutations in lexicographical order and return the $k$-th one, where `k` is 1-indexed. If the number of valid alternating permutations is smaller than `k`, return an empty list instead.

### Function Contract
**Inputs**

- `n`: The inclusive upper endpoint of the values `1` through `n` used exactly once.
- `k`: The 1-indexed lexicographical rank to retrieve.

The constraints are $1\le n\le100$ and $1\le k\le10^{15}$.

**Return value**

Return the requested alternating permutation, or `[]` when that rank does not exist.

### Examples
**Example 1**

- Input: `n = 4, k = 6`
- Output: `[3,4,1,2]`

This is the sixth of the eight alternating permutations of `[1,2,3,4]` in lexicographical order.

**Example 2**

- Input: `n = 3, k = 2`
- Output: `[3,2,1]`

With two odd values and one even value, the only valid permutations are `[1,2,3]` and `[3,2,1]`.

**Example 3**

- Input: `n = 2, k = 3`
- Output: `[]`

Only `[1,2]` and `[2,1]` are available, so the third rank is out of range.
