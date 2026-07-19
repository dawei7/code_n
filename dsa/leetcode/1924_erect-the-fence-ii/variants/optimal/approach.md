## General
**Use the small boundary of a minimum circle**

A minimum enclosing circle is determined by at most three boundary points: one point for radius zero, two endpoints of a diameter, or three non-collinear points defining a circumcircle. Randomly shuffle the points, then process them incrementally.

Maintain the minimum circle for the processed prefix. If the next point is already enclosed, the circle remains valid. Otherwise that point must lie on the boundary of the new prefix circle. Restart with its radius-zero circle and scan earlier points. Each earlier point found outside forces a two-point diameter circle. A third nested scan handles earlier points outside that diameter by constructing the unique three-point circumcircle.

For collinear triples, no finite unique circumcircle exists. Test the three pair-diameter circles and choose the smallest one enclosing all three points; this is the circle whose diameter uses the two farthest points.

**Why incremental repair is sufficient**

When a new point invalidates the previous prefix circle, some minimum replacement has that point on its boundary; otherwise the circle could move or shrink while still enclosing it. The same argument applies to the second and third boundary points in the nested repairs. Once at most three boundary constraints are fixed, their minimum circle is determined, and the remaining prefix checks ensure it encloses every earlier point.

## Complexity detail
Under a uniformly randomized order, boundary violations become progressively rarer. The standard backward-analysis result gives $O(N)$ expected time even though the explicit nested loops have an $O(N^3)$ worst case for an adversarial order. Shuffling and storing the point list use $O(N)$ space; the geometric state itself is constant-sized.

## Alternatives and edge cases
- **Enumerate every pair and triple:** Testing every candidate circle against all points is correct but takes up to $O(N^4)$ time.
- **Use only the farthest pair:** This fails for acute triangles, whose circumcircle is larger and centered away from every side midpoint.
- **Convex hull first:** Interior points can be removed, but the remaining hull still needs a minimum-circle algorithm.
- **Single point:** The center is that point and the radius is zero.
- **All points collinear:** The extreme pair determines the circle.
- **Duplicate coordinates:** Repeated trees impose the same constraint and do not change the answer.
- **Floating-point boundary:** A small comparison epsilon prevents roundoff from treating a boundary point as outside.
