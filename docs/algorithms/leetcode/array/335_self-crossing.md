# Self Crossing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 335 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry |
| Official Link | [self-crossing](https://leetcode.com/problems/self-crossing/) |

## Problem Description & Examples
### Goal
Given a sequence of line segments represented by their lengths in a 2D plane, determine if the path formed by these segments ever intersects itself. The path starts at (0,0) and moves sequentially in directions: North, West, South, East, and so on, repeating the cycle.

### Function Contract
**Inputs**

- `distance`: A list of integers representing the length of each consecutive move.

**Return value**

- `bool`: Returns `True` if the path crosses itself at any point, `False` otherwise.

### Examples
**Example 1**

- Input: `[2, 1, 1, 2]`
- Output: `True`

**Example 2**

- Input: `[1, 2, 3, 4]`
- Output: `False`

**Example 3**

- Input: `[1, 1, 1, 1]`
- Output: `True`

---

## Underlying Base Algorithm(s)
The problem is solved by identifying three specific geometric patterns that cause a self-intersection:
1. **Spiral Inward**: The current line segment crosses the segment three steps back.
2. **Spiral Outward to Inward**: The current line segment meets the segment four steps back.
3. **Bounded Spiral**: The current line segment crosses the segment five steps back (a combination of the previous two cases).

By checking these three conditions at each step, we can determine if the path intersects without needing to store the actual coordinates.

---

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of segments, as we iterate through the list exactly once.
- **Space Complexity**: O(1), as we only store a constant number of variables to track the relative lengths of recent segments.
