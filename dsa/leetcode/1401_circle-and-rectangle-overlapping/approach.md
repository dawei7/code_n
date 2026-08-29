## General

**Find the rectangle point closest to the circle center**

A circle and rectangle overlap exactly when some rectangle point lies within or on the circle. Among all rectangle points, the easiest one to test is the point closest to the circle center. If even that closest point is farther than the radius, every other rectangle point is farther too. If it is within the radius, it belongs to both shapes.

Because the rectangle is axis-aligned, the horizontal and vertical distances to it can be computed independently.

**Distance from one coordinate to an interval**

The helper `f(i, j, k)` returns the distance from coordinate `k` to closed interval `[i,j]`:

- If `i <= k <= j`, the coordinate already lies within the interval, so distance is zero.
- If `k < i`, the nearest interval endpoint is `i`, so distance is `i - k`.
- If `k > j`, the nearest endpoint is `j`, so distance is `k - j`.

For the x-axis, `a = f(x1, x2, xCenter)` is the horizontal gap from the circle center to the rectangle. For the y-axis, `b = f(y1, y2, yCenter)` is the vertical gap.

These components identify the closest rectangle point implicitly. Its x-coordinate is the center's x clamped into `[x1,x2]`, and its y-coordinate is the center's y clamped into `[y1,y2]`.

**The four geometric positions**

If the center lies inside the rectangle on both axes, $a=b=0$. The center itself belongs to both shapes, so overlap is immediate.

If the center aligns with the rectangle horizontally but lies above or below it, $a=0$ and $b$ is the vertical distance to the nearest horizontal edge.

If it aligns vertically but lies left or right, $b=0$ and $a$ is the distance to the nearest vertical edge.

If it lies diagonally beyond a corner, both components are positive, and the closest rectangle point is that corner.

The same formula handles all cases without separate edge and corner logic.

**Compare squared distances**

The Euclidean distance from the center to the closest point is

$$
\sqrt{a^2+b^2}.
$$

Overlap occurs when this is at most `radius`. Squaring both nonnegative sides gives the exact code:

`a * a + b * b <= radius * radius`.

Avoiding `sqrt` keeps the calculation integer-only and prevents unnecessary floating-point precision concerns.

The inequality is non-strict because touching counts as overlap. In the first sample, the nearest point is $(1,0)$ and its distance from center $(0,0)$ is exactly radius one, so the method returns true.

**Why checking only the closest point is sufficient**

The clamped coordinate minimizes squared x-distance and squared y-distance independently. Their sum is therefore the minimum squared distance from the center to any point in the rectangle.

If that minimum exceeds $r^2$, no rectangle point belongs to the circle. If it is at most $r^2$, the closest point satisfies the circle equation and already belongs to the rectangle by construction. This proves both directions.

**Boundary inclusion**

Both shapes include their boundaries. The helper treats center coordinates equal to rectangle edges as inside the interval, producing zero gap on that axis. The final less-than-or-equal test includes tangency to an edge or corner.

No rectangle normalization is required because the contract guarantees `x1 < x2` and `y1 < y2`.

**A concrete diagonal example**

Suppose the rectangle is `[2,5]` on the x-axis and `[3,7]` on the y-axis, while the circle center is `(0,1)`. The center lies two units left of the rectangle and two units below it, so `a=2` and `b=2`. The closest rectangle point is the bottom-left corner `(2,3)`, and its squared distance is $2^2+2^2=8$. A circle of radius three overlaps because $8\le9$, while radius two does not because $8>4$.

Containment needs no extra branch. If the circle center is inside the rectangle, distance zero proves overlap even when the circle is tiny. If the rectangle lies fully inside the circle, its closest point is inside the circle and the same test succeeds. The method asks only whether the intersection is nonempty, so it does not need to distinguish tangency, partial crossing, or full containment after the distance condition passes.

## Complexity detail

The algorithm performs a fixed number of comparisons, subtractions, multiplications, and additions, independent of coordinate magnitude. Time is $O(1)$ and auxiliary space is $O(1)$, matching the manifest.

Squared coordinate differences fit comfortably in Python integers. In fixed-width languages, one should use a sufficiently wide integer type before multiplication.

## Alternatives and edge cases

- **Explicit clamping:** Compute `closest_x = max(x1, min(xCenter, x2))` and similarly for y, then test squared distance. It is equivalent and often visually intuitive.
- **Separate edge and corner cases:** This works but creates many branches and makes it easy to miss a geometric position.
- **Rectangle-center projection:** Comparing only rectangle and circle centers is insufficient because rectangle dimensions matter.
- **Circle center inside rectangle:** Both gaps are zero, so overlap is true.
- **Rectangle inside circle:** Its closest point is certainly within the radius, so the method returns true.
- **Edge tangency:** One component is zero and the other equals the radius; non-strict comparison returns true.
- **Corner tangency:** $a^2+b^2=r^2$ also returns true.
- **Clearly separated shapes:** Minimum squared distance exceeds $r^2$, producing false.
- **Negative coordinates:** Interval distance uses ordinary ordering and works unchanged.
- **Large coordinates:** Squared comparison avoids floating-point square roots.
- **Axis alignment:** Independent coordinate clamping relies on the rectangle being axis-aligned, as guaranteed.
- **No mutation:** The method computes from scalar inputs and changes no shape representation.
