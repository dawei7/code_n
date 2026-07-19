# The Skyline Problem

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 218 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Sweep Line, Sorting, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/the-skyline-problem/) |

## Problem Description
### Goal
Each building is an axis-aligned rectangle described by `[left, right, height]`, occupying the half-open horizontal interval from `left` up to `right` at a positive height. The buildings are given in non-decreasing order by `left`. Buildings may overlap or hide one another. Viewed from far away, the skyline follows the maximum building height present at each horizontal coordinate.

Return the skyline as left-to-right key points `[x, height]` marking every change in visible height. Combine simultaneous starts and ends into the correct height at that coordinate, omit redundant adjacent points with equal heights, and include the final drop to ground level `0`. The result describes only the outer silhouette, not individual building edges concealed beneath taller rectangles.

### Function Contract
**Inputs**

- `buildings`: left-sorted triples `[left, right, height]`

**Return value**

Left-to-right key points `[x, height]`, including the final ground-level drop and no adjacent equal heights.

### Examples
**Example 1**

- Input: `[[2,9,10],[3,7,15],[5,12,12]]`
- Output begins: `[[2,10],[3,15],[7,12],[12,0]]`

**Example 2**

- Touching equal-height buildings merge into one plateau
- Output: one start and one final drop

**Example 3**

- A taller building is nested inside another
- Output rises and falls back to the outer height
