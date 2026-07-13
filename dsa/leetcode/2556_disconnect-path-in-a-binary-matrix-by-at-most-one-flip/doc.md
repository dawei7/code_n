# Disconnect Path in a Binary Matrix by at Most One Flip

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2556 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [disconnect-path-in-a-binary-matrix-by-at-most-one-flip](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/).

### Goal
Determine if it is possible to disconnect all paths from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1) of a binary grid by flipping at most one cell (changing a 1 to a 0). The start and end cells cannot be flipped.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers (0 or 1) representing the binary matrix.

**Return value**

- `bool`: Returns `True` if the path can be disconnected by flipping at most one cell, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[1,1,1],[1,0,0],[1,1,1]]`
- Output: `True`

**Example 2**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `False`

**Example 3**

- Input: `grid = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]`
- Output: `False`

---

## Solution
### Approach
The problem relies on two passes of Depth-First Search (DFS). First, we check if a path exists from start to end. If no path exists, we return `True`. If a path exists, we mark the cells visited during the first DFS as 0 (to "remove" them). Then, we perform a second DFS to see if another path still exists. If no path exists after the first removal, it implies that the path was a "bottleneck" (an articulation point), and we return `True`.

### Complexity Analysis
- **Time Complexity**: O(m * n), where m is the number of rows and n is the number of columns, as we traverse the grid at most twice.
- **Space Complexity**: O(m * n) in the worst case for the recursion stack of the DFS.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> bool:
    m = len(grid)
    n = len(grid[0])

    def dfs(r, c):
        if r == m - 1 and c == n - 1:
            return True

        grid[r][c] = 0

        # Try moving down or right
        for dr, dc in [(0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < m and nc < n and grid[nr][nc] == 1:
                if dfs(nr, nc):
                    return True
        return False

    # First pass: check if a path exists and remove it
    # We don't want to remove the start (0,0) or end (m-1, n-1)
    # So we temporarily set them back to 1 if they were flipped
    has_path1 = dfs(0, 0)

    if not has_path1:
        return True

    grid[0][0] = 1
    grid[m - 1][n - 1] = 1

    # Second pass: check if another path exists
    has_path2 = dfs(0, 0)

    return not has_path2
```
</details>
