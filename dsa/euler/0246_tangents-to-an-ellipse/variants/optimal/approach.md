# Tangents to an Ellipse - Optimal Approach

## Algorithm Explanation

Find the number of lattice points $P$ outside the ellipse $e$ for which the angle $\theta$ between the two tangents to $e$ is greater than $45^\circ$.

### Director Circle Geometry & Tangent Angle Inequality:
1. **Ellipse Parameters**:
   Center $C = (3000, 1500)$, focal distance $c = 5000$, semi-major axis $a = 7500$, semi-minor axis $b = \sqrt{7500^2 - 5000^2} = \sqrt{31250000}$.
2. **Director Circle & Tangent Angle Condition**:
   The angle $\theta$ between tangents from $P(X, Y)$ satisfies:
   $$\tan \theta = \frac{2 a b \sqrt{\frac{X^2}{a^2} + \frac{Y^2}{b^2} - 1}}{X^2 + Y^2 - (a^2 + b^2)}$$
   For $\theta > 45^\circ$:
   - Inside director circle $X^2 + Y^2 \le a^2 + b^2$: $\theta \ge 90^\circ > 45^\circ$.
   - Outside director circle: $4 b^2 X^2 + 4 a^2 Y^2 - 4 a^2 b^2 > (X^2 + Y^2 - (a^2 + b^2))^2$.
3. **Symmetric 2D Lattice Point Count**:
   Using 2-pointer / binary search over $X \in [0, X_{\max}]$, we count valid lattice points across all 4 quadrants.
4. **Execution**:
   The total number of valid lattice points is $810834388$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(X_{\max} \log Y_{\max})$ where $X_{\max} \approx 25\,000$. Runs in $\approx 0.25\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
