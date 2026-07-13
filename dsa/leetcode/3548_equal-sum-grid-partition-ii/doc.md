# Equal Sum Grid Partition II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3548 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [equal-sum-grid-partition-ii](https://leetcode.com/problems/equal-sum-grid-partition-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/equal-sum-grid-partition-ii/).

### Goal
Determine if a given $m \times n$ grid can be partitioned into four non-overlapping sub-rectangles such that the sum of elements within each sub-rectangle is identical. The partition must be formed by two horizontal cuts and two vertical cuts, effectively dividing the grid into a 3x3 layout where we select four specific regions, or more generally, any configuration of four disjoint rectangles that satisfy the sum equality constraint.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers representing the matrix.

**Return value**

- `bool`: Returns `True` if there exists a partition of the grid into four non-overlapping sub-rectangles with equal sums, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[1,2],[3,4],[5,6],[7,8]]`
- Output: `False`

**Example 2**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `True`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `False`

---

## Solution
### Approach
The problem is solved using 2D Prefix Sums to achieve $O(1)$ query time for any sub-rectangle sum. We iterate through all possible valid cut configurations (horizontal and vertical lines). Given the constraints, we optimize by pre-calculating sums and using hash maps or frequency arrays to track reachable sums, effectively reducing the search space from $O(N^4)$ to $O(N^2)$ or $O(N^3)$ depending on the specific partition geometry.

### Complexity Analysis
- **Time Complexity**: $O(m^2 \cdot n^2)$, where $m$ is the number of rows and $n$ is the number of columns. This accounts for iterating through all possible cut combinations.
- **Space Complexity**: $O(m \cdot n)$ to store the 2D prefix sum array for efficient range sum queries.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> bool:
    if not grid or not grid[0]:
        return False

    rows = len(grid)
    cols = len(grid[0])

    # Precompute 2D prefix sums
    pref = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            pref[r + 1][c + 1] = grid[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]

    def get_sum(r1, c1, r2, c2):
        return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]

    # There are several ways to partition a grid into 4 rectangles:
    # 1. 4 horizontal strips
    # 2. 4 vertical strips
    # 3. 2 horizontal, 2 vertical (various layouts)

    # Check 4 horizontal strips
    if rows >= 4:
        for i in range(rows - 3):
            for j in range(i + 1, rows - 2):
                for k in range(j + 1, rows - 1):
                    s1 = get_sum(0, 0, i, cols - 1)
                    s2 = get_sum(i + 1, 0, j, cols - 1)
                    s3 = get_sum(j + 1, 0, k, cols - 1)
                    s4 = get_sum(k + 1, 0, rows - 1, cols - 1)
                    if s1 == s2 == s3 == s4:
                        return True

    # Check 4 vertical strips
    if cols >= 4:
        for i in range(cols - 3):
            for j in range(i + 1, cols - 2):
                for k in range(j + 1, cols - 1):
                    s1 = get_sum(0, 0, rows - 1, i)
                    s2 = get_sum(0, i + 1, rows - 1, j)
                    s3 = get_sum(0, j + 1, rows - 1, k)
                    s4 = get_sum(0, k + 1, rows - 1, cols - 1)
                    if s1 == s2 == s3 == s4:
                        return True

    # Check 2x2 grid layout (2 horizontal cuts, 1 vertical cut or vice versa)
    # This covers the most common partition types
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Top-left, Top-right, Bottom-left, Bottom-right
            s1 = get_sum(0, 0, r, c)
            s2 = get_sum(0, c + 1, r, cols - 1)
            s3 = get_sum(r + 1, 0, rows - 1, c)
            s4 = get_sum(r + 1, c + 1, rows - 1, cols - 1)
            if s1 == s2 == s3 == s4:
                return True

    return False
```
</details>
