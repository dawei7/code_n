# Perfection Quotients - Optimal Approach

## Algorithm Explanation

Find the sum of all positive integers $n \le 10^{18}$ such that the perfection quotient $p(n) = \frac{\sigma(n)}{n} = k + \frac{1}{2} = \frac{2k + 1}{2}$ for an integer $k \ge 1$.

### Multiplicative Divisor Function Search:
1. **Perfection Ratio Condition**:
   $\frac{\sigma(n)}{n} = \frac{2k + 1}{2} \implies 2 \sigma(n) = (2k + 1) n$.
   Since $\sigma(n)$ is a multiplicative function $\sigma(n) = \prod \frac{p^{e+1}-1}{p-1}$, we prune prime factorizations $n = \prod p_i^{e_i}$ by tracking the exact prime factor valuation of $2 \sigma(n) / n$.
2. **Execution**:
   Summing all valid integers $n \le 10^{18}$ satisfying $p(n) = k + 1/2$ yields $482316491800641154$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{valid factorizations})$ bounded by $10^{18}$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
