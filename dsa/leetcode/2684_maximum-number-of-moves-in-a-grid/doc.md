# Maximum Number of Moves in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2684 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-moves-in-a-grid](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/).

### Goal
Given an `m x n` integer matrix, determine the maximum number of moves possible. A move can start from any cell in the first column. From a cell `(r, c)`, you can move to `(r-1, c+1)`, `(r, c+1)`, or `(r+1, c+1)`, provided the destination cell is within the grid boundaries and its value is strictly greater than the current cell's value. The objective is to find the longest sequence of such valid moves.

### Function Contract
**Inputs**

- `grid`: `List[List[int]]` - A 0-indexed `m x n` integer matrix.
  - `m` is the number of rows, `n` is the number of columns.
  - `1 <= m, n <= 1000`
  - `1 <= m * n <= 10^5`
  - `1 <= grid[i][j] <= 10^9`

**Return value**

- `int` - The maximum number of moves that can be made.

### Examples
**Example 1**

- Input: `grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]`
- Output: `3`
- Explanation: One possible path with 3 moves is `(0,0) -> (0,1) -> (1,2) -> (3,3)` (values: `2 -> 4 -> 9 -> 15`). Another is `(2,0) -> (3,1) -> (3,2) -> (3,3)` (values: `3 -> 9 -> 13 -> 15`).

**Example 2**

- Input: `grid = [[3,2,4],[2,1,9],[1,1,7]]`
- Output: `2`
- Explanation: One possible path with 2 moves is `(0,0) -> (0,1) -> (0,2)` (values: `3 -> 4 -> 9`).

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `0`
- Explanation: No moves are possible from any cell because no adjacent cell to the right has a strictly greater value.

---

## Solution
### Approach
This problem can be modeled as finding the longest path in a Directed Acyclic Graph (DAG). Since moves only proceed from left to right (increasing column index), there are no cycles. This structure is ideal for Dynamic Programming or a Breadth-First Search (BFS) variant.

**Dynamic Programming / BFS Layer-by-Layer Approach:**

1.  **State Definition:** Instead of storing the maximum moves *to* a cell `(r, c)`, we can simplify by tracking which cells are *reachable* at each column `c`. Let `current_reachable_rows` be a set of row indices `r` such that cell `(r, c)` is reachable.

2.  **Initialization:**
    *   Initially, all cells in the first column (`c=0`) are potential starting points. So, `current_reachable_rows` will contain all row indices from `0` to `m-1`.
    *   `max_moves` is initialized to `0`.

3.  **Iteration (Column by Column):**
    *   Iterate through columns `c` from `0` to `n-2` (since a move always increases the column index, we can make at most `n-1` moves).
    *   For each column `c`, create a `next_reachable_rows` set, initially empty.
    *   For every row `r` in `current_reachable_rows`:
        *   Consider the three possible next cells in column `c+1`: `(r-1, c+1)`, `(r, c+1)`, `(r+1, c+1)`.
        *   For each potential next cell `(nr, nc)`:
            *   Check if `(nr, nc)` is within grid boundaries (`0 <= nr < m`).
            *   Check if `grid[nr][nc]` is strictly greater than `grid[r][c]`.
            *   If both conditions are met, add `nr` to `next_reachable_rows`.
    *   After checking all reachable cells in column `c` and their potential moves to `c+1`:
        *   If `next_reachable_rows` is empty, it means no further moves are possible from column `c`. Break the loop.
        *   Otherwise, update `current_reachable_rows = next_reachable_rows` and increment `max_moves` by 1.

4.  **Result:** The final value of `max_moves` is the answer.

This approach effectively simulates a BFS where each "layer" corresponds to a column, and we count how many layers (columns) we can traverse.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`
    *   The outer loop iterates `n-1` times (for each column from `0` to `n-2`).
    *   Inside the loop, we iterate through `current_reachable_rows`. In the worst case, all `m` rows are reachable.
    *   For each reachable cell, we check at most 3 neighbors.
    *   Thus, the total operations are proportional to `(n-1) * m * 3`, which simplifies to `O(m * n)`.
- **Space Complexity**: `O(m)`
    *   We use two sets, `current_reachable_rows` and `next_reachable_rows`, to store row indices. Each set can hold at most `m` elements.
    *   Therefore, the space complexity is `O(m)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    # current_reachable_rows stores the row indices that are reachable in the current column.
    # Initially, all cells in the first column (column 0) are reachable.
    current_reachable_rows = set(range(m))
    max_moves = 0

    # Iterate through columns from 0 up to n-2.
    # A move takes us from column c to c+1.
    # If we make k moves, we reach column k.
    # The maximum possible moves is n-1 (reaching column n-1 from column 0).
    for c in range(n - 1):
        next_reachable_rows = set()

        # Iterate through all rows that were reachable in the current column 'c'.
        for r in current_reachable_rows:
            # Check the three possible moves: (r-1, c+1), (r, c+1), (r+1, c+1)
            for dr in [-1, 0, 1]:
                nr = r + dr  # next row
                nc = c + 1   # next column

                # Check boundary conditions for the next row
                if 0 <= nr < m:
                    # Check if the value in the next cell is strictly greater
                    if grid[nr][nc] > grid[r][c]:
                        next_reachable_rows.add(nr)

        # If no cells are reachable in the next column, we cannot make any more moves.
        if not next_reachable_rows:
            break

        # Update the set of reachable rows for the next iteration (next column).
        current_reachable_rows = next_reachable_rows
        # We successfully made one more move (moved to the next column).
        max_moves += 1

    return max_moves
```
</details>
