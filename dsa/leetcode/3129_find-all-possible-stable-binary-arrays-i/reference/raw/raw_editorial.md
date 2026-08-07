### Approach: Dynamic Programming

#### Intuition

The problem requires that every subarray of length greater than $\textit{limit}$ in the binary array $\textit{arr}$ contains both 0 and 1. This condition is equivalent to requiring that every subarray of length exactly $\textit{limit} + 1$ contains both 0 and 1. The reader is encouraged to verify why these two statements are equivalent.

We need to construct the binary array $\textit{arr}$ using exactly $\textit{zero}$ zeros and $\textit{one}$ ones.

Let $\textit{dp}_0[i][j]$ denote the number of valid schemes in which we have used $i$ zeros and $j$ ones, and the last placed number is $0$.
Let $\textit{dp}_1[i][j]$ denote the number of valid schemes in which we have used $i$ zeros and $j$ ones, and the last placed number is $1$.

We first analyze the transition for $\textit{dp}_0[i][j]$.

* When $j = 0$ and $i \in [0, \min(\textit{zero}, \textit{limit})]$, we can keep placing $0$s without violating the constraint. Thus, $\textit{dp}_0[i][j] = 1$.

* When $i = 0$, or when $j = 0$ but $i \notin [0, \min(\textit{zero}, \textit{limit})]$, no valid scheme exists. Thus, $\textit{dp}_0[i][j] = 0$.

* When $i > 0$ and $j > 0$, $\textit{dp}_0[i][j]$ can be derived from $\textit{dp}_0[i - 1][j]$ and $\textit{dp}_1[i - 1][j]$:

  * From $\textit{dp}_1[i - 1][j]$: we can always append a $0$ to these schemes, since the previous number was $1$.

  * From $\textit{dp}_0[i - 1][j]$:
    If $i \le \textit{limit}$, appending another $0$ does not violate the constraint.
    If $i > \textit{limit}$, appending $0$ may create more than $\textit{limit}$ consecutive zeros. In this case, we must subtract the invalid schemes where the previous $\textit{limit}$ elements were all zeros. These correspond to $\textit{dp}_1[i - \textit{limit} - 1][j]$.

Therefore, the transition for $\textit{dp}_0[i][j]$ is:

$$
\textit{dp}_0[i][j] =
\begin{cases}
1, & i \in [0, \min(\textit{zero}, \textit{limit})],\ j = 0 \
\textit{dp}_1[i - 1][j] + \textit{dp}_0[i - 1][j] - \textit{dp}_1[i - \textit{limit} - 1][j], & i > \textit{limit},\ j > 0 \
\textit{dp}_1[i - 1][j] + \textit{dp}_0[i - 1][j], & i \le \textit{limit},\ j > 0 \
0, & \text{otherwise}
\end{cases}
$$

Similarly, we derive the transition for $\textit{dp}_1[i][j]$:

$$
\textit{dp}_1[i][j] =
\begin{cases}
1, & i = 0,\ j \in [0, \min(\textit{one}, \textit{limit})] \
\textit{dp}_0[i][j - 1] + \textit{dp}_1[i][j - 1] - \textit{dp}_0[i][j - \textit{limit} - 1], & i > 0,\ j > \textit{limit} \
\textit{dp}_0[i][j - 1] + \textit{dp}_1[i][j - 1], & i > 0,\ j \le \textit{limit} \
0, & \text{otherwise}
\end{cases}
$$

Finally, the total number of stable binary arrays is:

$$
\textit{dp}_0[\textit{zero}][\textit{one}] + \textit{dp}_1[\textit{zero}][\textit{one}]
$$

#### Implementation


```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        mod = int(1e9 + 7)
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                if i > limit:
                    dp[i][j][0] = (
                        dp[i - 1][j][0]
                        + dp[i - 1][j][1]
                        - dp[i - limit - 1][j][1]
                    )
                else:
                    dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
                dp[i][j][0] = (dp[i][j][0] % mod + mod) % mod
                if j > limit:
                    dp[i][j][1] = (
                        dp[i][j - 1][1]
                        + dp[i][j - 1][0]
                        - dp[i][j - limit - 1][0]
                    )
                else:
                    dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0]
                dp[i][j][1] = (dp[i][j][1] % mod + mod) % mod
        return (dp[zero][one][0] + dp[zero][one][1]) % mod
```


#### Complexity Analysis

Let $\textit{zero}$ and $\textit{one}$ denote the number of zeros and ones, respectively.

- Time complexity: $O(\textit{zero} \times \textit{one})$.

- Space complexity: $O(\textit{zero} \times \textit{one})$.

---