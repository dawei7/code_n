### Approach: 2D Difference + Prefix Sum

#### Intuition

The problem asks us to perform multiple “increment all elements in a rectangle” operations on an $n \times n$ integer matrix $\textit{mat}$, and return the matrix $\textit{mat}$ after all operations have been applied. In the two-dimensional case, if we want to increment all elements within a rectangular submatrix, we can update a two-dimensional difference array $\textit{diff}$ as follows:

$$
\begin{aligned}
diff[row_1][col_1] &+= 1 \\
diff[row_2 + 1][col_1] &-= 1 \\
diff[row_1][col_2 + 1] &-= 1 \\
diff[row_2 + 1][col_2 + 1] &+= 1
\end{aligned}
$$

After processing all queries, the final matrix $\textit{mat}$ can be obtained by computing the prefix sum over the two-dimensional difference array:

$$
\textit{mat}[i][j] = \textit{diff}[i][j] + \textit{mat}[i - 1][j] + \textit{mat}[i][j - 1] - \textit{mat}[i - 1][j - 1]
$$

#### Implementation


```python
class Solution:
    def rangeAddQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row2 + 1][col1] -= 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                x1 = 0 if i == 0 else mat[i - 1][j]
                x2 = 0 if j == 0 else mat[i][j - 1]
                x3 = 0 if i == 0 or j == 0 else mat[i - 1][j - 1]
                mat[i][j] = diff[i][j] + x1 + x2 - x3
        return mat
```


#### Complexity Analysis

- Time complexity: $O( |queries| + n^2)$.

- Space complexity: $O(n^2)$.

---