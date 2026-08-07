[TOC]

---
### Approach #1: Row and Column Maximums [Accepted]

**Intuition and Algorithm**

The skyline looking from the top is `col_maxes = [max(column_0), max(column_1), ...]`.  Similarly, the skyline from the left is `row_maxes [max(row_0), max(row_1), ...]`

In particular, each building `grid[r][c]` could become height `min(max(row_r), max(col_c))`, and this is the largest such height.  If it were larger, say `grid[r][c] > max(row_r)`, then the part of the skyline `row_maxes = [..., max(row_r), ...]` would change.

These increases are also independent (none of them change the skyline), so we can perform them independently.


```python
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
```


**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the number of rows (and columns) of the grid.  We iterate through every cell of the grid.

* Space Complexity: $$O(N)$$, the space used by `row_maxes` and `col_maxes`.