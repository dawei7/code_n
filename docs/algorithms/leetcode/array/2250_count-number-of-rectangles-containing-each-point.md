# Count Number of Rectangles Containing Each Point

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2250 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Binary Indexed Tree, Sorting |
| Official Link | [count-number-of-rectangles-containing-each-point](https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/) |

## Problem Description & Examples
### Goal
For each point, count axis-aligned rectangles with lower-left corner at the origin that contain it, including their boundaries. Rectangle `[length, height]` contains point `[x, y]` exactly when both dimensions reach the point.

### Function Contract
**Inputs**

- `rectangles`: pairs `[length, height]`.
- `points`: query coordinates `[x, y]`.

**Return value**

One count per point, preserving query order.

### Examples
**Example 1**

- Input: `rectangles = [[1, 2], [2, 3], [2, 5]]`, `points = [[2, 1], [1, 4]]`
- Output: `[2, 1]`

**Example 2**

- Input: `rectangles = [[1, 1], [2, 2], [3, 3]]`, `points = [[1, 1], [2, 2], [3, 3]]`
- Output: `[3, 2, 1]`

**Example 3**

- Input: `rectangles = [[4, 2]]`, `points = [[5, 1], [4, 2]]`
- Output: `[0, 1]`

---

## Underlying Base Algorithm(s)
Group rectangle lengths by height and sort each group. Heights are bounded, so for point `(x, y)`, inspect every height at least `y` and binary-search its sorted lengths for the first value at least `x`. Sum the suffix sizes across those groups.

---

## Complexity Analysis
- **Time Complexity**: `O(R log R + P * H log R)`, where `H` is the bounded height range
- **Space Complexity**: `O(R)`
