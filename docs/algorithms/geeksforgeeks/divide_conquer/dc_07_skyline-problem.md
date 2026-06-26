# The Skyline Problem

| | |
|---|---|
| **ID** | `dc_07` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) |

## Problem statement

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
The buildings are given as an array of `buildings` where `buildings[i] = [left_i, right_i, height_i]`.
The skyline should be returned as a list of "key points" `[x_i, y_i]` sorted by their x-coordinate. A key point is the left endpoint of a horizontal line segment representing the top of a building.

**Input:** A 2D integer array `buildings`.
**Output:** A 2D integer array of key points forming the skyline contour.

## When to use it

- To demonstrate advanced Divide and Conquer merging, particularly how to merge two separate lists of overlapping intervals/coordinates.
- Note: This problem is equally famous for its Priority Queue (Max-Heap) solution. Both are acceptable and $O(N \log N)$.

## Approach

**1. The Divide Step:**
If we only have ONE building `[L, R, H]`, the skyline is trivial! It's just two key points: the top-left corner `[L, H]`, and the bottom-right corner where the building drops back to the ground `[R, 0]`.
We can divide the array of N buildings exactly in half recursively until every slice contains exactly one building!

**2. The Conquer (Merge) Step:**
The absolute hardest part of the problem. We have two skylines, `left_skyline` and `right_skyline`, both sorted by their X coordinates. We need to merge them into a single `merged_skyline`.
We use two pointers, `i` for the left skyline and `j` for the right skyline.
We also need to keep track of the *current height* of both skylines as we sweep across them. Let's call them `h1` (left) and `h2` (right).

- We pick whichever key point has the SMALLER X coordinate. Let's say `left_skyline[i]` is further left.
- We update our current `h1` to be `left_skyline[i].y`.
- What is the global height of the merged skyline at this X coordinate? Because the buildings overlap, the true height is simply the MAXIMUM of the current heights of both skylines! `max_h = max(h1, h2)`.
- If this `max_h` is DIFFERENT from the height of the last point we added to `merged_skyline`, it means the skyline just changed elevation! We add `[x, max_h]` to our `merged_skyline`.
- We increment `i`.
*(If the X coordinates are exactly identical, we update BOTH `h1` and `h2`, pick the max, and increment BOTH `i` and `j`)*.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_07: Skyline Problem.

Given n axis-aligned rectangular buildings as
"""


def solve(buildings, n):
    """Skyline via D&C: recurse, then merge two skylines."""
    if n == 0:
        return []
    if n == 1:
        l, h, r = buildings[0]
        return [[l, h], [r, 0]]
    mid = n // 2
    left = solve(buildings[:mid], mid)
    right = solve(buildings[mid:], n - mid)
    return _merge(left, right)

def _merge(left, right):
    result = []
    h1 = h2 = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x, h1 = left[i][0], left[i][1]
            i += 1
        elif left[i][0] > right[j][0]:
            x, h2 = right[j][0], right[j][1]
            j += 1
        else:
            x = left[i][0]
            h1 = left[i][1]
            h2 = right[j][1]
            i += 1
            j += 1
        h = max(h1, h2)
        if not result or result[-1][1] != h:
            result.append([x, h])
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
```

</details>

## Walk-through

*(Conceptual)*
`sk1 = [[2, 10], [9, 0]]` (Building 1)
`sk2 = [[3, 15], [7, 0]]` (Building 2)

1. `i=0`, `j=0`. `x1=2`, `x2=3`. `x1 < x2`.
   `x=2`, `h1=10`. `max_h = max(10, 0) = 10`.
   Add `[2, 10]`. `i=1`.
2. `i=1`, `j=0`. `x1=9`, `x2=3`. `x2 < x1`.
   `x=3`, `h2=15`. `max_h = max(10, 15) = 15`.
   Add `[3, 15]`. `j=1`.
3. `i=1`, `j=1`. `x1=9`, `x2=7`. `x2 < x1`.
   `x=7`, `h2=0`. `max_h = max(10, 0) = 10`.
   Add `[7, 10]`. `j=2`.
4. `j` is exhausted. Append remainder of `sk1`.
   Add `[9, 0]`. `i=2`.

Merged result: `[[2, 10], [3, 15], [7, 10], [9, 0]]`. ✓ (The skyline jumps up at 2, jumps higher at 3, drops back to the first building's roof at 7, and drops to the ground at 9).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

The recursion tree splits in half exactly like Merge Sort ($O(\log N)$ depth).
At each level, the `merge_skylines` function iterates through the sub-skylines linearly. The total merging work at any specific level of the tree sums to $O(N)$.
Therefore, T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Space complexity is $O(N)$ because the newly merged arrays at the top level will contain up to 2N points.

## Variants & optimizations

- **Sweep Line + Max-Heap:** The more common approach. Instead of dividing the buildings, you break every building into two "events": `(Left, Height, ENTER)` and `(Right, Height, EXIT)`. You sort all 2N events by their X coordinate. As you sweep left-to-right, if you hit an ENTER event, you push the height into a Max-Heap. If you hit an EXIT event, you lazily remove that height from the Max-Heap. The current top of the heap is ALWAYS the current skyline height! Also strictly $O(N \log N)$.

## Real-world applications

- **Computer Graphics (Hidden Surface Determination):** In 2D rendering engines, this exact algorithm determines which sprites (like mountains or parallax background layers) are visually occluding the layers behind them, allowing the engine to skip rendering the hidden pixels completely.

## Related algorithms in cOde(n)

- **[sort_01 - Merge Sort](../sorting/sort_01_merge-sort.md)** — The literal exact identical Divide and Conquer architectural pattern.
- **[heap_03 - Sweep Line Skyline](../heap/heap_03_sweep-line-skyline.md)** — The priority queue variant of this exact problem.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
