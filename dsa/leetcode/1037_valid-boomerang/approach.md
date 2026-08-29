## General

**Three points form a boomerang exactly when their area is nonzero**

Three distinct points fail the definition only when they lie on one straight line. Geometrically, three points form a triangle, and a triangle has positive area precisely when its points are noncollinear.

The method tests this using a two-dimensional cross product. It avoids computing slopes, so vertical lines and fractional values need no special cases.

**Build two direction vectors**

After unpacking the three points, consider the vector from point one to point two:

$$
u=(x_2-x_1,\ y_2-y_1).
$$

Consider the vector from point two to point three:

$$
v=(x_3-x_2,\ y_3-y_2).
$$

The points are collinear exactly when these vectors are parallel or antiparallel. In two dimensions, that happens exactly when their cross product is zero:

$$
u_xv_y-u_yv_x=0.
$$

Substituting coordinates gives

$$
(x_2-x_1)(y_3-y_2)
-
(y_2-y_1)(x_3-x_2)=0.
$$

The code rearranges this equality. It returns true when

`(y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)`.

The two products being unequal is exactly the statement that the cross product is nonzero, with the terms moved to opposite sides.

**Why consecutive vectors work**

A common area formula uses vectors from the same starting point, such as point one to point two and point one to point three. The exact code instead uses point one to point two and point two to point three.

These are equivalent because

$$
\overrightarrow{P_2P_3}
=
\overrightarrow{P_1P_3}
-
\overrightarrow{P_1P_2}.
$$

Taking the cross product with `\overrightarrow{P_1P_2}`, the self-cross-product term is zero. The remaining value is the same signed double area. Thus consecutive edge vectors detect collinearity just as reliably.

**Why no explicit distinctness test is needed**

If point one equals point two, vector `u` is zero. Both products in the code are zero, the inequality is false, and the method rejects.

If point two equals point three, vector `v` is zero and the same rejection occurs.

If point one equals point three while point two differs, the two consecutive vectors point in opposite directions along the same line. Their cross product is zero, so the method again rejects.

Therefore, any duplicate pair automatically makes the determinant zero. A nonzero cross product simultaneously proves that no points coincide and that they are not collinear. The single condition covers both parts of the boomerang definition.

**Trace the valid example**

For points `[1,1]`, `[2,3]`, and `[3,2]`:

- `y_2 - y_1 = 2`.
- `x_3 - x_2 = 1`.
- `y_3 - y_2 = -1`.
- `x_2 - x_1 = 1`.

The left product is two, and the right product is negative one. They are unequal, so the signed area is nonzero and the method returns true.

The points make a genuine bent shape rather than a straight segment.

**Trace the collinear example**

For `[1,1]`, `[2,2]`, and `[3,3]`, every coordinate difference in the formula is one. Both products equal one, so the inequality is false.

Each step moves one unit right and one unit up. The direction never changes, and the three points lie on the line `y = x`.

**Why comparing slopes is less reliable**

One might compare

$$
\frac{y_2-y_1}{x_2-x_1}
\quad\text{and}\quad
\frac{y_3-y_2}{x_3-x_2}.
$$

This requires special handling when a horizontal difference is zero. It may also introduce floating-point rounding for non-integer slopes. Cross multiplication produces the exact same comparison using only integer arithmetic:

$$
(y_2-y_1)(x_3-x_2)
=
(y_3-y_2)(x_2-x_1).
$$

The exact solution simply negates that equality to ask for a valid boomerang.

**Connection to triangle area**

The absolute value of the cross product is twice the triangle's area. A zero value means the “triangle” has collapsed into a line segment. A nonzero value means positive area.

The method does not need to divide by two or take an absolute value because it only asks whether the value is zero. The sign merely records whether the points turn clockwise or counterclockwise; both orientations are valid.

**Why the result is correct**

If the method returns true, the cross product is nonzero. The two direction vectors are not parallel, so the points are noncollinear. A nonzero cross product also rules out a zero vector and therefore rules out duplicate points. Both boomerang requirements hold.

If it returns false, the cross product is zero. The direction vectors are linearly dependent, including the possible zero-vector cases caused by duplicates. The points are collinear or not all distinct, so they cannot be a boomerang.

## Complexity detail

The input always contains exactly three points. Unpacking coordinates and evaluating two products, four differences, and one comparison takes a fixed amount of work. Time complexity is `O(1)`.

Only six coordinate variables and constant-sized arithmetic intermediates are used. No collection grows with input, so auxiliary space is `O(1)`. Both bounds match the manifest.

The coordinate bound of 100 ensures products are small, but the determinant method is valid for any integer coordinates supported by the numeric type.

## Alternatives and edge cases

- **Slope comparison:** It expresses the same geometry but needs vertical-line handling and may suffer floating-point precision problems. Cross multiplication is exact and uniform.
- **Shoelace area formula:** Compute twice the triangle area from all three coordinates and test whether it is nonzero. This is algebraically equivalent to the cross product.
- **Pairwise distance checks:** Distances can prove points are distinct, but they do not by themselves detect collinearity. An area or orientation test is still needed.
- **Explicit duplicate set:** Checking `len(set(map(tuple, points))) == 3` can enforce distinctness, followed by a collinearity test. The determinant already rejects duplicates, making the set unnecessary.
- **Vertical line:** Both relevant horizontal differences are zero, so both cross-multiplied products are zero and the points are correctly rejected without division.
- **Horizontal line:** Both vertical differences are zero, producing the same correct rejection.
- **Negative slope:** Signs are preserved in integer products, so diagonal direction does not need a separate case.
- **Clockwise versus counterclockwise:** The determinant sign changes, but any nonzero sign returns true because orientation is irrelevant.
- **Two identical points:** One direction vector is zero, making both sides equal and returning false.
- **First and third points identical:** The vectors are opposites, still giving zero cross product and returning false.
- **Very small nonzero area:** Integer arithmetic distinguishes it exactly; there is no epsilon threshold.
- **Point order:** Permuting three distinct noncollinear points may change determinant sign but never whether it is zero, so boomerang validity is order-independent.
