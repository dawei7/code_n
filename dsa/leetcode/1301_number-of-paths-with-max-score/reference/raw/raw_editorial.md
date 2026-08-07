### Approach 1: Dynamic Programming

#### Intuition

According to the problem statement, starting from the bottom-right corner `"S"`, we can only move **up**, **left**, or **diagonally up-left**. Therefore, each position on the board is visited at most once, making dynamic programming a natural approach.

Let `dp[i][j]` represent the state at position `(i, j)` on the board. Since we need to compute both the **maximum score** from `"S"` to `(i, j)` and the **number of paths** that achieve this maximum score, each state stores two values:
* the maximum score from the bottom-right corner to `(i, j)`;
* the number of paths that achieve this maximum score.

If position `(i, j)` is unreachable from the bottom-right corner, either because it is an obstacle or because all possible paths are blocked by obstacles, we set the maximum score to `-1`.

Since the starting position is the bottom-right corner, the dynamic programming states must be computed in reverse order, that is, from larger indices to smaller ones:

```
for i = n - 1 to 0
for j = n - 1 to 0
// process dp[i][j]
```

Next, consider the state transition. Position `(i, j)` can be reached from three neighboring positions: `(i + 1, j)`, `(i, j + 1)`, and `(i + 1, j + 1)`. Since each state consists of two values, directly writing a transition such as `dp[i][j] = max(...)` is inconvenient. Instead, we define an `update()` function that updates `dp[i][j]` using one candidate state at a time.

Suppose we use `dp[u][v]` to update `dp[i][j]`. There are three possible cases:
* If the maximum score stored in `dp[u][v]` is `-1`, then position `(u, v)` is unreachable, so it cannot contribute to `dp[i][j]`.
* If the maximum scores stored in `dp[u][v]` and `dp[i][j]` are equal, then both states achieve the same maximum score. In this case, we add the number of paths stored in `dp[u][v]` to that of `dp[i][j]`, thereby merging the path counts.
* If the maximum score stored in `dp[u][v]` is greater than that of `dp[i][j]`, then `dp[u][v]` provides a better solution. We replace both the maximum score and the number of paths in `dp[i][j]` with those from `dp[u][v]`.

After considering all three predecessor states, if the maximum score stored in `dp[i][j]` is not `-1`, then position `(i, j)` is reachable. We then add the score of the current cell to the maximum score, obtaining the final state for position `(i, j)`.


#### Implementation


```python
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[-1, 0]] * n for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]

        def update(x, y, u, v):
            if u >= n or v >= n or dp[u][v][0] == -1:
                return
            if dp[u][v][0] > dp[x][y][0]:
                dp[x][y] = dp[u][v][:]
            elif dp[u][v][0] == dp[x][y][0]:
                dp[x][y][1] += dp[u][v][1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not (i == n - 1 and j == n - 1) and board[i][j] != "X":
                    update(i, j, i + 1, j)
                    update(i, j, i, j + 1)
                    update(i, j, i + 1, j + 1)
                    if dp[i][j][0] != -1:
                        dp[i][j][0] += (
                            0 if board[i][j] == "E" else ord(board[i][j]) - 48
                        )
        return (
            [dp[0][0][0], dp[0][0][1] % (10**9 + 7)]
            if dp[0][0][0] != -1
            else [0, 0]
        )
```


#### Complexity Analysis

Let $N$ be the side length of the `board`.

- Time complexity: $O(N^2)$.

- Space complexity: $O(N^2)$.

---