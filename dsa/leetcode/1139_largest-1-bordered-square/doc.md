# Largest 1-Bordered Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1139 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [largest-1-bordered-square](https://leetcode.com/problems/largest-1-bordered-square/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/largest-1-bordered-square/).

### Goal
Find the area of the largest square in a binary grid whose four borders are all `1`. Cells inside the square may be either `0` or `1`.

### Function Contract
**Inputs**

- `grid`: an `m x n` matrix of `0` and `1`.

**Return value**

The area of the largest square with a border made entirely of `1`s, or `0` if no such square exists.

### Examples
**Example 1**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `9`

**Example 2**

- Input: `grid = [[1,1,0,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[0,0],[0,0]]`
- Output: `0`

---

## Solution
### Approach
Dynamic programming for directional run lengths.

### Complexity Analysis
- **Time Complexity**: `O(m * n * min(m, n))`
- **Space Complexity**: `O(m * n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    horizontal = [[0] * (cols + 1) for _ in range(rows + 1)]
    vertical = [[0] * (cols + 1) for _ in range(rows + 1)]

    best = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if grid[r - 1][c - 1] == 1:
                horizontal[r][c] = horizontal[r][c - 1] + 1
                vertical[r][c] = vertical[r - 1][c] + 1
                side = min(horizontal[r][c], vertical[r][c])
                while side > best:
                    if horizontal[r - side + 1][c] >= side and vertical[r][c - side + 1] >= side:
                        best = side
                        break
                    side -= 1
    return best * best
```
</details>
