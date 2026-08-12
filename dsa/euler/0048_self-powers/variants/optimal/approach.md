# Self Powers - Optimal Approach

## Algorithm Explanation

Find the last $10$ digits of the sum $\sum_{i=1}^{1000} i^i$.

Using modular arithmetic with modulus $M = 10^{10}$:
1. For each integer $i \in [1, 1000]$, compute $(i^i \bmod M)$ using binary exponentiation `pow(i, i, mod)`.
2. Accumulate the modular terms.
3. Take the final sum modulo $M$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N = 1000$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
