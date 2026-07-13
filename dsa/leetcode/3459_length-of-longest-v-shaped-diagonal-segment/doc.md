# Length of Longest V-Shaped Diagonal Segment

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3459 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Memoization, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [length-of-longest-v-shaped-diagonal-segment](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/).

### Goal
Given a 2D grid containing values 0, 1, and 2, find the length of the longest "V-shaped" diagonal segment. A V-shaped segment starts at a '2', moves diagonally through a sequence of '1's, reaches a '0' (the vertex), and then moves diagonally back through a sequence of '1's. The path must maintain a consistent diagonal direction (e.g., top-left to bottom-right, then bottom-left to top-right).

### Function Contract
**Inputs**

- `grid`: A 2D list of integers where each cell is 0, 1, or 2.

**Return value**

- An integer representing the maximum length of a valid V-shaped segment. If no such segment exists, return 0.

### Examples
**Example 1**

- Input: `grid = [[2,2,1],[1,0,1],[1,1,1]]`
- Output: `5`

**Example 2**

- Input: `grid = [[1,2,1],[0,1,0],[1,1,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[2,0,0],[0,0,0],[0,0,0]]`
- Output: `1`

---

## Solution
### Approach
The problem is solved using Dynamic Programming on a grid. We define four states for each cell representing the four possible diagonal directions. We compute the length of the "downward" path (from 2 to 1s) and the "upward" path (from 0 to 1s) using memoization. The V-shape is formed by connecting a downward path ending at a 0 with an upward path starting from that same 0.

### Complexity Analysis
- **Time Complexity**: O(M * N), where M is the number of rows and N is the number of columns, as each cell is visited a constant number of times for each of the four diagonal directions.
- **Space Complexity**: O(M * N) to store the memoization tables for the four directions.

### Reference Implementations
<details>
<summary>python</summary>

```python
from array import array


def solve(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    total = rows * cols
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    values = [value for row in grid for value in row]

    def ordered_indices(dr: int, dc: int):
        row_range = range(rows - 1, -1, -1) if dr > 0 else range(rows)
        col_range = range(cols - 1, -1, -1) if dc > 0 else range(cols)
        for row in row_range:
            base = row * cols
            for col in col_range:
                yield row, col, base + col

    straight: list[tuple[array, array]] = []
    for dr, dc in directions:
        take_two = array("H", [0]) * total
        take_zero = array("H", [0]) * total
        for row, col, idx in ordered_indices(dr, dc):
            next_row, next_col = row + dr, col + dc
            next_idx = next_row * cols + next_col
            has_next = 0 <= next_row < rows and 0 <= next_col < cols
            if values[idx] == 2:
                take_two[idx] = 1 + (take_zero[next_idx] if has_next else 0)
            elif values[idx] == 0:
                take_zero[idx] = 1 + (take_two[next_idx] if has_next else 0)
        straight.append((take_two, take_zero))

    answer = 1 if any(value == 1 for value in values) else 0
    for direction, (dr, dc) in enumerate(directions):
        turn_direction = (direction + 1) % 4
        turn_dr, turn_dc = directions[turn_direction]
        turn_two, turn_zero = straight[turn_direction]
        best_two = array("H", [0]) * total
        best_zero = array("H", [0]) * total
        for row, col, idx in ordered_indices(dr, dc):
            next_row, next_col = row + dr, col + dc
            next_idx = next_row * cols + next_col
            has_next = 0 <= next_row < rows and 0 <= next_col < cols
            turn_row, turn_col = row + turn_dr, col + turn_dc
            turn_idx = turn_row * cols + turn_col
            has_turn = 0 <= turn_row < rows and 0 <= turn_col < cols
            if values[idx] == 2:
                keep = best_zero[next_idx] if has_next else 0
                turn = turn_zero[turn_idx] if has_turn else 0
                best_two[idx] = 1 + max(keep, turn)
            elif values[idx] == 0:
                keep = best_two[next_idx] if has_next else 0
                turn = turn_two[turn_idx] if has_turn else 0
                best_zero[idx] = 1 + max(keep, turn)
        for row in range(rows):
            next_row = row + dr
            if next_row < 0 or next_row >= rows:
                continue
            row_base = row * cols
            next_base = next_row * cols
            for col in range(cols):
                next_col = col + dc
                if values[row_base + col] == 1 and 0 <= next_col < cols:
                    answer = max(answer, 1 + best_two[next_base + next_col])
    return answer
```
</details>
