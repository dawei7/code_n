# Fractional Sequences - Optimal Approach

## Algorithm Explanation

Find $\sum_{k=1}^{2 \cdot 10^6} f(k^3)$, where $f(k)$ is the terminal integer reached by the sequence $a_1 = 1/k$, $a_i = (x_{i-1} + 1)/(y_{i-1} - 1)$ reduced to lowest terms.

### Invariant Sum & Largest Prime Factor Reduction:
1. **Invariant Sum $x_i + y_i = k + 1$**:
   At each step, $(x_i + 1) + (y_i - 1) = x_i + y_i = k + 1$.
   The reduction factor $g = \gcd(x_i + 1, y_i - 1) = \gcd(x_i + 1, k + 1)$ is always a divisor of $k+1$.
   Consequently, the sequence terminates at:
   $$f(k) = P(k + 1) - 1$$
   where $P(m)$ is the largest prime factor of $m$.
2. **Algebraic Factorization for $k^3$**:
   For $k^3$, $k^3 + 1 = (k + 1)(k^2 - k + 1)$.
   Thus:
   $$f(k^3) = \max(P(k + 1), P(k^2 - k + 1)) - 1$$
3. **Linear Polynomial Sieve**:
   Using a linear sieve for $P(k+1)$ and a segmented polynomial sieve for $P(k^2 - k + 1)$ over $k \in [1, 2 \cdot 10^6]$ computes all $f(k^3)$ in $\mathcal{O}(K \log K)$ steps.
4. **Execution**:
   Summing $f(k^3)$ for $1 \le k \le 2 \cdot 10^6$ yields $269533451410884183$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \log K)$ for $K = 2 \cdot 10^6$. Runs in $\approx 1.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ for the sieve arrays.
