# Magnetic Force Between Two Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1552 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [magnetic-force-between-two-balls](https://leetcode.com/problems/magnetic-force-between-two-balls/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/magnetic-force-between-two-balls/).

### Goal
Place `m` balls into given basket positions so the minimum distance between any
two chosen positions is as large as possible.

### Function Contract
**Inputs**

- `position`: available basket coordinates.
- `m`: the number of balls to place.

**Return value**

The maximum achievable minimum pairwise distance.

### Examples
**Example 1**

- Input: `position = [1, 2, 3, 4, 7], m = 3`
- Output: `3`

**Example 2**

- Input: `position = [5, 4, 3, 2, 1, 1000000000], m = 2`
- Output: `999999999`

**Example 3**

- Input: `position = [1, 2, 8, 12, 17], m = 3`
- Output: `7`

---

## Solution
### Approach
Sort the positions and binary-search the candidate minimum distance. For a fixed
distance, greedily place balls from left to right whenever the next position is
far enough from the last chosen one. If at least `m` balls fit, the distance is
feasible.

### Complexity Analysis
- **Time Complexity**: `O(n log n + n log R)`, where `R` is the coordinate range.
- **Space Complexity**: `O(1)` extra space if sorting in place.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(position, m):
    points = sorted(set(position))
    if m <= 1 or len(points) <= 1:
        return 0
    if m > len(points):
        m = len(points)

    def can_place(distance):
        count = 1
        last = points[0]
        for point in points[1:]:
            if point - last >= distance:
                count += 1
                last = point
                if count >= m:
                    return True
        return False

    low = 0
    high = points[-1] - points[0]
    while low < high:
        mid = (low + high + 1) // 2
        if can_place(mid):
            low = mid
        else:
            high = mid - 1
    return low
```
</details>
