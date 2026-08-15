# Find Maximum Removals From Source String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3316 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-maximum-removals-from-source-string/) |

## Problem Description

### Goal

You receive a string `source` of length $n$, a string `pattern` that already occurs as a subsequence of `source`, and a sorted array `targetIndices` containing distinct source positions. An operation removes the character at one eligible position while requiring `pattern` to remain a subsequence of the characters that have not been removed.

Removed characters leave holes rather than changing the original indices of other characters. You may choose eligible positions in any order and may use a different occurrence of the pattern after removals. Return the greatest number of eligible characters that can be removed while at least one complete subsequence occurrence of `pattern` survives.

### Function Contract

**Inputs**

- `source`: A lowercase English string of length $n$, where $1\leq n\leq3000$.
- `pattern`: A nonempty lowercase string of length at most $n$ that is guaranteed to be a subsequence of `source`.
- `targetIndices`: Between 1 and $n$ distinct source indices in strictly ascending order, each in $[0,n-1]$.

**Return value**

Return the maximum number of indices from `targetIndices` whose characters can be removed while preserving `pattern` as a subsequence.

### Examples

#### Example 1

- **Input:** `source = "abbaa", pattern = "aba", targetIndices = [0, 1, 2]`
- **Output:** `1`

Index 0 must remain, but either index 1 or index 2 may be removed while another `b` still supports the pattern.

#### Example 2

- **Input:** `source = "bcda", pattern = "d", targetIndices = [0, 3]`
- **Output:** `2`

Neither eligible endpoint is needed for the one-character pattern.

#### Example 3

- **Input:** `source = "dda", pattern = "dda", targetIndices = [0, 1, 2]`
- **Output:** `0`

#### Example 4

- **Input:** `source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0, 2, 3, 4]`
- **Output:** `2`
