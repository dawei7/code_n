# Maximum Sum of an Hourglass

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2428 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-sum-of-an-hourglass](https://leetcode.com/problems/maximum-sum-of-an-hourglass/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-sum-of-an-hourglass/).

### Goal
Given a 2D integer matrix, identify all possible "hourglass" shapes within the grid. An hourglass is defined as a 3x3 subgrid pattern consisting of the top row (3 elements), the center element, and the bottom row (3 elements). The objective is to calculate the sum of the elements for every possible hourglass and return the maximum sum found.

### Function Contract
**Inputs**

- `grid`: A List[List[int]] representing an m x n matrix where m, n >= 3.

**Return value**

- `int`: The maximum sum obtained from any valid 3x3 hourglass pattern in the grid.

### Examples
**Example 1**

- Input: `grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]`
- Output: `30`

**Example 2**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `35`

**Example 3**

- Input: `grid = [[3,2,1],[1,0,0],[0,0,0]]`
- Output: `6`

---

## Solution
### Approach
The problem is solved using a **Brute Force Sliding Window** approach. Since the hourglass shape is fixed at 3x3, we iterate through all possible top-left corners `(i, j)` such that `0 <= i <= m-3` and `0 <= j <= n-3`. For each corner, we compute the sum of the seven specific cells forming the hourglass and track the global maximum.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns. We visit each valid top-left corner once, performing a constant number of additions (7) per window.
- **Space Complexity**: `O(1)`, as we only store a few integer variables to track the current and maximum sums, regardless of the input matrix size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(grid: List[List[int]]) -> int:
    """
    Calculates the maximum sum of an hourglass in a 2D grid.
    An hourglass at (r, c) consists of:
    grid[r][c]   grid[r][c+1]   grid[r][c+2]
                 grid[r+1][c+1]
    grid[r+2][c] grid[r+2][c+1] grid[r+2][c+2]
    """
    rows = len(grid)
    cols = len(grid[0])
    max_sum = float('-inf')

    # Iterate through all possible top-left corners of a 3x3 hourglass
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Calculate the sum of the 7 elements in the hourglass
            current_sum = (
                grid[r][c] + grid[r][c+1] + grid[r][c+2] +
                grid[r+1][c+1] +
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
            )

            if current_sum > max_sum:
                max_sum = current_sum

    return int(max_sum)
```
</details>
