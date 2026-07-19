# Beautiful Arrangement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 526 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/beautiful-arrangement/) |

## Problem Description
### Goal
Given a positive integer `n`, arrange every integer from `1` through `n` exactly once into one-based positions. An arrangement is beautiful when, at every position `i`, either the value stored there is divisible by `i` or `i` is divisible by that value.

Return the number of different beautiful arrangements. Position order matters, so swapping values creates another permutation when the divisibility rules still hold. Every position must satisfy at least one direction of divisibility; meeting the rule only for adjacent pairs or for a subset of positions is insufficient. The function returns the count rather than the permutations themselves.

### Function Contract
**Inputs**

- `n`: the positive upper bound of the values and the permutation length

**Return value**

- The number of permutations satisfying the divisibility condition at every position

### Examples
**Example 1**

- Input: `n = 1`
- Output: `1`

**Example 2**

- Input: `n = 2`
- Output: `2`

**Example 3**

- Input: `n = 4`
- Output: `8`
