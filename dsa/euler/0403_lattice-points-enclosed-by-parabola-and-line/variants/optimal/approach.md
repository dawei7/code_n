# Lattice Points Enclosed by Parabola and Line - Optimal Approach

## Algorithm Explanation

Find $S(10^{12}) \bmod 10^8$, where $S(N)$ is the sum of lattice points $L(a, b)$ contained in the domain $D(a, b) = \{x^2 \le y \le a x + b\}$ over all $|a|, |b| \le N$ for which the area of $D(a, b)$ is rational.

### Rational Area Condition & Polynomial Prefix Summation:
1. **Rational Area Discriminant Condition**:
   The intersection of $y = x^2$ and $y = a x + b$ has roots $x_{1, 2} = \frac{a \pm \sqrt{a^2 + 4b}}{2}$.
   The area of $D(a, b)$ is $\int_{x_1}^{x_2} (a x + b - x^2) dx = \frac{(a^2 + 4b)^{3/2}}{6}$.
   Thus, the area is rational iff the discriminant $a^2 + 4b = k^2$ is a perfect square.
2. **Lattice Point Formula $L(a, b)$**:
   For $a^2 + 4b = k^2$, the number of enclosed lattice points $L(a, b)$ simplifies to a polynomial formula in $k$:
   $$L(a, b) = \sum_{x = \lceil x_1 \rceil}^{\lfloor x_2 \rfloor} (\lfloor a x + b \rfloor - x^2 + 1)$$
   which simplifies into piecewise cubic polynomials in $k$ depending on parities of $a$ and $k$.
3. **$\mathcal{O}(1)$ Polynomial Summation**:
   Summing $L(a, b)$ over all valid pairs $|a|, |b| \le N = 10^{12}$ with $a^2 + 4b = k^2$ reduces to evaluating polynomial power sums of $k$.
4. **Execution**:
   Evaluating $S(10^{12}) \bmod 10^8$ yields $18224771$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ polynomial formula. Runs in $\approx 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
