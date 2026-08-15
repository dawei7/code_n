# Minimum Cuts to Divide a Circle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2481 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/) |

## Problem Description

### Goal

A valid straight cut of a circle has one of two forms. It may connect two boundary points while passing through the center, creating a diameter cut, or it may connect the center to one boundary point, creating a radius cut.

Given a positive integer `n`, determine the minimum number of valid cuts needed to divide the circle into exactly `n` slices of equal size. A single radius cut marks a boundary but does not by itself separate the circle into distinct pieces.

### Function Contract

**Inputs**

- `n`: The required number of equal circular slices, with $1 \le n \le 100$.

**Return value**

Return an integer: the minimum number of valid cuts that produces exactly `n` equal slices.

### Examples

#### Example 1

- **Input:** `n = 4`
- **Output:** `2`
- **Explanation:** Two diameter cuts through the center create four equal slices.

#### Example 2

- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:** Three radius cuts are needed to mark all three equal sectors.

#### Example 3

- **Input:** `n = 1`
- **Output:** `0`
- **Explanation:** The uncut circle is already one slice.
