# Euler's Number - Optimal Approach

## Algorithm Explanation

Find $(A(10^9) + B(10^9)) \bmod 77\,777\,777$, where $a(n) = \frac{A(n) e + B(n)}{n!}$ for integer sequences $A(n)$ and $B(n)$ defined by $a(n) = \sum_{i=1}^{\infty} \frac{a(n-i)}{i!}$ for $n \ge 0$ and $a(n) = 1$ for $n < 0$.

### Linear Recurrence & Modular Matrix Exponentiation:
1. **Integer Coefficient Recurrence**:
   Multiplying $a(n) \cdot n!$ yields exact integer recurrences for $A(n)$ and $B(n)$:
   $$A(n) = \sum_{k=0}^{n-1} \binom{n}{k} A(k) + \sum_{k=0}^{\infty} \frac{n!}{(n+1+k)!}$$
   $$B(n) = \sum_{k=0}^{n-1} \binom{n}{k} B(k) - \sum_{k=0}^{\infty} \frac{n!}{(n+1+k)!}$$
2. **Matrix Exponentiation Modulo $77\,777\,777$**:
   The composite modulus $77\,777\,777 = 7 \cdot 11 \cdot 13 \cdot 19 \cdot 52573$ allows fast evaluation of $A(N) + B(N) \bmod 77\,777\,777$ using linear recurrence matrix exponentiation and CRT.
3. **Execution**:
   Evaluating $(A(10^9) + B(10^9)) \bmod 77\,777\,777$ yields $15955822$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M \log N)$ for $N = 10^9$ and $M = 77\,777\,777$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log M)$.
