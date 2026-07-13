# Maximum Points Inside the Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3143 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-points-inside-the-square](https://leetcode.com/problems/maximum-points-inside-the-square/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-points-inside-the-square/).

### Goal
Given a set of points on a 2D plane, each associated with a character tag, determine the maximum number of points that can be enclosed within a square centered at the origin (0,0) such that no two points inside the square share the same character tag. The square's sides must be parallel to the coordinate axes.

### Function Contract
**Inputs**

- `points`: A list of lists where each element `[x, y]` represents the coordinates of a point.
- `s`: A string where `s[i]` is the character tag associated with `points[i]`.

**Return value**

- An integer representing the maximum number of points that can be contained in a square centered at (0,0) without any duplicate tags.

### Examples
**Example 1**

- Input: `points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"`
- Output: `2`

**Example 2**

- Input: `points = [[1,1],[-2,2],[-2,2]], s = "abb"`
- Output: `1`

**Example 3**

- Input: `points = [[1,1],[-1,-1],[2,-2]], s = "ccd"`
- Output: `0`

---

## Solution
### Approach
The problem relies on the observation that a point `(x, y)` is inside a square of side length `2 * side` if `max(|x|, |y|) < side`. To ensure no duplicate tags, we track the minimum distance (Chebyshev distance) for each character. If two points share the same tag, the square must be smaller than the distance of the *second* closest point of that tag. We identify the threshold distance `min_second_dist` (the smallest distance among all points that share a tag with another point) and count all points whose distance is strictly less than this threshold.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of points, as we iterate through the points once to populate a hash map and once to count valid points.
- **Space Complexity**: `O(K)`, where `K` is the size of the alphabet (at most 26), used to store the minimum and second-minimum distances for each character tag.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(points: list[list[int]], s: str) -> int:
    # min_dist[char] stores the smallest Chebyshev distance for a given tag
    # second_min_dist stores the smallest distance where a tag conflict occurs
    min_dist = {}
    second_min_dist = float('inf')

    for i in range(len(points)):
        x, y = points[i]
        char = s[i]
        # Chebyshev distance from origin is max(|x|, |y|)
        dist = max(abs(x), abs(y))

        if char in min_dist:
            # If we've seen this char, update the conflict threshold
            # using the second-smallest distance for this specific tag.
            second_min_dist = min(second_min_dist, max(dist, min_dist[char]))
            # Keep track of the absolute minimum for this char
            min_dist[char] = min(min_dist[char], dist)
        else:
            min_dist[char] = dist

    count = 0
    # Any point with distance strictly less than the conflict threshold is valid
    for char in min_dist:
        if min_dist[char] < second_min_dist:
            count += 1

    return count
```
</details>
