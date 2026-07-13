# Make a Square with the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3127 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [make-a-square-with-the-same-color](https://leetcode.com/problems/make-a-square-with-the-same-color/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/make-a-square-with-the-same-color/).

### Goal
Given a 3x3 grid containing characters 'B' (black) and 'W' (white), determine if it is possible to form a 2x2 square consisting of cells of the same color by changing at most one cell's color.

### Function Contract
**Inputs**

- `grid`: A list of lists of characters (3x3 matrix) where each element is either 'B' or 'W'.

**Return value**

- `bool`: Returns `True` if a monochromatic 2x2 square can be formed, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [["B","W","B"],["B","W","W"],["B","W","B"]]`
- Output: `True`

**Example 2**

- Input: `grid = [["B","W","B"],["W","B","W"],["B","W","B"]]`
- Output: `False`

**Example 3**

- Input: `grid = [["B","W","B"],["B","W","W"],["W","W","B"]]`
- Output: `True`

---

## Solution
### Approach
The problem is solved using **Brute Force Enumeration**. Since the grid is fixed at 3x3, there are exactly four possible 2x2 sub-grids. For each sub-grid, we count the occurrences of 'B' and 'W'. If either color appears 3 or 4 times, it implies that with at most one change, we can make all four cells the same color.

### Complexity Analysis
- **Time Complexity**: O(1). The grid size is constant (3x3), and we perform a fixed number of operations (checking 4 sub-grids).
- **Space Complexity**: O(1). We only use a constant amount of extra space for counters.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[str]]) -> bool:
    """
    Checks if any 2x2 subgrid can be made monochromatic by changing at most one cell.
    A 2x2 square can be made monochromatic if it contains at least 3 cells of the same color.
    """
    # There are four possible 2x2 squares in a 3x3 grid.
    # Their top-left corners are at (0,0), (0,1), (1,0), and (1,1).
    for i in range(2):
        for j in range(2):
            # Collect the four cells in the current 2x2 square
            cells = [
                grid[i][j],
                grid[i+1][j],
                grid[i][j+1],
                grid[i+1][j+1]
            ]

            # Count occurrences of 'B' and 'W'
            black_count = cells.count('B')
            white_count = cells.count('W')

            # If either color appears 3 or 4 times, we can form a monochromatic square
            if black_count >= 3 or white_count >= 3:
                return True

    return False
```
</details>
