## General
**Generate each unordered pair once**

Self-join `Point2D` as `first_point` and `second_point`. Keep a pair only when the first coordinate tuple is lexicographically smaller: its `x` is smaller, or the `x` values match and its `y` is smaller. Because points are unique, this condition selects exactly one orientation of every pair and never joins a point to itself.

**Measure Euclidean distance**

For each retained pair, compute the square root of the squared `x` difference plus the squared `y` difference. Coordinate differences may be negative, but squaring removes the sign.

**Aggregate before rounding**

Take `MIN` over the unrounded distances, then round that one minimum to two decimal places. Every possible pair contributes exactly once, so the aggregate cannot miss a closer pair; avoiding reversed duplicates changes only the work, not the minimum.

## Complexity detail
For `P` points there are $P(P - 1) / 2$ unordered pairs. The join computes constant arithmetic per pair, giving $O(P^2)$ time. A streaming minimum aggregate needs only $O(1)$ auxiliary state beyond the stored input and database execution internals, and the query returns one row.

## Alternatives and edge cases
- **Join both pair orientations:** excluding only identical coordinates is correct for the minimum, but evaluates every distance twice.
- **Plane sweep or divide and conquer:** procedural closest-pair algorithms reach $O(P \log P)$ time, but require ordered recursive or active-set state that is not natural in this SQL contract.
- **Manhattan distance:** $\lvert x_1-x_2\rvert+\lvert y_1-y_2\rvert$ solves a different metric and is incorrect here.
- Round after taking the minimum; rounding individual distances first can change which precise value is minimal.
- Points may share an `x` or a `y` coordinate, so pair selection must handle ties in one coordinate.
- Negative coordinates need no special case because differences are squared.
- With exactly two points, their distance is the answer.
