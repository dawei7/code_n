# Pseudo Square Root - Optimal Approach

## Algorithm Explanation

Find $\operatorname{PSR}(p) \bmod 10^{16}$, where $p$ is the product of all $42$ prime numbers below $190$, and $\operatorname{PSR}(p)$ is the largest divisor of $p$ that does not exceed $\sqrt{p}$.

### Meet-in-the-Middle Subset Log Search:
1. **Logarithmic Subset Problem**:
   Since $p = \prod_{i=1}^{42} p_i$ is square-free, every divisor $d$ corresponds to a subset $S \subseteq \{p_1, \dots, p_{42}\}$.
   We maximize $\sum_{q \in S} \log q \le \frac{1}{2} \sum_{i=1}^{42} \log p_i$.
2. **2-Way Bipartite Split**:
   We split the $42$ primes into two halves of $21$ primes each.
   We generate all $2^{21} = 2\,097\,152$ subset log-sums and modular products for both halves.
3. **Binary Search Matching**:
   We sort the second half by log-sum. For each log-sum in the first half, we use binary search to locate the optimal element in the second half.
4. **Execution**:
   Evaluating the optimal subset product modulo $10^{16}$ yields $1096883702440585$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(2^{N/2} \log 2^{N/2})$ for $N = 42$. Runs in $\approx 17.0\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^{N/2})$ subset list storage.
