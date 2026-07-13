# Shift 2D Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1260 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shift-2d-grid](https://leetcode.com/problems/shift-2d-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shift-2d-grid/).

### Goal
Shift every value in a matrix to the right by `k` positions, wrapping from the end of a row to the start of the next row and from the last cell to the first cell.

### Function Contract
**Inputs**

- `grid`: `m x n` matrix.
- `k`: number of shifts.

**Return value**

The shifted matrix.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
- Output: `[[9,1,2],[3,4,5],[6,7,8]]`

**Example 2**

- Input: `grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]`, `k = 4`
- Output: `[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 9`
- Output: `[[1,2,3],[4,5,6],[7,8,9]]`

---

## Solution
### Approach
Index mapping in a flattened matrix.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` for the returned grid.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid, k):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    total = rows * cols
    k %= total
    flat = [grid[r][c] for r in range(rows) for c in range(cols)]
    shifted = flat[-k:] + flat[:-k] if k else flat
    return [shifted[i * cols:(i + 1) * cols] for i in range(rows)]
```
</details>
