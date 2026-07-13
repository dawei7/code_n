# Number of Black Blocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2768 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-black-blocks](https://leetcode.com/problems/number-of-black-blocks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-black-blocks/).

### Goal
Given a grid of size `m x n` and a list of coordinates representing "black" cells, identify how many 2x2 subgrids contain exactly 0, 1, 2, 3, or 4 black cells. A 2x2 subgrid is defined by its top-left corner `(r, c)`, where `0 <= r < m-1` and `0 <= c < n-1`.

### Function Contract
**Inputs**

- `m`: An integer representing the number of rows.
- `n`: An integer representing the number of columns.
- `coordinates`: A list of lists, where each inner list `[r, c]` denotes the position of a black cell.

**Return value**

- A list of 5 integers where the index `i` represents the number of 2x2 subgrids containing exactly `i` black cells.

### Examples
**Example 1**

- Input: `m = 3, n = 3, coordinates = [[0,0]]`
- Output: `[3, 1, 0, 0, 0]`

**Example 2**

- Input: `m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]`
- Output: `[0, 2, 2, 0, 0]`

---

## Solution
### Approach
The problem is solved using a Hash Map (dictionary) to track the count of black cells for every affected 2x2 subgrid. Since a single black cell at `(r, c)` can be part of at most four 2x2 subgrids (top-left corners: `(r-1, c-1), (r-1, c), (r, c-1), (r, c)`), we iterate through the given coordinates, calculate these potential top-left corners, and increment their counts in the map if they fall within the valid grid boundaries. Finally, we calculate the number of subgrids with 0 black cells by subtracting the number of subgrids that have at least one black cell from the total possible 2x2 subgrids `(m-1) * (n-1)`.

### Complexity Analysis
- **Time Complexity**: `O(K)`, where `K` is the number of black cells. We perform a constant number of operations (at most 4) for each coordinate.
- **Space Complexity**: `O(K)`, as we store the counts of affected 2x2 subgrids in a hash map, which can contain at most `4K` entries.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(m: int, n: int, coordinates: list[list[int]]) -> list[int]:
    # A 2x2 subgrid is identified by its top-left corner (r, c).
    # Valid top-left corners are 0 <= r < m-1 and 0 <= c < n-1.
    # A black cell at (r, c) affects subgrids with top-left corners:
    # (r-1, c-1), (r-1, c), (r, c-1), (r, c)

    counts = {}
    for r, c in coordinates:
        for dr in range(-1, 1):
            for dc in range(-1, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m - 1 and 0 <= nc < n - 1:
                    counts[(nr, nc)] = counts.get((nr, nc), 0) + 1

    result = [0] * 5
    # Count how many subgrids have 1, 2, 3, or 4 black cells
    for val in counts.values():
        result[val] += 1

    # Total possible 2x2 subgrids
    total_subgrids = (m - 1) * (n - 1)
    # Subgrids with 0 black cells = Total - subgrids with at least 1 black cell
    result[0] = total_subgrids - sum(result[1:])

    return result
```
</details>
