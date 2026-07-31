## General

For a vertical side on the line $x=c$, twice the triangle's area is

$$
(\text{vertical base length}) \cdot \lvert x_3-c\rvert,
$$

where $x_3$ is the third vertex's x-coordinate. The base and height choices are independent: every point with x-coordinate different from $c$ is distinct from both base endpoints, and sliding that third vertex vertically does not change the height.

Consequently, the best vertical base on $x=c$ uses the minimum and maximum y-coordinates stored for that x-coordinate. The best height uses whichever of the global minimum or maximum x-coordinate lies farther from $c$. Multiplying those two extremes is optimal for every triangle whose axis-parallel side is vertical.

The horizontal case is symmetric. For each line $y=c$, use the minimum and maximum x-coordinates as its widest base, then multiply by the farther distance from $c$ to the global minimum or maximum y-coordinate.

One scan records the global coordinate extremes and the minimum/maximum coordinate within every vertical and horizontal group. A second scan over those group summaries evaluates all possible base lines. Since every qualifying triangle has either a vertical or horizontal side, one of these evaluated products equals its twice-area. Conversely, each positive product corresponds to a valid base and a third point at the selected global extreme, so the greatest product is attainable. If every product is zero, no positive-area qualifying triangle exists and the result is `-1`.

## Complexity detail

Let $n$ be the number of points. The point scan and the scans over all distinct x- and y-coordinate groups take $O(n)$ expected time with hash tables. The two group maps collectively store $O(n)$ entries in the worst case, so auxiliary space is $O(n)$.

The returned value is already twice the area: base times perpendicular height. No division or floating-point arithmetic is needed.

## Alternatives and edge cases

- **Sorting by each coordinate:** Sorting points by x and by y also exposes every group's extremes, but costs $O(n \log n)$ time instead of expected linear time.
- **Enumerating point pairs:** Trying every possible axis-parallel base and combining it with a global perpendicular extreme is correct, but takes $O(n^2)$ time.
- **Enumerating triangles:** Checking all triples directly takes $O(n^3)$ time and is infeasible for $n=10^5$.
- **Collinear points:** A nonzero axis-parallel base is insufficient when every possible perpendicular height is zero; the required answer is `-1`.
- **No repeated coordinate:** If no two points share an x-coordinate or a y-coordinate, no qualifying base exists.
- **Large coordinates:** Twice-area may exceed 32-bit integer range, so implementations in fixed-width languages need a 64-bit result type.
