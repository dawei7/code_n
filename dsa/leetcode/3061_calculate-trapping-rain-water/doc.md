# Calculate Trapping Rain Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3061 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-trapping-rain-water/) |

## Problem Description

### Goal

The rows describe a landscape of adjacent vertical bars. Sequential `id`
values give the bars' left-to-right order, each bar is one unit wide, and
`height` gives its elevation.

After rain, water above a bar is bounded by the tallest bar at or to its left
and the tallest bar at or to its right. Calculate the total number of water
units held across the complete landscape. Boundary bars and positions without
a taller boundary on both sides contribute zero. Return one value named
`total_trapped_water`; row order is irrelevant.

### Function Contract

**Inputs**

- `Heights(id, height)`: unique sequential `id` values order the unit-width
  bars, and `height` is the corresponding nonnegative elevation.

Let $n$ be the number of bars.

**Return value**

- A one-row, one-column table whose `total_trapped_water` value is the sum of
  trapped water above every bar.

### Examples

**Example 1**

For heights `[0,1,0,2,1,0,1,3,2,1,2,1]`, the individual bounded depressions
hold a total of `6` water units.

**Example 2**

Heights `[3,0,3]` form one three-unit basin, so the result is `3`.

**Example 3**

A monotonically increasing or decreasing landscape traps no water because no
interior position has a sufficiently high boundary on both sides.
