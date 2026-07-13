# Count Submatrices With Equal Frequency of X and Y

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3212 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-submatrices-with-equal-frequency-of-x-and-y](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/).

### Goal
Given a 2D grid containing characters 'X', 'Y', and '.', count the number of submatrices starting from the top-left corner (0, 0) and ending at any coordinate (i, j) such that the submatrix contains at least one 'X', and the total count of 'X's equals the total count of 'Y's within that submatrix.

### Function Contract
**Inputs**

- `grid`: A 2D list of characters (List[List[str]]) representing the matrix.

**Return value**

- An integer representing the total count of valid submatrices.

### Examples
**Example 1**

- Input: `grid = [["X","Y","."],["X",".","."]]`
- Output: `3`

**Example 2**

- Input: `grid = [["X","X"],["X","Y"]]`
- Output: `0`

**Example 3**

- Input: `grid = [["."],["Y"]]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using 2D Prefix Sums. By maintaining two separate 2D arrays (or updating in-place) to track the cumulative counts of 'X' and 'Y' for every sub-rectangle starting at (0,0) and ending at (i, j), we can determine the frequency of both characters in constant time for any given cell.

### Complexity Analysis
- **Time Complexity**: `O(M * N)`, where M is the number of rows and N is the number of columns, as we iterate through the grid exactly once to compute prefix sums and count valid submatrices.
- **Space Complexity**: `O(M * N)` to store the prefix sum matrices. This can be optimized to `O(N)` if we only store the current and previous row, but `O(M * N)` is standard for clarity.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # prefix_x[i][j] stores count of 'X' in grid[0...i-1][0...j-1]
    # prefix_y[i][j] stores count of 'Y' in grid[0...i-1][0...j-1]
    prefix_x = [[0] * (cols + 1) for _ in range(rows + 1)]
    prefix_y = [[0] * (cols + 1) for _ in range(rows + 1)]

    count = 0

    for i in range(rows):
        for j in range(cols):
            # Calculate prefix sums using inclusion-exclusion principle
            val_x = 1 if grid[i][j] == 'X' else 0
            val_y = 1 if grid[i][j] == 'Y' else 0

            prefix_x[i+1][j+1] = (prefix_x[i][j+1] + prefix_x[i+1][j] -
                                  prefix_x[i][j] + val_x)
            prefix_y[i+1][j+1] = (prefix_y[i][j+1] + prefix_y[i+1][j] -
                                  prefix_y[i][j] + val_y)

            # Check condition: count of X == count of Y and count of X > 0
            if prefix_x[i+1][j+1] == prefix_y[i+1][j+1] and prefix_x[i+1][j+1] > 0:
                count += 1

    return count
```
</details>
