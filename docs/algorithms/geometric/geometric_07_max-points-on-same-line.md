# Max Points on a Line

| | |
|---|---|
| **ID** | `geometric_07` |
| **Category** | geometric |
| **Complexity (required)** | $O(N^2)$ |
| **Difficulty** | 6/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) |

## Problem statement

Given an array of N points in a 2D plane, find the maximum number of points that lie on the exact same straight line.
A naive approach would define a line using every pair of points $O(N^2)$, and then check every other point to see if it lies on that line $O(N)$, resulting in an $O(N^3)$ algorithm.
You must solve this in $O(N^2)$ using a Hash Map and slope representation.

**Input:** A list of `(x, y)` coordinate tuples.
**Output:** An integer representing the maximum number of collinear points.

## When to use it

- A classic technical interview question designed to trap candidates who use floating-point division (`y / x`) to represent slopes, which inevitably fails due to precision errors.

## Approach

If we anchor on a specific point A, we can draw a line from A to every other point B, C, D...
If the line A \to B has the exact same **slope** as the line A \to C, then A, B, and C must be collinear!
Therefore, for a fixed anchor point A:
1. Calculate the slope to every other point.
2. Store the count of each slope in a Hash Map.
3. The maximum count in the Hash Map (plus 1 for the anchor point itself) is the max collinear points passing through A.
Repeat this for every point as the anchor, taking $O(N^2)$ time.

**The Floating-Point Trap:**
Slope is M = \frac{\Delta Y}{\Delta X} = \frac{y_2 - y_1}{x_2 - x_1}.
If you do floating point division, `0.3333333333333333` might hash differently than `0.3333333333333334`. Furthermore, vertical lines cause a Division by Zero error!
**The Solution:** Represent the slope as an irreducible fraction (a string or a tuple of two integers).
To make a fraction irreducible, divide both \Delta Y and \Delta X by their Greatest Common Divisor (GCD)!
Example: \frac{6}{4} reduces to \frac{3}{2}. \frac{-9}{-6} reduces to \frac{3}{2}. We store the tuple `(3, 2)` as the dictionary key!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for geometric_07: Max Points on Same Line.

Given n points in the plane, find the maximum
"""


def solve(points, n):
    """Max points on the same line via slope hashing."""
    from math import gcd
    if n < 2:
        return n
    best = 0
    for i in range(n):
        slopes = {}
        duplicates = 0
        vertical = 0
        for j in range(n):
            if i == j:
                continue
            if points[i] == points[j]:
                duplicates += 1
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0:
                # Vertical line.
                vertical += 1
            else:
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                # Normalize sign: force dx > 0 (or both zero).
                if dx < 0:
                    dx = -dx
                    dy = -dy
                key = (dy, dx)
                slopes[key] = slopes.get(key, 0) + 1
        local_max = vertical
        for c in slopes.values():
            if c > local_max:
                local_max = c
        total = local_max + duplicates + 1  # +1 for the pivot itself
        if total > best:
            best = total
    return best
```

</details>

## Walk-through

`points = [(1,1), (2,2), (3,3), (4,5)]`

**Iteration 1: Anchor `(1,1)`**
- vs `(2,2)`: dx=1, dy=1. GCD=1. Slope `(1, 1)`. `counts[(1,1)] = 1`.
- vs `(3,3)`: dx=2, dy=2. GCD=2. Slope `(1, 1)`. `counts[(1,1)] = 2`.
- vs `(4,5)`: dx=3, dy=4. GCD=1. Slope `(3, 4)`. `counts[(3,4)] = 1`.
- Max slope count is 2 (for slope `1,1`).
- Line size = 2 (\text{slope match}) + 1 (\text{anchor}) = 3.
- `global_max = 3`.

**Iteration 2: Anchor `(2,2)`**
- vs `(3,3)`: Slope `(1, 1)`.
- vs `(4,5)`: dx=2, dy=3. Slope `(2, 3)`.
- Max line size = 2.

**Final:** `global_max = 3`. ✓

*(Notice how we start the inner loop at `j = i + 1`. We don't need to look backwards because any line involving `points[i]` and previous points was already fully counted when the previous point was the anchor!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2)$ | $O(N)$ |
| **Average** | $O(N^2 log M)$ | $O(N)$ |
| **Worst** | $O(N^2 log M)$ | $O(N)$ |

The double loop iterates $O(N^2)$ times. Inside the inner loop, calculating the GCD takes logarithmic time relative to the coordinate values M. So technically, $O(N^2 log(\max(|dx|, |dy|)$)). Since coordinates are usually bounded, this is effectively considered $O(N^2)$ in interviews.
Space complexity is $O(N)$ because the dictionary at worst holds N distinct slope keys for a single anchor.

## Variants & optimizations

- **Hough Transform:** If N is millions (like pixels in an image) and you want to find the longest lines (detecting edges), $O(N^2)$ is too slow. Computer Vision engines use the Hough Transform, mapping points to a parametric (r, \theta) space and finding intersections via a voting accumulator matrix, achieving near $O(N)$ speeds!

## Real-world applications

- **Autonomous Driving:** Processing LIDAR dot clouds and detecting massive sequences of collinear dots to mathematically define the physical boundaries of a road lane or wall.

## Related algorithms in cOde(n)

- **[math_01 - GCD/LCM](../math/math_01_gcd-lcm-euclidean.md)** — The Euclidean algorithm powering the fractional reduction that avoids floating-point errors.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
