# Shortest Distance in a Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 613 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-in-a-line/) |

## Problem Description
### Goal
Given a `Point` table containing unique integer positions `x` on a one-dimensional number line, consider every pair of distinct stored points. The distance between positions `x1` and `x2` is their absolute difference `abs(x1 - x2)`.

Return the minimum distance over all such pairs in a column named `shortest`. Input row order has no geometric meaning, and a point cannot be paired with itself; because all stored positions are unique, the shortest valid distance is positive.

### Function Contract
**Inputs**

- `Point(x)`: unique integer positions on a one-dimensional line

**Return value**

- One column named `shortest` containing the minimum absolute difference between two positions

### Examples
**Example 1**

- Input positions: `-1`, `0`, `2`
- Output: `1`

**Example 2**

- Input positions: `10`, `25`
- Output: `15`
