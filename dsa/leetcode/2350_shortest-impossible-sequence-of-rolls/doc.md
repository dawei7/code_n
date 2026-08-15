# Shortest Impossible Sequence of Rolls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2350 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/) |

## Problem Description

### Goal

An array `rolls` records $n$ outcomes from a die whose faces are numbered 1
through `k`. A possible roll sequence of length $\ell$ is any length-$\ell$
string over those `k` face values. Such a sequence occurs in `rolls` when it
can be selected as a subsequence, preserving order while allowing skipped
recorded rolls.

Return the smallest positive length for which at least one possible roll
sequence does not occur as a subsequence of `rolls`. Only the length is
required; several different missing sequences may attain it.

### Function Contract

**Inputs**

- `rolls`: An integer array of length $n$, where $1 \le n \le 10^5$ and every
  value lies in $[1,k]$.
- `k`: The number of die faces, where $1 \le k \le 10^5$.

**Return value**

The length of the shortest roll sequence that is not a subsequence of `rolls`.

### Examples

#### Example 1

- **Input:** `rolls = [4,2,1,2,3,3,2,4,1]`, `k = 4`
- **Output:** `3`
- **Explanation:** Every one- and two-roll sequence occurs, but some length-three
  sequence does not.

#### Example 2

- **Input:** `rolls = [1,1,2,2]`, `k = 2`
- **Output:** `2`
- **Explanation:** Both single faces occur, while `[2,1]` is absent.

#### Example 3

- **Input:** `rolls = [1,1,3,2,2,2,3,3]`, `k = 4`
- **Output:** `1`
- **Explanation:** Face 4 never occurs.
