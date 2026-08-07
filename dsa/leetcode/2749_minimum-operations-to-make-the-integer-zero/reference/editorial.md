### Approach: Enumeration

#### Intuition

We can start enumerating the values of the operand $k$ from $1$, and as we enumerate each number, we check whether the current number of operations can make $\textit{num}_1$ equal to $0$. If so, we return the current $k$ value.

Assuming the operation is performed $k$ times, this is equivalent to subtracting $\textit{num}_2$, $k$ times, from $\textit{num}_1$, and then determining whether the remainder can be expressed as the sum of $k$ powers of two (not necessarily distinct). Let $x = \textit{num}_1 - k \times \textit{num}_2$. We only need to determine whether $x$ can be expressed as the sum of $k$ powers of two.

Let $f(x)$ be the number of 1s in the binary representation of $x$. For $k$ to be valid, the following conditions must be met:

* $k \le x$, this is the upper limit of $k$. When $k > x$, even $k$ copies of $2^0$ are not sufficient.
* $k \ge f(x)$, this is the lower bound of $k$. We need at least $f(x)$ powers of two to form $x$. Of course, we can use more than $f(x)$ powers of two, since two $2^{i-1}$ can combine to form $2^i$.

The value of $k$ is valid if and only if $f(x) \le k \le x$.

Next, observe how $x$ changes as $k$ increases. When $k = 0$, we have $x > k$, and $x$ decreases monotonically as $k$ increases. Therefore, if $x < k$ ever occurs, the inequality will continue to hold as $k$ increases further. Thus, when $x < k$ occurs for the first time, we can conclude that the problem has no solution and return $-1$ immediately.

#### Implementation

```python
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1
```

#### Complexity Analysis

- Time complexity: $O(\log \textit{num}_1)$

    Each iteration increases $k$ by $1$ while simultaneously decreasing $x = \textit{num}_1 - k \times \textit{num}_2$. Since $x$ decreases monotonically with $k$, the number of iterations is bounded by how quickly $x$ becomes smaller than $k$. This transition occurs at most on the order of $\log(\textit{num}_1)$, because representing $x$ in terms of powers of two relates directly to its binary length. Therefore, the overall time complexity is $O(\log \textit{num}_1)$.

- Space complexity: $O(1)$.

---