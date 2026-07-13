# Length of the Longest Increasing Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3288 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [length-of-the-longest-increasing-path](https://leetcode.com/problems/length-of-the-longest-increasing-path/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/length-of-the-longest-increasing-path/).

### Goal
Given a list of 2D points and an index `k`, determine the length of the longest sequence of points that includes `coordinates[k]` and is strictly increasing in both x-coordinate and y-coordinate.

### Function Contract
**Inputs**

- `coordinates`: A list of lists of integers, where each inner list `[x, y]` represents a point in a 2D plane.
- `k`: An integer index identifying the point that must be included in the path.

**Return value**

- An integer representing the maximum number of points in an increasing sequence that includes the starting point `k`.

### Examples
**Example 1**

- Input: `coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]]`, `k = 1`
- Output: `3`
- Explanation: One possible path is `[0,0] -> [2,2] -> [5,3]`.

**Example 2**

- Input: `coordinates = [[2,1],[7,0],[5,6]]`, `k = 0`
- Output: `2`
- Explanation: One possible path is `[2,1] -> [5,6]`.

**Example 3**

- Input: `coordinates = [[4,5],[2,2],[6,7],[2,3],[5,4],[3,3]]`, `k = 5`
- Output: `4`
- Explanation: One possible path is `[2,2] -> [3,3] -> [5,4] -> [6,7]`.

---

## Solution
### Approach
The problem is a variation of the "Longest Increasing Subsequence" (LIS) problem. We split the points into two sets: those that can precede `k` (where `x < kx` and `y < ky`) and those that can follow `k` (where `x > kx` and `y > ky`). For the preceding set, we sort by `x` ascending and `y` ascending to find the LIS. For the following set, we sort by `x` ascending and `y` descending to find the LIS. The result is `1 + LIS(preceding) + LIS(following)`.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of coordinates, due to sorting and the binary search approach for LIS.
- **Space Complexity**: `O(N)` to store the filtered points and the auxiliary array for the LIS calculation.

### Reference Implementations
<details>
<summary>python</summary>

```python
import bisect

def solve(coordinates: list[list[int]], k) -> int:
    if isinstance(k, int):
        kx, ky = coordinates[k]
    else:
        kx, ky = k

    # Points that can come before k: x < kx and y < ky
    before = [p for p in coordinates if p[0] < kx and p[1] < ky]
    # Equal x-values cannot both appear in a strictly increasing path.
    before.sort(key=lambda p: (p[0], -p[1]))

    # Points that can come after k: x > kx and y > ky
    after = [p for p in coordinates if p[0] > kx and p[1] > ky]
    # Sort by x ascending, then y descending
    # This allows us to find LIS on y-coordinates alone
    after.sort(key=lambda p: (p[0], -p[1]))

    def get_lis_len(points):
        if not points:
            return 0
        tails = []
        for _, y in points:
            idx = bisect.bisect_left(tails, y)
            if idx < len(tails):
                tails[idx] = y
            else:
                tails.append(y)
        return len(tails)

    return 1 + get_lis_len(before) + get_lis_len(after)
```
</details>
