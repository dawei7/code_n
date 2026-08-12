# Primonacci - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{100\,000} F(a(n)) \bmod 1234567891011$, where $a(1) = \text{next\_prime}(10^{14})$, $a(n) = \text{next\_prime}(a(n-1))$, and $F(k)$ is the $k$-th Fibonacci number.

### Segmented Sieve & Fast Doubling Fibonacci Recursion:
1. **Segmented Prime Sieve**:
   The $100\,000$-th prime after $10^{14}$ occurs at $\approx 10^{14} + 3.23 \times 10^6$.
   We use a segmented sieve of Eratosthenes over window $[10^{14}+1, 10^{14} + 4 \times 10^6]$ to stream the $100\,000$ primes $a(1) \dots a(100\,000)$.
2. **Fast Doubling Fibonacci Evaluation**:
   For each prime index $p = a(n)$, $F(p) \bmod M$ ($M = 1234567891011$) is computed using the Fast Doubling ladder:
   $$F(2k) = F(k) \cdot (2 F(k+1) - F(k)) \pmod M$$
   $$F(2k+1) = F(k)^2 + F(k+1)^2 \pmod M$$
   in $\mathcal{O}(\log p)$ steps.
3. **Execution**:
   Summing $F(a(n)) \bmod M$ across all $100\,000$ prime indices yields $283988410192$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \cdot \log(\text{start}))$ for $K = 100\,000$ and $\text{start} = 10^{14}$. Runs in $\approx 2.20\text{s}$.
- **Space Complexity:** $\mathcal{O}(W)$ segmented sieve memory for window $W = 4 \times 10^6$.
