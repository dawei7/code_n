### Approach 1: Memoization Search

#### Intuition

From the first two conditions of a stable array, we know that its length is $\textit{zero} + \textit{one}$. The third condition states that there must be no subarray of length $\textit{limit} + 1$ that consists entirely of $0$s or entirely of $1$s.

We break the problem into smaller subproblems. Consider stable arrays that contain $\textit{zero}$ zeros and $\textit{one}$ ones, where the last element can be either $0$ or $1$.

* **If the last element is $1$**, we start with the number of stable arrays containing $\textit{zero}$ zeros and $\textit{one} - 1$ ones. However, we must subtract the cases where appending a $1$ makes the array unstable. This happens when the original array ends with exactly $\textit{limit}$ consecutive $1$s. In such cases, adding another $1$ creates $\textit{limit} + 1$ consecutive $1$s. The number of such arrays equals the number of stable arrays containing $\textit{zero}$ zeros and $\textit{one} - 1 - \textit{limit}$ ones, with the last element being $0$.

* **If the last element is $0$**, the reasoning is symmetric. We start with the number of stable arrays containing $\textit{zero} - 1$ zeros and $\textit{one}$ ones, and subtract the cases where appending a $0$ causes the array to exceed the allowed consecutive limit.

Thus, the problem reduces to smaller subproblems and can be solved using dynamic programming. We define
$\textit{dp}(\textit{zero}, \textit{one}, \textit{lastBit})$
as the number of stable arrays containing $\textit{zero}$ zeros and $\textit{one}$ ones, with the last element equal to $\textit{lastBit}$, where $\textit{lastBit}$ is either 0 or 1.

The recurrence relations are:

* $\textit{dp}(\textit{zero}, \textit{one}, 0)$
  = $\textit{dp}(\textit{zero} - 1, \textit{one}, 0)$

  * $\textit{dp}(\textit{zero} - 1, \textit{one}, 1)$
    − $\textit{dp}(\textit{zero} - 1 - \textit{limit}, \textit{one}, 1)$

* $\textit{dp}(\textit{zero}, \textit{one}, 1)$
  = $\textit{dp}(\textit{zero}, \textit{one} - 1, 0)$

  * $\textit{dp}(\textit{zero}, \textit{one} - 1, 1)$
    − $\textit{dp}(\textit{zero}, \textit{one} - 1 - \textit{limit}, 0)$

We also need to handle boundary cases:

* If $\textit{zero} = 0$, then no valid array exists when $\textit{lastBit} = 0$ or when $\textit{one} > \textit{limit}$. Otherwise, exactly one valid array exists.
* If $\textit{one} = 0$, the situation is symmetric.

We compute the result using memoized recursion, store intermediate states, and finally return

$\textit{dp}(\textit{zero}, \textit{one}, 0) + \textit{dp}(\textit{zero}, \textit{one}, 1)$

modulo the given value.

#### Implementation


```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(zero, one, lastBit):
            if zero == 0:
                if lastBit == 0 or one > limit:
                    return 0
                else:
                    return 1
            elif one == 0:
                if lastBit == 1 or zero > limit:
                    return 0
                else:
                    return 1
            if lastBit == 0:
                res = dp(zero - 1, one, 0) + dp(zero - 1, one, 1)
                if zero > limit:
                    res -= dp(zero - limit - 1, one, 1)
            else:
                res = dp(zero, one - 1, 0) + dp(zero, one - 1, 1)
                if one > limit:
                    res -= dp(zero, one - limit - 1, 0)
            return res % mod

        res = (dp(zero, one, 0) + dp(zero, one, 1)) % mod
        dp.cache_clear()
        return res
```


#### Complexity Analysis

- Time complexity: $O(\textit{zero} \times \textit{one})$.
  
  The number of DP states is $O(\textit{zero} \times \textit{one})$, and each state is computed in constant time.

- Space complexity: $O(\textit{zero} \times \textit{one})$.

### Approach 2: Dynamic Programming

#### Intuition

Approach 1 solves the problem using memoized recursion in a top down manner. In this approach, we compute all states bottom up using an iterative dynamic programming table. The state transitions are identical to those in Approach 1.

#### Implementation


```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(zero + 1):
            for j in range(one + 1):
                for lastBit in range(2):
                    if i == 0:
                        if lastBit == 0 or j > limit:
                            dp[i][j][lastBit] = 0
                        else:
                            dp[i][j][lastBit] = 1
                    elif j == 0:
                        if lastBit == 1 or i > limit:
                            dp[i][j][lastBit] = 0
                        else:
                            dp[i][j][lastBit] = 1
                    elif lastBit == 0:
                        dp[i][j][lastBit] = dp[i - 1][j][0] + dp[i - 1][j][1]
                        if i > limit:
                            dp[i][j][lastBit] -= dp[i - limit - 1][j][1]
                    else:
                        dp[i][j][lastBit] = dp[i][j - 1][0] + dp[i][j - 1][1]
                        if j > limit:
                            dp[i][j][lastBit] -= dp[i][j - limit - 1][0]
                    dp[i][j][lastBit] %= mod
        return (dp[-1][-1][0] + dp[-1][-1][1]) % mod
```


#### Complexity Analysis

- Time complexity: $O(\textit{zero} \times \textit{one})$.
  
  Each state is computed exactly once, and each transition takes constant time.

- Space complexity: $O(\textit{zero} \times \textit{one})$.

---