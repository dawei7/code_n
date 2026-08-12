# Diophantine Reciprocals I - Optimal Approach

## Algorithm Explanation

Find the least positive integer $n$ for which the number of distinct positive integer solutions $(x, y)$ to $\frac{1}{x} + \frac{1}{y} = \frac{1}{n}$ exceeds $1000$.

### Algebraic Factorization:
$$\frac{1}{x} + \frac{1}{y} = \frac{1}{n} \implies n(x + y) = xy \implies (x - n)(y - n) = n^2$$

Let $u = x - n$ and $v = y - n$. Every factor pair $(u, v)$ with $u \cdot v = n^2$ produces a valid positive integer solution $(x, y) = (n + u, n + v)$.

### Divisor Function Formula:
For $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$, $n^2 = p_1^{2e_1} p_2^{2e_2} \cdots p_k^{2e_k}$.
The total number of divisors of $n^2$ is:
$$d(n^2) = (2e_1 + 1)(2e_2 + 1) \cdots (2e_k + 1)$$

Since $(u, v)$ and $(v, u)$ represent symmetric pairs (with $u = v = n$ when $x = y = 2n$), the number of distinct unordered solutions is:
$$\text{Solutions}(n) = \frac{d(n^2) + 1}{2}$$

Increment $n = 1, 2 \dots$, factor $n$, evaluate $\frac{d(n^2) + 1}{2}$, and return $n$ when solutions exceed $1000$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \sqrt{N})$ where $N = 180180$. Runs in $< 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
