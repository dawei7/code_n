# Restore Finishing Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3668 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/restore-finishing-order/) |

## Problem Description

### Goal

A race has $n$ participants identified by the integers from $1$ through $n$. The array `order` is a permutation of those IDs listed from the earliest finisher to the latest.

The array `friends` contains the distinct IDs of your friends. It is sorted by numerical ID, not by race result, and every listed friend is guaranteed to occur in `order`.

Return exactly the friend IDs arranged by their positions in the race's finishing order. Non-friends must be omitted, and the relative order inherited from `order` must be preserved.

### Function Contract

**Inputs**

- `order`: a length-$n$ permutation of the integers $1$ through $n$, where $1\le n\le100$.
- `friends`: a strictly increasing array of friend IDs present in `order`, with at most eight entries.

**Return value**

Return the stable subsequence of `order` containing precisely the IDs listed in `friends`.

### Examples

#### Example 1

- **Input:** `order = [3, 1, 2, 5, 4]`, `friends = [1, 3, 4]`
- **Output:** `[3, 1, 4]`

#### Example 2

- **Input:** `order = [1, 4, 5, 3, 2]`, `friends = [2, 5]`
- **Output:** `[5, 2]`

#### Example 3

- **Input:** `order = [4, 3, 2, 1]`, `friends = [1]`
- **Output:** `[1]`
- The only friend finished last, but still appears in the result.
