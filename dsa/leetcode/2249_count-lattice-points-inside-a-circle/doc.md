# Count Lattice Points Inside a Circle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2249 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Geometry, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-lattice-points-inside-a-circle](https://leetcode.com/problems/count-lattice-points-inside-a-circle/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-lattice-points-inside-a-circle/).

### Goal
Count distinct integer-coordinate points lying inside or on at least one supplied circle.

### Function Contract
**Inputs**

- `circles`: triples `[center_x, center_y, radius]`.

**Return value**

The number of distinct lattice points covered by the union of the circles.

### Examples
**Example 1**

- Input: `circles = [[2, 2, 1]]`
- Output: `5`

**Example 2**

- Input: `circles = [[2, 2, 2], [3, 4, 1]]`
- Output: `16`

**Example 3**

- Input: `circles = [[1, 1, 1]]`
- Output: `5`

---

## Solution
### Approach
For each circle, enumerate integer `x` and `y` coordinates in its bounding square. Insert a point into a set when `(x - center_x)^2 + (y - center_y)^2 <= radius^2`. The set removes overlaps among circles.

### Complexity Analysis
- **Time Complexity**: `O(sum(radius_i^2))`
- **Space Complexity**: `O(P)`, where `P` is the number of covered lattice points

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
