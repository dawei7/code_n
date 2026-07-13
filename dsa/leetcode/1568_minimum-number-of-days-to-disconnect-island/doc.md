# Minimum Number of Days to Disconnect Island

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1568 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Strongly Connected Component |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-days-to-disconnect-island](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/).

### Goal
Remove land cells one day at a time until the grid is no longer exactly one
connected island. Find the minimum number of days needed.

### Function Contract
**Inputs**

- `grid`: a binary matrix where `1` is land and `0` is water.

**Return value**

The fewest land removals required to make the island disconnected or empty.

### Examples
**Example 1**

- Input: `grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1, 1]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1, 0, 1, 0]]`
- Output: `0`

---

## Solution
### Approach
First count islands. If the grid is already disconnected or has no island,
return `0`. Otherwise, try removing each land cell and recounting islands; if
any single removal disconnects the grid, return `1`. If not, the answer is `2`
because any connected island can be disconnected by removing at most two cells.

### Complexity Analysis
- **Time Complexity**: `O((m * n)^2)` for testing every land cell with a grid traversal.
- **Space Complexity**: `O(m * n)` for visited state during traversal.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    def is_land(value):
        return value == 1

    def island_count(skip=None):
        seen = [[False] * cols for _ in range(rows)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if skip == (r, c) or seen[r][c] or not is_land(grid[r][c]):
                    continue
                count += 1
                stack = [(r, c)]
                seen[r][c] = True
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr = cr + dr
                        nc = cc + dc
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            continue
                        if skip == (nr, nc) or seen[nr][nc] or not is_land(grid[nr][nc]):
                            continue
                        seen[nr][nc] = True
                        stack.append((nr, nc))
        return count

    if island_count() != 1:
        return 0
    for r in range(rows):
        for c in range(cols):
            if is_land(grid[r][c]) and island_count((r, c)) != 1:
                return 1
    return 2
```
</details>
