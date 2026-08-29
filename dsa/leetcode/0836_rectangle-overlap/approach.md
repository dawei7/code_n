## General

**Positive-area overlap must exist on both axes**

Because the rectangles are axis-aligned, each rectangle is the Cartesian product of:

- an open-width interval along the x-axis;
- an open-height interval along the y-axis.

The two rectangles have a positive-area intersection exactly when their x-intervals overlap with positive length and their y-intervals overlap with positive length.

The source tests the opposite condition: it lists every way the rectangles can be separated on at least one axis, then negates that disjunction.

**Name the boundaries**

For `rec1 = [x1,y1,x2,y2]`:

- `x1` is its left edge and `x2` its right edge;
- `y1` is its bottom edge and `y2` its top edge.

For `rec2 = [x3,y3,x4,y4]`, the analogous boundaries are left `x3`, bottom `y3`, right `x4`, and top `y4`.

Validity guarantees each left edge is strictly left of its right edge and each bottom edge is strictly below its top edge.

**The four separating cases**

The rectangles do not overlap with positive area if any one of these is true:

1. `y3 >= y2`: rectangle 2's bottom is at or above rectangle 1's top.
2. `y4 <= y1`: rectangle 2's top is at or below rectangle 1's bottom.
3. `x3 >= x2`: rectangle 2's left edge is at or to the right of rectangle 1's right edge.
4. `x4 <= x1`: rectangle 2's right edge is at or to the left of rectangle 1's left edge.

The exact return is the negation of these cases:

`not (y3 >= y2 or y4 <= y1 or x3 >= x2 or x4 <= x1)`.

If none is true, neither rectangle is entirely above, below, left, or right of the other. Their projections overlap positively on both axes, so their intersection has positive width and height.

**Why equality means no overlap**

The problem requires positive intersection area. If `x3 == x2`, the rectangles touch along a vertical boundary but share zero width. If `y3 == y2`, they touch along a horizontal boundary but share zero height.

This is why the separating comparisons use `>=` and `<=` rather than strict inequalities. Edge and corner contact must return false.

**Equivalent interval formula**

The horizontal intersection width is

$$
\min(x_2,x_4)-\max(x_1,x_3),
$$

and the vertical height is

$$
\min(y_2,y_4)-\max(y_1,y_3).
$$

Both must be strictly positive. The four-case test is the logical complement of either dimension being nonpositive, expressed without calculating an area.

**Trace the examples**

For `[0,0,2,2]` and `[1,1,3,3]`, none of the four separation cases holds. Their horizontal and vertical overlaps both have length one, so the function returns true.

For `[0,0,1,1]` and `[1,0,2,1]`, `x3 >= x2` is true because both equal one. They touch at an edge but have no positive-width intersection, so the function returns false.

**Why the test is exhaustive**

Two one-dimensional intervals fail to overlap positively exactly when one begins at or after the other ends. Along x, that is `x3 >= x2` or `x4 <= x1`. Along y, it is `y3 >= y2` or `y4 <= y1`.

A two-dimensional positive rectangle intersection exists only when neither axis is separated. The disjunction covers every failure, and negation returns true exactly for positive-area overlap.

Another way to see the completeness is to project both rectangles onto each coordinate axis. Projection loses no information relevant to an axis-aligned intersection: any point shared by the rectangles must have an x-coordinate inside both horizontal projections and a y-coordinate inside both vertical projections. Positive overlap lengths on both projections can be combined into a positive-area rectangular region, while a nonpositive overlap on either projection makes such a region impossible.

## Complexity detail

The algorithm unpacks eight coordinates and performs four comparisons, three Boolean `or` operations, and one negation. The amount of work does not depend on coordinate magnitudes or any input collection size, so time complexity is `O(1)`.

It stores only a fixed number of coordinate variables and the Boolean expression result, so auxiliary space is `O(1)`.

No multiplication is needed, avoiding even theoretical concerns about area overflow in fixed-width languages with large coordinates.

## Alternatives and edge cases

- **Compute intersection width and height:** Check `min(rights) > max(lefts)` and `min(tops) > max(bottoms)`. This is equally constant-time and directly expresses positive dimensions.

- **Multiply intersection dimensions:** Multiplication is unnecessary and can be misleading if one or both dimensions are negative. Check both dimensions separately.

- **Edge contact:** Equality on one separating boundary returns false because shared area is zero.

- **Corner contact:** Both dimensions may meet at a single point, but at least one separation equality holds and the answer is false.

- **One rectangle inside the other:** None of the separation cases holds, so the answer is true.

- **Identical rectangles:** They have positive width and height by the validity guarantee and overlap completely.

- **Separated horizontally:** Either the third or fourth condition detects it regardless of vertical placement.

- **Separated vertically:** Either the first or second condition detects it regardless of horizontal placement.

- **Negative coordinates:** Only relative order matters; comparisons work unchanged.

- **Very large coordinates:** The method uses no coordinate products.

- **Valid nonzero rectangles:** Degenerate input rectangles are excluded, so each original rectangle itself has positive area.

- **Input immutability:** Coordinate lists are unpacked and never modified.
