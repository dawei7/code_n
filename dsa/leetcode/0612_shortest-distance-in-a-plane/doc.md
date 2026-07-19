# Shortest Distance in a Plane

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 612 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-in-a-plane/) |

## Problem Description
### Goal
Given a `Point2D` table containing unique Cartesian coordinates `(x, y)`, consider every pair of distinct stored points. For each pair, measure the ordinary Euclidean distance using the horizontal and vertical coordinate differences.

Return the minimum pairwise distance in a single column named `shortest`, rounded to two decimal places. A point cannot be paired with itself, and uniqueness of the coordinate pairs prevents a zero distance caused by duplicate rows; the result is based on the closest pair anywhere in the table, not only adjacent input rows.

### Function Contract
**Inputs**

- `Point2D(x, y)`: unique points with integer Cartesian coordinates

**Return value**

- One column named `shortest` containing the minimum pairwise Euclidean distance
- The value is rounded to two digits after the decimal point

### Examples
**Example 1**

- Input points: `(0, 0)`, `(-1, -1)`, `(100, 100)`
- Output: `1.41`

**Example 2**

- Input points: `(0, 0)`, `(3, 4)`
- Output: `5.00`
