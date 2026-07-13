# Find the Number of Ways to Place People I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3025 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Geometry, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-number-of-ways-to-place-people-i](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/).

### Goal
Given a set of 2D points representing people on a grid, determine the number of pairs of points (A, B) such that A can "fence" B. A point A can fence point B if A is located at the top-left of B (i.e., $x_A \le x_B$ and $y_A \ge y_B$) and there are no other points located within the rectangular region defined by A and B, excluding A and B themselves.

### Function Contract
**Inputs**

- `points`: A list of lists, where each inner list contains two integers `[x, y]` representing the coordinates of a person.

**Return value**

- An integer representing the total count of valid pairs (A, B) that satisfy the fencing condition.

### Examples
**Example 1**

- Input: `points = [[1,1],[2,2],[3,3]]`
- Output: `0`

**Example 2**

- Input: `points = [[6,2],[4,4]]`
- Output: `1`

**Example 3**

- Input: `points = [[3,1],[1,3],[1,1]]`
- Output: `2`

---

## Solution
### Approach
The problem is solved using a sorting-based enumeration approach. First, we sort the points primarily by their x-coordinate (ascending) and secondarily by their y-coordinate (descending). This ordering ensures that for any pair (A, B) where A comes before B in the sorted list, A is guaranteed to be to the left of or at the same x-position as B. By iterating through all pairs and checking the y-coordinate condition ($y_A \ge y_B$) and verifying that no intermediate points exist within the rectangle, we can count the valid pairs.

### Complexity Analysis
- **Time Complexity**: $O(n^3)$, where $n$ is the number of points. We iterate through all pairs ($O(n^2)$) and for each pair, we iterate through all other points to check if they lie within the rectangle ($O(n)$).
- **Space Complexity**: $O(1)$ (excluding the space required for sorting), as we only use a few variables for counting and indexing.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(points: list[list[int]]) -> int:
    # Sort points: x ascending, then y descending.
    # This ensures that if i < j, then points[i][0] <= points[j][0].
    # If points[i][0] <= points[j][0] and points[i][1] >= points[j][1],
    # then point i is top-left of point j.
    points.sort(key=lambda p: (p[0], -p[1]))

    n = len(points)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Since we sorted by x ascending and y descending:
            # x1 <= x2 is guaranteed.
            # We need y1 >= y2 for point i to be top-left of point j.
            if y1 >= y2:
                # Check if any other point k is inside the rectangle defined by i and j.
                # A point k is inside if x1 <= xk <= x2 and y2 <= yk <= y1.
                # We already know i and j are the corners.
                is_valid = True
                for k in range(n):
                    if k == i or k == j:
                        continue

                    xk, yk = points[k]
                    if x1 <= xk <= x2 and y2 <= yk <= y1:
                        is_valid = False
                        break

                if is_valid:
                    count += 1

    return count
```
</details>
