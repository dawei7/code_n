# Firecracker - Optimal Approach

## Algorithm Explanation

Find the volume (in $\text{m}^3$) of the region through which firecracker fragments move before reaching the ground, given initial explosion height $h_0 = 100 \text{ m}$, initial fragment velocity $v_0 = 20 \text{ m/s}$, and uniform gravity $g = 9.81 \text{ m/s}^2$, rounded to 4 decimal places.

### Paraboloid of Revolution Kinematic Trajectory Envelope:
1. **Kinematic Envelope Equation**:
   By classical Newtonian mechanics, the outer boundary envelope of all parabolic trajectories emitted uniformly in all 3D directions forms a paraboloid of revolution:
   $$y(r) = H - \frac{g}{2 v_0^2} r^2 \quad \text{where } H = h_0 + \frac{v_0^2}{2g}$$
2. **Exact Volume Integration**:
   Integrating the circular cross-sections of the paraboloid from ground $y = 0$ to max peak $y = H$:
   $$V = \int_{0}^{H} \pi r^2(y) \, dy = \pi \int_{0}^{H} \frac{2 v_0^2}{g} (H - y) \, dy = \frac{\pi v_0^2 H^2}{g}$$
3. **Execution**:
   Substituting $h_0 = 100$, $v_0 = 20$, and $g = 9.81$ yields $V = 1856532.8455$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ closed form. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
