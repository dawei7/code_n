## General

**Restore the chart's chronological order**

The input points may be arbitrarily ordered, but chart adjacency is defined by
increasing day. Sort the pairs by their first coordinate. Since all days are
distinct, every consecutive pair now defines exactly one nonvertical chart
edge.

**Count maximal runs of one slope**

One point needs no line. With at least two points, the first edge starts one
line. For each later point, compare the new edge's slope with the preceding
edge's slope. Equal slopes mean the three consecutive points are collinear and
the current line can continue. A different slope forces a new line.

Avoid division. If the preceding edge has changes $(\Delta x_1,\Delta y_1)$
and the current edge has changes $(\Delta x_2,\Delta y_2)$, their slopes are
equal exactly when

$$
\Delta y_1\Delta x_2=\Delta y_2\Delta x_1.
$$

Every horizontal change is positive after sorting, so this cross-product test
has no zero-denominator ambiguity. Integer multiplication also preserves exact
equality for large coordinates.

Each counted line is necessary because it begins at a genuine slope change,
where one straight line cannot cover both neighboring edges. Conversely, each
maximal run of equal adjacent slopes is collinear and is covered by one line.
Thus counting those runs gives the minimum.

## Complexity detail

Let $n$ be the number of points. Sorting takes $O(n \log n)$ time, and the
slope-change scan takes $O(n)$ time. Python's in-place sort may use $O(n)$
auxiliary storage.

## Alternatives and edge cases

- **Floating-point slopes:** Division can round distinct rational slopes to the same value, whereas cross multiplication compares them exactly.
- **Reduced slope pairs:** Dividing each `(dy, dx)` pair by its greatest common divisor is exact but performs more work than the direct cross product.
- **Repeated sorting:** Sorting the entire remaining point set after every extracted day is correct but takes $O(n^2 \log n)$ time.
- **One point:** There is no connection, so the result is zero.
- **Two points:** Their single connection always needs exactly one line.
- **Horizontal runs:** Consecutive zero price changes have equal slope and share one line.
- **Falling prices:** Negative vertical changes work without special handling in the cross-product equality.
- **A repeated slope after a bend:** Only consecutive equal slopes merge; returning to an earlier slope later still starts another line.
- **Unsorted input:** Comparing slopes before ordering by day would use the wrong chart edges.
