# Minimize Manhattan Distances

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3102 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Geometry, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimize-manhattan-distances](https://leetcode.com/problems/minimize-manhattan-distances/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimize-manhattan-distances/).

### Goal
Given a set of 2D points, determine the minimum possible maximum Manhattan distance between any two points in the set after removing exactly one point from the collection.

### Function Contract
**Inputs**

- `points`: A list of lists, where each inner list contains two integers `[x, y]` representing the coordinates of a point.

**Return value**

- An integer representing the minimum possible value of the maximum Manhattan distance between any two remaining points after one point is removed.

### Examples
**Example 1**

- Input: `points = [[3,10],[5,15],[10,2],[4,4]]`
- Output: `12`

**Example 2**

- Input: `points = [[1,1],[1,1],[1,1]]`
- Output: `0`

**Example 3**

- Input: `points = [[3,10],[5,15],[10,2],[4,4],[1,1]]`
- Output: `14`

---

## Solution
### Approach
The Manhattan distance between $(x_1, y_1)$ and $(x_2, y_2)$ is $|x_1 - x_2| + |y_1 - y_2|$. This can be transformed using the coordinate rotation identity: $|x_1 - x_2| + |y_1 - y_2| = \max(|(x_1+y_1) - (x_2+y_2)|, |(x_1-y_1) - (x_2-y_2)|)$. By defining $u = x+y$ and $v = x-y$, the Manhattan distance becomes $\max(|u_1 - u_2|, |v_1 - v_2|)$. The maximum distance in the set is determined by the extreme values of $u$ and $v$. Removing a point that contributes to these extreme values is the only way to potentially reduce the maximum distance.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$ due to sorting the transformed coordinates (or $O(N)$ if using a single pass to find the top two extremes).
- **Space Complexity**: $O(N)$ to store the transformed coordinates.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(points: list[list[int]]) -> int:
    # Transform coordinates: u = x + y, v = x - y
    # Manhattan distance = max(|u1 - u2|, |v1 - v2|)
    transformed = []
    for x, y in points:
        transformed.append((x + y, x - y))

    def get_max_dist(indices_to_skip):
        min_u, max_u = float('inf'), float('-inf')
        min_v, max_v = float('inf'), float('-inf')

        for i in range(len(transformed)):
            if i in indices_to_skip:
                continue
            u, v = transformed[i]
            min_u, max_u = min(min_u, u), max(max_u, u)
            min_v, max_v = min(min_v, v), max(max_v, v)

        return max(max_u - min_u, max_v - min_v)

    # The maximum distance is determined by the points with min/max u or v.
    # We only need to check removing these specific points.
    candidates = set()
    for i in range(len(transformed)):
        u, v = transformed[i]
        # Check if this point is an extreme
        # We collect indices of points that define the current max distance
        pass

    # Find indices of points that result in min_u, max_u, min_v, max_v
    u_vals = [t[0] for t in transformed]
    v_vals = [t[1] for t in transformed]

    idx_min_u = u_vals.index(min(u_vals))
    idx_max_u = u_vals.index(max(u_vals))
    idx_min_v = v_vals.index(min(v_vals))
    idx_max_v = v_vals.index(max(v_vals))

    to_check = {idx_min_u, idx_max_u, idx_min_v, idx_max_v}

    ans = float('inf')
    for i in to_check:
        ans = min(ans, get_max_dist({i}))

    return ans
```
</details>
