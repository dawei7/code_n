# Generate Random Point in a Circle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 478 |
| Difficulty | Medium |
| Topics | Math, Geometry, Rejection Sampling, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-random-point-in-a-circle/) |

## Problem Description
### Goal
Construct a generator for a circle with the supplied positive radius and center `(x_center, y_center)`. Each `randPoint()` call must return a floating-point point lying inside or on that circle.

Points must be uniform over the circle's area, so equal-area regions have equal probability; choosing the radius uniformly would incorrectly concentrate samples near the center. Successive calls produce independent samples using the available random source. Translate generated offsets by the center and never return a point outside the boundary. The app provides deterministic random values to verify the mapping, while the native class uses the standard random source.

### Function Contract
**Inputs**

- `radius`, `x_center`, `y_center`: the circle geometry
- `random_values`: the app's deterministic cyclic stream of values in `[0, 1]`
- `draws`: the number of points to generate in the app trace

**Return value**

- The generated point list. The native artifact exposes a constructor and `randPoint()` using the standard random source.

### Examples
**Example 1**

- Input: `radius = 1, x_center = 0, y_center = 0, random_values = [0, 0], draws = 2`
- Output: `[[0, 0], [0, 0]]`

**Example 2**

- Input: `radius = 2, x_center = 1, y_center = -1, random_values = [0.25, 0], draws = 1`
- Output: `[[2, -1]]`

**Example 3**

- Input: `radius = 4, x_center = -2, y_center = 3, random_values = [0.25, 0.25], draws = 1`
- Output: `[[-2, 5]]`

### Required Complexity

- **Time:** $O(draws)$
- **Space:** $O(draws)$

<details>
<summary>Approach</summary>

#### General

**Choose angle uniformly**

Map one uniform value `v` to angle `2πv`. Equal angle intervals then have equal probability, providing rotational symmetry around the center.

**Correct the radial distribution for area**

Let $R$ be the input circle's radius. Area inside radius $r$ is proportional to $r^{2}$, so choosing $r$ uniformly would crowd points near the center. For a uniform value $u$, use $r=R\sqrt{u}$. Then
$\Pr(r \le d) = d^{2}/R^{2}$ for $0 \le d \le R$, exactly the circle's area fraction.

**Translate polar coordinates to the requested center**

If the center is $(x_c,y_c)$ and the sampled angle is $\theta$, return the point $(x_c+r\cos\theta,\ y_c+r\sin\theta)$. Its distance from the center is at most $R$, and the angle/radius construction makes equal-area regions equally likely.

**Make the app trace reproducible**

The app consumes authored `random_values` cyclically in radial/angle pairs. This validates center translation, square-root radius, and stream progression deterministically while the native artifact uses independent random calls.

#### Complexity detail

Each point uses two random values and constant arithmetic, so `draws` points take $O(draws)$ time. The returned trace uses $O(draws)$ space; one native `randPoint()` call uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Rejection sample the bounding square:** accept uniform square points lying inside the circle; expected work is constant because the acceptance probability is $\pi/4$.
- **Uniform radius without square root:** is biased toward the center and is not area-uniform.
- **Uniform disk area via Cartesian rejection:** avoids trigonometry but may consume a variable number of random calls.
- **Zero radial value:** returns the center regardless of angle.
- **Boundary radial value:** lies on the circle and remains valid.
- **Non-origin center:** translate only after generating the relative point.
- **Floating-point comparison:** validate deterministic traces with coordinate tolerance.

</details>
