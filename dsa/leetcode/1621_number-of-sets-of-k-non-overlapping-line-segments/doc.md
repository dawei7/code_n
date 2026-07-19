# Number of Sets of K Non-Overlapping Line Segments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1621 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/) |

## Problem Description
### Goal
There are `n` points on a one-dimensional plane at integral coordinates 0 through `n - 1`. Draw exactly `k` line segments whose endpoints are chosen from these points. Every segment must have positive length and therefore cover at least two points.

The interiors of the segments may not overlap, but consecutive segments are allowed to share an endpoint. The segments do not need to cover every point. Count the distinct sets of `k` valid segments and return the result modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the number of points, where $2 \le n \le 1000$.
- `k`: the exact number of segments, where $1 \le k \le n-1$.
- Let $M=10^9+7$ be the required prime modulus.

**Return value**

Return the number of sets of exactly `k` non-overlapping positive-length segments, allowing shared endpoints, reduced modulo $M$.

### Examples
**Example 1**

- Input: `n = 4, k = 2`
- Output: `5`

**Example 2**

- Input: `n = 3, k = 1`
- Output: `3`

**Example 3**

- Input: `n = 30, k = 7`
- Output: `796297179`
