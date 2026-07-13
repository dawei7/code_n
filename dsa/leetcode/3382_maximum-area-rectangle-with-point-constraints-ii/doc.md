# Maximum Area Rectangle With Point Constraints II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3382 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Indexed Tree, Segment Tree, Geometry, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-area-rectangle-with-point-constraints-ii](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/).

### Goal
Given a set of points in a 2D plane, find the maximum area of a rectangle whose sides are parallel to the coordinate axes, such that all four corners of the rectangle are present in the input set, and no other points from the input set lie strictly inside or on the boundary of the rectangle.

### Function Contract
**Inputs**

- `x`: A list of integers representing the x-coordinates of the points.
- `y`: A list of integers representing the y-coordinates of the points.

**Return value**

- An integer representing the maximum area found, or -1 if no such rectangle exists.

### Examples
**Example 1**

- Input: `x = [1, 1, 3, 3], y = [1, 3, 1, 3]`
- Output: `4`

**Example 2**

- Input: `x = [1, 1, 3, 3, 2], y = [1, 3, 1, 3, 2]`
- Output: `-1`

**Example 3**

- Input: `x = [1, 1, 3, 3, 1, 3], y = [1, 3, 1, 3, 2, 2]`
- Output: `2`

---

## Solution
### Approach
The problem is solved by grouping points by their x-coordinates and identifying potential vertical segments. By sorting these segments by their x-coordinates, we can use a sweep-line approach combined with a Fenwick Tree (Binary Indexed Tree) or a Segment Tree to efficiently query the existence of points within a specific y-range. The constraint of "no points inside" is handled by verifying that no points exist between the two vertical edges of a candidate rectangle.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where N is the number of points. This accounts for sorting the points and performing sweep-line operations with logarithmic time queries.
- **Space Complexity**: `O(N)` to store the points, the coordinate mapping, and the auxiliary data structures used for the sweep-line.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(x: list[int], y: list[int]) -> int:
    points = list(zip(x, y))
    columns = defaultdict(list)
    for px, py in points:
        columns[px].append(py)

    segment_columns = defaultdict(list)
    for px, ys in columns.items():
        ys.sort()
        for lower, upper in zip(ys, ys[1:]):
            segment_columns[(lower, upper)].append(px)

    candidates = []
    for (lower, upper), xs in segment_columns.items():
        xs.sort()
        for left, right in zip(xs, xs[1:]):
            candidates.append((left, right, lower, upper))

    if not candidates:
        return -1

    compressed_y = {value: index + 1 for index, value in enumerate(sorted(set(y)))}
    size = len(compressed_y)
    tree = [0] * (size + 1)

    def add(index: int) -> None:
        while index <= size:
            tree[index] += 1
            index += index & -index

    def prefix(index: int) -> int:
        total = 0
        while index > 0:
            total += tree[index]
            index -= index & -index
        return total

    def range_sum(lower: int, upper: int) -> int:
        return prefix(compressed_y[upper]) - prefix(compressed_y[lower] - 1)

    events = []
    for query_index, (left, right, lower, upper) in enumerate(candidates):
        events.append((right, query_index, 1, lower, upper))
        events.append((left - 1, query_index, -1, lower, upper))
    events.sort(key=lambda event: event[0])

    sorted_points = sorted(points)
    point_index = 0
    counts = [0] * len(candidates)

    for limit, query_index, sign, lower, upper in events:
        while point_index < len(sorted_points) and sorted_points[point_index][0] <= limit:
            add(compressed_y[sorted_points[point_index][1]])
            point_index += 1
        counts[query_index] += sign * range_sum(lower, upper)

    best = -1
    for count, (left, right, lower, upper) in zip(counts, candidates):
        if count == 4:
            best = max(best, (right - left) * (upper - lower))

    return best
```
</details>
