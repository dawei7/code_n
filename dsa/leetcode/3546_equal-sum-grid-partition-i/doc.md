# Equal Sum Grid Partition I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3546 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [equal-sum-grid-partition-i](https://leetcode.com/problems/equal-sum-grid-partition-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/equal-sum-grid-partition-i/).

### Goal
Given a 2D grid of integers, determine if it is possible to partition the grid into four rectangular sub-grids by drawing one horizontal line and one vertical line. The goal is to check if there exists a configuration where the sum of elements in each of the four resulting quadrants is equal.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the 2D matrix.

**Return value**

- `bool`: Returns `True` if there exists a horizontal cut at row `i` and a vertical cut at column `j` such that the four resulting rectangular regions have identical sums, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[1, 2], [3, 4]]`
- Output: `False`

**Example 2**

- Input: `grid = [[1, 1], [1, 1]]`
- Output: `True`

**Example 3**

- Input: `grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `False`

---

## Solution
### Approach
The problem is solved using 2D Prefix Sums (or Summed-Area Table). By precomputing the prefix sums, we can calculate the sum of any rectangular sub-grid in $O(1)$ time. We then iterate through all possible horizontal cut positions (between rows) and vertical cut positions (between columns), checking if the four resulting quadrants have equal sums.

### Complexity Analysis
- **Time Complexity**: $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. We perform a single pass to build the prefix sum table and a nested loop to check all possible cut combinations.
- **Space Complexity**: $O(M \times N)$ to store the 2D prefix sum table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> bool:
    if not grid or not grid[0]:
        return False

    rows = len(grid)
    cols = len(grid[0])

    # Build 2D prefix sum table
    # pref[i][j] stores sum of grid[0...i-1][0...j-1]
    pref = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            pref[r + 1][c + 1] = grid[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]

    def get_sum(r1, c1, r2, c2):
        # Returns sum of rectangle from (r1, c1) to (r2, c2) inclusive
        return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]

    # Iterate through all possible horizontal cuts (after row i)
    # and vertical cuts (after column j)
    # i ranges from 0 to rows-2, j ranges from 0 to cols-2
    for i in range(rows - 1):
        for j in range(cols - 1):
            sum1 = get_sum(0, 0, i, j)
            sum2 = get_sum(0, j + 1, i, cols - 1)
            sum3 = get_sum(i + 1, 0, rows - 1, j)
            sum4 = get_sum(i + 1, j + 1, rows - 1, cols - 1)

            if sum1 == sum2 == sum3 == sum4:
                return True

    return False
```
</details>
