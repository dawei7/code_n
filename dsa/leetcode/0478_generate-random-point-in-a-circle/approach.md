## General

A point uniformly distributed inside a circle must be uniform by area: regions of equal area must have equal probability. Choosing an angle uniformly is correct, but choosing the radius uniformly is not. Rings farther from the center have larger circumference and therefore more area, so they must receive proportionally more samples.

The exact solution uses inverse transform sampling. It generates one uniform random value for squared radius and one for angle, then converts the resulting polar coordinates to Cartesian coordinates.

**Uniform angle**

`random.uniform(0, 1) * 2 * math.pi` produces an angle `degree` uniformly over a full turn from zero through approximately $2\pi$. Equal angular intervals form sectors with equal fractions of the circle's area when radial sampling is handled correctly.

The variable name `degree` is slightly misleading: the value is in radians, because Python's `sin` and `cos` functions expect radians.

**Why squared radius must be uniform**

For a circle of radius `R`, the fraction of total area lying within distance `r` of the center is

$$
\frac{\pi r^2}{\pi R^2}=\frac{r^2}{R^2}.
$$

Thus a uniform area sample must satisfy cumulative distribution

$$
P(\text{radius}\le r)=\frac{r^2}{R^2}.
$$

If `U` is uniform on `[0, R^2]` and `length = sqrt(U)`, then

$$
P(\texttt{length}\le r)
=P(U\le r^2)
=\frac{r^2}{R^2},
$$

which is exactly the required area distribution.

That is why the code uses

`math.sqrt(random.uniform(0, self.radius**2))`.

It is equivalent to `R * sqrt(U0)` for `U0` uniform on `[0,1]`.

**Why a uniform radius would cluster points at the center**

If radius itself were uniform, half the samples would lie inside radius `R/2`. But that inner disk has only one quarter of the total area. It would receive twice the probability it should, producing excessive central density. The square root corrects this by assigning only probability `1/4` to radii at most `R/2`.

**Convert and translate**

Polar coordinates relative to the origin convert to

$$
x'=\texttt{length}\cos(\theta),\qquad
y'=\texttt{length}\sin(\theta).
$$

Adding the stored center translates the unit construction:

$$
x=x_{center}+x',\qquad y=y_{center}+y'.
$$

Translation preserves both area and uniformity. The returned list is `[x, y]`.

Because `length <= radius`, the generated point satisfies

$$
(x-x_{center})^2+(y-y_{center})^2
=\texttt{length}^2
\le R^2,
$$

so it lies inside or on the circle.

**Why the joint distribution is uniform**

The angle and squared-radius draws are independent. For any annular sector spanning angle fraction `alpha` and radii from `r1` to `r2`, the probability is

$$
\alpha\cdot\frac{r_2^2-r_1^2}{R^2},
$$

which equals that sector's area divided by the full circle area. Since every such region receives probability proportional to area, the generated point is uniform over the disk.

**Boundary values**

If the radial draw is zero, the point is exactly the center, regardless of angle. If it is `R^2`, the point lies on the circumference, which the contract permits. These exact endpoint events have probability zero in an ideal continuous distribution but remain valid outputs for a floating-point generator or deterministic adapter.

The native implementation stores radius and center once in the constructor. Every `randPoint` call uses two new random values and performs no rejection loop.

## Complexity detail

One `randPoint` call performs two random draws and a fixed number of arithmetic, square-root, sine, and cosine operations. Under the standard numerical model, expected and worst-case time are $O(1)$ and auxiliary space is $O(1)$ per native call.

For an app trace requesting $D$ points, generation takes $O(D)$ time and the returned list occupies $O(D)$ space, matching the draws-based manifest. Internal sampling state remains constant size.

The analysis treats floating-point transcendental operations as constant-time library primitives, as is customary for fixed-precision doubles.

## Alternatives and edge cases

- **Rejection sample a bounding square:** Draw uniformly from the `2R x 2R` square and reject points outside the circle. It is correct with expected about $4/\pi$ attempts, but has unbounded worst-case retries.
- **Choose radius uniformly:** Incorrect; it overweights the center because equal radial bands do not have equal areas.
- **Choose `sqrt(U)` for `U in [0,1]`:** Correct when multiplied by `R`; it is algebraically the same as the exact squared-radius draw.
- **Angle in degrees:** `sin` and `cos` require radians; the exact `2 * pi` scaling is correct despite the variable name.
- **Point at center:** Valid and naturally produced when radial value is zero.
- **Point on circumference:** Valid when radial value equals `R`.
- **Non-origin center:** Adding center coordinates translates every sample without changing uniformity.
- **Very large radius:** Fixed-precision arithmetic handles the stated bounds, though returned coordinates are approximate floating-point values.
- **Deterministic app stream:** Two supplied values reproduce the same radial and angular transformations per point.
- **No input mutation:** Constructor values are stored and remain unchanged across calls.
