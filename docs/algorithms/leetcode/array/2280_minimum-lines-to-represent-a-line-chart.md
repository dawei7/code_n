# Minimum Lines to Represent a Line Chart

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2280 |
| Difficulty | Medium |
| Topics | Array, Math, Geometry, Sorting, Number Theory |
| Official Link | [minimum-lines-to-represent-a-line-chart](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/) |

## Problem Description & Examples
### Goal
Sort stock-price points by day and connect consecutive points. Count the minimum straight line segments needed, merging adjacent connections whenever their slopes are equal.

### Function Contract
**Inputs**

- `stockPrices`: distinct-day points `[day, price]`.

**Return value**

The number of maximal collinear runs between consecutive sorted points; a single point requires zero lines.

### Examples
**Example 1**

- Input: `stockPrices = [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]`
- Output: `3`

**Example 2**

- Input: `stockPrices = [[3, 4], [1, 2], [7, 8], [2, 3]]`
- Output: `1`

**Example 3**

- Input: `stockPrices = [[5, 10]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Sort by day. Begin with one segment when at least two points exist, then compare each consecutive slope with the previous slope. Avoid floating-point division by cross-multiplying `dy1 * dx2` and `dy2 * dx1`; start a new line whenever they differ.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space when sorting in place
