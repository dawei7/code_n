# Quadratic Primes - Optimal Approach

## Algorithm Explanation

Find coefficients $|a| < 1000$ and $|b| \le 1000$ such that $P(n) = n^2 + an + b$ produces the maximum consecutive primes starting at $n = 0$.

### Mathematical Constraints
1. **$b$ must be Prime**: At $n = 0$, $P(0) = b$. Thus $b$ must be a positive prime $2 \le b \le 1000$.
2. **$1 + a + b$ must be Prime**: At $n = 1$, $P(1) = 1 + a + b$ must be prime.

### Search Strategy:
- Pre-generate primes $b \in [2, 1000]$.
- For each prime $b$ and integer $a \in (-1000, 1000)$, increment $n = 0, 1, 2 \dots$ while $P(n)$ is prime.
- Track maximum $n$ and output product $a \cdot b$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(A \cdot \pi(B) \cdot N)$ where $A = 2000, \pi(B) = 168$ primes. Runs in under $0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory for prime testing.
