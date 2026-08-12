# Best Approximations - Optimal Approach

## Algorithm Explanation

Find the sum of all denominators of the best rational approximations to $\sqrt{n}$ for denominator bound $D = 10^{12}$, for all non-square integers $1 < n \le 100000$.

### Continued Fractions & Semiconvergents:
1. **Convergents of $\sqrt{n}$**:
   The continued fraction expansion of $\sqrt{n} = [a_0; a_1, a_2, \dots]$ generates convergents $\frac{p_k}{q_k}$ satisfying:
   $$p_k = a_k p_{k-1} + p_{k-2}, \quad q_k = a_k q_{k-1} + q_{k-2}$$
   Every best rational approximation to $\sqrt{n}$ is either a convergent or a semiconvergent.
2. **Semiconvergent Comparison**:
   Iterate convergents until $q_{k+1} > D$.
   The largest possible semiconvergent with denominator $\le D$ uses coefficient:
   $$a_{\max} = \left\lfloor \frac{D - q_{k-1}}{q_k} \right\rfloor$$
   forming $\frac{p_{\text{semi}}}{q_{\text{semi}}} = \frac{p_{k-1} + a_{\max} p_k}{q_{k-1} + a_{\max} q_k}$.
3. **Distance Check**:
   Compare $\left|\frac{p_k}{q_k} - \sqrt{n}\right|$ against $\left|\frac{p_{\text{semi}}}{q_{\text{semi}}} - \sqrt{n}\right|$ using $100$-digit precision arithmetic.
   The closer fraction yields the optimal denominator.
4. **Summation**:
   Summing denominators over all non-square $n \le 100,000$ yields $57,060,635,927,998,347$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log D)$ where $N = 100,000$ and $D = 10^{12}$. Runs in $\approx 1.5\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - High-precision scalar variables.
