## General

**Reduce valid sides to adjacent vertical segments.** Group points by their $x$-coordinate and sort every column by $y$. If a rectangle is valid, its lower and upper corner in either side column must be consecutive in that sorted list; any point between them would lie on the rectangle's border. Emit each consecutive pair $(y_1,y_2)$ as a vertical segment keyed by its two heights.

For each height pair, sort the columns that contain that segment. Only consecutive columns in this list need consideration. The two side columns of any valid rectangle must be consecutive: an intervening column with the same segment would put at least its two endpoints inside the rectangle or on its horizontal borders. Thus the total number of candidate rectangles remains linear in $n$.

**Count every point in each closed candidate rectangle.** Having four corners is not sufficient because a different point can still be inside or on a border. Coordinate-compress the $y$ values and sweep all points from left to right. A Fenwick tree stores counts by compressed height for points whose $x$-coordinate has entered the sweep.

For candidate $[x_1,x_2]\times[y_1,y_2]$, create two offline events. The prefix event at $x_2$ adds the number of points with $x\leq x_2$ and $y_1\leq y\leq y_2$; the event at $x_1-1$ subtracts the corresponding count strictly left of $x_1$. Coordinates are integers, so the difference is exactly the number of supplied points in the closed rectangle.

Every candidate already has its four corners. It is valid precisely when this inclusive count equals four. Compute its area $(x_2-x_1)(y_2-y_1)$ and retain the maximum among those candidates.

## Complexity detail

Let $n$ be the number of points. There are at most $n$ adjacent vertical segments and at most $n$ candidate pairs. Sorting columns, segment groups, points, and events costs $O(n\log n)$. Each point update and each event query costs $O(\log n)$ in the Fenwick tree, so total time is $O(n\log n)$. The groups, candidates, events, compressed coordinates, and tree use $O(n)$ space.

The benchmark defines `size` as $n$ and supplies many adjacent clean vertical strips. The reference builds all candidates and answers their inclusive range counts in $O(n\log n)$. A correct slower baseline builds the same candidates but scans all $n$ points to validate each one, taking $O(n^2)$ time.

## Alternatives and edge cases

- **Try every pair of columns and heights:** Direct rectangle enumeration grows far beyond the input limit even before emptiness checks.
- **Hash only the four corners:** Corner existence cannot detect points strictly inside the rectangle or elsewhere on a border.
- **Scan all points per candidate:** This validates the geometry correctly but costs $O(n^2)$ when there are linearly many candidates.
- **Use nonconsecutive points in one column:** Any intervening point lies on a vertical side, so such a rectangle can never be valid.
- **Use nonconsecutive columns for one height pair:** An intervening matching segment contributes forbidden points, so no valid rectangle is lost by checking adjacent columns only.
- **Inclusive boundaries:** The range count must include both endpoint heights and both side columns; accepting a count other than exactly four would overlook a forbidden border or interior point.
- **Points outside the vertical span:** A point between the side columns but above or below the rectangle does not invalidate it and is excluded by the Fenwick range query.
- **Large coordinates:** The maximum area can exceed 32-bit range, so fixed-width implementations need a 64-bit result.
- **No candidate:** Fewer than two matching adjacent vertical segments cannot form a rectangle, and the answer remains `-1`.
