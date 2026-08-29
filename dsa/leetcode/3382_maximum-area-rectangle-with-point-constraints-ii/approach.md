## General

**A valid vertical side must join consecutive points in its column.** Group all points by `x` in `columns` and sort each column's `y` values. Suppose a rectangle uses lower and upper corners at the same $x$. If another point in that column had a $y$ strictly between them, it would lie on the rectangle's vertical border and invalidate the rectangle.

Therefore the two corner heights must be adjacent in that column's sorted list. The source records every consecutive pair `(lower,upper)` and appends the column coordinate to `segment_columns[lower,upper]`.

This preprocessing creates only $O(n)$ vertical segments: a column with $p$ points contributes $p-1$ adjacent pairs.

**A rectangle needs the same vertical segment in two columns.** For each height pair, `segment_columns` contains all $x$ coordinates where both corner points exist with no point between them on that vertical side. Sorting those coordinates lets the source consider left/right columns.

It considers only consecutive `x` values in this list. If another column between them contained the same valid vertical segment, its two corner points would lie on the candidate's horizontal borders and invalidate the larger rectangle. Hence any valid rectangle must use consecutive occurrences for its `(lower,upper)` pair.

This produces candidate tuples `(left,right,lower,upper)`. Each candidate already has all four corner points and clean open portions of its two vertical sides.

**Candidate generation is necessary but not sufficient.** An unrelated point can still lie:

- inside the rectangle;
- on its top or bottom border;
- on a vertical side outside the open segment logic through another configuration.

The source therefore performs an inclusive point-count query for every candidate. Since the four corners are known to exist, the rectangle is valid exactly when the closed box contains four points total.

**Compress y-coordinates for a Fenwick tree.** Coordinates may be as large as $8\cdot10^7$, so a dense array over raw $y$ values is impossible. `y_rank` maps each distinct height to a one-based index in sorted order.

The Fenwick tree stores how many processed points occur at each compressed height. `add` inserts one point, `prefix` counts inserted points up through a rank, and `range_count(lower,upper)` counts inserted points whose $y$ lies inclusively between the two candidate heights.

One-based ranks are essential because Fenwick traversal uses the lowest set bit and index zero would not advance.

**Convert a 2D rectangle count into two x-prefix events.** Let

$$
F(X,\ell,u)
$$

be the number of points with $x\le X$ and $\ell\le y\le u$. Then the number in the inclusive rectangle $[L,R]\times[\ell,u]$ is

$$
F(R,\ell,u)-F(L-1,\ell,u).
$$

For each candidate, the source creates:

- a positive event at `right`;
- a negative event at `left - 1`.

Sorting all events by their $x$ limit lets one Fenwick sweep answer every prefix query.

**Sweep points and events together.** `sorted_points` orders points first by $x$. Before answering an event with limit `X`, the while-loop inserts every point whose $x \le X$ into the Fenwick tree. The range query then returns `F(X,lower,upper)`.

Multiplying by event `sign` and accumulating into `counts[query_index]` performs the inclusion-exclusion formula. An event at `left-1=-1` occurs before all nonnegative points and correctly contributes zero.

Events sharing the same limit are safe. The first such event inserts all points through that $x$; subsequent events see the same completed prefix.

**Accept exactly four inclusive points.** Candidate construction guarantees four distinct corners. If its offline count is four, no extra point is inside or on any border. If the count exceeds four, at least one forbidden point exists. A count below four should be impossible for a correctly generated candidate, but it is conservatively rejected.

**Compute the best area.** For every accepted candidate, area is

`(right - left) * (upper - lower)`.

`answer` remains `-1` when no candidate passes. All generated sides have distinct consecutive coordinates, so accepted areas are positive.

**Why no valid rectangle is missed.** In a valid rectangle, each vertical side's corners must be consecutive within its column, so both columns appear under the same segment key. They must also be consecutive columns for that key; an intervening occurrence would add border points. Candidate generation therefore includes the rectangle. Its inclusive count is exactly four, so it is accepted.

**Why every accepted rectangle is valid.** The segment key supplies all corners and positive height; different consecutive columns supply positive width. Inclusive count four proves those corners are the only points in the closed box. This is exactly the statement's corner, interior, and border requirement.

**Trace an obstructing center point.** Four corners at $(1,1),(1,3),(3,1),(3,3)$ create candidate $(1,3,1,3)$. Point $(2,2)$ is inserted by the right-prefix event and lies in the y range, so the difference count is five. The candidate is rejected without scanning its points individually.

## Complexity detail

Let $n$ be the number of points. Sorting y-values within columns costs at most $O(n\log n)$ in aggregate. There are $O(n)$ adjacent vertical segments and therefore $O(n)$ candidate pairs across all segment groups. Sorting their x-lists is also $O(n\log n)$ aggregate work.

Coordinate compression, points, and $O(n)$ events are sorted in $O(n\log n)$. Each point insertion and event range query costs $O(\log n)$ with the Fenwick tree. Total time is $O(n\log n)$.

Columns, segments, candidates, ranks, Fenwick storage, events, sorted points, and counts all use $O(n)$ space. This matches the manifest.

## Alternatives and edge cases

- **Cubic scan from version I:** It is simple for ten points but impossible for $2\cdot10^5$.
- **2D prefix grid:** Raw coordinates are too large and sparse.
- **2D range tree:** It can answer rectangle counts but is more complex than the offline x sweep.
- **Nonconsecutive vertical corners:** A point between them lies on the side, so they cannot form a valid rectangle.
- **Nonconsecutive matching columns:** An intermediate matching segment supplies forbidden border points.
- **Interior point:** Inclusive count becomes greater than four.
- **Horizontal-border point:** It is included by the closed y range and also raises the count.
- **Vertical-border point:** Consecutive-y filtering often prevents the candidate; inclusive counting provides final protection.
- **Duplicate coordinates:** The contract forbids them, which makes four counted points equal four distinct corners.
- **One point or one column:** No candidate exists and the answer is `-1`.
- **`left = 0`:** Negative prefix limit correctly sees no points.
- **Coordinate compression:** It preserves ordering and inclusive range semantics, not geometric distances; area still uses raw coordinates.
- **Fenwick one-based indexing:** Rank zero is never used.
- **Same x event limits:** Points are inserted once and all events receive the complete prefix.
- **Count below four:** It is rejected even though candidate construction should prevent it.
- **Generated source status:** With no local editorial, this derivation follows the exact segment generation, events, and Fenwick queries in `solution.py`.
- **Input preservation:** New zipped points and dictionaries are built without altering coordinate arrays.
