### 1. Description

Given the radius and the position of the center of a circle, implement the function `randPoint` which generates a uniform random point inside the circle.

Implement the `Solution` class:

- $Solution(double radius, double x_{center}, double y_{center})$ initializes the object with the radius of the circle `radius` and the position of the center $(x_{center}, y_{center})$.

- `randPoint()` returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array `[x, y]`.

### 2. Function Contract

**Inputs**

- `radius`: the circle's positive radius
- $x_{center}$: the center's horizontal coordinate
- $y_{center}$: the center's vertical coordinate
- $\text{random}_{values}$: the app adapter's deterministic cyclic stream of values in `[0, 1]`
- `draws`: the number of points requested from the app adapter

**Return value**

- The app-local `solve(...)` returns the generated list of `[x, y]` points. The native interface instead constructs
  $Solution(radius, x_{center}, y_{center})$ and returns one point from each argument-free `randPoint()` call.

Every returned point must lie inside or on the circle, and the native distribution must be uniform over area. The
deterministic app stream exposes the same two random inputs per point so that the coordinate mapping is reproducible.

### 3. Examples

#### Example 1

```
**Input**
["Solution", "randPoint", "randPoint", "randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
**Output**
[null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]

**Explanation**
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint(); // return [-0.02493, -0.38077]
solution.randPoint(); // return [0.82314, 0.38945]
solution.randPoint(); // return [0.36572, 0.17248]
```

### 4. Constraints

- $0 < radius \le 10^{8}$

- $-10^{7} \le x_{center}, y_{center} \le 10^{7}$

- At most $3 * 10^{4}$ calls will be made to `randPoint`.
