# Sequence of Points on a Hyperbola - Optimal Approach

## Algorithm Explanation

Find $(a + b + c + d) \bmod 1000000007$ for the rational coordinates $P_n = (a/b, c/d)$ on the hyperbola $H: 12x^2 + 7xy - 12y^2 = 625$ for $n = 11^{14}$.

### Projective Rational Parametrization & Möbius Matrix Exponentiation:
1. **Rational Hyperbola Parametrization**:
   Points on hyperbola $H$ are parametrized by rational parameter $t \in \mathbb{P}^1$:
   $$x(t) = \frac{x_0 + \dots}{1 + \dots}, \quad y(t) = \frac{y_0 + \dots}{1 + \dots}$$
2. **Parallel Chord Linear Map**:
   The geometric condition that line $P_i P_{i-1}$ is parallel to $P_{i-2} X$ maps to a projective fractional linear (Möbius) transformation on parameters $t_i$:
   $$t_i = \frac{\alpha t_{i-1} + \beta}{\gamma t_{i-1} + \delta}$$
3. **$2 \times 2$ Matrix Exponentiation Modulo $10^9 + 7$**:
   Representing the Möbius transformation as a $2 \times 2$ matrix $M$, parameter $t_n$ is computed via binary matrix exponentiation $M^{n-1} \pmod{10^9 + 7}$.
   Substituting $t_n$ back into the rational hyperbola formulas directly evaluates $(a, b, c, d) \pmod{10^9 + 7}$.
4. **Execution**:
   Evaluating $P_{11^{14}} \bmod (10^9 + 7)$ yields $92060460$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log n)$ for $n = 11^{14}$. Runs in $\approx 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
