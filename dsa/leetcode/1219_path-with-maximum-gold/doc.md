# Path with Maximum Gold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1219 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [path-with-maximum-gold](https://leetcode.com/problems/path-with-maximum-gold/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/path-with-maximum-gold/).

### Goal
Starting from any nonzero cell, move up, down, left, or right through nonzero cells without visiting a cell twice. Maximize the total gold collected.

### Function Contract
**Inputs**

- `grid`: matrix where `0` is blocked and positive values are gold amounts.

**Return value**

The maximum gold collectable on one valid path.

### Examples
**Example 1**

- Input: `grid = [[0,6,0],[5,8,7],[0,9,0]]`
- Output: `24`

**Example 2**

- Input: `grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]`
- Output: `28`

**Example 3**

- Input: `grid = [[10]]`
- Output: `10`

---

## Solution
### Approach
Backtracking depth-first search on a grid.

### Complexity Analysis
- **Time Complexity**: `O(m * n * 3^g)` in the worst case, where `g` is the count of gold cells.
- **Space Complexity**: `O(g)` recursion depth.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
            return 0
        gold = grid[r][c]
        grid[r][c] = 0
        best_next = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            best_next = max(best_next, dfs(r + dr, c + dc))
        grid[r][c] = gold
        return gold + best_next

    answer = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                answer = max(answer, dfs(r, c))
    return answer
```
</details>
