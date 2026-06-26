# Rectangle Overlap (Axis-Aligned)

| | |
|---|---|
| **ID** | `geometric_06` |
| **Category** | geometric |
| **Complexity (required)** | $O(1)$ |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) |

## Problem statement

Given two axis-aligned rectangles (rectangles whose edges are perfectly parallel to the X and Y axes).
Each rectangle is represented by two coordinates: its bottom-left corner `(x1, y1)` and its top-right corner `(x2, y2)`.
Determine if the two rectangles overlap. Touching at a corner or sharing a mathematical line segment as an edge does *not* constitute an overlap (the overlapping area must be strictly positive).

**Input:** Two arrays representing the rectangles: `rect1 = [x1, y1, x2, y2]` and `rect2 = [x1, y1, x2, y2]`.
**Output:** A boolean: `True` if they overlap, `False` otherwise.

## When to use it

- Constantly asked in FAANG interviews as a fundamental test of writing clean, logical, and bug-free condition checks.
- The foundation of 2D game collision detection (AABB - Axis-Aligned Bounding Box).

## Approach

A naive approach tries to define all the ways rectangles *can* overlap (Corners inside, forming a cross, one fully enclosing the other). This results in massive, unreadable, and bug-prone `if/else` chains.

**The Inverted Logic Trick:**
Instead of checking if they overlap, it is vastly easier to check **if they DO NOT overlap!**
Two rectangles absolutely cannot overlap if one is completely strictly to the Left, Right, Top, or Bottom of the other.

1. **Left:** Is `rect1` fully to the left of `rect2`?
   - `rect1_right_x <= rect2_left_x`
2. **Right:** Is `rect1` fully to the right of `rect2`?
   - `rect1_left_x >= rect2_right_x`
3. **Bottom:** Is `rect1` fully below `rect2`?
   - `rect1_top_y <= rect2_bottom_y`
4. **Top:** Is `rect1` fully above `rect2`?
   - `rect1_bottom_y >= rect2_top_y`

If **ANY** of these 4 conditions are true, the rectangles do not overlap!
Therefore, if **ALL** of these conditions are false, they MUST overlap!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for geometric_06: Rectangle Overlap (Axis-Aligned).

Given two axis-aligned rectangles (each given by its
"""


def solve(l1, r1, l2, r2):
    """Two rectangles do not overlap iff one is entirely left
    of the other, or one is entirely above the other.
    l1 = top-left, r1 = bottom-right (y-axis points up).
    """
    # If rectangle 1 is to the right of rectangle 2, no overlap.
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False
    # If rectangle 1 is above rectangle 2, no overlap.
    # "Above" means l1.y > r2.y (r1.y is the lower y-bound of rect 1).
    if r1[1] > l2[1] or r2[1] > l1[1]:
        return False
    return True
```

</details>

## Walk-through

`rect1 = [0, 0, 2, 2]` (A 2 x 2 square at origin).
`rect2 = [1, 1, 3, 3]` (A 2 x 2 square offset by 1).

1. `is_left`: `2 <= 1`? False.
2. `is_right`: `0 >= 3`? False.
3. `is_bottom`: `2 <= 1`? False.
4. `is_top`: `0 >= 3`? False.

All conditions are False. Overlap is `True`. ✓

**Calculate Area:**
`overlap_left_x = max(0, 1) = 1`
`overlap_right_x = min(2, 3) = 2`
`width = max(0, 2 - 1) = 1`
`overlap_bottom_y = max(0, 1) = 1`
`overlap_top_y = min(2, 3) = 2`
`height = max(0, 2 - 1) = 1`
Area = 1 x 1 = 1. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(1)$ | $O(1)$ |
| **Worst** | $O(1)$ | $O(1)$ |

The algorithm performs a constant number of integer comparisons and assignments. Time and space are strictly $O(1)$.

## Variants & optimizations

- **Sweep Line (Finding intersections among N rectangles):** If you have 10,000 rectangles, finding intersecting pairs by checking every $O(N^2)$ combination is too slow. You can project the rectangles onto the X-axis as "Start" and "End" events, sweep a vertical line across the X-axis, and maintain the active Y-intervals using a Segment Tree! This reduces the time to $O(N log N + I)$ where I is the number of actual overlaps.

## Real-world applications

- **Web Rendering Engines:** Browsers calculate the intersection of HTML `<div>` bounding rects with the user's viewport rect to determine if an element should be rendered or culled (lazy loading).

## Related algorithms in cOde(n)

- **[geometric_03 - Line Intersection](geometric_03_line-segment-intersection.md)** — The 1D line equivalent logic.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
