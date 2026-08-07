### Approach: 2D Prefix Sum

#### Intuition

We follow the conditions in the problem to identify valid submatrices.

First, the submatrix must include $\textit{grid}[0][0]$. With this constraint, the top-left corner is fixed, and we only need to determine the bottom-right corner to uniquely define a submatrix.

Second, the frequencies of $X$ and $Y$ must be equal. We can model this by maintaining a count: increment the count by $1$ for each $X$, decrement it by $1$ for each $Y$, and leave it unchanged for each `.`. A submatrix satisfies this condition if its total count is $0$. This value can be computed efficiently using a 2D prefix sum.

Finally, the submatrix must contain at least one $X$ to be considered valid. To enforce this, we extend the prefix sum structure with an additional dimension that tracks whether a submatrix with bottom-right corner at $(i, j)$ contains at least one $X$. The logic is as follows:

1. If $\textit{grid}[i][j] = X$, then the submatrix ending at $(i, j)$ must contain an $X$.
2. If $\textit{grid}[i][j] \neq X$, then whether the submatrix contains an $X$ depends on the submatrices ending at $(i - 1, j)$ or $(i, j - 1)$. If either of those contains an $X$, then the current submatrix also contains an $X$.

Alternatively, we could construct two separate prefix sum matrices to count the number of $X$ and $Y$ independently and compare them, but we do not elaborate on that approach here.

#### Implementation

```python
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        sum = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "X":
                    sum[i + 1][j + 1][0] = (
                        sum[i + 1][j][0] + sum[i][j + 1][0] - sum[i][j][0] + 1
                    )
                    sum[i + 1][j + 1][1] = 1
                elif grid[i][j] == "Y":
                    sum[i + 1][j + 1][0] = (
                        sum[i + 1][j][0] + sum[i][j + 1][0] - sum[i][j][0] - 1
                    )
                    sum[i + 1][j + 1][1] = sum[i + 1][j][1] | sum[i][j + 1][1]
                else:
                    sum[i + 1][j + 1][0] = (
                        sum[i + 1][j][0] + sum[i][j + 1][0] - sum[i][j][0]
                    )
                    sum[i + 1][j + 1][1] = sum[i + 1][j][1] | sum[i][j + 1][1]
                if sum[i + 1][j + 1][0] == 0 and sum[i + 1][j + 1][1] == 1:
                    ans += 1

        return ans
```

#### Complexity Analysis

Let $n$ be the number of rows and $m$ be the number of columns in $\textit{grid}$.

- Time complexity: $O(nm)$.

  We traverse each cell once to compute the prefix sums.

- Space complexity: $O(nm)$.

  We maintain a 2D prefix sum matrix $\textit{sum}$ of size $(n + 1) \times (m + 1) \times 2$.

---