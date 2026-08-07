[TOC]

## Solution
---
### Approach 1: Mathematical

**Intuition and Algorithm**

From the top, the shadow made by the shape will be 1 square for each non-zero value.

From the side, the shadow made by the shape will be the largest value for each row in the grid.

From the front, the shadow made by the shape will be the largest value for each column in the grid.

**Example**

With the example `[[1,2],[3,4]]`:

* The shadow from the top will be 4, since there are four non-zero values in the grid;

* The shadow from the side will be $2 + 4$, since the maximum value of the first row is `2`, and the maximum value of the second row is `4`;

* The shadow from the front will be $3 + 4$, since the maximum value of the first column is `3`, and the maximum value of the second column is `4`.

```python
class Solution:
    def projectionArea(self, grid):
        N = len(grid)
        ans = 0

        for i in xrange(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in xrange(N):
                if grid[i][j]: ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ans += best_row + best_col

        return ans

        """ Alternative solution:
        ans = sum(map(max, grid))
        ans += sum(map(max, zip(*grid)))
        ans += sum(v > 0 for row in grid for v in row)
        """
```

**Complexity Analysis**

* Time Complexity:  $O(N^2)$, where $N$ is the length of `grid`.

* Space Complexity:  $O(1)$.
<br />
<br />