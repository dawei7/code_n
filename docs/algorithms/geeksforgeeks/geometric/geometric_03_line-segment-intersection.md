# Line Segment Intersection

| | |
|---|---|
| **ID** | `geometric_03` |
| **Category** | geometric |
| **Complexity (required)** | $O(1)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **Wikipedia** | [Line–line intersection](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line) |

## Problem statement

Given two line segments defined by their endpoints: Segment 1 from P_1 to P_2, and Segment 2 from P_3 to P_4.
Determine if the two line segments strictly or tangentially intersect each other.
You must solve this purely using integer arithmetic (the **Cross Product orientation** check), avoiding calculating floating-point slopes, division by zero, or dealing with infinite y=mx+b equations.

**Input:** Four `(x, y)` coordinate tuples: `p1`, `p2`, `p3`, `p4`.
**Output:** A boolean: `True` if the segments intersect, `False` otherwise.

## When to use it

- To determine if a line of sight is blocked by a wall in a 2D game.
- As the fundamental building block for the "Point in Polygon" Ray-Casting algorithm (`geo_04`).

## Approach

We use the same **Cross Product Orientation** concept from Graham Scan.
`orientation(A, B, C)` returns:
- `1` if the path A \to B \to C turns Clockwise.
- `2` if the path turns Counter-Clockwise.
- `0` if A, B, C are perfectly collinear.

**The Intersection Rule:**
Two segments (P_1, P_2) and (P_3, P_4) intersect if and only if:
1. P_3 and P_4 fall on **opposite sides** of the line created by (P_1, P_2).
   - Meaning `orientation(p1, p2, p3)` is different from `orientation(p1, p2, p4)`.
2. **AND** P_1 and P_2 fall on **opposite sides** of the line created by (P_3, P_4).
   - Meaning `orientation(p3, p4, p1)` is different from `orientation(p3, p4, p2)`.

If both conditions are met, the segments form an X shape and must cross!

**The Collinear Edge Case:**
What if the lines don't form an X, but they lie perfectly on top of each other (collinear)?
If `orientation == 0`, we must check if the point actually falls directly *between* the endpoints on the X/Y axes (using a simple bounding box check). If it falls inside the bounding box, they overlap and therefore intersect!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for geometric_03: Line Segment Intersection.

Given two line segments, each as ((x1, y1), (x2, y2)). They
intersect iff the orientations of the two endpoint triples
straddle each other. Standard cross-product trick.
"""


def solve(seg1, seg2):
    def orient(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def on_segment(a, b, c):
        return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and
                min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))

    (p1, q1) = seg1
    (p2, q2) = seg2
    o1 = orient(p1, q1, p2)
    o2 = orient(p1, q1, q2)
    o3 = orient(p2, q2, p1)
    o4 = orient(p2, q2, q1)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    if o1 == 0 and on_segment(p1, q1, p2):
        return True
    if o2 == 0 and on_segment(p1, q1, q2):
        return True
    if o3 == 0 and on_segment(p2, q2, p1):
        return True
    if o4 == 0 and on_segment(p2, q2, q1):
        return True
    return False
```

</details>

## Walk-through

*(Conceptual)*
`L1: p1(1,1) to p2(10,1)` (A horizontal line at y=1).
`L2: p3(1,2) to p4(10,2)` (A horizontal line at y=2).

1. `o1 = orient(p1, p2, p3)` -> `(1,1)` to `(10,1)` to `(1,2)`. Turns Counter-Clockwise. `o1 = 2`.
2. `o2 = orient(p1, p2, p4)` -> `(1,1)` to `(10,1)` to `(10,2)`. Turns Counter-Clockwise. `o2 = 2`.
3. General Check: `o1 != o2`? No! (They are both 2). P_3 and P_4 are on the *same side* of L1.
4. Result: `False`. They do not intersect. ✓

`L1: p1(10,0) to p2(0,10)`
`L2: p3(0,0) to p4(10,10)`
1. `o1 = orient((10,0), (0,10), (0,0))` -> Clockwise (`1`).
2. `o2 = orient((10,0), (0,10), (10,10))` -> Counter-Clockwise (`2`).
3. `o3 = orient((0,0), (10,10), (10,0))` -> Clockwise (`1`).
4. `o4 = orient((0,0), (10,10), (0,10))` -> Counter-Clockwise (`2`).
5. General Check: `(o1 != o2)` AND `(o3 != o4)`. True AND True!
6. Result: `True`. They form an X! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(1)$ | $O(1)$ |
| **Worst** | $O(1)$ | $O(1)$ |

The algorithm performs exactly 4 cross-product calculations and up to 4 bounding box checks. Everything relies on pure $O(1)$ arithmetic multiplication and subtraction. Time complexity is strictly $O(1)$.

## Variants & optimizations

- **Sweep Line (Bentley-Ottmann):** What if you are given N line segments and need to find if *any* two intersect? Comparing all pairs is $O(N^2)$. The Bentley-Ottmann sweep-line algorithm uses a balanced BST to solve it in $O((N + I)$ log N) time, where I is the number of intersections!

## Real-world applications

- **Computer Aided Design (CAD):** Ensuring traces on a printed circuit board (PCB) do not overlap and short-circuit.
- **Geofencing:** Validating that a user-drawn polygonal delivery zone does not intersect itself (forming a complex polygon).

## Related algorithms in cOde(n)

- **[geometric_02 - Graham Scan](geometric_02_convex-hull-graham-scan.md)** — Relies on the exact same cross-product math to determine turns.
- **[geometric_04 - Point in Polygon](geometric_04_point-in-polygon-ray-casting.md)** — Casts a ray (a line segment) and counts how many polygon edges it intersects using this exact function!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
