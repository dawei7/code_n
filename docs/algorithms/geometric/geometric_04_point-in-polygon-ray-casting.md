# Point in Polygon (Ray-Casting)

| | |
|---|---|
| **ID** | `geometric_04` |
| **Category** | geometric |
| **Complexity (required)** | $O(V)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Point in polygon](https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm) |

## Problem statement

Given a polygon represented by an array of V vertices in order, and a single test point P.
Determine if the point P lies strictly inside the polygon, on the boundary, or outside the polygon. The polygon can be convex or highly complex/concave.
Implement the **Ray-Casting (Even-Odd) Algorithm**.

**Input:** A list of `(x, y)` coordinate tuples defining the polygon edges, and a `(x, y)` test point.
**Output:** A boolean: `True` if inside or on the boundary, `False` otherwise.

## When to use it

- To determine if a user's mouse click landed inside a specific UI element or geographic map territory.
- Ray-Casting works on *any* polygon (convex or concave), whereas simpler math (like checking if the point is "Left" of every edge) ONLY works on strictly Convex polygons.

## Approach

Imagine you are standing at the test point P. You fire a laser beam (a ray) directly horizontally to the right, extending to infinity.
- If you are standing outside a polygon, the ray will either miss the polygon completely (0 intersections), or it will pierce through it, entering and exiting. (2, 4, or 6 intersections).
- If you are standing INSIDE the polygon, the ray MUST pierce the polygon boundary to escape! (1, 3, or 5 intersections).

**The Even-Odd Rule:**
Count how many times the horizontal ray starting at P intersects the edges of the polygon.
- If the intersection count is **ODD**, the point is INSIDE.
- If the intersection count is **EVEN**, the point is OUTSIDE.

**Edge Cases & Mathematical Tricks:**
1. To avoid floating-point math and complex infinite ray equations, we simply create a finite line segment from P=(x, y) to an extreme point far outside the polygon bounding box, e.g., Extreme=(1000000, y).
2. We then loop through all adjacent pairs of vertices in the polygon array (which form its edges) and use our `do_intersect()` function from `geometric_03`!
3. If the point lies exactly on an edge, the Even-Odd logic breaks. We must explicitly check if P is collinear with the edge and within its bounding box (`on_segment`) to return True immediately.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for geometric_04: Point in Polygon (Ray Casting).

Given a simple polygon (as a list of (x, y) vertices
"""


def solve(polygon, point, m):
    """Ray-casting point-in-polygon test."""
    if m < 3:
        return False
    x, y = point
    inside = False
    j = m - 1
    for i in range(m):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        # Edge (xj, yj) -> (xi, yi). Check if the horizontal
        # ray at y=y from the point crosses this edge.
        if ((yi > y) != (yj > y)):
            # The edge straddles the ray. Compute the x
            # intersection and check it's to the right of the
            # point.
            x_int = (xj * (yi - y) + xi * (y - yj)) / (yi - yj)
            if x < x_int:
                inside = not inside
        # Also: if the point lies on this edge, count as inside.
        # We can detect collinearity by checking the cross product
        # and bounding box.
        def _on_seg(a, b, c):
            return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0])
                    and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])
                    and (b[0] - a[0]) * (c[1] - a[1])
                        == (b[1] - a[1]) * (c[0] - a[0]))
        if _on_seg(polygon[i], polygon[j], point):
            return True
        j = i
    return inside
```

</details>

## Walk-through

*(Conceptual)*
Square Polygon: `(0,0)`, `(10,0)`, `(10,10)`, `(0,10)`.

**Test Point P(5, 5):**
- Ray: `(5,5)` to `(INF, 5)`.
- Edge 1 `(0,0)->(10,0)`: Ray misses.
- Edge 2 `(10,0)->(10,10)`: Ray crosses! (Intersects exactly at `10,5`). `count = 1`.
- Edge 3 `(10,10)->(0,10)`: Ray misses.
- Edge 4 `(0,10)->(0,0)`: Ray misses.
- Count is 1 (ODD). Return True! ✓

**Test Point P(15, 5):**
- Ray: `(15,5)` to `(INF, 5)`.
- Misses all edges (since all X coordinates of the polygon are \le 10).
- Count is 0 (EVEN). Return False! ✓

*(Note: The naive Ray-Casting algorithm shown above has a known edge case: if the ray passes exactly through a vertex, it might count as intersecting TWO edges! In production code, the ray is often tilted slightly (e.g. fired at an epsilon angle) to prevent vertex hits, or explicit `y`-coordinate endpoint exclusion rules are added).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V)$ | $O(1)$ |
| **Average** | $O(V)$ | $O(1)$ |
| **Worst** | $O(V)$ | $O(1)$ |

The algorithm iterates through every edge of the polygon exactly once.
Inside the loop, the `do_intersect` check takes strictly $O(1)$ time.
Total time complexity is $O(V)$, where V is the number of vertices.
Space complexity is $O(1)$ as we only maintain intersection counters.

## Variants & optimizations

- **Winding Number Algorithm:** An alternative to Ray-Casting. Imagine a string tied to P, extending to a point traversing the perimeter of the polygon. The "Winding Number" counts how many full 360-degree wraps the string makes around P. If W=0, the point is outside. If W \neq 0, the point is inside. Winding Number flawlessly handles the "ray hits a vertex" edge case and is the industry standard for GIS mapping engines.
- **Convex-Only Binary Search:** If the polygon is strictly Convex, you can find a center point, sort the vertices by angle, and use Binary Search to find which "slice" of the polygon P falls into, reducing the query time to $O(log V)$!

## Real-world applications

- **Computer Graphics:** Rendering vector graphics (SVG) by determining which pixels fall inside the path commands.
- **Geofencing:** Triggering a mobile notification when a GPS coordinate crosses into a predetermined geometric zone (e.g. entering an airport).

## Related algorithms in cOde(n)

- **[geometric_03 - Line Intersection](geometric_03_line-segment-intersection.md)** — The engine that powers the Ray-Casting checks.
- **[geometric_02 - Convex Hull](geometric_02_convex-hull-graham-scan.md)** — A convex hull algorithm is often used to calculate a fast "Bounding Box / Bounding Hull" around a complex polygon. If a point is outside the hull, you instantly know it's outside the polygon without running Ray-Casting!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
