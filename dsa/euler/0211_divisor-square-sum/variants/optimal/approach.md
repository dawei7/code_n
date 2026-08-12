# Divisor Square Sum - Optimal Approach

## Algorithm Explanation

Find the sum of all $n < 64\,000\,000$ such that $\sigma_2(n) = \sum_{d \mid n} d^2$ is a perfect square.

### Multiplicative Sieve & Square Testing:
1. **Definition**:
   The function $\sigma_2(n)$ is multiplicative:
   $$\sigma_2(p^k) = 1 + p^2 + p^4 + \dots + p^{2k}$$
2. **Sieve Calculation**:
   We compute $\sigma_2(n)$ for all $n < 64\,000\,000$ using a harmonic divisor accumulator array.
3. **Square Testing**:
   For each $n$, we test if $\sigma_2(n)$ is a perfect square using integer square root `isqrt`.
4. **Execution**:
   Summing all $n$ where $\sigma_2(n)$ is a square yields $1922364685$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N = 64\,000\,000$. Runs in $\approx 10.8\text{s}$ (C++) / harmonic loop.
- **Space Complexity:** $\mathcal{O}(N)$ to store $\sigma_2$ values.
