## General
Add the two individual rectangle areas, then apply inclusion–exclusion by subtracting their intersection once. The separate sum counts points covered by only one rectangle once and points in both rectangles twice.

The intersection of axis-aligned rectangles is the product of their one-dimensional overlaps:

`overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))`

`overlap_height = max(0, min(ay2, by2) - max(ay1, by1))`.

The smaller right edge and larger left edge delimit the common x-interval; the y formula is analogous. Clamping at zero is not merely defensive: disjoint intervals give a negative raw difference, while rectangles touching at one edge or point have zero-area intersection.

For $A=(-3,0)-(3,4)$ and $B=(0,-1)-(9,2)$, the individual areas are `24` and `27`. Their overlap is width `3` and height `2`, area `6`, so the union is $24 + 27 - 6 = 45$.

This formula is exact because the intersection of two axis-aligned rectangles is itself an axis-aligned rectangle (or empty). Subtracting its area changes the twice-counted common region to one count without affecting any other covered point.

## Complexity detail
The calculation uses a fixed number of comparisons, subtractions, and multiplications, so time and auxiliary space are both $O(1)$.

## Alternatives and edge cases
- A coordinate sweep or plane subdivision is useful for many rectangles but unnecessary for two.
- Omitting the zero clamp can produce a positive-looking or negative overlap contribution for disjoint rectangles.
- Adding the individual areas without subtraction double-counts the intersection.
- Identical and nested rectangles reduce to the larger rectangle's area.
- Edge- and point-touching rectangles have zero overlap area; fixed-width implementations may need a wider type for coordinate products.
