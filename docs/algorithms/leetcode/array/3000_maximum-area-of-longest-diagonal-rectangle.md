# Maximum Area of Longest Diagonal Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3000 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [maximum-area-of-longest-diagonal-rectangle](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/) |

## Problem Description & Examples
### Goal
Given a collection of rectangles defined by their width and height, identify the rectangle that possesses the longest diagonal. If multiple rectangles share the same maximum diagonal length, return the one with the largest area.

### Function Contract
**Inputs**

- `dimensions`: A list of lists, where each inner list contains two integers `[width, height]` representing the dimensions of a rectangle.

**Return value**

- An integer representing the area of the rectangle that satisfies the criteria (longest diagonal, then largest area).

### Examples
**Example 1**

- Input: `[[9,3],[8,6]]`
- Output: `48`
- Explanation: Diagonal of [9,3] is sqrt(90), diagonal of [8,6] is sqrt(100). 100 > 90, so area 8*6=48.

**Example 2**

- Input: `[[3,4],[4,3]]`
- Output: `12`
- Explanation: Both have diagonal 5. Both have area 12. Return 12.

**Example 3**

- Input: `[[1,1],[2,2]]`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is solved using a single-pass linear scan. We maintain the current "best" rectangle found so far, updating it whenever we encounter a rectangle with a strictly longer diagonal or an equal diagonal with a larger area. Since the diagonal length squared ($w^2 + h^2$) is monotonically increasing with the diagonal length, we can compare squared values to avoid floating-point precision issues.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of rectangles, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only store a few variables to track the maximum diagonal and area found so far.
