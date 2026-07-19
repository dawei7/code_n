# Find Array Given Subset Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1982 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-array-given-subset-sums/) |

## Problem Description
### Goal
An unknown integer array has length `n`. You receive the multiset of all
$2^n$ subset sums of that array in arbitrary order. A subset is formed by
deleting any selection of positions, including none or all; equal values at
different positions still represent separate choices, and the empty subset
contributes sum `0`.

Recover and return any length-`n` integer array whose complete multiset of
subset sums equals the supplied multiset `sums`, including every duplicate
multiplicity. More than one reconstruction may be valid, and any valid one is
accepted. The input is guaranteed to admit at least one reconstruction.

### Function Contract
**Inputs**

- `n`: the unknown array length $N$, where $1 \le N \le 15$.
- `sums`: a list of exactly $2^N$ integers containing every subset sum with
  multiplicity, where each value lies between $-10^4$ and $10^4$, inclusive.

**Return value**

- Any list of $N$ integers whose multiset of $2^N$ subset sums is exactly
  `sums`.

### Examples
**Example 1**

- Input: `n = 3, sums = [-3, -2, -1, 0, 0, 1, 2, 3]`
- Output: `[1, 2, -3]`

The eight subsets of `[1, 2, -3]` produce precisely the supplied values.
Permutations and some sign-alternative reconstructions are also valid.

**Example 2**

- Input: `n = 2, sums = [0, 0, 0, 0]`
- Output: `[0, 0]`

**Example 3**

- Input: `n = 4, sums = [0, 0, 5, 5, 4, -1, 4, 9, 9, -1, 4, 3, 4, 8, 3, 8]`
- Output: `[0, -1, 4, 5]`
