# Matrix Cells in Distance Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1030 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [matrix-cells-in-distance-order](https://leetcode.com/problems/matrix-cells-in-distance-order/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/matrix-cells-in-distance-order/).

### Goal
Return all coordinates in a `rows x cols` matrix ordered by their Manhattan distance from a given center cell.

### Function Contract
**Inputs**

- `rows`: int
- `cols`: int
- `rCenter`: int
- `cCenter`: int

**Return value**

List[List[int]] - all matrix coordinates in nondecreasing distance order

### Examples
**Example 1**

- Input: `rows = 1, cols = 2, rCenter = 0, cCenter = 0`
- Output: `[[0, 0], [0, 1]]`

**Example 2**

- Input: `rows = 2, cols = 2, rCenter = 0, cCenter = 1`
- Output: `[[0, 1], [0, 0], [1, 1], [1, 0]]`

**Example 3**

- Input: `rows = 2, cols = 3, rCenter = 1, cCenter = 2`
- Output: `[[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]`

---

## Solution
### Approach
Coordinate enumeration sorted by Manhattan distance.

### Complexity Analysis
- **Time Complexity**: `O(rows * cols * log(rows * cols))`
- **Space Complexity**: `O(rows * cols)` for the output

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1030: Matrix Cells in Distance Order."""


def solve(rows: int, cols: int, r_center: int, c_center: int) -> list[list[int]]:
    cells = [[r, c] for r in range(rows) for c in range(cols)]
    cells.sort(key=lambda cell: abs(cell[0] - r_center) + abs(cell[1] - c_center))
    return cells
```
</details>
