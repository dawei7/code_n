# Pythagorean Odds - Optimal Approach

## Algorithm Explanation

Find the expected value of Albert's total score over $10^5$ turns with $k = 1, 2, \dots, 10^5$, rounded to $5$ decimal places. In turn $k$, $a, b \in [0, 1]$ are uniform random variables, scoring $k$ points if $\lfloor \sqrt{(k a + 1)^2 + (k b + 1)^2} + 0.5 \rfloor = k$.

### Continuous Integral Geometry on Circular Annulus:
1. **Coordinate Substitution**:
   Setting $x = k a + 1$ and $y = k b + 1$, the domain $a, b \in [0, 1]$ maps to $(x, y) \in [1, k+1]^2$ with area scaling $1 / k^2$.
2. **Annular Region Area**:
   The rounding condition is satisfied iff $k - 0.5 \le \sqrt{x^2 + y^2} \le k + 0.5$.
   The probability $P(k)$ is the area of this concentric annulus intersected with $[1, k+1]^2$ divided by $k^2$.
3. **Exact Integration**:
   The area of $x^2 + y^2 \le R^2$ in $x \ge 1, y \ge 1$ is evaluated using the antiderivative:
   $$\int \sqrt{R^2 - x^2} \, dx = \frac{1}{2} \left( x \sqrt{R^2 - x^2} + R^2 \arctan \frac{x}{\sqrt{R^2 - x^2}} \right)$$
4. **Execution**:
   Summing $k \cdot P(k)$ over $k = 1 \dots 10^5$ yields $157055.80999$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 10^5$. Runs in $\approx 0.14\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
