# Strange Printer II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1591 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Graph Theory, Topological Sort, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [strange-printer-ii](https://leetcode.com/problems/strange-printer-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/strange-printer-ii/).

### Goal
Decide whether a grid can be printed by repeatedly choosing one color and
printing a solid rectangle of that color, with later rectangles allowed to cover
earlier ones.

### Function Contract
**Inputs**

- `targetGrid`: the desired color grid.

**Return value**

`true` if some rectangle-printing order can produce the grid; otherwise `false`.

### Examples
**Example 1**

- Input: `targetGrid = [[1, 1, 1], [3, 1, 3]]`
- Output: `false`

**Example 2**

- Input: `targetGrid = [[1, 1, 1], [3, 1, 3], [3, 3, 3]]`
- Output: `true`

**Example 3**

- Input: `targetGrid = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]`
- Output: `false`

---

## Solution
### Approach
For each color, compute its bounding rectangle. If another color appears inside
that rectangle, the rectangle color must be printed before that inner color is
covered. Build these dependencies and check whether the color graph is acyclic,
or equivalently repeatedly remove colors whose rectangle currently contains only
that color or already removed cells.

### Complexity Analysis
- **Time Complexity**: `O(C * m * n)`, where `C` is the number of distinct colors.
- **Space Complexity**: `O(C^2 + m * n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
