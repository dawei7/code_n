# Convex Hull (Graham Scan)

| | |
|---|---|
| **ID** | `geometric_02` |
| **Category** | geometric |
| **Complexity (required)** | $O(N \log N)$ |
| **Difficulty** | 6/10 |
| **Interview relevance** | 5/10 |
| **Wikipedia** | [Graham scan](https://en.wikipedia.org/wiki/Graham_scan) |

## Problem statement

Given an array of N points in a 2D plane, find the **Convex Hull**: the smallest convex polygon that completely encloses all the points.
Imagine stretching a rubber band around the entire cloud of points and letting it snap shut. The points that the rubber band touches are the vertices of the Convex Hull.
Implement the **Graham Scan** algorithm to find these vertices in strictly $O(N \log N)$ time.

**Input:** A list of `(x, y)` coordinate tuples.
**Output:** A list of `(x, y)` tuples representing the vertices of the Convex Hull, typically in counter-clockwise order.

## When to use it

- To find the bounding area of a shape, detect outliers in a dataset, or as a prerequisite step for finding the diameter of a point cloud (Rotating Calipers algorithm).
- Graham Scan is the standard, most elegant $O(N \log N)$ algorithm for this problem.

## Approach

The core of Graham Scan is a Stack and a mathematical concept called the **Cross Product**.
The cross product of three points A, B, C tells us the "orientation" of the turn from line segment AB to line segment BC:
- If the cross product is > 0, it's a **Left Turn** (Counter-Clockwise).
- If it's < 0, it's a **Right Turn** (Clockwise).
- If it's 0, the points are collinear (a straight line).

A convex polygon traced counter-clockwise MUST strictly be composed of only Left Turns!

**The Steps:**
1. **Find the Anchor:** Find the point with the lowest Y-coordinate (break ties with the lowest X). This point is mathematically guaranteed to be on the hull. Let's call it P_0.
2. **Sort by Angle:** Sort all other points based on the polar angle they make with P_0 relative to the X-axis. (If two points have the same angle, keep the one furthest from P_0).
3. **The Stack:** Push P_0 and the first sorted point onto a stack.
4. **Scan:** Iterate through the rest of the sorted points.
   - For every new point P_i, look at the top two points on the stack (top and second\_top).
   - Does the sequence `second_top -> top -> P_i` form a Left Turn?
   - If NO (it's a Right Turn or straight line), we just created a "dent" in our hull! This means top cannot be on the convex hull. Pop it from the stack! Repeat this check until a Left Turn is formed.
   - Once it forms a Left Turn, push P_i onto the stack.
5. The stack now contains the exact vertices of the Convex Hull!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for geometric_02: Convex Hull (Graham Scan).

Bottom-most, then leftmost point is the pivot. Sort the rest
by polar angle to the pivot. Walk the sorted list, pushing to
a stack; pop the stack while the top two and the new point
make a non-left turn. O(n log n).
"""


def solve(points, n):
    import math
    if n < 3:
        return sorted(points)
    pivot = min(points)

    def angle_key(p):
        if p == pivot:
            return (-math.inf,)
        dx = p[0] - pivot[0]
        dy = p[1] - pivot[1]
        return (math.atan2(dy, dx), dx * dx + dy * dy)

    rest = [p for p in points if p != pivot]
    rest.sort(key=angle_key)
    hull = [pivot]
    for p in rest:
        while len(hull) >= 2:
            o, a = hull[-2], hull[-1]
            cross = (a[0] - o[0]) * (p[1] - o[1]) - (a[1] - o[1]) * (p[0] - o[0])
            if cross <= 0:
                hull.pop()
            else:
                break
        hull.append(p)
    return sorted(hull)
```

</details>

## Walk-through

*(Conceptual)*
Points: `A(0,0)`, `B(3,1)`, `C(1,2)`, `D(0,3)`, `E(-2,1)`

1. **Anchor:** Lowest Y is `A(0,0)`.
2. **Sort by Angle:**
   - `B` is roughly 18 degrees.
   - `C` is roughly 63 degrees.
   - `D` is 90 degrees.
   - `E` is roughly 153 degrees.
   - Order: `B, C, D, E`.
3. **Stack:** `[A, B]`.
4. **Scan C:** `A -> B -> C`. Forms a Left Turn! Stack: `[A, B, C]`.
5. **Scan D:** `B -> C -> D`. Forms a Left Turn! Stack: `[A, B, C, D]`.
6. **Scan E:** `C -> D -> E`. Forms a Left Turn! Stack: `[A, B, C, D, E]`.

What if we had a point `X(1, 1)`?
- `X`'s angle is 45 degrees. Order: `B, X, C, D, E`.
- Stack: `[A, B]`.
- Scan X: `A -> B -> X` is Left Turn. Stack `[A, B, X]`.
- Scan C: `B -> X -> C` is a **Right Turn**! We are denting inward!
  - Pop `X`! Stack is `[A, B]`.
  - Now check `A -> B -> C`. Left turn! Push `C`. Stack `[A, B, C]`.
  - `X` was successfully excluded from the hull! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

The initial sorting of the points by polar angle takes strictly $O(N \log N)$ time.
The scan loop processes each point exactly once. A point is pushed to the stack exactly once, and popped at most once. Therefore, the stack operations take strictly $O(N)$ total time. The bottleneck is the sorting, making the total time exactly $O(N \log N)$.
Space complexity is $O(N)$ to store the sorted array and the Stack.

## Variants & optimizations

- **Monotone Chain Algorithm:** A highly popular alternative to Graham Scan. Instead of sorting by polar angle (which requires heavy `math.atan2` floating-point calculations), it simply sorts the points by X-coordinate. It builds an "Upper Hull" and a "Lower Hull" using the exact same Left-Turn stack logic, and then concatenates them! It is generally preferred in competitive programming because it only uses integer math.

## Real-world applications

- **Collision Detection:** Calculating the "hitbox" of complex 3D objects in video game physics engines by reducing them to their convex hulls.
- **Geographic Information Systems (GIS):** Determining the territorial boundaries of animal habitats from GPS tracking data.

## Related algorithms in cOde(n)

- **[geometric_05 - Jarvis March](geometric_05_convex-hull-jarvis-march.md)** — The $O(N \cdot H)$ "Gift Wrapping" alternative to finding the Convex Hull.
- **[stack_01 - Next Greater Element](../stacks/stack_01_next-greater-element.md)** — The identical Monotonic Stack logic used to pop invalid interior elements.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
