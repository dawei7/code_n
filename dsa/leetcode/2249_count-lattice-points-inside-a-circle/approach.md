## General

**Search every lattice point that could possibly be covered**

A lattice point has integer coordinates. For circle center `(x,y)` and radius `r`, a point `(i,j)` is inside or on the circle exactly when

$$
(i-x)^2 + (j-y)^2 \le r^2.
$$

The solution enumerates candidate integer coordinates and checks this squared-distance condition. Squared values avoid floating-point square roots and include the circumference through `<=`.

**Find global upper coordinate bounds**

No circle extends right of `x + r` or above `y + r`. The code computes

`mx = max(x + r for x, _, r in circles)`

and the analogous `my`. Every covered point must have horizontal coordinate at most `mx` and vertical coordinate at most `my`.

The loops begin at zero. This is sufficient because the constraints state `r <= min(x, y)`, so every circle's leftmost coordinate `x-r` and lowest coordinate `y-r` are nonnegative. There are no covered negative-coordinate lattice points to examine.

Thus, the rectangle `[0,mx] \times [0,my]` contains the union of all circles.

**Test one point against circles**

For each integer pair `(i,j)` in the bounding rectangle, the innermost loop visits circles. It calculates `dx = i - x` and `dy = j - y`, then checks

`dx * dx + dy * dy <= r * r`.

On the first circle that contains the point, `ans` is incremented and `break` exits the circle loop.

The break is essential for union counting. A point inside three overlapping circles is still one lattice point and must be counted once, not three times.

If no circle passes, the loop finishes without changing `ans`.

**Why every counted point belongs**

The algorithm increments only after one exact squared-distance inequality succeeds. That inequality is the mathematical definition of being inside or on that circle. Therefore, every counted coordinate lies in at least one circle.

**Why no covered point is missed**

Take any lattice point inside a given circle. Its coordinates lie between `x-r` and `x+r` horizontally and between `y-r` and `y+r` vertically. The lower bounds are nonnegative by constraint; the upper bounds do not exceed global `mx` and `my`.

The nested loops therefore visit that integer coordinate. When the inner loop reaches its containing circle, the squared-distance condition passes and the point is counted. Hence, all points in the union are included.

**Why boundary points are included exactly**

A circumference point satisfies equality `dx^2 + dy^2 = r^2`. The code uses `<=` rather than `<`, so equality passes. A point just outside has a strictly larger squared distance and fails.

All calculations are integer-exact. There is no rounding near the boundary.

**Trace the radius-one circle**

For center `(2,2)` and radius one, the center has squared distance zero. The four axis neighbors have squared distance one and pass. Diagonal points such as `(1,1)` have squared distance two and fail. Exactly five points are counted.

**Exact implementation versus manifest summary**

The manifest says the method enumerates each circle's bounding square and inserts covered points into a union set, with `O(\sum r_i^2)` time and `O(P)` space. The stored solution does something different: it enumerates one global bounding rectangle, tests every candidate against circles, and counts directly.

It allocates no point set. The `break` prevents duplicates during the single coordinate visit.

With centers and radii at most one hundred, `mx` and `my` are at most two hundred, so the global scan remains bounded enough for the given constraints.

## Complexity detail

Let `C` be the number of circles, `X = mx + 1`, and `Y = my + 1`. The code visits `XY` candidate points and may test all `C` circles for each. Worst-case time is `O(XYC)`.

Under the constraints, `X,Y <= 201` and `C <= 200`. This is not the manifest's `O(\sum r_i^2)` bound because the exact implementation does not enumerate per-circle squares.

The method stores only scalar bounds, coordinates, differences, and the answer. Its auxiliary space is `O(1)`, not `O(P)`, because it uses no union set.

## Alternatives and edge cases

- **Per-circle enumeration with a set:** Visit each circle's bounding square and insert covered coordinates into a set. This matches the manifest and can avoid testing distant points against every circle, but uses space proportional to the union.
- **Scan only each circle's horizontal slices:** For each integer row, derive the covered x interval. Merging intervals can be more efficient but is more complex.
- **Use Euclidean square roots:** Floating-point calculations are unnecessary and can create boundary precision issues; squared distances are exact.
- **Overlapping circles:** A point is counted once because its coordinate is visited once and the circle loop breaks.
- **Point on circumference:** Equality is included.
- **One circle:** The same global scan checks its exact disk.
- **Radius one:** The center and four axis neighbors are the only lattice points.
- **Disjoint circles:** Points from both regions are visited and counted independently.
- **Nonnegative lower bound:** Starting loops at zero relies on `r <= x` and `r <= y`.
- **Maximum coordinates:** Global bounds include `x+r` and `y+r` through the `+1` range endpoints.
- **No set allocation:** Duplicate avoidance comes from visiting each coordinate once.
- **Input preservation:** Circle definitions are only read.
