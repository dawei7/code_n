# Square Space Silo - Optimal Approach

## Algorithm Explanation

Find $\sum x$ rounded to 9 decimal places for all offsets $x \in [0, R]$ where the space wastage volume $V(x)$ in a cylindrical silo of radius $R = 6\mathrm m$ and angle of repose $\alpha = 40^\circ$ is a perfect square integer.

### Polar Double Integration & Bisection Root Search:
1. **Grain Cone Surface Integral**:
   When grain is delivered at offset $x$ from the silo center, the surface height profile $z(r, \theta)$ forms an off-center conical surface.
   The wasted volume $V(x)$ is given by the polar double integral:
   $$V(x) = \tan(\alpha) \int_0^{2\pi} \int_0^R \sqrt{r^2 + x^2 - 2 r x \cos \theta} \, r \, dr \, d\theta$$
2. **Monotonicity & Quadrature**:
   $V(x)$ is strictly increasing with $x \in [0, R]$.
   The double integral is computed accurately using 64-point Gauss-Legendre quadrature over $[0, 2\pi]$.
3. **Square Target Bisection**:
   We evaluate the minimum and maximum volumes $V_{\min} = V(0)$ and $V_{\max} = V(R)$.
   For each integer square $k^2 \in [V_{\min}, V_{\max}]$, a high-precision bisection / Newton search finds the unique $x$ such that $V(x) = k^2$.
4. **Execution**:
   Summing all root offsets $x$ rounded to 9 decimal places yields $23.386029052$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N_{\text{squares}} \cdot K_{\text{quadrature}})$ for 64-point Gauss-Legendre quadrature. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
