# Find the Minimum Area to Cover All Ones II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3197 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Matrix, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-minimum-area-to-cover-all-ones-ii](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/).

### Goal
Given a binary matrix, determine the minimum total area required to cover all '1's in the grid using exactly three non-overlapping rectangles. The rectangles must be axis-aligned and can be placed anywhere as long as they cover all existing '1's in the matrix.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers (0 or 1) representing the binary matrix.

**Return value**

- An integer representing the minimum combined area of three rectangles that cover all '1's.

### Examples
**Example 1**

- Input: `grid = [[0,1,0],[1,0,1]]`
- Output: `6`

**Example 2**

- Input: `grid = [[1,0,1,0],[0,1,0,1]]`
- Output: `5`

---

## Solution
### Approach
The problem is solved by partitioning the grid into three regions using two cuts. There are two primary ways to partition the grid:
1. **Three parallel cuts**: Either three horizontal cuts or three vertical cuts.
2. **One cut followed by a perpendicular cut**: One horizontal cut splitting the grid into two, then one of those halves is split by a vertical cut (or vice versa).

For any defined sub-rectangle, the minimum area to cover all '1's is the area of the bounding box of all '1's contained within that sub-rectangle. We iterate through all possible cut positions to find the minimum sum of areas.

### Complexity Analysis
- **Time Complexity**: $O(M \cdot N \cdot (M + N))$, where $M$ is the number of rows and $N$ is the number of columns. We iterate through all possible cut combinations, and calculating the bounding box takes $O(M \cdot N)$.
- **Space Complexity**: $O(M \cdot N)$ to store the grid and potentially $O(1)$ auxiliary space if we optimize bounding box calculations.

### Reference Implementations
<details>
<summary>python</summary>

```python
from functools import lru_cache


def solve(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    row_prefix = [[0] * (n + 1) for _ in range(m)]
    col_prefix = [[0] * (m + 1) for _ in range(n)]
    for r in range(m):
        for c in range(n):
            row_prefix[r][c + 1] = row_prefix[r][c] + grid[r][c]
    for c in range(n):
        for r in range(m):
            col_prefix[c][r + 1] = col_prefix[c][r] + grid[r][c]

    @lru_cache(maxsize=None)
    def area(r1: int, r2: int, c1: int, c2: int) -> int:
        if r1 > r2 or c1 > c2:
            return 0

        top = bottom = left = right = -1
        for r in range(r1, r2 + 1):
            if row_prefix[r][c2 + 1] - row_prefix[r][c1]:
                top = r
                break
        if top == -1:
            return 0
        for r in range(r2, r1 - 1, -1):
            if row_prefix[r][c2 + 1] - row_prefix[r][c1]:
                bottom = r
                break
        for c in range(c1, c2 + 1):
            if col_prefix[c][r2 + 1] - col_prefix[c][r1]:
                left = c
                break
        for c in range(c2, c1 - 1, -1):
            if col_prefix[c][r2 + 1] - col_prefix[c][r1]:
                right = c
                break
        return (bottom - top + 1) * (right - left + 1)

    answer = float("inf")

    for first in range(m - 2):
        for second in range(first + 1, m - 1):
            answer = min(
                answer,
                area(0, first, 0, n - 1)
                + area(first + 1, second, 0, n - 1)
                + area(second + 1, m - 1, 0, n - 1),
            )

    for first in range(n - 2):
        for second in range(first + 1, n - 1):
            answer = min(
                answer,
                area(0, m - 1, 0, first)
                + area(0, m - 1, first + 1, second)
                + area(0, m - 1, second + 1, n - 1),
            )

    for row_cut in range(m - 1):
        for col_cut in range(n - 1):
            answer = min(
                answer,
                area(0, row_cut, 0, col_cut)
                + area(0, row_cut, col_cut + 1, n - 1)
                + area(row_cut + 1, m - 1, 0, n - 1),
                area(0, row_cut, 0, n - 1)
                + area(row_cut + 1, m - 1, 0, col_cut)
                + area(row_cut + 1, m - 1, col_cut + 1, n - 1),
                area(0, m - 1, 0, col_cut)
                + area(0, row_cut, col_cut + 1, n - 1)
                + area(row_cut + 1, m - 1, col_cut + 1, n - 1),
                area(0, row_cut, 0, col_cut)
                + area(row_cut + 1, m - 1, 0, col_cut)
                + area(0, m - 1, col_cut + 1, n - 1),
            )

    return int(answer)
```
</details>
