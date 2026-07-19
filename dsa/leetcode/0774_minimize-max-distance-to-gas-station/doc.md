# Minimize Max Distance to Gas Station

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 774 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) |

## Problem Description

### Goal

Given strictly increasing positions of existing gas stations along a number line, add exactly `k` new stations at arbitrary real-valued positions between or around the existing coordinates.

After insertion, consider the distances between every pair of consecutive stations in sorted order. Place the new stations to minimize the maximum of those adjacent distances, and return that minimum possible value within the accepted floating-point tolerance. Multiple new stations may divide the same original gap when beneficial.

### Function Contract

**Inputs**

- `stations`: a strictly increasing list of existing integer positions.
- `k`: the number of additional stations available.

**Return value**

- The smallest achievable maximum adjacent-station distance as a floating-point value.

### Examples

**Example 1**

- Input: `stations = [1,2,3,4,5,6,7,8,9,10]`, `k = 9`
- Output: `0.5`
- Explanation: Placing one new station in every unit gap halves all nine gaps.

**Example 2**

- Input: `stations = [23,24,36,39,46,56,57,65,84,98]`, `k = 1`
- Output: `14.0`
- Explanation: Splitting the length-19 gap leaves the existing length-14 gap as the maximum.

**Example 3**

- Input: `stations = [0,10]`, `k = 3`
- Output: `2.5`
- Explanation: Four equal segments are optimal.
