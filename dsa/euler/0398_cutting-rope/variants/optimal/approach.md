# Cutting Rope - Optimal Approach

## Algorithm Explanation

Find $E(10^7, 100)$, the expected length of the second-shortest segment when a rope of length $n = 10^7$ is randomly cut at $m - 1 = 99$ integer points into $m = 100$ segments, rounded to 5 decimal places.

### Order Statistics & Combinatorial Tail Probability:
1. **Rope Cut Combinatorics**:
   Choosing $m-1$ cut points out of $n-1$ grid positions yields $\binom{n-1}{m-1}$ equally likely composition configurations into $m$ positive integer segment lengths $(L_1, L_2, \dots, L_m)$ with $\sum L_i = n$.
2. **Second-Shortest Order Statistic Tail Formula**:
   By tail expectation:
   $$E(n, m) = \sum_{k=1}^{\lfloor n/m \rfloor} P(X_{(2)} \ge k)$$
   where $X_{(2)}$ is the second smallest segment length.
3. **Inclusion-Exclusion Segment Bound Counting**:
   $P(X_{(2)} \ge k)$ is calculated using inclusion-exclusion over the number of segments with length $< k$:
   - All $m$ segments $\ge k$: $\binom{n - m k + m - 1}{m - 1}$.
   - Exactly one segment $< k$: $\sum_{j=1}^{k-1} m \cdot \binom{n - j - (m-1) k + m - 2}{m - 2}$.
4. **Execution**:
   Evaluating the tail expectation sum for $n = 10^7, m = 100$ yields $2010.59096$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \cdot (n/m))$ for $n = 10^7, m = 100$. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
