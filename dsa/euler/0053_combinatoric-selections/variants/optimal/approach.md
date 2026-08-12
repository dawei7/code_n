# Combinatoric Selections - Optimal Approach

## Algorithm Explanation

Find the number of combinations $\binom{n}{r}$ for $1 \le n \le 100$ and $1 \le r \le n$ that exceed $1,000,000$.

### Pascal's Triangle Symmetry Optimization
In row $n$, binomial values $\binom{n}{r}$ increase up to $r = \lfloor \frac{n}{2} \rfloor$ and are symmetric ($\binom{n}{r} = \binom{n}{n-r}$).

1. If $r_0$ is the first index in row $n$ for which $\binom{n}{r_0} > 1,000,000$, then all values $r \in [r_0, n - r_0]$ are also strictly greater than $1,000,000$.
2. The count of such values for row $n$ is simply $n - 2 r_0 + 1$.
3. Sum across rows $n \in [23, 100]$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ where $N = 100$. Evaluates in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
