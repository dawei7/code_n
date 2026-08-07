### Approach 1: Memoization Search

#### Intuition

This problem is essentially the same as the problem statement of “[188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/)”, except that here we also allow an additional action: short selling. Because of this extra operation, the state definition from the original problem needs to be extended.

In the editorial for problem 188, the dynamic programming states are defined like this. The value `dfs(i, j, 0)` represents the maximum profit after day `i` if exactly `j` transactions have been completed and we end the day holding no stock. Similarly, `dfs(i, j, 1)` represents the maximum profit after day `i` with exactly `j` completed transactions while holding one stock.

Since this problem allows short selling, meaning we can sell first and buy later, we introduce a third state. The value `dfs(i, j, 2)` represents the maximum profit after day `i` with exactly `j` completed transactions while holding a short position.

With these three states defined, consider what can happen on day `i` when we want to end up with exactly `j` completed transactions.

One possibility is that nothing happens on that day. If we neither buy nor sell, then all three states simply carry over from day $i - 1$:

* $dfs(i, j, 0) = dfs(i - 1, j, 0)$
* $dfs(i, j, 1) = dfs(i - 1, j, 1)$
* $dfs(i, j, 2) = dfs(i - 1, j, 2)$

Another possibility is that we buy on day `i`. There are two situations in which this can occur. If we were not holding anything at the end of day $i - 1$, buying the stock starts the `j`th normal transaction, so we come from $dfs(i - 1, j - 1, 0)$ and pay the cost of $\text{prices}[i]$, giving
$dfs(i, j, 1) = dfs(i - 1, j - 1, 0) - \text{prices}[i]$.

The other case is that we were holding a short position. Buying in this situation closes the short transaction, so we move from $dfs(i - 1, j, 2)$ and again subtract the cost, giving
$dfs(i, j, 0) = dfs(i - 1, j, 2) - \text{prices}[i]$.

The third possibility on day `i` is that we sell. If we were holding a stock at the end of the previous day, selling completes the `j`th ordinary transaction, so we move from $dfs(i - 1, j, 1)$ and gain $\text{prices}[i]$, which results in
$dfs(i, j, 0) = dfs(i - 1, j, 1) + \text{prices}[i]$.

If instead we were holding nothing at the end of the previous day, selling opens the `j`th short selling transaction. In that case we come from $dfs(i - 1, j - 1, 0)$ and add the profit $\text{prices}[i]$, which gives
$dfs(i, j, 2) = dfs(i - 1, j - 1, 0) + \text{prices}[i]$.

These cases lead directly to the final recurrence:

$\text{dfs}(i,j,0) = \max(\text{dfs}(i - 1,j,0),\ \text{dfs}(i - 1,j,1) + \textit{prices}[i],\ \text{dfs}(i - 1,j,2) - \textit{prices}[i])$

$\text{dfs}(i,j,1) = \max(\text{dfs}(i - 1,j,1),\ \text{dfs}(i - 1,j - 1,0) - \textit{prices}[i])$

$\text{dfs}(i,j,2) = \max(\text{dfs}(i - 1,j,2),\ \text{dfs}(i - 1,j - 1,0) + \textit{prices}[i])$

Next consider the boundary conditions. On day `0`, only one price exists. If no action is taken, the profit is zero. If we buy, the profit is $-\text{prices}[0]$. If we short, the profit is $\text{prices}[0]$. When $j = 0$, no transactions are allowed, so the profit must be zero in all states. Translating these observations into formulas:

* For all `i`, if $j = 0$, then $dfs(i, 0, 0) = dfs(i, 0, 1) = dfs(i, 0, 2) = 0$.
* For $i = 0$ and any `1 ≤ j ≤ k`, we have $dfs(0, j, 0) = 0$, $dfs(0, j, 1) = -\text{prices}[0]$, and $dfs(0, j, 2) = \text{prices}[0]$.

After computing all states up to day $n - 1$, the final answer is $dfs(n - 1, k, 0)$, since we can make at most `k` total transactions and we must end with no stock or short position.

#### Implementation

```python
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(i, j, state):
            if j == 0:
                return 0
            if i == 0:
                return (
                    0 if state == 0 else -prices[0] if state == 1 else prices[0]
                )
            p = prices[i]
            if state == 0:
                res = max(
                    dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p
                )
            elif state == 1:
                res = max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
            else:
                res = max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)

            return res

        ans = dfs(n - 1, k, 0)
        dfs.cache_clear()
        return ans
```

#### Complexity Analysis

Let $n$ be the length of the given array $\textit{prices}$, and $k$ be the given number.

- Time complexity: $O(nk)$.

  Memorized search has a total of $3\times n\times k$ substates, so the time complexity is $O(nk)$.

- Space complexity: $O(nk)$.

  Memorized search requires storing a total of $3\times n\times k$ substates, so the maximum space needed is $O(nk)$.

### Approach 2: Dynamic Programming

#### Intuition

Similarly, we can solve it using a bottom-up dynamic programming approach, by expanding the memoized search recursively.

#### Implementation

```python
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]

        # initialize the state on day 0
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]
            dp[0][j][2] = prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(
                    dp[i - 1][j][0],
                    max(
                        dp[i - 1][j][1] + prices[i], dp[i - 1][j][2] - prices[i]
                    ),
                )
                dp[i][j][1] = max(
                    dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]
                )
                dp[i][j][2] = max(
                    dp[i - 1][j][2], dp[i - 1][j - 1][0] + prices[i]
                )

        return dp[n - 1][k][0]
```

We observe that the optimal state on day $i$ depends only on the optimal state on day $i-1$, and is unrelated to the optimal states on earlier days. At this point, we can use a rolling array, retaining only the optimal state of the previous day, thereby reducing the space complexity to $O(k)$. During actual traversal, we can calculate sequentially in the order of $j$ from large to small, without the need to create temporary variables.

```python
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(k + 1)]
        # initialize the state on day 0
        for j in range(1, k + 1):
            dp[j][1] = -prices[0]
            dp[j][2] = prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[j][0] = max(
                    dp[j][0], max(dp[j][1] + prices[i], dp[j][2] - prices[i])
                )
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
                dp[j][2] = max(dp[j][2], dp[j - 1][0] + prices[i])

        return dp[k][0]
```

#### Complexity Analysis

Let $n$ be the length of the given array $\textit{prices}$, and $k$ be the given number.

- Time complexity: $O(nk)$.

  Dynamic programming has a total of $3\times n\times k$ substates, so the time complexity is $O(nk)$.

- Space complexity: $O(k)$.

  After space optimization, only $3k$ states need to be stored each time, so the space complexity is $O(k)$.

---