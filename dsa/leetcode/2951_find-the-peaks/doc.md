# Find the Peaks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2951 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-peaks/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `mountain`. An element is a peak when
it is strictly greater than both immediate neighboring elements. The first and
last elements are never peaks because they do not have two neighbors.

For every interior index `i`, both comparisons must hold: its value must exceed
the value immediately before it and the value immediately after it. Equality
with either neighbor is not enough, and the array may contain no qualifying
interior position or several separated peaks.

Return an array containing the indices of every peak. The indices may appear
in any order.

### Function Contract

**Inputs**

- `mountain`: the array of heights to inspect

Let $N=\lvert\texttt{mountain}\rvert$. The contract guarantees
$3\le N\le100$ and $1\le\texttt{mountain[i]}\le100$.

**Return value**

An array containing exactly the indices whose values are strictly greater than
both adjacent values; any index order is accepted.

### Examples

#### Example 1

- **Input:** `mountain = [2,4,4]`
- **Output:** `[]`
- **Explanation:** The only interior value equals its right neighbor, so it is not strictly greater.

#### Example 2

- **Input:** `mountain = [1,4,3,8,5]`
- **Output:** `[1,3]`
- **Explanation:** Values at indices `1` and `3` are each greater than both neighbors.
