### Approach: 2D Prefix Sum

#### Intuition

The problem requires counting the number of submatrices that include the top-left element of the matrix $\textit{grid}$ and have a sum not exceeding $k$.

We start from the top-left corner and traverse the matrix in row-major order, treating each position $(i, j)$ as the bottom-right corner of a submatrix. To efficiently compute submatrix sums in a single pass, we maintain an array $\textit{cols}[j]$ that stores the sum of elements in column $j$ up to the current row.

While processing row $i$, we iterate over columns $j$ from left to right. For each column, we add $\textit{grid}[i][j]$ to $\textit{cols}[j]$, and then accumulate $\textit{cols}[j]$ into a running sum for the current row. If the accumulated sum is $\le k$, we increment the result by $1$.

#### Implementation


```python
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        cols = [0] * n
        res = 0

        for i in range(m):
            row_sum = 0
            for j in range(n):
                cols[j] += grid[i][j]
                row_sum += cols[j]
                if row_sum <= k:
                    res += 1

        return res
```


#### Complexity Analysis

Let $m$ be the number of rows in the matrix $\textit{grid}$, and $n$ be the number of columns.

- Time Complexity: $O(mn)$.
- Space Complexity: $O(n)$.

---