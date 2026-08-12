# 2011 Nines - Optimal Approach

## Algorithm Explanation

Find $\sum N(p, q)$ for all positive integer pairs $1 \le p < q$ with $p + q \le 2011$, where $N(p, q)$ is the minimum $n$ such that the fractional part of $(\sqrt{p} + \sqrt{q})^{2n}$ begins with at least $2011$ consecutive nines.

### Conjugate Error Logarithmic Ceiling Formula:
1. **Algebraic Conjugate Identity**:
   Consider the algebraic conjugate $(\sqrt{q} - \sqrt{p}) > 0$.
   The sum $(\sqrt{q} + \sqrt{p})^{2n} + (\sqrt{q} - \sqrt{p})^{2n}$ is an integer $I_{2n}$.
   Thus, the fractional part of $(\sqrt{q} + \sqrt{p})^{2n}$ is $1 - (\sqrt{q} - \sqrt{p})^{2n}$.
2. **Convergence & Nines Condition**:
   The fractional part approaches $1$ iff $\sqrt{q} - \sqrt{p} < 1$.
   The number of initial nines equals $2011$ when $(\sqrt{q} - \sqrt{p})^{2n} \le 10^{-2011}$.
   Taking $\log_{10}$ yields the exact closed form:
   $$n \ge \frac{2011}{-2 \log_{10}(\sqrt{q} - \sqrt{p})} \implies N(p, q) = \left\lceil \frac{2011}{-2 \log_{10}(\sqrt{q} - \sqrt{p})} \right\rceil$$
3. **Execution**:
   Summing $N(p, q)$ for all valid pairs $p + q \le 2011$ with $\sqrt{q} - \sqrt{p} < 1$ yields $709313889$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L^2)$ for $L = 2011$. Runs in $\approx 0.17\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
