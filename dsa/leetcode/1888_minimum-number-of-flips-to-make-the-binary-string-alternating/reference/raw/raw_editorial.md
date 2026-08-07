### Approach: Analysis + Prefix Sum + Suffix Sum

#### Intuition

**Hint $1$**

We can schedule all type $2$ operations before type $1$ operations.

**Hint $1$ Explanation**

Type $2$ operations flip any character, while type $1$ operations only change the relative order of characters without altering their values. Since type $1$ operations do not modify character values, we can first perform all necessary type $2$ operations to fix the characters, and then use type $1$ operations to adjust their positions. Therefore, without loss of generality, we may assume that all type $2$ operations are performed first.

**Hint $2$**

Let the length of the string $s$ be $n$.

If $n$ is even, then after all type $2$ operations are completed, $s$ must already be an alternating string.

**Hint $2$ Explanation**

When $n$ is even, an alternating string can only be of the form
$0101 \cdots 01$ or $1010 \cdots 10$.

Performing operation type $1$ on either of these strings will transform it into the other.

Since operation type $1$ is reversible and does not change character values, an alternating string can only be obtained from another alternating string using operation type $1$. Therefore, after completing all type $2$ operations, the string $s$ must already be alternating.

**Hint $3$**

If $n$ is odd, then an alternating string must be of the form
$0101 \cdots 010$ or $1010 \cdots 101$.

First, consider the pattern $0101 \cdots 010$. After all type $2$ operations are completed, the string $s$ can be one of the following:

* $s$ is already $0101 \cdots 010$;
* $s$ is formed by concatenating two alternating strings, such as
  $01 \cdots 010 \mid 01 \cdots 01$, or
  $10 \cdots 10 \mid 01 \cdots 010$.

Here, the vertical bar $\mid$ represents the effect of a type $1$ operation, where the characters to the left of the bar are moved to the end of the string. After such a rotation, the final string becomes $0101 \cdots 010$.

Therefore, $s$ is either an alternating string itself, or it is formed by concatenating two alternating strings where the left part ends with $0$ and the right part starts with $0$.

Similarly, if we consider the pattern $1010 \cdots 101$, then $s$ is either that pattern itself, or it is formed by concatenating two alternating strings where the left part ends with $1$ and the right part starts with $1$.

Now we define the dynamic programming states.

Let $\textit{pre}[i][j]$ denote the minimum number of type $2$ operations required to transform the prefix $s[0..i]$ into an alternating string ending with digit $j$, where $j \in {0,1}$. According to this definition, it satisfies the recurrence relation:

$$
\begin{cases}
\textit{pre}[i][0] = \textit{pre}[i-1][1] + \mathbb{I}(s[i], 1) \
\textit{pre}[i][1] = \textit{pre}[i-1][0] + \mathbb{I}(s[i], 0)
\end{cases}
$$

Here, $\mathbb{I}(x, y)$ is the indicator function, which equals $1$ if $x = y$, and $0$ otherwise.

For example, $\mathbb{I}(s[i], 1)$ means that if $s[i] = 1$, we must flip it to $0$ using a type $2$ operation; otherwise, no operation is needed.

Similarly, let $\textit{suf}[i][j]$ denote the minimum number of type $2$ operations required to transform the suffix $s[i..n-1]$ into an alternating string starting with digit $j$. It satisfies the recurrence relation:

$$
\begin{cases}
\textit{suf}[i][0] = \textit{suf}[i+1][1] + \mathbb{I}(s[i], 1) \
\textit{suf}[i][1] = \textit{suf}[i+1][0] + \mathbb{I}(s[i], 0)
\end{cases}
$$

After computing the arrays $\textit{pre}$ and $\textit{suf}$:

* One possible answer is
  $\textit{pre}[n-1][0]$ or $\textit{pre}[n-1][1]$,
  which corresponds to transforming the entire string into an alternating string.

* If $n$ is odd, another possibility is splitting the string into two alternating parts. In that case, we consider
  $\textit{pre}[i][0] + \textit{suf}[i+1][0]$ and
  $\textit{pre}[i][1] + \textit{suf}[i+1][1]$
  for all valid $i$.

The minimum among all these values is the minimum number of type $2$ operations required.

> If $n$ is even, we only need to compute $\textit{pre}$. Computing $\textit{suf}$ is unnecessary.
#### Implementation


```python
class Solution:
    def minFlips(self, s: str) -> int:
        # Characteristic function
        I = lambda ch, x: int(ord(ch) - ord("0") == x)

        n = len(s)
        pre = [[0, 0] for _ in range(n)]
        # Note the boundary case when i=0
        for i in range(n):
            pre[i][0] = (0 if i == 0 else pre[i - 1][1]) + I(s[i], 1)
            pre[i][1] = (0 if i == 0 else pre[i - 1][0]) + I(s[i], 0)

        ans = min(pre[n - 1][0], pre[n - 1][1])
        if n % 2 == 1:
            # If n is an odd number, it is also necessary to calculate suf
            suf = [[0, 0] for _ in range(n)]
            # Note the boundary case when i = n - 1
            for i in range(n - 1, -1, -1):
                suf[i][0] = (0 if i == n - 1 else suf[i + 1][1]) + I(s[i], 1)
                suf[i][1] = (0 if i == n - 1 else suf[i + 1][0]) + I(s[i], 0)

            for i in range(n - 1):
                ans = min(ans, pre[i][0] + suf[i + 1][0])
                ans = min(ans, pre[i][1] + suf[i + 1][1])

        return ans
```


#### Complexity Analysis

Let $n$ be the length of the string $s$.

- Time complexity: $O(n)$.

- Space complexity: $O(n)$.
  
  This space is required for the arrays $\textit{pre}$ and $\textit{suf}$. Although the space complexity can be optimized to $O(1)$, doing so makes the implementation less intuitive. Therefore, this solution does not present the space-optimized version.

---