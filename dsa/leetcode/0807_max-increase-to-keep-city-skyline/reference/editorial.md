
---
### Approach #1: Row and Column Maximums [Accepted]

**Intuition and Algorithm**

The skyline looking from the top is $\text{col}_{maxes} = [max(\text{column}_{0}), max(\text{column}_{1}), ...]$.  Similarly, the skyline from the left is $\text{row}_{maxes} [max(\text{row}_{0}), max(\text{row}_{1}), ...]$

In particular, each building $\text{grid}[r][c]$ could become height $min(max(\text{row}_{r}), max(\text{col}_{c}))$, and this is the largest such height.  If it were larger, say $\text{grid}[r][c] > max(\text{row}_{r})$, then the part of the skyline $\text{row}_{maxes} = [..., max(\text{row}_{r}), ...]$ would change.

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

* Time Complexity:  $O(N^2)$, where $N$ is the number of rows (and columns) of the grid.  We iterate through every cell of the grid.

* Space Complexity: $O(N)$, the space used by $\text{row}_{maxes}$ and $\text{col}_{maxes}$.