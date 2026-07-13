# Check if Grid Satisfies Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3142 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-grid-satisfies-conditions](https://leetcode.com/problems/check-if-grid-satisfies-conditions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-grid-satisfies-conditions/).

### Goal
Determine if a 2D grid of integers adheres to two specific structural rules: every cell must be equal to the cell directly below it (if one exists), and every cell must be different from the cell immediately to its right (if one exists).

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the matrix.

**Return value**

- `bool`: Returns `True` if the grid satisfies both conditions, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[1,0,2],[1,0,2]]`
- Output: `True`

**Example 2**

- Input: `grid = [[1,1,1],[0,0,0]]`
- Output: `False`

**Example 3**

- Input: `grid = [[1],[2],[3]]`
- Output: `False`

---

## Solution
### Approach
The solution utilizes a linear scan (nested iteration) over the grid dimensions. By checking the vertical adjacency condition `grid[r][c] == grid[r+1][c]` and the horizontal adjacency condition `grid[r][c] != grid[r][c+1]`, we can validate the grid properties in a single pass.

### Complexity Analysis
- **Time Complexity**: `O(R * C)`, where `R` is the number of rows and `C` is the number of columns, as we visit each cell at most once.
- **Space Complexity**: `O(1)`, as we perform the validation in-place without allocating extra data structures.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> bool:
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            # Check vertical condition: cell must equal the one below it
            if r + 1 < rows:
                if grid[r][c] != grid[r + 1][c]:
                    return False

            # Check horizontal condition: cell must not equal the one to the right
            if c + 1 < cols:
                if grid[r][c] == grid[r][c + 1]:
                    return False

    return True
```
</details>
