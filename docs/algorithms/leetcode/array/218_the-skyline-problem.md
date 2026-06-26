# The Skyline Problem

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 218 |
| Difficulty | Hard |
| Topics | Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Sweep Line, Sorting, Heap (Priority Queue), Ordered Set |
| Official Link | [the-skyline-problem](https://leetcode.com/problems/the-skyline-problem/) |

## Problem Description & Examples
### Goal
Compute the outer skyline formed by axis-aligned buildings. Each building occupies `[left, right)` at a fixed height. Return the horizontal positions where the visible maximum height changes, including the final drop to ground level.

### Function Contract
**Inputs**

- `buildings`: triples `[left, right, height]`, ordered by `left`.

**Return value**

A left-to-right list of key points `[x, height]`; adjacent points never have the same height.

### Examples
**Example 1**

- Input: `buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]`
- Output: `[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]`

**Example 2**

- Input: `buildings = [[0, 2, 3], [2, 5, 3]]`
- Output: `[[0, 3], [5, 0]]`

**Example 3**

- Input: `buildings = [[1, 4, 5], [2, 3, 7]]`
- Output: `[[1, 5], [2, 7], [3, 5], [4, 0]]`

---

## Underlying Base Algorithm(s)
Sweep from left to right through building starts and relevant right edges. Maintain active buildings in a max-heap keyed by height and carrying each right endpoint. At every event coordinate, add all starting buildings and lazily remove heap entries whose right edge is no farther than the coordinate. Emit a key point only when the current maximum height differs from the previous one.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
