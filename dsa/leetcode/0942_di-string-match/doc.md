# DI String Match

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 942 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/di-string-match/) |

## Problem Description

### Goal

A permutation `perm` contains each integer from $0$ through $n$ exactly once, so it has $n+1$ elements. Its adjacent comparisons can be encoded by a string `s` of length $n$: the character `"I"` at position $i$ requires `perm[i] < perm[i + 1]`, while `"D"` requires `perm[i] > perm[i + 1]`.

Given such a string `s`, reconstruct a permutation of the integers in the inclusive range $[0,n]$ whose adjacent values satisfy every encoded strict comparison. More than one permutation may meet the pattern; return any valid one.

### Function Contract

Let $n$ be the length of `s`.

**Inputs**

- `s`: a string with $1 \le n \le 10^5$ in which every character is either `"I"` or `"D"`.

**Return value**

Return a list `perm` of length $n+1$ containing every integer from $0$ through $n$ exactly once. For each index $i$, `"I"` requires `perm[i] < perm[i + 1]`, and `"D"` requires `perm[i] > perm[i + 1]`.

### Examples

**Example 1**

- Input: `s = "IDID"`
- Output: `[0, 4, 1, 3, 2]`

Each adjacent pair follows the corresponding increase or decrease. Other valid permutations are also acceptable.

**Example 2**

- Input: `s = "III"`
- Output: `[0, 1, 2, 3]`

**Example 3**

- Input: `s = "DDI"`
- Output: `[3, 2, 0, 1]`
