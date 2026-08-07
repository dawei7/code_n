## Function Contract

**Inputs**

- `radius`: the circle's positive radius
- `x_center`: the center's horizontal coordinate
- `y_center`: the center's vertical coordinate
- `random_values`: the app adapter's deterministic cyclic stream of values in `[0, 1]`
- `draws`: the number of points requested from the app adapter

**Return value**

- The app-local `solve(...)` returns the generated list of `[x, y]` points. The native interface instead constructs
  `Solution(radius, x_center, y_center)` and returns one point from each argument-free `randPoint()` call.

Every returned point must lie inside or on the circle, and the native distribution must be uniform over area. The
deterministic app stream exposes the same two random inputs per point so that the coordinate mapping is reproducible.
