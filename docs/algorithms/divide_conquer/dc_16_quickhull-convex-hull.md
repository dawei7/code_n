# Quickhull (Convex Hull)

| | |
|---|---|
| **ID** | `dc_16` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Quickhull](https://en.wikipedia.org/wiki/Quickhull) |

## Problem statement

Given a set of N points in a 2D plane, find the Convex Hull of these points.
The Convex Hull is the smallest convex polygon that completely encloses all the points.
*Constraint:* Solve this using the Quickhull algorithm.

**Input:** An array of `Points` where `Point` has properties `x` and `y`.
**Output:** An array of `Points` representing the convex hull.

## When to use it

- To understand the spatial geometry equivalent of Quicksort.
- While the pure Divide and Conquer method (`dc_15`) splits points arbitrarily down the middle by X-coordinate, Quickhull uses extreme points as "pivots" to geometrically discard massive chunks of inner points instantly.

## Approach

**1. The "Pivot" Initial Split:**
Find the point with the minimum X coordinate (P_{min}) and the point with the maximum X coordinate (P_{max}).
Because these are the absolute furthest points horizontally, they MUST mathematically be vertices on the Convex Hull!
Draw a line between them. This line splits all remaining points into two sets: points "above" the line, and points "below" the line.

**2. The Geometric "Partition" (Discarding Points):**
Let's focus on the points "above" the line.
Find the point P_{far} in this set that is the **furthest perpendicular distance** away from the line P_{min} - P_{max}.
Because P_{far} is the absolute peak of the curve on this side of the line, it MUST also be a vertex on the Convex Hull!
Now we have a triangle formed by P_{min}, P_{max}, and P_{far}.
*The Magic Optimization:* Any point that is currently INSIDE this triangle cannot possibly be on the outer boundary of the Convex Hull. We can permanently discard all of them!

**3. The Recursive Step (Decrease and Conquer):**
The original line P_{min} - P_{max} has now been replaced by two new outer lines forming a "tent":
Line 1: P_{min} to P_{far}
Line 2: P_{far} to P_{max}

We recursively call our Quickhull function twice!
- Once for the points sitting "outside" Line 1.
- Once for the points sitting "outside" Line 2.
The recursion bottoms out when there are no more points "outside" a given line.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_16: Quickhull Convex Hull.

Given n points in the plane, return the vertices of
"""


def _line_side(p1, p2, p):
    """+1 / -1 / 0 for the side of p w.r.t. the line p1->p2."""
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def _line_dist(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) -
               (p2[1] - p1[1]) * (p[0] - p1[0]))

def solve(points, n):
    """Convex hull via Quickhull. Return as a Python set."""
    if n < 3:
        return set(points)
    # Find leftmost and rightmost points.
    min_x = max_x = 0
    for i in range(1, n):
        if points[i][0] < points[min_x][0]:
            min_x = i
        if points[i][0] > points[max_x][0]:
            max_x = i
    a, b = points[min_x], points[max_x]
    hull = set()

    # quickHull re-scans the full set and selects points on
    # `side` of the line p1->p2, exactly like the GfG reference
    # implementation. Average O(n log n), worst O(n^2).
    def quickHull(pts, p1, p2, side):
        ind = -1
        max_dist = 0
        for i, p in enumerate(pts):
            if _line_side(p1, p2, p) == side:
                d = _line_dist(p1, p2, p)
                if d > max_dist:
                    ind = i
                    max_dist = d
        if ind == -1:
            hull.add(p1)
            hull.add(p2)
            return
        P = pts[ind]
        quickHull(pts, P, p1, -_line_side(P, p1, p2))
        quickHull(pts, P, p2, -_line_side(P, p2, p1))

    quickHull(points, a, b, 1)
    quickHull(points, a, b, -1)
    return hull
```

</details>

## Walk-through

*(Conceptual)*
1. Find P_{min} (far left) and P_{max} (far right). Add them to `hull`.
2. Draw a line between them. Divide all other points into `left_set` (above) and `right_set` (below).
3. **Process `left_set`:**
   - Find the point P_{top} with the highest vertical altitude relative to the line. Add P_{top} to `hull`.
   - The line P_{min} \rightarrow P_{max} is replaced by a triangle.
   - Any points inside the triangle (underneath P_{top}) are permanently discarded!
   - We create a new `s1` set for points outside the line P_{min} \rightarrow P_{top}.
   - We create a new `s2` set for points outside the line P_{top} \rightarrow P_{max}.
   - Recurse on `s1` and `s2`!
4. **Process `right_set`:**
   - Same process, but finding P_{bottom}.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(\log N)$ |
| **Average** | $O(N \log N)$ | $O(\log N)$ |
| **Worst** | $O(N^2)$ | $O(N)$ |

Just like Quicksort, if the pivot point (P_{far}) splits the remaining points relatively evenly (a "fat" triangle that discards lots of points), the recursion depth is $O(\log N)$ and the work per level is $O(N)$, resulting in $O(N \log N)$ average time.
However, if all points are perfectly arranged in a circle, no points are ever discarded by the triangles! The algorithm devolves into processing 1 point per level, resulting in an $O(N^2)$ worst-case time limit exceeded disaster.
Space complexity averages $O(\log N)$ for the recursion stack.

## Variants & optimizations

- **Graham Scan:** As always, Graham Scan guarantees $O(N \log N)$ worst-case time by sorting the points by polar angle first, completely avoiding Quickhull's worst-case vulnerability.
- **Chan's Algorithm:** A mind-bending algorithm that mathematically combines Graham Scan and Jarvis March to achieve strict $O(N log H)$ time, where H is the number of points that actually end up on the hull!

## Real-world applications

- **Computer Graphics (Hitboxes):** Generating the simplified 2D convex collision hitbox for a highly complex sprite. Quickhull is generally faster in practice than Graham Scan for randomized points because it aggressively discards interior pixels almost instantly.

## Related algorithms in cOde(n)

- **[dc_15 - Convex Hull Divide & Conquer](dc_15_convex-hull-divide-and-conquer.md)** — The strict $O(N \log N)$ recursive merge method.
- **[sort_02 - Quick Sort](../sorting/sort_02_quick-sort.md)** — The 1D array analogue that suffers the exact same $O(N^2)$ worst-case pivot vulnerability.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
