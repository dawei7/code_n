# Find the Grid of Region Average

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3030 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-grid-of-region-average](https://leetcode.com/problems/find-the-grid-of-region-average/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-grid-of-region-average/).

### Goal
Given a 2D grid of integers and a threshold value, identify all 3x3 subgrids where the intensity difference between any two adjacent cells (horizontally or vertically) does not exceed the threshold. For such "valid" regions, calculate the integer average of the 9 cells. The output is a grid of the same dimensions where each cell contains the average of all valid 3x3 regions it belongs to, or the original value if it belongs to no valid regions.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers of size `m x n`.
- `threshold`: An integer representing the maximum allowed absolute difference between adjacent cells in a valid region.

**Return value**

- A 2D list of integers of size `m x n` representing the processed grid.

### Examples
**Example 1**

- Input: `grid = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1`
- Output: `[[9,9,9],[9,9,9],[9,9,9]]`

**Example 2**

- Input: `grid = [[10,20,30],[15,25,35],[50,60,70]], threshold = 200`
- Output: `[[34,34,34],[34,34,34],[34,34,34]]`

**Example 3**

- Input: `grid = [[10],[20],[30]], threshold = 1`
- Output: `[[10],[20],[30]]`

---

## Solution
### Approach
The solution utilizes a sliding window approach over the 2D grid. For every possible top-left corner `(i, j)` of a 3x3 subgrid, we perform a local validation check by iterating through the 9 cells and verifying the adjacency threshold condition. We maintain a secondary data structure to store the sum of averages and a count of how many valid regions cover each cell, allowing us to compute the final result in a single pass.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` and `n` are the dimensions of the grid. We iterate through the grid once to identify regions and once to compute the final averages.
- **Space Complexity**: `O(m * n)` to store the auxiliary grids for region sums and counts.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]], threshold: int) -> list[list[int]]:
    m = len(grid)
    n = len(grid[0])

    # sum_grid stores the sum of averages for each cell
    # count_grid stores how many valid 3x3 regions cover each cell
    sum_grid = [[0] * n for _ in range(m)]
    count_grid = [[0] * n for _ in range(m)]

    def is_valid(r, c):
        # Check horizontal adjacency
        for i in range(r, r + 3):
            for j in range(c, c + 2):
                if abs(grid[i][j] - grid[i][j + 1]) > threshold:
                    return False
        # Check vertical adjacency
        for i in range(r, r + 2):
            for j in range(c, c + 3):
                if abs(grid[i][j] - grid[i + 1][j]) > threshold:
                    return False
        return True

    # Iterate through all possible 3x3 top-left corners
    for i in range(m - 2):
        for j in range(n - 2):
            if is_valid(i, j):
                # Calculate average
                total = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        total += grid[r][c]
                avg = total // 9

                # Update auxiliary grids
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        sum_grid[r][c] += avg
                        count_grid[r][c] += 1

    # Construct final result
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if count_grid[i][j] > 0:
                result[i][j] = sum_grid[i][j] // count_grid[i][j]
            else:
                result[i][j] = grid[i][j]

    return result
```
</details>
