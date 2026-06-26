# Maximum Number of Darts Inside of a Circular Dartboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1453 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry |
| Official Link | [maximum-number-of-darts-inside-of-a-circular-dartboard](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/) |

## Problem Description & Examples
### Goal
Given dart coordinates and a dartboard radius, place the board center anywhere to cover as many darts as possible.

### Function Contract
**Inputs**

- `darts`: a list of `[x, y]` dart coordinates.
- `r`: the board radius.

**Return value**

The maximum number of darts that can lie inside or on one circle of radius `r`.

### Examples
**Example 1**

- Input: `darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2`
- Output: `4`

**Example 2**

- Input: `darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5`
- Output: `5`

**Example 3**

- Input: `darts = [[1,2],[3,5],[1,-1]], r = 2`
- Output: `2`

---

## Underlying Base Algorithm(s)
Computational geometry over circle centers. For every pair of darts within diameter `2r`, compute the possible circle centers through both points, then count darts within each candidate circle.

---

## Complexity Analysis
- **Time Complexity**: `O(n^3)` with pair-generated centers and full recounts.
- **Space Complexity**: `O(1)` besides temporary center data.
