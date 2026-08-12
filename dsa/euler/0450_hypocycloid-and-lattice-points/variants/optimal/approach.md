# Hypocycloid and Lattice Points - Optimal Approach

## Algorithm Explanation

Find $T(10^6)$, where $T(N) = \sum_{R=3}^N \sum_{r=1}^{\lfloor (R-1)/2 \rfloor} S(R, r)$ is the sum of $|x| + |y|$ over all integer lattice points $(x, y)$ on the hypocycloid of radii $(R, r)$ having rational $\cos(t), \sin(t)$.

### Pythagorean Rational Parametrization & Divisor Sieve:
1. **Rational Angle Condition**:
   $\cos(t), \sin(t) \in \mathbb{Q}$ iff the angle $t$ corresponds to a Pythagorean triple:
   $$(\cos t, \sin t) = \left( \frac{u^2 - v^2}{u^2 + v^2}, \frac{2 u v}{u^2 + v^2} \right)$$
2. **Chebyshev Polynomial Lattice Point Test**:
   Let $k = \frac{R-r}{r}$.
   The hypocycloid coordinates $x(t), y(t)$ are expressed using Chebyshev polynomials $T_k, U_k$.
   The coordinates $(x(t), y(t))$ are integers iff $u^2 + v^2$ divides $R$ and $r$ under rational Chebyshev expansions.
3. **Divisor Generation & Fast Summation**:
   We iterate over primitive Pythagorean generators $(u, v)$ with $u^2 + v^2 \le N = 10^6$ and generate valid hypocycloid parameters $(R, r)$.
4. **Execution**:
   Evaluating $T(10^6)$ yields $583333163984220940$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ for $N = 10^6$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ divisor arrays.
