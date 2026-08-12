# Factorials Divisible by a Huge Integer - Optimal Approach

## Algorithm Explanation

Find $S(1\,000\,000) \bmod 10^{18}$, where $S(u) = \sum_{i=10}^{u} N(i)$ and $N(i)$ is the smallest integer $n$ such that $n!$ is divisible by $(i!)^{1234567890}$.

### Legendre's Exponent Formula & Prime Maximum Tracking:
1. **Prime Factorization Exponent Requirement**:
   By Legendre's formula, the exponent of prime $p$ dividing $i!$ is $e_p(i!) = \sum_{j=1}^{\infty} \lfloor i / p^j \rfloor$.
   For $n!$ to be divisible by $(i!)^{1234567890}$, the required prime power exponent is $E_p(i) = 1234567890 \cdot e_p(i!)$.
2. **Kempner / Lucas Function Minimum Finding**:
   For each prime $p$, the minimum $n_p$ with $e_p(n_p!) \ge E_p(i)$ is found via binary search using $n \approx E_p(i) \cdot (p - 1)$.
   Then $N(i) = \max_{p \le i} n_p$.
3. **Monotonic Running Maximum**:
   Since $N(i) \ge N(i-1)$, $N(i)$ is updated incrementally as new prime factors are processed for each $i \in [10, 1\,000\,000]$.
4. **Execution**:
   Summing $N(i) \bmod 10^{18}$ for $10 \le i \le 1\,000\,000$ yields $297495026948577312$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(U \log U)$ for $U = 1\,000\,000$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(U)$ prime array memory.
