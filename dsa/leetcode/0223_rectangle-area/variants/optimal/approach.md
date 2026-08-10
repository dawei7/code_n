## General

**Start with inclusion-exclusion**

The area of rectangle A is its horizontal side length times its vertical side
length:

$$
A = (\texttt{ax2}-\texttt{ax1})(\texttt{ay2}-\texttt{ay1}).
$$

Rectangle B has the analogous area

$$
B = (\texttt{bx2}-\texttt{bx1})(\texttt{by2}-\texttt{by1}).
$$

Adding $A+B$ counts every point covered by either rectangle, but a point in
their intersection is included once in $A$ and once in $B$. The union area
therefore follows the two-set inclusion-exclusion formula:

$$
\operatorname{area}(A\cup B)
= A+B-\operatorname{area}(A\cap B).
$$

The only nontrivial part is finding the intersection area. Because both
rectangles are axis-aligned, their two-dimensional intersection is determined
independently by the overlap of their x-intervals and y-intervals.

**Find the horizontal interval shared by both rectangles**

Rectangle A spans horizontally from `ax1` to `ax2`, while B spans from `bx1`
to `bx2`. Any shared interval must begin at the later left edge,
`max(ax1, bx1)`, because points before that coordinate are outside whichever
rectangle starts later. It must end at the earlier right edge,
`min(ax2, bx2)`, because points after that coordinate are outside whichever
rectangle ends earlier.

The candidate overlap width is therefore

$$
\texttt{width}
= \min(\texttt{ax2},\texttt{bx2})
- \max(\texttt{ax1},\texttt{bx1}).
$$

If this value is positive, it is the length of the shared horizontal segment.
If it is zero, the projections only touch at an edge, which has zero area. If
it is negative, there is a horizontal gap and no intersection. The expression
`max(width, 0)` converts all non-overlap cases to zero while retaining a real
overlap length unchanged.

**Apply the same reasoning vertically**

The shared vertical interval begins at the higher bottom edge,
`max(ay1, by1)`, and ends at the lower top edge,
`min(ay2, by2)`. Its candidate height is

$$
\texttt{height}
= \min(\texttt{ay2},\texttt{by2})
- \max(\texttt{ay1},\texttt{by1}).
$$

Again, `max(height, 0)` is the actual nonnegative overlap length.

Two rectangles have positive intersection area only when their projections
overlap positively on both axes. Since the intersection, when present, is
itself an axis-aligned rectangle, its area is
`max(height, 0) * max(width, 0)`.

Clamping each dimension separately is important. Using
`max(width * height, 0)` would be wrong: if the rectangles are separated both
horizontally and vertically, both candidate lengths can be negative, and their
product would be spuriously positive even though the rectangles do not meet.

**Complete the one-line union calculation**

The exact return expression subtracts the clamped overlap product from `a + b`.
If the rectangles do not overlap in either dimension, one clamped factor is
zero, so no area is subtracted. If they overlap, the common area was counted
twice in `a + b`; subtracting it once leaves every covered point counted
exactly once.

For the first example, rectangle A has width 6 and height 4, so `a = 24`.
Rectangle B has width 9 and height 3, so `b = 27`. Their horizontal overlap is
from x-coordinate 0 to 3, of width 3, and their vertical overlap is from 0 to
2, of height 2. The union is `24 + 27 - 3 * 2 = 45`.

For two identical rectangles, both individual areas are the same and the
intersection equals that full area. The formula returns `area + area - area`,
so it correctly counts the shared rectangle once.

**Why the formula covers every geometric arrangement**

On each axis, the `max(left endpoints)` and `min(right endpoints)` construction
gives the exact intersection of two intervals when it is nonempty, and the
clamp gives length zero otherwise. Cartesian products distribute here: a point
lies in both rectangles exactly when its x-coordinate lies in both horizontal
intervals and its y-coordinate lies in both vertical intervals. Thus the
product of the two overlap lengths is precisely the intersection area.

Inclusion-exclusion then gives the desired covered area. The reasoning does not
depend on which rectangle is leftmost, tallest, larger, or contained inside the
other; `min` and `max` handle all relative positions symmetrically.

## Complexity detail

The method performs a fixed number of subtractions, multiplications, `min`
calls, and `max` calls regardless of coordinate values. Its time complexity is
$O(1)$.

It stores only four derived integers—`a`, `b`, `width`, and `height`—in
addition to the parameters, so auxiliary space is $O(1)$. Python integers
handle the possible products without fixed-width overflow.

## Alternatives and edge cases

- **Explicit overlap branch:** Test whether `width > 0 and height > 0`, set overlap to their product only then, and otherwise use zero. It is equivalent to separately clamping both dimensions but needs more control flow.
- **Plane partitioning:** Split the plane at all rectangle edges and sum covered cells. It can work but is unnecessary for only two rectangles and introduces much more machinery than inclusion-exclusion.
- **No overlap on one axis:** A horizontal or vertical gap makes one clamped dimension zero, so the intersection area is zero regardless of the other dimension.
- **Touching edges:** Candidate width or height is exactly zero. A shared boundary line has zero area, so subtracting zero is correct.
- **Touching at one corner:** Both overlap dimensions are zero; the single shared point has zero area.
- **One rectangle inside the other:** Both overlap intervals equal the inner rectangle's intervals. Subtracting the inner area from the sum leaves exactly the outer area.
- **Identical rectangles:** The overlap equals either full rectangle, preventing the same area from being counted twice.
- **Degenerate rectangles:** The constraints permit equal left and right coordinates or equal bottom and top coordinates. Such a rectangle has zero area, and the same formulas still produce the correct union.
- **Negative coordinates:** Side lengths use differences between ordered endpoints, so crossing or lying left/below the origin changes no reasoning.
- **Large coordinate products:** Python has arbitrary-precision integers. In a fixed-width language, an adequately wide integer type should be used for multiplication.
- **Axis mix-up:** Horizontal overlap must use only x-coordinates and vertical overlap only y-coordinates. Combining an x endpoint with a y endpoint has no geometric meaning.
- **Input preservation:** All coordinates are immutable numbers, and the method computes derived values without changing any input object.
