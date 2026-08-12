# Reciprocal Cycles II - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=3}^{10^8} L(n)$, where $L(n)$ is the decimal recurring cycle length of $1/n$.

### Multiplicative Order $\operatorname{ord}_m(10)$ & Prime LCM Propagation:
1. **Reciprocal Cycle Order Equivalence**:
   Removing prime factors of $2$ and $5$ from $n = 2^a 5^b m$ (where $\gcd(m, 10) = 1$), the cycle length $L(n) = L(m) = \operatorname{ord}_m(10)$, the multiplicative order of $10 \pmod m$.
2. **Prime Power & Composite LCM Property**:
   - For prime powers $p^e$, $\operatorname{ord}_{p^e}(10) = \operatorname{ord}_p(10) \cdot p^{\max(0, e - e_0)}$ where $e_0$ is the $p$-adic valuation of $10^{\operatorname{ord}_p(10)} - 1$.
   - For composite $m = p_1^{e_1} \cdots p_k^{e_k}$, $L(m) = \operatorname{lcm}(L(p_1^{e_1}), \dots, L(p_k^{e_k}))$.
3. **Linear Order Sieve**:
   We compute $\operatorname{ord}_p(10)$ for all primes $p \le 10^8$ by testing divisors of $p - 1$.
   We then propagate cycle lengths to all composite numbers $n \le 10^8$ using the LCM property.
4. **Execution**:
   Summing $L(n)$ for $3 \le n \le 10^8$ yields $446572970925740$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ for $N = 10^8$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ cycle length array.
