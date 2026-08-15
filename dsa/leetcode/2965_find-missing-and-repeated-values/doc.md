# Find Missing and Repeated Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2965 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-missing-and-repeated-values/) |

## Problem Description

### Goal

You are given a 0-indexed square integer matrix `grid` with $N$ rows and $N$
columns. Its entries lie from $1$ through $N^2$.

The grid would contain every integer in that range exactly once except for two
exceptions: one value `a` appears twice, while a different value `b` does not
appear at all. No other frequency differs from one.

Return `[a, b]`, placing the repeated value first and the missing value second.

### Function Contract

**Inputs**

- `grid`: the $N\times N$ matrix containing one duplicate and one omission

The contract guarantees $2\le N\le50$, every cell lies in $[1,N^2]$, exactly
one value occurs twice, exactly one value is absent, and every other value
occurs once.

**Return value**

A two-element array `[repeated, missing]` in that exact order.

### Examples

#### Example 1

- **Input:** `grid = [[1,3],[2,2]]`
- **Output:** `[2,4]`
- **Explanation:** `2` occurs twice and `4` does not occur.

#### Example 2

- **Input:** `grid = [[9,1,7],[8,9,2],[3,4,6]]`
- **Output:** `[9,5]`
- **Explanation:** `9` is repeated, while `5` is the only value from one through nine that is missing.
