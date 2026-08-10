## General

A trapezoid is determined by choosing two non-collinear line segments with the same slope. Those segments become one pair of opposite parallel sides.

The source enumerates every segment between two input points and groups it in two different ways:

- by slope and supporting line, to count pairs of parallel sides;
- by midpoint and slope, to identify parallelograms that the first count includes twice.

The final answer is:

`parallel-side pair count - parallelogram count`.

**Representing one segment's line**

For endpoints `(x1,y1)` and `(x2,y2)`, the source computes `dx=x2-x1` and `dy=y2-y1`.

For a nonvertical segment:

`k = dy/dx`

is its slope. The expression:

`b = (y1*dx - x1*dy)/dx`

equals `y1-k*x1`, the y-intercept. Segments have the same slope and intercept exactly when they lie on the same infinite supporting line.

For a vertical segment, ordinary slope is undefined. The source uses sentinel `k=1e9` and uses `b=x1` to distinguish vertical supporting lines by x-coordinate. Actual finite slopes are at most 2000 in magnitude under the coordinate limits, so the sentinel does not overlap them.

**First grouping: slope to supporting-line counts**

`cnt1[k][b]` counts how many point-pair segments lie on supporting line `b` with slope `k`.

For one slope group, let the counts on distinct lines be `t1,t2,...`. Choosing one segment from line A and one from different parallel line B gives four distinct endpoints:

- different parallel lines cannot share a point;
- the two segments form opposite parallel sides;
- connecting their endpoints in boundary order creates a convex trapezoid.

The source combines line groups with a running total `s`. For current count `t`, `s*t` counts choices with every earlier supporting line. This sums:

$$
\sum_{a<b}t_at_b.
$$

Pairs from the same supporting line are deliberately excluded because four collinear endpoints do not form a quadrilateral.

**Why parallelograms are counted twice**

A trapezoid with exactly one pair of parallel opposite sides appears in exactly one slope group.

A parallelogram has two pairs of parallel opposite sides. Its four vertices therefore generate:

- one segment pair for one side slope;
- another segment pair for the other side slope.

The first phase counts the same four-point parallelogram twice, while the problem wants each unique quadrilateral once. One duplicate contribution per parallelogram must be subtracted.

**Identifying a parallelogram by diagonals**

A quadrilateral is a parallelogram exactly when its diagonals bisect each other. In coordinate terms, the two diagonal segments share the same midpoint.

The source avoids fractions by representing midpoint with coordinate sums:

`(x1+x2, y1+y2)`.

Two segments have the same actual midpoint exactly when both doubled coordinates match.

For a fixed midpoint, choosing two segments with different slopes gives two non-collinear diagonals sharing their midpoint. Their four endpoints form one nondegenerate parallelogram. Choosing same-slope centered segments would place all endpoints on one line and must not be counted.

`cnt2[p][k]` counts segments of slope `k` at encoded midpoint `p`. The second running-total loop counts pairs from different slopes and subtracts each from `ans`.

**Why every parallelogram is subtracted once**

Every parallelogram has exactly two diagonals. They share a midpoint and have different slopes for a nondegenerate convex quadrilateral, so their pair appears once in the corresponding `cnt2` group.

Conversely, two non-collinear segments with the same midpoint define four points whose diagonals bisect each other, so they form a parallelogram. Thus the subtraction count is in one-to-one correspondence with duplicated parallelograms.

**Canonical segment enumeration**

The nested loops use `j in range(i)`, so every unordered pair of input points is processed once. No segment is duplicated with reversed endpoints.

Changing endpoint order can change signs of `dx` and `dy` simultaneously, leaving `dy/dx` and the intercept unchanged. The chosen enumeration is therefore consistent.

**Floating-point keys**

Slopes and intercepts are stored as Python floats. With these small integer coordinates, equivalent rational divisions commonly round to the same float, but exact normalized integer pairs would be more robust and make mathematical equality explicit.

A safer representation for slope is a gcd-normalized integer pair `(dy,dx)` with a fixed sign convention. A supporting line can likewise use an exact integer invariant rather than division.

**A genuine midpoint-key collision**

The source compresses doubled midpoint coordinates into:

`p = (sum_x+2000)*4000 + (sum_y+2000)`.

Each coordinate sum ranges from -2000 through 2000 inclusive. After offsetting, `sum_y+2000` has 4001 possible values: 0 through 4000.

Using base 4000 is therefore insufficient. For example, encoded pair `(a,4000)` collides with `(a+1,0)`:

$$
a\cdot4000+4000=(a+1)\cdot4000+0.
$$

Segments at different midpoints can be merged into one `cnt2` group, causing false parallelogram subtraction. A collision-free base must be at least 4001, or the tuple `(sum_x,sum_y)` should be used directly.

This is a correctness defect in the exact source for legal boundary coordinates.

**Overall counting proof when keys are exact**

The first phase counts every trapezoid once for each pair of parallel sides it has. A non-parallelogram has one such pair and is counted once. A parallelogram has two and is counted twice.

The midpoint phase counts every parallelogram exactly once and no non-parallelogram. Subtracting changes parallelogram multiplicity from two to one while leaving other trapezoids at one.

That proves the intended formula, subject to using collision-free and equality-safe keys.

**Environment dependencies**

The file uses `defaultdict` and `List` without shown imports. Standalone execution must import them. This is separate from the midpoint collision, which remains even when names are supplied.

## Complexity detail

Let `n` be the number of points and `q=n(n-1)/2=O(n^2)` the number of segments.

Segment enumeration performs constant expected hash-map work per pair, taking expected `O(n^2)` time. Across all nested maps, the total number of stored segment counts/group entries is bounded by `O(n^2)`.

The two final passes visit the nested frequency entries. Their total size is also `O(n^2)`, so expected total time is `O(n^2)` and space is `O(n^2)`.

These bounds assume expected constant-time hashing. Exact tuple/integer normalized keys preserve the same asymptotic costs.

## Alternatives and edge cases

- **Exact normalized slope:** Divide `(dy,dx)` by their gcd and normalize sign, avoiding float-key concerns.
- **Tuple midpoint key:** Use `(x1+x2,y1+y2)` directly, eliminating the base-4000 collision.
- **Base 4001 encoding:** It also distinguishes every legal offset pair, though a tuple is clearer.
- **Only one parallel-side pair:** The quadrilateral is counted once in `cnt1` and not subtracted.
- **Parallelogram:** It is counted twice by side slopes and once by diagonal midpoint, leaving one.
- **Rectangle or rhombus:** Both are parallelograms and follow the same correction.
- **Four collinear points:** Same-line segment pairs are not combined because the intercept group is not paired with itself.
- **Vertical sides:** Sentinel slope and x-coordinate line key group them separately.
- **Segments sharing an endpoint:** Parallel segments on different lines cannot share an endpoint, so first-phase selections use four distinct points.
- **Same-midpoint collinear segments:** Equal slopes are not paired in `cnt2`, avoiding degenerate subtraction.
- **Boundary coordinate sums:** They expose the exact source's midpoint encoding collision.
- **No parallel segments:** The first phase contributes zero, so the answer is zero.
- **Duplicate points:** The constraints exclude them; zero-length segments need no handling.
- **Missing imports:** Standalone use must provide `defaultdict` and `List`.
- **Input preservation:** The algorithm only reads `points` and stores derived segment statistics.
