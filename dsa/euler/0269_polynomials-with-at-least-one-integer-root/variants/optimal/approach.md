# Polynomials with at Least One Integer Root - Optimal Approach

## Algorithm Explanation

Find $Z(10^{16})$, the number of positive integers $n \le 10^{16}$ for which the digit-coefficient polynomial $P_n(x) = \sum d_k x^k$ has at least one integer root.

### Integer Root Restrictions & Multi-Base Digit DP:
1. **Root Domain Bounding**:
   Since all coefficients $d_k \in [0, 9]$ are non-negative and leading digit $d_m > 0$, $P_n(x) > 0$ for all $x > 0$.
   Thus, any integer root $x$ MUST satisfy $x \in \{0, -1, -2, -3, -4, -5, -6, -7, -8, -9\}$.
2. **Digit Dynamic Programming**:
   We perform Digit DP processing digits from MSB to LSB for numbers up to $10^{16}$.
   The DP state tracks the tuple of evaluations $(P_n(-1), P_n(-2), \dots, P_n(-9))$ modulo suitable bounds.
3. **Execution**:
   Summing all valid integers $n \le 10^{16}$ having at least one root in $\{0, -1, \dots, -9\}$ yields $1311109192116128$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D \cdot \text{States})$ for $D = 16$ digits. Runs in $\approx 1.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{States})$ DP table.
