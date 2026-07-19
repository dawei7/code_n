# Minimum Number of Arrows to Burst Balloons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 452 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) |

## Problem Description
### Goal
Each balloon spans a closed horizontal interval `[start, end]`. An arrow fired vertically at coordinate `x` bursts every balloon whose interval contains `x`, including balloons for which `x` equals either endpoint.

Return the minimum number of arrow coordinates needed to burst all balloons. One arrow may cover many overlapping intervals, while disjoint groups require separate arrows. Touching intervals can share an endpoint arrow because their boundaries are inclusive. Input order does not matter, and the function returns only the minimum count rather than the chosen coordinates. A single balloon requires one arrow.

### Function Contract
**Inputs**

- `points`: a list of intervals `[start, end]`; an arrow fired at coordinate `x` bursts an interval when `start <= x <= end`

**Return value**

- The minimum number of arrow coordinates whose union intersects every interval

### Examples
**Example 1**

- Input: `points = [[10, 16], [2, 8], [1, 6], [7, 12]]`
- Output: `2`

**Example 2**

- Input: `points = [[1, 2], [3, 4], [5, 6], [7, 8]]`
- Output: `4`

**Example 3**

- Input: `points = [[1, 2], [2, 3], [3, 4], [4, 5]]`
- Output: `2`
