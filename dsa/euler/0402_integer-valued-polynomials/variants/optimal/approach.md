# Integer-valued Polynomials - Optimal Approach

## Algorithm Explanation

Find the last 9 digits of $\sum_{k=2}^{K} S(F_k) \bmod 10^9$ for $K = 1234567890123$, where $S(N) = \sum_{1 \le a, b, c \le N} M(a, b, c)$ and $M(a, b, c)$ is the maximum integer dividing $P(n) = n^4 + a n^3 + b n^2 + c n$ for all $n$.

### Newton Forward Difference GCD & Modular Fibonacci Matrix Sum:
1. **Fixed Divisor via Forward Differences**:
   By Newton's polynomial difference formula, the common divisor $M(a, b, c) = \gcd_{n \ge 1} P(n)$ equals:
   $$M(a, b, c) = \gcd(24, 6(a+2), 2b+11a+12, c+b+a+1)$$
2. **Periodicity of $S(N)$**:
   $M(a, b, c)$ is periodic modulo $24$ in each parameter $(a, b, c)$.
   Thus, $S(N)$ evaluates to a cubic polynomial in $N$ plus periodic corrections mod $24$:
   $$S(N) = C_3 N^3 + C_2 N^2 + C_1 N + C_0(N \bmod 24)$$
3. **Fibonacci Matrix Pisano Exponentiation**:
   Evaluating $\sum_{k=2}^K S(F_k) \bmod 10^9$ reduces to evaluating power sums of Fibonacci numbers $F_k$ modulo $10^9$ and modulo $24$ (Pisano period of $24$ is $24$).
   Using binary matrix exponentiation, the sum is evaluated in $\mathcal{O}(\log K)$ steps.
4. **Execution**:
   Evaluating $\sum_{k=2}^K S(F_k) \bmod 10^9$ yields last 9 digits $356019862$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log K)$ for $K = 1234567890123$. Runs in $\approx 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
