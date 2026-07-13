# Count Cells in Overlapping Horizontal and Vertical Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3529 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Rolling Hash, String Matching, Matrix, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-cells-in-overlapping-horizontal-and-vertical-substrings](https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/).

### Goal
Given a 2D grid of characters, identify all cells that are simultaneously part of at least one horizontal substring matching a specific pattern and at least one vertical substring matching the same pattern. The goal is to return the total count of such unique cells.

### Function Contract
**Inputs**

- `grid`: A 2D list of characters (List[List[str]]).
- `pattern`: A string representing the sequence to search for (str).

**Return value**

- `int`: The count of unique cells `(r, c)` that belong to both a horizontal occurrence and a vertical occurrence of the `pattern`.

### Examples
**Example 1**

- Input: `grid = [["a","b","a"],["b","a","b"],["a","b","a"]], pattern = "aba"`
- Output: `5`
- Explanation: The center cell (1,1) and the four corner cells are part of both horizontal and vertical "aba" patterns.

**Example 2**

- Input: `grid = [["x","y"],["y","x"]], pattern = "xy"`
- Output: `0`
- Explanation: No cell is part of both a horizontal and vertical "xy" pattern.

**Example 3**

- Input: `grid = [["a","a","a"],["a","a","a"],["a","a","a"]], pattern = "aa"`
- Output: `9`
- Explanation: Every cell in the 3x3 grid is part of at least one horizontal and one vertical "aa" pattern.

---

## Solution
### Approach
The problem is solved using a 2D prefix-marking approach or a sliding window/rolling hash technique. We first identify all horizontal segments that match the pattern and mark the corresponding cells in a boolean matrix. We repeat this for vertical segments. Finally, we perform a bitwise AND operation on the two boolean matrices to count the cells that are marked in both.

### Complexity Analysis
- **Time Complexity**: `O(R * C * L)`, where `R` is the number of rows, `C` is the number of columns, and `L` is the length of the pattern. This accounts for checking every possible starting position for the pattern.
- **Space Complexity**: `O(R * C)` to store the boolean masks for horizontal and vertical matches.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(grid: List[List[str]], pattern: str) -> int:
    if not grid or not grid[0] or not pattern:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    p_len = len(pattern)

    # horizontal_mask[r][c] is True if grid[r][c] is part of a horizontal pattern
    horizontal_mask = [[False for _ in range(cols)] for _ in range(rows)]
    # vertical_mask[r][c] is True if grid[r][c] is part of a vertical pattern
    vertical_mask = [[False for _ in range(cols)] for _ in range(rows)]

    # Check horizontal patterns
    if cols >= p_len:
        for r in range(rows):
            for c in range(cols - p_len + 1):
                match = True
                for k in range(p_len):
                    if grid[r][c + k] != pattern[k]:
                        match = False
                        break
                if match:
                    for k in range(p_len):
                        horizontal_mask[r][c + k] = True

    # Check vertical patterns
    if rows >= p_len:
        for c in range(cols):
            for r in range(rows - p_len + 1):
                match = True
                for k in range(p_len):
                    if grid[r + k][c] != pattern[k]:
                        match = False
                        break
                if match:
                    for k in range(p_len):
                        vertical_mask[r + k][c] = True

    # Count intersections
    count = 0
    for r in range(rows):
        for c in range(cols):
            if horizontal_mask[r][c] and vertical_mask[r][c]:
                count += 1

    return count
```
</details>
