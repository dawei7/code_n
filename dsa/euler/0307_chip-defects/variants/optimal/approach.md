# Chip Defects - Optimal Approach

## Algorithm Explanation

Find $p(20\,000, 1\,000\,000)$, the probability that at least one chip has at least $3$ defects when $k = 20\,000$ independent defects are randomly distributed across $n = 1\,000\,000$ chips, rounded to 10 decimal places.

### Complementary Log-Gamma Multinomial Summation:
1. **Safe Complement Event**:
   A configuration is safe (no chip has $\ge 3$ defects) iff every chip contains either $0$, $1$, or $2$ defects.
   Let $i$ be the number of chips with $2$ defects, and $j = k - 2i$ be the number of chips with $1$ defect ($0 \le i \le \lfloor k/2 \rfloor$).
2. **Combinatorial Multinomial Weight**:
   The number of safe defect placements with $i$ double-defect chips and $j$ single-defect chips is:
   $$N_{\text{safe}}(i) = \frac{n!}{i! j! (n - i - j)!} \times \frac{k!}{(2!)^i (1!)^j}$$
3. **Log-Space Evaluation**:
   Dividing by total outcomes $n^k$, the safe probability is evaluated in log-space using `math.lgamma`:
   $$P_{\text{safe}} = \sum_{i=0}^{\lfloor k/2 \rfloor} \exp \left( \ln P(n, i+j) - \ln(i!) - \ln(j!) + \ln(k!) - i \ln 2 - k \ln n \right)$$
4. **Execution**:
   Computing $1 - P_{\text{safe}}$ yields $0.7311720251$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K)$ for $K = 20\,000$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
