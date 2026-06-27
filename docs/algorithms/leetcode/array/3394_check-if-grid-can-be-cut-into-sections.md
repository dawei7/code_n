# Check if Grid can be Cut into Sections

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3394 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [check-if-grid-can-be-cut-into-sections](https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/) |

## Problem Description & Examples
### Goal
Determine if a grid of size `n x n` can be partitioned into at least three distinct sections by making either horizontal or vertical cuts. A cut is valid if it spans the entire width or height of the grid and does not intersect any of the given rectangular regions. Specifically, we must check if we can create at least three sections using only horizontal cuts or only vertical cuts.

### Function Contract
**Inputs**

- `n`: An integer representing the dimensions of the `n x n` grid.
- `rectangles`: A list of lists, where each sub-list `[x1, y1, x2, y2]` defines a rectangle with top-left corner `(x1, y1)` and bottom-right corner `(x2, y2)`.

**Return value**

- `bool`: Returns `True` if it is possible to divide the grid into at least three sections using either horizontal or vertical cuts, otherwise `False`.

### Examples
**Example 1**

- Input: `n = 3, rectangles = [[0,0,1,1],[1,1,2,2]]`
- Output: `True`

**Example 2**

- Input: `n = 3, rectangles = [[0,0,1,1],[1,0,2,1],[0,1,2,2]]`
- Output: `False`

**Example 3**

- Input: `n = 5, rectangles = [[0,0,5,1],[2,1,5,5]]`
- Output: `True`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Interval Merging** approach. To determine if we can make at least two cuts (creating three sections), we track the intervals occupied by rectangles along a specific axis. We sort these intervals and merge overlapping ones. If the number of merged intervals is less than 3, it implies we have enough "gaps" between the rectangles to place at least two lines that do not intersect any rectangle.

---

## Complexity Analysis
- **Time Complexity**: `O(R log R)`, where `R` is the number of rectangles, due to the sorting of intervals.
- **Space Complexity**: `O(R)` to store the intervals.
