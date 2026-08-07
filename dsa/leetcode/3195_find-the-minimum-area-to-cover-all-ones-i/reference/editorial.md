### Approach: One-time Traversal

#### Intuition

During traversal, we need to find the upper, lower, left, and right boundaries where $1$ appears. Once the boundaries are identified, we calculate the minimum area they enclose.

#### Implementation

```python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        min_i, max_i = n, 0
        min_j, max_j = m, 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    max_j = max(max_j, j)

        return (max_i - min_i + 1) * (max_j - min_j + 1)
```

#### Complexity Analysis

Let $n$ be the number of rows in the $\textit{grid}$, and $m$ be the number of columns in $\textit{grid}[0]$.

- Time complexity: $O(n \cdot m)$.

  We traverse the entire matrix once.

- Space complexity: $O(1)$.

  Only a few additional variables are needed.

---