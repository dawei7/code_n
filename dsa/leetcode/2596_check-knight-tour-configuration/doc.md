# Check Knight Tour Configuration

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2596 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-knight-tour-configuration](https://leetcode.com/problems/check-knight-tour-configuration/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-knight-tour-configuration/).

### Goal
Given an $n \times n$ grid representing a sequence of moves made by a knight on a chessboard, determine if the sequence forms a valid knight's tour. A valid tour must start at the top-left corner (0, 0) with the value 0, and each subsequent move must follow the standard L-shaped movement pattern of a knight, visiting every cell from 0 to $n^2 - 1$ exactly once.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers of size $n \times n$ representing the order in which cells were visited.

**Return value**

- `bool`: Returns `True` if the provided grid represents a valid knight's tour, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]`
- Output: `True`

**Example 2**

- Input: `grid = [[0,3,6],[5,8,1],[2,7,4]]`
- Output: `False`

---

## Solution
### Approach
The problem is solved using **Simulation**. Since the grid contains exactly one instance of every number from $0$ to $n^2 - 1$, we can map each value to its coordinate $(r, c)$. We then iterate through the sequence from $0$ to $n^2 - 1$ and verify that the distance between the coordinates of step $i$ and step $i+1$ satisfies the knight's move condition: $|r_1 - r_2| \times |c_1 - c_2| = 2$ (specifically, the set of absolute differences must be $\{1, 2\}$).

### Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the dimension of the grid. We traverse the grid once to map the positions and once to validate the moves.
- **Space Complexity**: $O(n^2)$ to store the mapping of each step value to its $(r, c)$ coordinate.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> bool:
    n = len(grid)
    # Map each step value to its (row, col) coordinate
    pos = [None] * (n * n)
    for r in range(n):
        for c in range(n):
            pos[grid[r][c]] = (r, c)

    # A valid tour must start at (0, 0)
    if grid[0][0] != 0:
        return False

    # Validate each consecutive move
    for i in range(n * n - 1):
        r1, c1 = pos[i]
        r2, c2 = pos[i + 1]

        dr = abs(r1 - r2)
        dc = abs(c1 - c2)

        # A knight move is valid if the absolute differences are {1, 2}
        # This is equivalent to checking if the product is 2 and sum is 3
        if not ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
            return False

    return True
```
</details>
