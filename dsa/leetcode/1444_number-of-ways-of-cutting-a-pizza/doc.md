# Number of Ways of Cutting a Pizza

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1444 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Memoization, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-ways-of-cutting-a-pizza](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/).

### Goal
Cut a rectangular pizza into `k` pieces using horizontal or vertical straight cuts. Each final piece must contain at least one apple.

### Function Contract
**Inputs**

- `pizza`: a list of strings where `A` marks an apple and `.` marks an empty cell.
- `k`: the number of final pieces.

**Return value**

The number of valid cutting sequences modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `pizza = ["A..","AAA","..."], k = 3`
- Output: `3`

**Example 2**

- Input: `pizza = ["A..","AA.","..."], k = 3`
- Output: `1`

**Example 3**

- Input: `pizza = ["A..","A..","..."], k = 1`
- Output: `1`

---

## Solution
### Approach
2D suffix sums plus memoized DP. A suffix apple count answers whether any rectangle has an apple; the DP tries every valid next horizontal or vertical cut and recurses on the remaining lower/right rectangle.

### Complexity Analysis
- **Time Complexity**: `O(kmn(m+n))` for an `m x n` pizza.
- **Space Complexity**: `O(kmn)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from functools import lru_cache


def solve(pizza, k):
    mod = 1_000_000_007
    grid = [list(row) if isinstance(row, str) else list(row) for row in pizza]
    rows = len(grid)
    cols = max((len(row) for row in grid), default=0)
    for row in grid:
        row.extend(["."] * (cols - len(row)))
    has_apple = [[0] * (cols + 1) for _ in range(rows + 1)]
    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            cell = grid[row][col]
            apple = cell == "A" or (isinstance(cell, int) and cell != 0)
            has_apple[row][col] = (
                int(apple)
                + has_apple[row + 1][col]
                + has_apple[row][col + 1]
                - has_apple[row + 1][col + 1]
            )

    @lru_cache(None)
    def dp(row, col, pieces):
        if has_apple[row][col] == 0:
            return 0
        if pieces == 1:
            return 1
        ways = 0
        for next_row in range(row + 1, rows):
            if has_apple[row][col] - has_apple[next_row][col] > 0:
                ways += dp(next_row, col, pieces - 1)
        for next_col in range(col + 1, cols):
            if has_apple[row][col] - has_apple[row][next_col] > 0:
                ways += dp(row, next_col, pieces - 1)
        return ways % mod

    return dp(0, 0, max(1, min(k, rows + cols))) if rows and cols else 0
```
</details>
