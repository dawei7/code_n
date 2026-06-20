# Rat in a Maze

| | |
|---|---|
| **ID** | `backtrack_05` |
| **Category** | backtracking |
| **Complexity (required)** | $O(4^(N^2)$) Time, $O(N^2)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **GeeksForGeeks Equivalent** | [Rat in a Maze](https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/) |

## Problem statement

Consider a rat placed at `(0, 0)` in a square `N x N` matrix. It has to reach the destination at `(N - 1, N - 1)`. Find all possible paths that the rat can take to reach from source to destination.
The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).
Value `0` at a cell in the matrix represents that it is blocked and cannot be crossed, while value `1` represents an open path.

**Input:** An `N x N` integer matrix.
**Output:** A list of strings, where each string represents a valid path (e.g. `"DDRR"`).

## When to use it

- To demonstrate classical **2D Grid Backtracking**.
- When you need to find *all* paths, or the *exact sequence of moves*, rather than just the shortest distance (which would be BFS).

## Approach

**1. The Decision Tree:**
At any cell `(r, c)` in the maze, the rat has up to 4 choices: move Up, Down, Left, or Right.
If a move leads to a wall (`0`) or goes out of bounds, that branch is pruned immediately.
Crucially, if a move leads to a cell the rat has *already visited on this specific path*, the branch must be pruned to prevent infinite loops (e.g., oscillating Left and Right forever)!

**2. The Backtracking State:**
`backtrack(r, c, current_path)`:
- `r`, `c`: The current row and column coordinates of the rat.
- `current_path`: A string or list of characters representing the moves taken so far (e.g., `["D", "R", "D"]`).

**3. State Management (The Visited Array):**
Because the rat can move in all 4 directions, we MUST track which cells are currently in the path.
We can use a separate `visited` boolean matrix.
- **Make Choice:** Mark `visited[r][c] = True`. Append move to `current_path`.
- **Recurse:** Call `backtrack()` for the adjacent cell.
- **Backtrack:** Mark `visited[r][c] = False`! This is critical! We un-visit the cell so that a completely *different* path can eventually use this cell later!

**4. Base Case:**
When `r == N - 1` and `c == N - 1`, the rat has reached the cheese!
Append `"".join(current_path)` to the global result list and return.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for backtrack_05: Rat in a Maze.

Find a path from (0, 0) to (n-1, n-1) in a 0/1 maze. 1 = open.
Move 4-neighbour. Backtracking DFS.
"""


def solve(maze, n):
    if n == 0 or maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []
    visited = [[False] * n for _ in range(n)]
    path = []

    def helper(r, c):
        if r == n - 1 and c == n - 1:
            path.append((r, c))
            return True
        if r < 0 or c < 0 or r >= n or c >= n:
            return False
        if visited[r][c] or maze[r][c] == 0:
            return False
        visited[r][c] = True
        path.append((r, c))
        if helper(r + 1, c) or helper(r, c + 1):
            return True
        path.pop()
        return False

    if helper(0, 0):
        return path
    return []
```

</details>

## Walk-through

`maze = [[1, 0], [1, 1]]`. N=2.

1. `backtrack(0, 0, [])`:
   - `visited[0][0] = True`.
   - Try 'D' (Down): `nr = 1, nc = 0`. Cell is `1`. Not visited.
     - Append 'D'. Path=`["D"]`.
     - `backtrack(1, 0, ["D"])`:
       - `visited[1][0] = True`.
       - Try 'D': Out of bounds.
       - Try 'L': Out of bounds.
       - Try 'R' (Right): `nr = 1, nc = 1`. Cell is `1`. Not visited.
         - Append 'R'. Path=`["D", "R"]`.
         - `backtrack(1, 1, ["D", "R"])`:
           - `r=1, c=1 == N-1`. BASE CASE! Append `"DR"` to result. Return.
         - Pop 'R'.
       - Try 'U' (Up): `nr = 0, nc = 0`. Cell is `1`, BUT `visited[0][0]` is True! Prune.
       - `visited[1][0] = False`.
     - Pop 'D'.
   - Try 'L': Out of bounds.
   - Try 'R': `nr = 0, nc = 1`. Cell is `0` (Wall). Prune.
   - Try 'U': Out of bounds.
   - `visited[0][0] = False`.

Result: `["DR"]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2)$ | $O(N^2)$ |
| **Average** | $O(3^(N^2)$) | $O(N^2)$ |
| **Worst** | $O(4^(N^2)$) | $O(N^2)$ |

In the absolute worst-case (a completely open matrix of 1s), the rat can wander endlessly taking extremely long, winding paths. At each cell, it has up to 3 valid choices (excluding the cell it just came from). The path length can be up to N^2. Thus, the upper bound time complexity is roughly $O(3^{N^2})$ or $O(4^{N^2})$.
Space complexity is $O(N^2)$ for the recursive call stack (which can go as deep as the total number of cells in the grid), and $O(N^2)$ for the `visited` boolean matrix.

## Variants & optimizations

- **In-Place Modification (Space Optimization):** You can completely drop the $O(N^2)$ `visited` matrix! When visiting `maze[r][c]`, temporarily mutate it to `0` (or `-1`). When backtracking, mutate it back to `1`. This saves memory, but mutating input references is often discouraged in production.

## Real-world applications

- **Robot Vacuum Pathfinding:** Calculating all exhaustive topological sweeps for a cleaning robot across an obstructed floor plan.

## Related algorithms in cOde(n)

- **[graph_01 - BFS (Shortest Path)](../graphs/graph_01_bfs.md)** — If the question only asks for the *shortest* path, BFS finds it in strictly $O(N^2)$ time, dwarfing Backtracking's exponential time!
- **[backtrack_06 - Knight's Tour](backtrack_06_knight-s-tour.md)** — Another 2D grid backtracking algorithm, but with highly restricted L-shaped jumps.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
