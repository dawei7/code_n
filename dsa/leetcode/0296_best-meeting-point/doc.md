# Best Meeting Point

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 296 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-meeting-point/) |

## Problem Description
### Goal
Given a nonempty binary grid, each cell marked `1` contains one person. Choose a grid cell where everyone will meet; the meeting location may be occupied or empty. Travel distance is Manhattan distance, the sum of horizontal and vertical coordinate differences.

Return the minimum possible sum of distances from all people to one meeting cell. Each person contributes independently, and diagonal movement offers no shortcut under this metric. The function returns only the smallest total, not the meeting coordinates. The grid contains at least one person, and its rectangular dimensions define all candidate cells.

### Function Contract
**Inputs**

- `grid`: a nonempty rectangular binary matrix

**Return value**

The minimum total Manhattan distance from all `1` cells to one meeting cell.

### Examples
**Example 1**

- Input: `grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]`
- Output: `6`

**Example 2**

- Input: `grid = [[1]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,1]]`
- Output: `1`
