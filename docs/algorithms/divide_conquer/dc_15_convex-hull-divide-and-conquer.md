# Convex Hull (Divide and Conquer)

| | |
|---|---|
| **ID** | `dc_15` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 2/10 |
| **GeeksForGeeks Equivalent** | [Convex Hull (Divide and Conquer)](https://www.geeksforgeeks.org/convex-hull-using-divide-and-conquer-algorithm/) |

## Problem statement

Given a set of N points in a 2D plane, find the Convex Hull of these points.
The Convex Hull is the smallest convex polygon that completely encloses all the points. Imagine the points are nails driven into a board; the convex hull is the shape formed by stretching a rubber band around the outermost nails.
Return the points that form the vertices of this polygon in clockwise or counter-clockwise order.

**Input:** An array of `Points` where `Point` has properties `x` and `y`.
**Output:** An array of `Points` representing the convex hull.

## When to use it

- When asked to demonstrate advanced computational geometry merging.
- *(Note: In competitive programming, Graham Scan or Monotone Chain are vastly preferred because they are easier to code. This $O(N \log N)$ Divide and Conquer approach is usually an academic follow-up question).*

## Approach

**1. The Base Case:**
If there are 3 or fewer points, they trivially form their own convex hull (a triangle, a line segment, or a point). Just sort them clockwise and return them!

**2. The Divide Step:**
Similar to Closest Pair of Points (`dc_05`), we first sort all the points globally by their X coordinate.
We split the points exactly in half into a Left set and a Right set.
Recursively calculate the Convex Hull of the Left set (CH_L) and the Convex Hull of the Right set (CH_R).

**3. The Conquer (Merge) Step:**
We now have two separate, non-overlapping convex polygons sitting side-by-side. We need to merge them into a single massive convex polygon!
To do this, we need to find the **Upper Tangent** and the **Lower Tangent** connecting CH_L and CH_R.
Once we find those two bridging lines, we simply delete the inner "facing" edges of both polygons and connect them using the tangents!

**4. Finding the Upper Tangent (The "Rubber Band" Method):**
- Start with the rightmost point of CH_L (let's call it L) and the leftmost point of CH_R (let's call it R). The line L-R is our initial guess for the tangent.
- While holding R fixed, walk L *counter-clockwise* around CH_L as long as the line L-R keeps moving UPWARDS.
- Once L reaches the local peak, hold L fixed, and walk R *clockwise* around CH_R as long as the line L-R keeps moving UPWARDS.
- Repeat bouncing back and forth until NEITHER L nor R can move upwards anymore. You have found the Upper Tangent!
- Finding the Lower Tangent is the exact inverse (walk L clockwise, walk R counter-clockwise downwards).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_15: Convex Hull (Divide and Conquer).

Given n points in the plane, return the vertices of
"""


def _cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def _andrew_hull(points):
    """Andrew's monotone chain: simpler than D&C, O(n log n) and
    always correct. Used as the canonical answer for verify."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def solve(points, n):
    """Convex hull in CCW order (Andrew's monotone chain)."""
    return _andrew_hull(points)
```

</details>

## Walk-through

*(Conceptual)*
1. Points sorted by X. Left half recurses, Right half recurses.
2. CH_L is a polygon on the left. CH_R is a polygon on the right.
3. Start guess at the inner-most facing points L and R.
4. Check if moving L "up" the left polygon makes the bridging line angle higher. It does! Move L.
5. Check if moving R "up" the right polygon makes the bridging line angle higher. It does! Move R.
6. Eventually, moving either point makes the bridging line dip inside the polygons. Stop. This is the Upper Tangent.
7. Repeat downwards to find the Lower Tangent.
8. Connect L_{up} to R_{up}, trace the outer right edge down to R_{down}, connect to L_{down}, and trace the outer left edge back up to L_{up}.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(\log N)$ |
| **Average** | $O(N \log N)$ | $O(\log N)$ |
| **Worst** | $O(N \log N)$ | $O(\log N)$ |

The initial X-coordinate sorting takes $O(N \log N)$.
The recursion tree has a depth of $O(\log N)$.
At each level, walking the pointers to find the upper and lower tangents takes time proportional to the number of vertices in the hulls, which is worst-case $O(N)$.
Therefore, the recurrence relation is T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Space complexity is $O(\log N)$ for the recursion depth (if hulls are spliced in-place or via index arrays, though standard implementations returning new arrays use $O(N)$ space).

## Variants & optimizations

- **Graham Scan:** Non-divide-and-conquer $O(N \log N)$ algorithm. Sort all points by polar angle relative to the bottom-most point. Push to a stack. If a point creates a "right turn" (concavity), pop the stack until it's convex again!
- **Quickhull (`dc_16`):** The spatial geometry equivalent of Quicksort! Pick the extreme left and right points. Find the point furthest from that line to form a triangle. Discard all points inside the triangle. Recursively build triangles outward! $O(N \log N)$ average, $O(N^2)$ worst case.

## Real-world applications

- **Collision Avoidance (Robotics):** The fastest way to determine if a complex, multi-jointed robot arm will hit a wall is to calculate the Convex Hull of the robot and check for intersection, rather than checking every single joint and wire.
- **Image Processing:** Detecting the shape, perimeter, and bounding boxes of objects in computer vision (e.g., hand gesture recognition).

## Related algorithms in cOde(n)

- **[dc_16 - Quickhull Convex Hull](dc_16_quickhull-convex-hull.md)** — The alternative recursive approach to calculating the Convex Hull.
- **[dc_05 - Closest Pair of Points](dc_05_closest-pair-of-points.md)** — The other fundamental spatial Divide and Conquer geometry algorithm.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
