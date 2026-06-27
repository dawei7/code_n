# Minimum Rectangles to Cover Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3111 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-rectangles-to-cover-points](https://leetcode.com/problems/minimum-rectangles-to-cover-points/) |

## Problem Description & Examples
### Goal
Given a set of 2D points and a fixed width `w`, determine the minimum number of rectangles of height infinity and width `w` required to cover all provided points. A point is covered if it lies within the horizontal range `[x, x + w]` of any rectangle.

### Function Contract
**Inputs**

- `points`: A list of lists, where each inner list contains two integers `[x, y]` representing the coordinates of a point.
- `w`: An integer representing the fixed width of each rectangle.

**Return value**

- An integer representing the minimum number of rectangles needed to cover all points.

### Examples
**Example 1**

- Input: `points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1`
- Output: `2`

**Example 2**

- Input: `points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2`
- Output: `3`

**Example 3**

- Input: `points = [[2,3],[1,2]], w = 0`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach** combined with **Sorting**. Since the height of the rectangles is infinite, the y-coordinates are irrelevant. We only need to cover the x-coordinates. By sorting the x-coordinates, we can iterate through them and place a rectangle starting at the current leftmost uncovered point `x_i`, which covers all points up to `x_i + w`. We then skip all points covered by this rectangle and repeat the process.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of points. This is dominated by the sorting step. The subsequent linear scan takes `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements (Python's Timsort uses `O(N)`).
