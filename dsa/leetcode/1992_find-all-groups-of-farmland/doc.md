# Find All Groups of Farmland

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1992 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-all-groups-of-farmland](https://leetcode.com/problems/find-all-groups-of-farmland/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-all-groups-of-farmland/).

### Goal
Farmland cells form non-overlapping rectangular groups in a binary grid. Find the corner coordinates of every group.

### Function Contract
**Inputs**

- `land`: a binary matrix where `1` is farmland and `0` is forest.

**Return value**

Return rectangles `[topRow, leftCol, bottomRow, rightCol]` for all farmland groups.

### Examples
**Example 1**

- Input: `land = [[1,0,0],[0,1,1],[0,1,1]]`
- Output: `[[0,0,0,0],[1,1,2,2]]`

**Example 2**

- Input: `land = [[1,1],[1,1]]`
- Output: `[[0,0,1,1]]`

**Example 3**

- Input: `land = [[0]]`
- Output: `[]`

---

## Solution
### Approach
Scan the grid for the top-left cell of each unvisited farmland rectangle. Extend downward and rightward to locate its bottom-right corner, record it, and mark or skip the rectangle's cells.

### Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(1)` extra if marking in place, excluding output.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
