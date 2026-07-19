## General
**Choose angle uniformly**

Map one uniform value `v` to angle `2πv`. Equal angle intervals then have equal probability, providing rotational symmetry around the center.

**Correct the radial distribution for area**

Let $R$ be the input circle's radius. Area inside radius $r$ is proportional to $r^{2}$, so choosing $r$ uniformly would crowd points near the center. For a uniform value $u$, use $r=R\sqrt{u}$. Then
$\Pr(r \le d) = d^{2}/R^{2}$ for $0 \le d \le R$, exactly the circle's area fraction.

**Translate polar coordinates to the requested center**

If the center is $(x_c,y_c)$ and the sampled angle is $\theta$, return the point $(x_c+r\cos\theta,\ y_c+r\sin\theta)$. Its distance from the center is at most $R$, and the angle/radius construction makes equal-area regions equally likely.

**Make the app trace reproducible**

The app consumes authored `random_values` cyclically in radial/angle pairs. This validates center translation, square-root radius, and stream progression deterministically while the native artifact uses independent random calls.

## Complexity detail
Each point uses two random values and constant arithmetic, so `draws` points take $O(draws)$ time. The returned trace uses $O(draws)$ space; one native `randPoint()` call uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Rejection sample the bounding square:** accept uniform square points lying inside the circle; expected work is constant because the acceptance probability is $\pi/4$.
- **Uniform radius without square root:** is biased toward the center and is not area-uniform.
- **Uniform disk area via Cartesian rejection:** avoids trigonometry but may consume a variable number of random calls.
- **Zero radial value:** returns the center regardless of angle.
- **Boundary radial value:** lies on the circle and remains valid.
- **Non-origin center:** translate only after generating the relative point.
- **Floating-point comparison:** validate deterministic traces with coordinate tolerance.
