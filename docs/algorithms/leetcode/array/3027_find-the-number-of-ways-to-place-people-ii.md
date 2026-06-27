# Find the Number of Ways to Place People II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3027 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Sorting, Enumeration |
| Official Link | [find-the-number-of-ways-to-place-people-ii](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/) |

## Problem Description & Examples
### Goal
Given a set of 2D points on a Cartesian plane, determine the number of pairs of points (A, B) such that A can "fence" B. A fences B if A and B form the diagonal of a rectangle (with sides parallel to the axes) that contains no other points from the set inside or on its boundary, excluding the points A and B themselves.

### Function Contract
**Inputs**

- `points`: A list of lists, where each inner list contains two integers `[x, y]` representing the coordinates of a point.

**Return value**

- An integer representing the total count of valid pairs (A, B) that satisfy the fencing condition.

### Examples
**Example 1**

- Input: `points = [[1,1],[2,2],[3,3]]`
- Output: `0`

**Example 2**

- Input: `points = [[6,2],[4,4],[2,6]]`
- Output: `2`

**Example 3**

- Input: `points = [[3,1],[1,3],[1,1]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved by sorting the points primarily by their x-coordinate (ascending) and secondarily by their y-coordinate (descending). This sorting strategy ensures that for any pair (A, B) where A.x <= B.x and A.y >= B.y, we only need to check if any other point C exists within the rectangle defined by A and B. By iterating through all pairs and maintaining the y-coordinate constraints, we can efficiently count valid rectangles.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the number of points. Sorting takes `O(n log n)`, and the nested loop structure to check point containment takes `O(n^2)`.
- **Space Complexity**: `O(n)` to store the sorted list of points.
