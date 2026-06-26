# Convex Hull (Jarvis March / Gift Wrapping)

| | |
|---|---|
| **ID** | `geometric_05` |
| **Category** | geometric |
| **Complexity (required)** | $O(N * H)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Gift wrapping algorithm](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm) |

## Problem statement

Given an array of N points in a 2D plane, find the **Convex Hull**: the smallest convex polygon that completely encloses all the points.
While Graham Scan (`geo_02`) takes strictly $O(N \log N)$ time, implement the **Jarvis March** algorithm (often called the Gift Wrapping algorithm).
This algorithm takes $O(N \cdot H)$ time, where H is the number of points that actually end up on the hull. This makes it an output-sensitive algorithm!

**Input:** A list of `(x, y)` coordinate tuples.
**Output:** A list of `(x, y)` tuples representing the vertices of the Convex Hull.

## When to use it

- When you strongly suspect the Convex Hull will have very few vertices compared to the total number of points (e.g., 10^6 points densely packed inside a square. H will be 4, so Jarvis March runs in $O(4N)$, massively beating Graham Scan's $O(N \log N)$).
- It's conceptually much simpler to implement than Graham Scan as it avoids initial sorting and stack logic.

## Approach

Imagine driving a car around the perimeter of the point cloud.
You start at the absolute leftmost point (lowest X). You know this point MUST be on the convex hull.
Now, you want to turn your car to point at the *next* vertex on the hull. To do this, you just look at every single point in the cloud, and pick the one that forces you to make the widest possible **Right Turn**!
Once you find that point, you drive to it, and repeat the process until you arrive back at your starting point.

1. **Find Anchor:** Find the leftmost point. Let `current_point` be this anchor.
2. **Initialize Hull:** Add `current_point` to the hull.
3. **The Loop:** Let's guess the next point on the hull is `next_point = points[0]`.
4. **Scan:** Iterate through every point `p` in the array:
   - Use the **Cross Product** to check the orientation of `current_point -> next_point -> p`.
   - If `p` is further to the Right (Counter-Clockwise) than our current `next_point` guess, update `next_point = p`.
   - *(Edge case: If `p` and `next_point` are perfectly collinear with `current_point`, pick the one that is further away).*
5. **Update:** After checking all points, `next_point` is mathematically guaranteed to be the next vertex on the hull. Add it to the hull.
6. Set `current_point = next_point`. Repeat Steps 3-6 until `next_point` equals our original Anchor.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for geometric_05: Convex Hull (Jarvis March).

Compute the convex hull of n points using Jarvis
"""


def solve(points, n):
    """Convex hull via Jarvis March (gift wrapping)."""
    if n < 3:
        return sorted(points)
    # Find the leftmost point.
    leftmost = min(range(n), key=lambda i: (points[i][0], points[i][1]))
    hull = []
    cur = leftmost
    while True:
        hull.append(cur)
        # Find the next hull vertex: the most counterclockwise
        # point with respect to the current edge.
        candidate = None
        for j in range(n):
            if j == cur:
                continue
            if candidate is None:
                candidate = j
                continue
            # We want (candidate - cur) to be the most
            # counterclockwise of all points. Cross product
            # positive means j is more CCW than candidate.
            cross = ((points[candidate][0] - points[cur][0])
                     * (points[j][1] - points[cur][1])
                     - (points[candidate][1] - points[cur][1])
                     * (points[j][0] - points[cur][0]))
            if cross < 0:
                candidate = j
        # If the next candidate is the leftmost, we're done.
        if candidate == leftmost:
            break
        cur = candidate
        # Safety: avoid infinite loop on degenerate inputs.
        if len(hull) > n:
            break
    return [points[i] for i in hull]
```

</details>

## Walk-through

*(Conceptual)*
Points: `A(0,0)`, `B(1,1)`, `C(2,0)`, `D(1,2)`

1. **Leftmost:** `A(0,0)`. `hull = [A]`.
2. **Current:** `A`. Guess `next_idx = B`.
   - Check `C`: `A -> B -> C` turns Right. `C` is more "outer" than `B`. Update `next_idx = C`.
   - Check `D`: `A -> C -> D` turns Left. Keep `next_idx = C`.
3. **Move:** `next_idx` is `C`. `hull = [A, C]`.
4. **Current:** `C`. Guess `next_idx = A`.
   - Check `B`: `C -> A -> B` turns Left. Keep `next_idx = A`.
   - Check `D`: `C -> A -> D` turns Right. `D` is more outer! Update `next_idx = D`.
5. **Move:** `next_idx` is `D`. `hull = [A, C, D]`.
6. **Current:** `D`. Guess `next_idx = A`.
   - Check `B`: `D -> A -> B` turns Left. Keep `A`.
   - Check `C`: `D -> A -> C` turns Left. Keep `A`.
7. **Move:** `next_idx` is `A`. This is the start point! Loop breaks!
Result: `[A, C, D]`. ✓ (`B` was strictly inside!).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N * H)$ | $O(1)$ |
| **Worst** | $O(N^2)$ | $O(1)$ |

*Where H is the number of vertices on the hull.*
If every single point is on the hull (e.g., they form a massive circle), the loop runs N times, checking N points each time, yielding $O(N^2)$. This is worse than Graham Scan!
But if H is small, it runs incredibly fast.
Space complexity is strictly $O(1)$ auxiliary space (excluding the output array), making it highly memory efficient.

## Variants & optimizations

- **Chan's Algorithm:** The ultimate Convex Hull algorithm. It marries Graham Scan and Jarvis March to achieve an output-sensitive time of exactly $O(N log H)$. It works by splitting the points into chunks of size H, running Graham Scan on each chunk, and then running Jarvis March on the resulting sub-hulls!

## Real-world applications

- **Robotics:** Determining the absolute outer boundary of a swarm of robots to calculate the minimum size of a bounding net.

## Related algorithms in cOde(n)

- **[geometric_02 - Graham Scan](geometric_02_convex-hull-graham-scan.md)** — The $O(N \log N)$ counterpart.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
