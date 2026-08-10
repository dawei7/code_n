## General

Twice a triangle’s area is `base * height`. If one side is vertical, its two endpoints share an x-coordinate, its base length is their y-distance, and the height is the horizontal distance from the third point to that vertical line.

The helper `calc` finds the best triangle with a vertical base. The method then swaps every point’s x and y coordinates and calls the same helper again, turning original horizontal bases into vertical ones.

**Best base on one vertical line**

For every x-coordinate, dictionaries `f` and `g` store the minimum and maximum y-coordinates seen on that line.

Any vertical base on line `x` has length at most:

`g[x]-f[x]`.

Using the extreme endpoints is always optimal for any fixed third-point height because it maximizes the base independently.

If only one point exists on that line, the difference is zero and no positive-area triangle can use it as a vertical base.

**Best perpendicular height**

`mn` and `mx` are the smallest and largest x-coordinates among all points. For a base on line `x`, the farthest possible horizontal distance is:

`max(mx-x, x-mn)`.

No interior x-coordinate can be farther than both global extremes. The y-coordinate of the third point does not affect perpendicular height to a vertical line, so any point at the chosen extreme x works.

The candidate doubled area is therefore:

`(g[x]-f[x]) * max(mx-x, x-mn)`.

The helper maximizes this product over every line containing points.

**Why base and height choices combine**

The two base endpoints are chosen from points sharing `x`. The third point is chosen at an extreme different x-coordinate. These selections are independent: changing the third point’s y does not change horizontal height, and changing base endpoints within the same line does not change that height.

If height is zero, all points lie on the same vertical line and any triangle is degenerate. If base is zero, the line has fewer than two distinct points. Only a positive product forms a valid triangle.

**Covering horizontal bases**

After the first call, the source swaps `c[0]` and `c[1]` for every coordinate. In transposed coordinates:

- an original horizontal line with equal y becomes a vertical line with equal first coordinate;
- its original x-span becomes the helper’s y-span;
- original vertical distance becomes helper horizontal height.

Thus the second call checks every triangle with a horizontal side. Taking the maximum covers both permitted orientations.

**Return value**

The products are already twice the geometric area, so no division or later multiplication is needed. If the maximum remains zero, every candidate is degenerate or no axis-parallel pair exists, and the source returns `-1`.

**Input mutation**

The coordinate swap is performed directly inside each two-element list and is never reversed. Consequently, this exact source leaves `coords` transposed after returning.

The problem does not ask to preserve the argument, so this does not change the computed answer in the judge. It is nevertheless a material source behavior. A nonmutating second helper call or a final swap-back pass would avoid surprising callers.

## Complexity detail

Each `calc` call scans all `n` points and then all distinct line keys, taking `O(n)` expected time with hash dictionaries. Two calls plus the transpose pass remain `O(n)`.

The minimum/maximum dictionaries can store one entry per distinct coordinate line, so auxiliary space is `O(n)`. No point copies are allocated; the second orientation reuses the input by mutation.

## Alternatives and edge cases

- **Group both axes separately:** Build extrema maps for equal x and equal y without mutating coordinates. This uses similar `O(n)` time and space with clearer input preservation.
- **Enumerate triples:** Testing every three points costs `O(n^3)` and is unnecessary because only line extrema matter.
- **Enumerate bases and third points:** Even grouping axis-parallel pairs can become quadratic; line and global extrema collapse both choices.
- **All points on one line:** Perpendicular height is zero, so the answer is `-1`.
- **Axis-parallel pair but no off-line point:** The product remains zero and cannot form a triangle.
- **Several points on one line:** Only minimum and maximum perpendicular coordinates are needed for the widest base.
- **Third point vertically between base endpoints:** Its parallel coordinate is irrelevant; perpendicular distance alone determines area.
- **Unique coordinates:** Base endpoints are distinct whenever their stored extrema differ.
- **One or two points:** No positive-area triangle exists, and zero maximum maps to `-1`.
- **Horizontal-only optimum:** It is discovered after transposition.
- **Vertical-only optimum:** It is discovered by the first call.
- **Equal best orientations:** Either produces the same stored maximum.
- **Positive coordinate constraint:** Initial `mx=0` is safe because every coordinate is at least one; generalized negative coordinates would require `-inf`.
- **Mutated argument:** After the method, every input point is `[old_y,old_x]`; this should be documented or repaired in reusable code.
- **Why twice-area is integral:** Coordinate differences are integers, so `base*height` is an integer even when the geometric area itself is a half-integer. Returning the product exactly matches the requested doubled quantity.
