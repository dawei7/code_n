# Highly Divisible Triangular Number - Optimal Approach

## Algorithm Explanation

A triangle number is $T_n = \frac{n(n + 1)}{2}$.

Since $\text{GCD}(n, n + 1) = 1$, the terms $\frac{n}{2}$ and $n+1$ (or $n$ and $\frac{n+1}{2}$) are **coprime**.

The divisor function $d(x)$ is **multiplicative**:
$$d(T_n) = d\left(\frac{n}{2}\right) \times d(n+1) \quad \text{if } n \text{ is even}$$
$$d(T_n) = d(n) \times d\left(\frac{n+1}{2}\right) \quad \text{if } n \text{ is odd}$$

By computing $d(x)$ via prime factorization on small integers $n \sim 10^4$ rather than factorizing large numbers $T_n \sim 10^8$, execution completes in under $0.05\text{s}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \sqrt{N})$ where $N \approx 12500$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
