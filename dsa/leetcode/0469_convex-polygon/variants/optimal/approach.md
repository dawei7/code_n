## General

**Measure every consecutive boundary turn**

For each position `i`, the candidate selects `first = points[i]`, `second = points[(i + 1) % count]`, and `third = points[(i + 2) % count]`. The modulo positions include the two turns that cross the end of the list. It then computes the 2D cross product of the consecutive edge vectors `second - first` and `third - second`.

A positive cross product is a left turn, a negative value is a right turn, and zero means that the three vertices are collinear. The candidate ignores zero turns and stores the most recent nonzero value in `orientation`. Each later nonzero cross product must have the same sign; the first sign reversal returns `False` immediately.

**Why one turn orientation characterizes convexity**

Along the ordered boundary of a simple convex polygon, every genuine turn faces the same side of the traversal, whether the vertices are clockwise or counterclockwise. Collinear boundary vertices do not create a reflex angle and therefore do not change that orientation. Conversely, if the scan contains both a left and a right turn, the opposite turn is an inward reflex angle, so the polygon is not convex. Checking all cyclic triples is therefore both necessary and sufficient under the guaranteed simple-polygon boundary order.

## Complexity detail

Let $n = \texttt{points.length}$. The candidate computes one constant-time cross product per vertex, giving $O(n)$ time. It stores the vertex count, one orientation value, and three point references, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Compare every pair of turn signs:** is correct but repeats work and takes $O(n^2)$ time, which the benchmark rejects.
- **Construct a convex hull:** can compare the hull with the polygon, but costs $O(n \log n)$ time and discards the useful boundary order already supplied.
- **Compute angles with trigonometry:** introduces floating-point error where an integer cross product is exact.
- **Clockwise order:** produces only negative nonzero cross products and is just as valid as counterclockwise order.
- **Collinear consecutive vertices:** produce zero and neither establish nor contradict the remembered orientation.
- **Wraparound turns:** require modulo positions so the closing edge participates at both endpoints.
- **Coordinate products:** should use an integer type wide enough for the difference products in fixed-width languages.
