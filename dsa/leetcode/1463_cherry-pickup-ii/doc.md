# Cherry Pickup II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1463 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [cherry-pickup-ii](https://leetcode.com/problems/cherry-pickup-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/cherry-pickup-ii/).

### Goal
Two robots start at the top row, one at the leftmost column and one at the rightmost column. On each step both move to the next row and may shift left, stay, or shift right. Maximize the total cherries collected.

### Function Contract
**Inputs**

- `grid`: a matrix where each cell contains cherries.

**Return value**

The maximum number of cherries both robots can collect.

### Examples
**Example 1**

- Input: `grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]`
- Output: `24`

**Example 2**

- Input: `grid = [[1,0,0,0],[0,0,0,0],[0,0,2,0]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1,1],[1,1]]`
- Output: `4`

---

## Solution
### Approach
Row-by-row dynamic programming over the two robot columns. Each state `(row, c1, c2)` stores the best cherries after both robots reach those columns; transitions try all nine next-column pairs.

### Complexity Analysis
- **Time Complexity**: `O(rows * cols^2 * 9)`
- **Space Complexity**: `O(cols^2)` with rolling rows.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    if not rows or not cols:
        return 0
    dp = {(0, cols - 1): grid[0][0] + (grid[0][cols - 1] if cols > 1 else 0)}
    for row in range(1, rows):
        next_dp = {}
        for (c1, c2), value in dp.items():
            for nc1 in (c1 - 1, c1, c1 + 1):
                for nc2 in (c2 - 1, c2, c2 + 1):
                    if 0 <= nc1 < cols and 0 <= nc2 < cols:
                        gain = grid[row][nc1] + (grid[row][nc2] if nc1 != nc2 else 0)
                        key = (nc1, nc2)
                        next_dp[key] = max(next_dp.get(key, -1), value + gain)
        dp = next_dp
    return max(dp[key] for key in dp)
```
</details>
