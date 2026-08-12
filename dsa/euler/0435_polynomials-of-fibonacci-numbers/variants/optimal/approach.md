# Polynomials of Fibonacci Numbers - Optimal Approach

## Algorithm Explanation

Find $\sum_{x=0}^{100} F_n(x) \bmod 15!$ for $n = 10^{15}$, where $F_n(x) = \sum_{i=0}^n f_i x^i$ and $f_i$ is the $i$-th Fibonacci number.

### Closed-Form Generating Function & Matrix Exponentiation:
1. **Fibonacci Polynomial Closed-Form**:
   Multiplying $F_n(x)$ by $1 - x - x^2$ yields the closed-form relation:
   $$(1 - x - x^2) F_n(x) = x - f_{n+1} x^{n+1} - f_n x^{n+2}$$
2. **Matrix Binary Exponentiation**:
   For $n = 10^{15}$, $f_n \bmod M$ and $f_{n+1} \bmod M$ (and powers $x^n \bmod M$) are computed in $\mathcal{O}(\log n)$ time using $3 \times 3$ matrix binary exponentiation.
3. **Modular Division & CRT**:
   For values of $x$ where $\gcd(1 - x - x^2, 15!) > 1$, we evaluate the partial sum matrix directly modulo $15! \cdot |1 - x - x^2|$ before dividing by $1 - x - x^2$.
4. **Execution**:
   Summing $F_{10^{15}}(x) \bmod 15!$ for $x = 0 \dots 100$ yields $252541322550$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(X \log n)$ for $X = 100$ and $n = 10^{15}$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
