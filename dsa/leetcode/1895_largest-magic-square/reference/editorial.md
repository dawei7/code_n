### Approach: Enumerating Squares + Prefix Sum Optimization

#### Intuition

We enumerate the square edge length $\textit{edge}$ in descending order. For each possible edge length, we enumerate all squares of size $\textit{edge}$ in the given matrix $\textit{grid}$ and check whether they satisfy the conditions of a magic square.

Let $l = \min(m, n)$. The possible values of $\textit{edge}$ lie in the range $[1, l]$. For a fixed edge length $\textit{edge}$, the number of squares of this size is $(m - \textit{edge} + 1)(n - \textit{edge} + 1)$, which is $O(mn)$.

For each square, we need to compute the sums of all rows, columns, and the two diagonals. There are $\textit{edge}$ rows, $\textit{edge}$ columns, and $2$ diagonals. Without any optimization, computing each row or column sum takes $O(\textit{edge})$ time, so the total time for checking one square is $O(\textit{edge}^2)$.

Combining all factors, the total time complexity of this brute-force approach is

$O\left(\sum_{\textit{edge}=1}^{l} mn \cdot \textit{edge}^2\right) =$\mathcal{O}(l^3 mn)$.$

An $O(l^3 mn)$ algorithm may struggle to pass all test cases. Although the constant factor is small, this complexity is still risky for the given constraints. Therefore, we apply a prefix sum optimization to reduce the cost of computing line sums.

##### Prefix Sum Optimization

We precompute prefix sums for each row and each column of the matrix $\textit{grid}$.

* Each row sum can be computed in $O(1)$ time using row prefix sums. Since there are $\textit{edge}$ rows, the total time is $O(\textit{edge})$.
* Each column sum can be computed in $O(1)$ time using column prefix sums. Since there are $\textit{edge}$ columns, the total time is $O(\textit{edge})$.
* We do not preprocess diagonal prefix sums because there are only two diagonals. Computing them directly still takes $O(\textit{edge})$ time.

As a result, the total time for checking one square is reduced from $O(\textit{edge}^2)$ to $O(\textit{edge})$.

Therefore, the overall time complexity becomes

$O\left(\sum_{\textit{edge}=1}^{l} mn \cdot \textit{edge}\right) =$\mathcal{O}(l^2 mn)$,$

which is acceptable for the given constraint $m, n \leq 50$.

Since a square of edge length $1$ is always a magic square, we only need to enumerate $\textit{edge}$ in descending order over the range $[2, l]$.

#### Implementation

```python
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # prefix sum of each row
        rowsum = [[0] * n for _ in range(m)]
        for i in range(m):
            rowsum[i][0] = grid[i][0]
            for j in range(1, n):
                rowsum[i][j] = rowsum[i][j - 1] + grid[i][j]

        # prefix sum of each column
        colsum = [[0] * n for _ in range(m)]
        for j in range(n):
            colsum[0][j] = grid[0][j]
            for i in range(1, m):
                colsum[i][j] = colsum[i - 1][j] + grid[i][j]

        # enumerate edge lengths from largest to smallest
        for edge in range(min(m, n), 1, -1):
            # enumerate the top-left corner position (i,j) of the square
            for i in range(m - edge + 1):
                for j in range(n - edge + 1):
                    # the value for each row, column, and diagonal should be calculated (using the first row as a sample)
                    stdsum = rowsum[i][j + edge - 1] - (
                        0 if j == 0 else rowsum[i][j - 1]
                    )
                    check = True
                    # enumerate each row and directly compute the sum using prefix sums
                    # since we have already used the first line as a sample, we can skip the first line here.
                    for ii in range(i + 1, i + edge):
                        if (
                            rowsum[ii][j + edge - 1]
- (0 if j == 0 else rowsum[ii][j - 1])
                            != stdsum
                        ):
                            check = False
                            break
                    if not check:
                        continue

                    # enumerate each column and directly calculate the sum using prefix sums
                    for jj in range(j, j + edge):
                        if (
                            colsum[i + edge - 1][jj]
- (0 if i == 0 else colsum[i - 1][jj])
                            != stdsum
                        ):
                            check = False
                            break
                    if not check:
                        continue

                    # d1 and d2 represent the sums of the two diagonals respectively.
                    # here d denotes diagonal
                    d1 = d2 = 0
                    # sum directly by traversing without using the prefix sum.
                    for k in range(edge):
                        d1 += grid[i + k][j + k]
                        d2 += grid[i + k][j + edge - 1 - k]
                    if d1 == stdsum and d2 == stdsum:
                        return edge

        return 1
```

#### Complexity Analysis

- Time complexity: $O(mn\min(m, n)^2)$.

- Space complexity: $O(mn)$.

  This space is used to store the row and column prefix sums.

---