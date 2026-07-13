# Zigzag Grid Traversal With Skip

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3417 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [zigzag-grid-traversal-with-skip](https://leetcode.com/problems/zigzag-grid-traversal-with-skip/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/zigzag-grid-traversal-with-skip/).

### Goal
Traverse a 2D grid in a zigzag pattern, starting from the top-left corner. Move row by row, alternating the direction of traversal (left-to-right for even-indexed rows, right-to-left for odd-indexed rows). During this traversal, collect every second element encountered, starting with the very first element at (0, 0).

### Function Contract
**Inputs**

- `grid`: A 2D list of integers (`List[List[int]]`) representing the matrix to traverse.

**Return value**

- A list of integers (`List[int]`) containing the elements collected during the zigzag traversal, skipping every other element.

### Examples
**Example 1**

- Input: `grid = [[1, 2], [3, 4]]`
- Output: `[1, 3]`

**Example 2**

- Input: `grid = [[2, 1], [2, 1], [2, 1]]`
- Output: `[2, 1, 2]`

**Example 3**

- Input: `grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]`
- Output: `[1, 3, 5, 9, 7]`

---

## Solution
### Approach
The problem is solved using a **Simulation** approach. We iterate through the rows of the matrix, maintaining a flag or checking the row index to determine the traversal direction. For even rows, we iterate from index `0` to `n-1`; for odd rows, we iterate from `n-1` down to `0`. A counter or a boolean toggle is used to track whether the current element should be included in the result list, ensuring we pick every second element.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns, as we visit each cell in the grid exactly once.
- **Space Complexity**: `O(k)`, where `k` is the number of elements collected (approximately `(m * n) / 2`), required to store the output list.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(grid: List[List[int]]) -> List[int]:
    result = []
    take = True

    for r in range(len(grid)):
        # Determine the range based on row index
        # Even rows: left to right (0 to n-1)
        # Odd rows: right to left (n-1 to 0)
        if r % 2 == 0:
            cols = range(len(grid[r]))
        else:
            cols = range(len(grid[r]) - 1, -1, -1)

        for c in cols:
            if take:
                result.append(grid[r][c])
            take = not take

    return result
```
</details>
