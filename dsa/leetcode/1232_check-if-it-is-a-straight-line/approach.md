## General

**Use the first two points to define the candidate line**

The input contains at least two distinct points. Exactly one straight line passes through the first two, so there is no need to compare every pair of points. The solution stores the first point as `(x1, y1)` and the second as `(x2, y2)`. Every remaining point must lie on that same line.

A familiar test would compare slopes:

\[
\frac{y-y_1}{x-x_1}
=
\frac{y_2-y_1}{x_2-x_1}.
\]

Direct division is inconvenient. A vertical line has a zero horizontal difference, causing division by zero, and floating-point division can introduce rounding error. Cross multiplication removes both problems:

\[
(x-x_1)(y_2-y_1)
=
(y-y_1)(x_2-x_1).
\]

The exact code checks this equality for each point after the first two. If any point fails, it returns `False` immediately. If all pass, it returns `True`.

**Geometric meaning of the cross product**

The vectors from the first point to the second and from the first point to the current point are

\[
\mathbf{u}=(x_2-x_1,y_2-y_1),
\qquad
\mathbf{v}=(x-x_1,y-y_1).
\]

Their two-dimensional cross product is

\[
u_xv_y-u_yv_x.
\]

It equals zero exactly when the vectors are parallel. Rearranging that zero condition gives the equality used by the code. Because both vectors begin at the same point, parallel vectors mean all three points are collinear.

This view covers horizontal, vertical, increasing, and decreasing lines uniformly.

**Why a single anchor point is enough**

Suppose every point has zero cross product with the fixed vector from point zero to point one. Every vector from point zero to another point is parallel to that fixed nonzero vector. Therefore, every point belongs to the unique line through the first two points.

Comparing consecutive slopes instead would also work, but it is unnecessary and can make correctness reasoning more complicated. A fixed anchor provides one unchanging reference throughout the scan.

**Following the first example**

The first two points are `[1,2]` and `[2,3]`, giving differences \(\Delta x=1\) and \(\Delta y=1\). For point `[3,4]`, the code compares

\[
(3-1)(3-2)
\quad\text{with}\quad
(4-2)(2-1).
\]

Both sides are two. Every later point in the example produces equal sides, so the method returns true.

In the second example, point `[3,4]` is tested against the line through `[1,1]` and `[2,2]`. The left side is \((3-1)(2-1)=2\), while the right side is \((4-1)(2-1)=3\). The mismatch proves that point is off the candidate line, and the method returns false without examining later points.

**Vertical and horizontal lines**

For a vertical line, `x2 - x1 == 0`. The right-hand side becomes zero. Since the first two points are distinct, `y2 - y1` is nonzero, so the left side is zero exactly when `x - x1 == 0`. Every accepted point has the same \(x\)-coordinate.

For a horizontal line, `y2 - y1 == 0`. The left side becomes zero, and equality requires `y - y1 == 0` because the horizontal difference of the first vector is nonzero. Every accepted point has the same \(y\)-coordinate.

No special-case branch is necessary.

**Why integer arithmetic is preferable**

All coordinates are integers, so every subtraction and multiplication in the test is exact. Python integers expand as needed and cannot overflow. A floating slope could represent mathematically equal rational numbers with slightly different approximations, and vertical slopes would need a sentinel. Cross multiplication stays within exact arithmetic.

In fixed-width languages, coordinate differences can double the input magnitude and products can be larger, so an adequately wide integer type should be used. With the stated bounds, ordinary wider integer types are sufficient.


The first two distinct points define a unique candidate line. For each later point, the tested equality holds exactly when its displacement from the first point is parallel to the displacement from the first point to the second. If an equality fails, that point is not on the candidate line, so returning false is correct. If no equality fails, every point lies on the candidate line, so returning true is correct.

The no-duplicate-points guarantee ensures the first vector is nonzero. Even without that guarantee, choosing two identical anchor points would fail to define a unique line and make every cross product trivially zero.

## Complexity detail

Let \(n=\lvert\texttt{coordinates}\rvert\). The loop checks \(n-2\) points with constant arithmetic per point, so running time is \(O(n)\). An early mismatch can stop sooner, but the worst case examines them all.

The expression `coordinates[2:]` creates a new Python list containing references to the remaining \(n-2\) point objects. Therefore, this exact source uses \(O(n)\) auxiliary space, despite the manifest’s \(O(1)\) claim. Iterating by index or with `islice` would avoid that copy and achieve \(O(1)\) auxiliary space.

## Alternatives and edge cases

- **Index-based cross-product loop:** Iterate indices from two onward instead of slicing. It keeps the same \(O(n)\) time and reduces auxiliary space to \(O(1)\).
- **Floating-point slope comparison:** It is shorter mathematically but requires vertical-line handling and risks precision errors.
- **Reduced rational slopes:** Normalize each \((\Delta x,\Delta y)\) by its greatest common divisor. This remains exact but does more work than one cross multiplication.
- **Exactly two points:** The slice is empty and the loop finds no contradiction. Any two distinct points form a straight line, so the method returns true.
- **Vertical line:** Cross multiplication handles zero horizontal difference without division.
- **Horizontal line:** Zero vertical difference is handled by the same equality.
- **Negative coordinates and slopes:** Subtraction and signed multiplication work unchanged.
- **Early off-line point:** The method returns false immediately because one counterexample is enough.
- **Duplicate anchor points:** The contract excludes duplicates. If the first two were identical, they could not define the reference direction.
- **Integer overflow outside Python:** Use a wide enough product type in languages with fixed-width integers.
