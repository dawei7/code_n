## General
**Form two direction vectors:** From the first point, use vectors ((x_2-x_1,y_2-y_1)) and ((x_3-x_1,y_3-y_1)).

**Test their two-dimensional cross product:** The signed doubled area of the triangle is
$$
(x_2-x_1)(y_3-y_1)-(y_2-y_1)(x_3-x_1).
$$
It is zero exactly when the vectors are linearly dependent and the three points are collinear. Return whether it is nonzero.

A duplicate point produces a zero direction vector, so the same test also rejects every failure of the distinctness requirement without a separate set check. A nonzero cross product simultaneously proves distinctness and non-collinearity, exactly matching the boomerang definition.

## Complexity detail
The input always contains three points. A fixed number of integer subtractions and multiplications takes $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Compare slopes with division:** Equal slopes identify collinearity, but vertical lines require special handling and floating-point division can introduce precision concerns.
- **Enumerate lattice positions:** Choose the farthest point pair and walk through integer positions on its segment to see whether the third lies there. This can take time proportional to the coordinate span.
- **Duplicate points:** Any duplicate makes the cross product zero and the answer false.
- **Vertical or horizontal line:** The determinant handles both without special cases.
- **Third point outside the other two:** Collinearity still makes the answer false; the test concerns the entire line, not only one segment.
- **Boundary coordinates:** Values at zero and 100 remain safe for ordinary integer arithmetic.
