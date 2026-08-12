# Squarefree Binomial Coefficients - Optimal Approach

## Algorithm Explanation

Find the sum of distinct squarefree numbers in the first $51$ rows ($n = 0 \dots 50$) of Pascal's triangle.

### Kummer's Bound & Divisibility Test:
1. **Prime Power Limit**:
   For any $n \le 50$, a prime square $p^2$ can divide $\binom{n}{k}$ only if $p \le 50$. For any prime $p > 50$, $p^2 > 2500 > 50$, so $p^2$ can never divide any binomial coefficient in the first $51$ rows.
2. **Primes $\le 50$**:
   We only need to test divisibility against $p^2$ for the $15$ primes $p \le 50$.
3. **Distinct Set Filtering**:
   Collect all distinct values of $\binom{n}{k}$ for $0 \le n \le 50$, filter out any divisible by $p^2$ for $p \le 50$, and sum the remaining values.
4. **Execution**:
   Summing the distinct squarefree values yields $34029210557338$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R^2 \cdot \pi(R))$ where $R = 51$. Runs in $\approx 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(R^2)$ to store distinct numbers in the set.
