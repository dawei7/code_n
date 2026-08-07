### Approach: Dynamic Programming

#### Intuition

Unless otherwise specified, all matrix indices start from $1$. That is, given a square matrix of dimension $n$, the top-left element has index $(1, 1)$ and is located in the first row and first column, while the bottom-right element has index $(n, n)$ and is located in the $n$-th row and $n$-th column.

Start with a dynamic programming approach of $O(n^4)$

From the problem statement, we can observe that after any number of operations, each column must end up with black cells on top and white cells on the bottom. Formally, each column can be viewed as an array of length $n$, where the first $i$ elements are black and the remaining $n - i$ elements are white, for some $0 \le i \le n$.

Since the state of each column can be described by a boundary index, and the score of each column depends only on its adjacent columns, dynamic programming is a natural approach for this problem.

We first compute prefix sums for each column as a preprocessing step. Let $S_{i,j}$ denote the sum of the first $j$ elements in the $i$-th column, where $0 \le j \le n$. We define the state $\textit{dp}[i][h_\textit{curr}][h_\textit{prev}]$ as the maximum score obtained after processing up to the $i$-th column, where the first $h_\textit{curr}$ elements of column $i$ are black, and the first $h_\textit{prev}$ elements of column $i-1$ are black.

The state transition can be derived as follows:

- The state $\textit{dp}[i]$ captures the coloring of columns $i$ and $i-1$. This corresponds to fixing $h_\textit{curr}$ in $\textit{dp}[i-1]$. Therefore, we enumerate $h_\textit{prev}$ from $\textit{dp}[i-1]$, which implicitly enumerates the coloring of column $i-2$. In this way, we effectively consider three consecutive columns and can compute the resulting score.

- When $h_\textit{curr} \le h_\textit{prev}$, the current column has fewer black cells than the previous column. In this case, the additional score contributed by the current column must be included, corresponding to the blue region in the figure.

    ![situation-1](images/1.png)

- When $h_\textit{curr} > h_\textit{prev}$, the current column has more black cells than the previous column. Let the previous state's parameter be $k$. We consider three cases:
  - Case 1: When $k < h_\textit{prev}$, we add the score of the newly covered region introduced by $h_\textit{curr}$.

    ![situation-2_1](images/2.png)

  - Case 2: When $h_\textit{prev} \le k < h_\textit{curr}$, we add only the newly covered region and avoid double counting the already covered part.

    ![situation-2_2](images/3.png)

  - Case 3: When $k \ge h_\textit{curr}$, no new contribution is added, and we directly inherit the previous state.

    ![situation-2_3](images/4.png)

The resulting transition is:

$$
\textit{dp}[i][h_\textit{curr}][h_\textit{prev}] =
\begin{cases}
\max\limits_{0 \le k \le n} \{ \textit{dp}[i-1][h_\textit{prev}][k] \} + S_{i, h_\textit{prev}} - S_{i, h_\textit{curr}}, & h_\textit{curr} \le h_\textit{prev} \\
\max\limits_{0 \le k \le n} \{ \textit{dp}[i-1][h_\textit{prev}][k] + \max(0, S_{i-1, h_\textit{curr}} - S_{i-1, \max(h_\textit{prev}, k)}) \}, & h_\textit{curr} \gt h_\textit{prev}
\end{cases}
$$

Additionally, we need to handle edge case for the first and last columns:

- For the first column, since column $0$ does not exist, $h_\textit{prev}$ must be fixed to $0$. Therefore, $k$ can only take the value $0$.
- For the last column, the optimal configuration must be either fully black or fully white. This is because changing the last column does not affect any future columns, so only extreme configurations can maximize the score.

**Optimizing the $h_\textit{prev}$ state**

The above approach has a time complexity of $O(n^4)$, which is too slow. The bottleneck is the enumeration of $k$. We aim to eliminate this by preprocessing useful maximum values.

When $h_\textit{curr} \le h_\textit{prev}$, the transition does not depend on $k$ except through:

$$
\max\limits_{0 \le k \le n} { \textit{dp}[i-1][h_\textit{prev}][k] }
$$

This allows us to compute the transition in $O(1)$ time if we precompute this maximum.

For the case $h_\textit{curr} > h_\textit{prev}$, we analyze based on whether $k \le h_\textit{curr}$:

* When $k \le h_\textit{curr}$, we always add a fixed extra score. To avoid double counting, we maintain a prefix maximum that excludes contributions from column $i-1$:

$$
\textit{prevMax}[h_\textit{prev}][j] = \max\limits_{0 \le k \le j} \left( \textit{dp}[i-1][h_\textit{prev}][k] - \max(0, S_{i-1, k} - S_{i-1, h_\textit{prev}}) \right)
$$

Now the transition becomes independent of $k$, and we can update in $O(1)$ time.

* When $k > h_\textit{curr}$, no additional score is added. We only need the suffix maximum:

$$
\textit{prevSuffixMax}[h_\textit{prev}][j] = \max\limits_{j \le k \le n} { \textit{dp}[i-1][h_\textit{prev}][k] }
$$

The optimized transition becomes:

$$
\textit{dp}[i][h_\textit{curr}][h_\textit{prev}] =
\begin{cases}
\textit{prevSuffixMax}[h_\textit{prev}][0] + S_{i, h_\textit{prev}} - S_{i, h_\textit{curr}}, & h_\textit{curr} \le h_\textit{prev} \
\max\left(
\textit{prevSuffixMax}[h_\textit{prev}][h_\textit{curr}],
\textit{prevMax}[h_\textit{prev}][h_\textit{curr}] + S_{i-1, h_\textit{curr}} - S_{i-1, h_\textit{prev}}
\right), & h_\textit{curr} > h_\textit{prev}
\end{cases}
$$

#### Implementation


```python
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1:
            return 0

        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]
        col_sum = [[0] * (n + 1) for _ in range(n)]

        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        for i in range(1, n):
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        extra_score = col_sum[i][prev_h] - col_sum[i][curr_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][0] + extra_score,
                        )
                    else:
                        extra_score = (
                            col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        )
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][curr_h],
                            prev_max[prev_h][curr_h] + extra_score,
                        )

            for curr_h in range(n + 1):
                prev_max[curr_h][0] = dp[i][curr_h][0]
                for prev_h in range(1, n + 1):
                    penalty = (
                        col_sum[i][prev_h] - col_sum[i][curr_h]
                        if prev_h > curr_h
                        else 0
                    )
                    prev_max[curr_h][prev_h] = max(
                        prev_max[curr_h][prev_h - 1],
                        dp[i][curr_h][prev_h] - penalty,
                    )

                prev_suffix_max[curr_h][n] = dp[i][curr_h][n]
                for prev_h in range(n - 1, -1, -1):
                    prev_suffix_max[curr_h][prev_h] = max(
                        prev_suffix_max[curr_h][prev_h + 1],
                        dp[i][curr_h][prev_h],
                    )

        ans = 0
        for k in range(n + 1):
            ans = max(ans, dp[n - 1][n][k], dp[n - 1][0][k])

        return ans
```


#### Complexity Analysis

Let $n$ be the dimension of the square matrix $\textit{grid}$.

- Time complexity: $O(n^3)$.
  
  Computing prefix sums takes $O(n^2)$. Each DP transition, along with prefix and suffix maximum computations, takes $O(n^2)$ per column. Over all columns, this results in $O(n^3)$.

- Space complexity: $O(n^3)$.
  
  The DP table requires $O(n^3)$ space. Additional arrays for prefix sums and auxiliary maximums require $O(n^2)$. Using a rolling array can reduce space to $O(n^2)$.

---