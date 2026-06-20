# Closest Pair of Points

| | |
|---|---|
| **ID** | `dc_05` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 3/10 |
| **GeeksForGeeks Equivalent** | [Closest Pair of Points](https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/) |

## Problem statement

Given an array of N points in a 2D plane, where each point is defined by its `(x, y)` coordinates, find the pair of points that have the smallest Euclidean distance between them.
Return that minimum distance.

**Input:** An array of `Points` where `Point` has properties `x` and `y`.
**Output:** A floating-point number representing the minimum distance.

## When to use it

- The quintessential Computational Geometry problem for Divide and Conquer.
- Shows how sorting heavily optimizes the "Conquer" (merge) step of spatial algorithms to bypass $O(N^2)$ checks.

## Approach

**1. The Naive Approach:**
Calculate the Euclidean distance between every possible pair of points. \frac{N(N-1)}{2} pairs means this is strictly $O(N^2)$ time.

**2. Divide and Conquer:**
Let's sort all the points by their `x` coordinate.
We can divide the points into a Left half and a Right half by drawing a vertical line `L` right down the middle `x` coordinate.
Recursively find the closest pair in the Left half (d_{left}) and the closest pair in the Right half (d_{right}).
Let d = \min(d_{left}, d_{right}).
Is d the absolute minimum distance? Not necessarily! What if one point is on the extreme right edge of the Left half, and the other point is on the extreme left edge of the Right half? They straddle the dividing line `L` and could be closer than d!

**3. The "Strip" (Conquer Step):**
We only care about points that are closer to the dividing line `L` than the distance d. If a point is further than d from the line, it is mathematically impossible for it to form a pair across the line with a distance less than d.
1. Create an array `strip` containing only the points whose `x` coordinate is within d of the dividing line `L`.
2. **Sort the `strip` array by their `y` coordinates.**
3. Iterate through the `strip`. For every point, compare it to the next points in the strip.
   *The Magic Optimization:* Because the points in the strip are bounded by a width of 2d and we sorted them by `y`, it is mathematically proven that we ONLY need to check the next **7 points** ahead of it in the sorted array! Any point beyond 7 spots will definitively have a `y` distance greater than d.
   This drops the merge step from an $O(N^2)$ cross-comparison down to an $O(N)$ linear scan!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_05: Closest Pair of Points.

Given n points in the plane, return the smallest
"""


def solve(points, n):
    """Closest pair of points via D&C plane sweep."""
    if n < 2:
        return 0.0
    px = sorted(points, key=lambda p: (p[0], p[1]))
    return _closest(px, 0, n - 1)

def _dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def _brute(pts, lo, hi):
    best = float("inf")
    for i in range(lo, hi + 1):
        for j in range(i + 1, hi + 1):
            d = _dist(pts[i], pts[j])
            if d < best:
                best = d
    return best

def _closest(px, lo, hi):
    n = hi - lo + 1
    if n <= 3:
        return _brute(px, lo, hi)
    mid = (lo + hi) // 2
    mid_x = px[mid][0]
    dl = _closest(px, lo, mid)
    dr = _closest(px, mid + 1, hi)
    d = min(dl, dr)
    strip = [px[k] for k in range(lo, hi + 1) if abs(px[k][0] - mid_x) < d]
    strip.sort(key=lambda p: p[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) ** 2 >= d * d:
                break
            cand = _dist(strip[i], strip[j])
            if cand < d:
                d = cand
    return d
```

</details>

## Walk-through

*(Conceptual due to spatial layout)*

1. Points are sorted by X. Left half recurses, Right half recurses.
2. Assume `d_left = 5` and `d_right = 7`.
3. The current absolute minimum is `d = 5`.
4. The dividing line `L` is at `X = 10`.
5. We scan the points. Any point whose X coordinate is between `5` and `15` is added to the `strip`.
6. We sort the `strip` by Y coordinate. (e.g. from bottom to top).
7. We iterate through the `strip`. For point P_1, we check P_2, P_3 \dots
8. If the vertical distance between P_1 and P_k exceeds `5`, we IMMEDIATELY break the inner loop because no point higher up can possibly be closer than `5`.
9. The inner loop never executes more than 7 times per point, keeping the comparison lightning fast.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N log^2 N)$ | $O(N)$ |
| **Worst** | $O(N log^2 N)$ | $O(N)$ |

The code above takes $O(N log^2 N)$ time. Why? The recursion depth is $O(\log N)$. At each level, building the strip takes $O(N)$, but sorting the strip by Y takes $O(k log k)$ where k \le N. The inner while loop is strictly $O(N)$ total. Thus the sort dominates the merge step: T(N) = 2T(N/2) + $O(N \log N)$ -> $O(N log^2 N)$.
**Optimization to strict $O(N \log N)$:** If we pre-sort the points by Y globally at the very beginning (`points_sorted_y`), and carefully split this Y-sorted array into Left and Right halves during the Divide step, we don't need to re-sort the strip! The merge step becomes purely $O(N)$, fulfilling T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Space complexity is $O(N)$ to hold the arrays during recursion.

## Variants & optimizations

- **Sweep Line Algorithm:** An entirely non-Divide and Conquer approach using a Binary Search Tree (like `std::set` in C++). You sweep a vertical line from left to right, maintaining an "active window" of points within distance d sorted by Y. It achieves $O(N \log N)$ but is often much faster and easier to code in practice.

## Real-world applications

- **Air Traffic Control:** Detecting if two planes are on a collision course (violating minimum safe separation distances) in 3D radar space.
- **Physics Simulators (Collision Detection):** Identifying which particles are interacting or bouncing off each other in the current frame without checking every single pair of atoms in the simulation.

## Related algorithms in cOde(n)

- **[dc_02 - Majority Element](dc_02_majority-element.md)** — Another algorithm where the Conquer step requires validating elements against a dynamically derived threshold.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
