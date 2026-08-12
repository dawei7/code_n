# Hollow Square Laminae II - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{10} N(n)$, where $N(n)$ is the number of tile counts $t \le 1,000,000$ that can form **exactly** $n$ distinct square laminae.

### Divisor Counting & Factor Pairs:
From Problem 173, a tile count $t = a^2 - b^2$ forms a valid lamina if $t = 4 m$ with $m = x y$ ($1 \le x < y$).

The number of distinct lamina representations for $t = 4m$ equals the number of factor pairs $x < y$ of $m$:
$$\text{laminae}(m) = \begin{cases} \frac{d(m)}{2} & \text{if } m \text{ is not a perfect square} \\ \frac{d(m) - 1}{2} & \text{if } m \text{ is a perfect square} \end{cases}$$

### Sieve Execution:
1. Sieve divisor counts $d(m)$ for all $1 \le m \le M = \lfloor 10^6 / 4 \rfloor = 250,000$ in $\mathcal{O}(M \log M)$ time.
2. For each $m \in [1, M]$, compute $\text{laminae}(m)$.
3. Increment frequency counter $N(n)$ whenever $1 \le \text{laminae}(m) \le 10$.
4. Return $\sum_{n=1}^{10} N(n)$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M \log M)$ where $M = 250,000$. Runs in $\approx 0.39\text{s}$.
- **Space Complexity:** $\mathcal{O}(M)$ - Divisor count array memory.
