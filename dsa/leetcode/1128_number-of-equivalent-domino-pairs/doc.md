# Number of Equivalent Domino Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1128 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-equivalent-domino-pairs/) |

## Problem Description

### Goal

You are given a list `dominoes`, where `dominoes[i] = [a,b]` records the two values on domino `i`. Two dominoes `[a,b]` and `[c,d]` are equivalent if they are identical in their current orientation, meaning $a=c$ and $b=d$, or if rotating one makes them identical, meaning $a=d$ and $b=c$.

Return the number of index pairs `(i, j)` satisfying $0 \le i < j < n$ for which `dominoes[i]` and `dominoes[j]` are equivalent. Distinct pairs of indices count separately even when several dominoes all belong to the same equivalence group.

### Function Contract

**Inputs**

- `dominoes`: an array of $n$ two-element integer arrays, where $1 \le n \le 4 \times 10^4$ and every half value lies in $[1,9]$.

**Return value**

The number of equivalent index pairs `(i, j)` with `i < j`.

### Examples

**Example 1**

- Input: `dominoes = [[1,2],[2,1],[3,4],[5,6]]`
- Output: `1`

**Example 2**

- Input: `dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]`
- Output: `3`
