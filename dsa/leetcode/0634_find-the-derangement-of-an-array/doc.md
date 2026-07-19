# Find the Derangement of An Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 634 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Combinatorics |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-derangement-of-an-array/) |

## Problem Description
### Goal
Given a positive integer `n`, consider all permutations of `n` distinct values relative to their original positions. A derangement is a permutation in which no value appears at the same index it occupied originally.

Return the number of derangements of `n` values, modulo `1,000,000,007`. Every position must receive a different original value; a permutation with even one fixed point is excluded. For $n = 1$, no derangement exists because the sole value cannot move to another position.

### Function Contract
**Inputs**

- `n`: the positive number of distinct values and original positions

**Return value**

- The number of derangements of `n` values, reduced modulo `1,000,000,007`

### Examples
**Example 1**

- Input: `n = 3`
- Output: `2`

**Example 2**

- Input: `n = 2`
- Output: `1`

**Example 3**

- Input: `n = 1`
- Output: `0`
