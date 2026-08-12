# Eating Pie - Optimal Approach

## Algorithm Explanation

Find $E(40)$, the expected number of times Jeff repeats the pie eating procedure until the remaining pie fraction is less than $F = 1/40$, rounded to 10 decimal places.

### Continuous Distribution & Volterra Integral Equation:
1. **Remaining Fraction Probability Density**:
   Making two independent uniform random cuts on remaining pie fraction $x$ divides $x$ into three parts $X_1, X_2, X_3$.
   The remaining pie piece is $X_3 = x (1 - U_1 - U_2)$.
   The ratio $t = X_3 / x \in (0, 1)$ follows the density distribution $f(t) = 2(1-t)$.
2. **Volterra Renewal Integral Equation**:
   The expected procedure count $E(x)$ satisfies:
   $$E(x) = 1 + \int_{F/x}^1 2(1-t) E(t x) dt$$
3. **Differential Equation Closed-Form**:
   Differentiating the integral equation yields a linear ordinary differential equation whose exact closed-form solution is:
   $$E(x) = \frac{7}{9} + \frac{2}{9 x^3} + \frac{2}{3} \ln x$$
4. **Execution**:
   Evaluating $E(40) = \frac{7}{9} + \frac{2}{9 \cdot 40^3} + \frac{2}{3} \ln(40)$ yields $3.2370342194$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ logarithmic formula. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
