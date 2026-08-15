# Count the Number of Inversions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3193 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-inversions/) |

## Problem Description

### Goal

You are given an integer `n` and an array `requirements`. Each entry
`[end, cnt]` constrains a prefix: the permutation positions from `0` through
`end` must contain exactly `cnt` inversions.

For an integer array `nums`, an inversion is a pair of indices $(i,j)$ such
that $i<j$ and `nums[i] > nums[j]`. Count the permutations of
`[0, 1, 2, ..., n - 1]` that satisfy every prefix requirement. Because the
count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The permutation length, with $2 \le n \le 300$.
- `requirements`: Between $1$ and $n$ pairs `[end, cnt]`. Every `end` is
  unique and lies in $[0,n-1]$; every `cnt` lies in $[0,400]$.

At least one requirement has `end = n - 1`, so the inversion count of the
complete permutation is always specified. Let

$$
C = \max_{[e,c]\in\texttt{requirements}} c.
$$

**Return value**

The number of permutations satisfying all requirements, reduced modulo
$10^9+7$.

### Examples

#### Example 1

- **Input:** `n = 3, requirements = [[2, 2], [0, 0]]`
- **Output:** `2`

The valid permutations are `[2, 0, 1]` and `[1, 2, 0]`. Each has two
inversions in its full length-three prefix and zero in its length-one prefix.

#### Example 2

- **Input:** `n = 3, requirements = [[2, 2], [1, 1], [0, 0]]`
- **Output:** `1`

Only `[2, 0, 1]` also has exactly one inversion in its first two positions.

#### Example 3

- **Input:** `n = 2, requirements = [[0, 0], [1, 0]]`
- **Output:** `1`

Only the increasing permutation `[0, 1]` has no inversion in either required
prefix.
