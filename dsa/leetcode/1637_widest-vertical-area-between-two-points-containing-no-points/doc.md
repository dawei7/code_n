# Widest Vertical Area Between Two Points Containing No Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1637 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [widest-vertical-area-between-two-points-containing-no-points](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/).

### Goal
Find the maximum width of a vertical strip between two x-coordinates such that no
point lies strictly inside the strip.

### Function Contract
**Inputs**

- `points`: point coordinates.

**Return value**

The widest empty vertical area.

### Examples
**Example 1**

- Input: `points = [[8, 7], [9, 9], [7, 4], [9, 7]]`
- Output: `1`

**Example 2**

- Input: `points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]`
- Output: `3`

**Example 3**

- Input: `points = [[1, 1], [2, 2], [4, 3]]`
- Output: `2`

---

## Solution
### Approach
Only x-coordinates matter. Extract them, sort them, and compute the largest
difference between consecutive distinct x-coordinates.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(n)` for the extracted x-coordinates.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
