# Bézier Curves - Optimal Approach

## Algorithm Explanation

Find the percentage error $100 \times \frac{L - \pi/2}{\pi/2}$ rounded to 10 decimal places, where $L$ is the arc length of the cubic Bézier curve $B(t)$ with control points $P_0(1, 0), P_1(1, v), P_2(v, 1), P_3(0, 1)$ chosen such that the enclosed area equals $\frac{\pi}{4}$.

### Area Integration & Numerical Arc Length:
1. **Control Point Parameter $v$**:
   The parametric equations of the cubic Bézier curve are:
   $$x(t) = (1-t)^3 + 3t(1-t)^2 + 3t^2(1-t)v = (1-t)^2 (1 + 2t + 3t v)$$
   $$y(t) = x(1-t)$$
   Setting the enclosed area $\int_0^1 y(t) x'(t) dt = \frac{\pi}{4}$ determines $v = \frac{32 - 3\pi}{6} \approx 0.55158377$.
2. **Arc Length Integration**:
   The length of the curve is computed via arc length numerical integration:
   $$L = \int_0^1 \sqrt{(x'(t))^2 + (y'(t))^2} dt$$
3. **Percentage Error**:
   $$\text{Error} = 100 \times \frac{L - \frac{\pi}{2}}{\frac{\pi}{2}}$$
4. **Execution**:
   Evaluating the arc length integral yields percentage error $0.0000372091$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ numerical integration. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
