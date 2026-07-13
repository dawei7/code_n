# Maximize the Distance Between Points on a Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3464 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Geometry, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-the-distance-between-points-on-a-square](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/).

### Goal
Given a square with side length `side` and a set of points located on its perimeter, you must select `k` points from the given set such that the minimum Manhattan distance between any two selected points is maximized. The perimeter is defined by coordinates (0,0) to (side, side).

### Function Contract
**Inputs**

- `side`: An integer representing the side length of the square.
- `points`: A list of lists, where each inner list `[x, y]` represents the coordinates of a point on the perimeter.
- `k`: An integer representing the number of points to select.

**Return value**

- An integer representing the maximum possible value of the minimum Manhattan distance between any two selected points.

### Examples
**Example 1**

- Input: `side = 4, points = [[0,0],[0,1],[0,2],[0,3],[0,4],[1,4],[2,4],[3,4],[4,4],[4,3],[4,2],[4,1],[4,0],[3,0],[2,0],[1,0]], k = 4`
- Output: `4`

**Example 2**

- Input: `side = 3, points = [[0,0],[1,0],[2,0],[3,0],[3,1],[3,2],[3,3],[2,3],[1,3],[0,3],[0,2],[0,1]], k = 3`
- Output: `4`

**Example 3**

- Input: `side = 2, points = [[0,0],[1,0],[2,0],[2,1],[2,2],[1,2],[0,2],[0,1]], k = 4`
- Output: `2`

---

## Solution
### Approach
The problem is solved using **Binary Search on the Answer**. Since the minimum distance is monotonic (if a distance `d` is achievable, any distance `d' < d` is also achievable), we search for the largest `d` in the range `[0, 4 * side]`. For a fixed distance `d`, we use a **Greedy approach** to check if it is possible to pick `k` points such that every pair is at least distance `d` apart. We map the 2D perimeter points to a 1D linear scale `[0, 4 * side)` to simplify distance calculations.

### Complexity Analysis
- **Time Complexity**: `O(N log N + N log(4 * side))`, where `N` is the number of points. Sorting the points takes `O(N log N)`, and the binary search performs `O(log(4 * side))` iterations, each taking `O(N)` to verify the greedy condition.
- **Space Complexity**: `O(N)` to store the linearized coordinates of the points.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(side: int, points: list[list[int]], k: int) -> int:
    def perimeter_position(x: int, y: int) -> int:
        if y == 0:
            return x
        if x == side:
            return side + y
        if y == side:
            return 3 * side - x
        return 4 * side - y

    perimeter = 4 * side
    positions = sorted(perimeter_position(x, y) for x, y in points)
    n = len(positions)
    doubled = positions + [position + perimeter for position in positions]

    def feasible(distance: int) -> bool:
        next_index = [0] * (2 * n)
        pointer = 0
        for index in range(2 * n):
            if pointer < index + 1:
                pointer = index + 1
            while pointer < 2 * n and doubled[pointer] - doubled[index] < distance:
                pointer += 1
            next_index[index] = pointer

        for start in range(n):
            current = start
            possible = True
            for _ in range(k - 1):
                current = next_index[current]
                if current >= start + n:
                    possible = False
                    break
            if possible and doubled[current] - doubled[start] <= perimeter - distance:
                return True
        return False

    low, high = 1, perimeter // k
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if feasible(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer
```
</details>
