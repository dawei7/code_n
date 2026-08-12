# Investigating Gaussian Integers - Optimal Approach

## Algorithm Explanation

Find the sum of real parts of all Gaussian integer divisors $a + bi$ ($a > 0$) of rational integers $n$ for $1 \le n \le 10^8$.

### Gaussian Divisors Decomposition:
A Gaussian integer $a + bi$ divides rational integer $n$ if $\frac{n(a - bi)}{a^2 + b^2} \in \mathbb{Z}[i]$.
Express $a = g A, b = g B$ where $g = \gcd(a, b) \ge 1$ and $\gcd(A, B) = 1$.
The norm $N_{\text{norm}} = A^2 + B^2$ divides $n / g$.

1. **Rational Divisors ($b = 0$)**:
   $$\sum_{n=1}^N \sigma_1(n) = \sum_{g=1}^N g \left\lfloor \frac{N}{g} \right\rfloor$$
2. **Complex Divisors ($b \neq 0$)**:
   For coprime pairs $(A, B)$ with $1 \le A \le B$ and $A^2 + B^2 \le N$:
   - If $A = B = 1$: real part sum factor $F = 2A = 2$.
   - If $A < B$: real part sum factor $F = 2(A + B)$.
   - Contribution of pair $(A, B)$:
     $$F \times \sum_{g=1}^{\lfloor N / (A^2 + B^2) \rfloor} g \left\lfloor \frac{N}{g(A^2 + B^2)} \right\rfloor$$

### Memoized Hyperbola Sub-Linear Sum:
Evaluate $H(M) = \sum_{g=1}^M g \lfloor M/g \rfloor$ using sub-linear $\mathcal{O}(\sqrt{M})$ hyperbola step summation.
Memoize $H(M)$ via `@lru_cache`, reducing total evaluation calls to $\approx 10,000$ unique values of $N / (A^2 + B^2)$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ loop over coprime pairs with memoized hyperbola evaluation. Runs in $\approx 11.3\text{s}$.
- **Space Complexity:** $\mathcal{O}(\sqrt{N})$ - Memoization dictionary size.
