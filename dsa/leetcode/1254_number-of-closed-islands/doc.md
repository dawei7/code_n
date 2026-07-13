# Number of Closed Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1254 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-closed-islands](https://leetcode.com/problems/number-of-closed-islands/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-closed-islands/).

### Goal
Count islands of `0` cells that are completely surrounded by `1` cells and do not touch the grid border.

### Function Contract
**Inputs**

- `grid`: matrix where `0` is land and `1` is water.

**Return value**

The number of closed land islands.

### Examples
**Example 1**

- Input: `grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `1`

---

## Solution
### Approach
Flood fill / depth-first search.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)` recursion depth in the worst case.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    def flood(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if grid[r][c] == 1:
            return True
        grid[r][c] = 1
        closed = True
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            closed = flood(r + dr, c + dc) and closed
        return closed

    answer = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and flood(r, c):
                answer += 1
    return answer
```
</details>
