# Depth-First Search (DFS) on a Grid

| | |
|---|---|
| **ID** | `search_04` |
| **Category** | searching |
| **Complexity (required)** | $O(R \times C)$ Time, $O(R \times C)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 10/10 |
| **LeetCode Equivalent** | [Number of Islands](https://leetcode.com/problems/number-of-islands/) |

## Problem statement

Given an R x C 2D grid representing a map of `'1'`s (land) and `'0'`s (water).
Return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

**Input:** A 2D array `grid`.
**Output:** An integer representing the number of islands.

## When to use it

- To find connected components in a matrix (e.g., finding the boundary of an object).
- When you need to exhaustively search all possible paths (Backtracking) rather than finding the shortest path (BFS).
- The most frequently asked algorithm pattern in software engineering interviews.

## Approach

**1. The "Maze Runner" Strategy:**
Unlike BFS which explores everything evenly like a ripple, DFS is like running through a maze by keeping your right hand strictly on the wall.
You go as deep as physically possible down a single path. You only turn around (backtrack) when you hit a dead end (water, a wall, or out of bounds).
When you hit a dead end, you take one step backward and try the next available direction.

**2. The Call Stack (LIFO):**
BFS uses an explicit Queue. DFS inherently uses the system's Call Stack.
When we call `dfs(r, c)`, the function immediately calls `dfs(r+1, c)`. The original function pauses and WAITS for the sub-function to completely finish exploring the entire downward path before it even considers checking `dfs(r-1, c)`.

**3. State Tracking (Sinking the Island):**
Just like BFS, if we don't track visited cells, we will bounce infinitely between two adjacent land cells.
Instead of using a separate `visited` set, a brilliant optimization for this specific problem is to modify the grid in-place! When we visit a land cell `'1'`, we instantly turn it into water `'0'` (sinking the island). This physically prevents us from ever revisiting it.

**4. The Main Loop:**
We iterate through every single cell in the grid with a nested double loop.
If we find water `'0'`, we ignore it.
If we find land `'1'`, it MUST be a brand new, undiscovered island! We increment our `island_count`, and then we launch the `dfs()` torpedo to recursively sink every single piece of connected land.
When the `dfs()` finishes, the entire island has been erased, ensuring we never double-count it.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_04: DFS on a 2D grid.

Explore reachable cells depth-first using a LIFO stack.
O(n^2) for an n x n grid.

The engine no longer ships a TrackedStack - the player
brings their own (a plain list with .append() / .pop()
gives the standard LIFO semantics; a plain list is fine
here because the engine doesn't count plain-list ops
and the budget is enforced by the grid reads / writes).
"""


def solve(grid, start, size):
    visited = set()
    stack = [start]
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and grid[nr][nc] == 0:
                stack.append((nr, nc))
    return len(visited)
```

</details>

## Walk-through

Grid:
`1 1 0`
`1 0 0`
`0 0 1`
`island_count = 0`.

1. `r=0, c=0`: `grid[0][0] == '1'`.
   - `island_count = 1`.
   - Call `dfs(0, 0)`.
2. **Inside `dfs(0, 0)`**:
   - `grid[0][0] = '0'`.
   - Call `dfs(1, 0)` (Down).
3. **Inside `dfs(1, 0)`**:
   - `grid[1][0] = '0'`.
   - Call `dfs(2, 0)` (Down) -> Base case (`grid[2][0] == '0'`). Returns.
   - Call `dfs(0, 0)` (Up) -> Base case (It's already `0`!). Returns.
   - Call `dfs(1, 1)` (Right) -> Base case (`0`). Returns.
   - Call `dfs(1, -1)` (Left) -> Base case (Out of bounds). Returns.
   - `dfs(1, 0)` finishes!
4. **Back in `dfs(0, 0)`**:
   - Call `dfs(-1, 0)` (Up) -> Out of bounds.
   - Call `dfs(0, 1)` (Right) -> It's `'1'`!
5. **Inside `dfs(0, 1)`**:
   - `grid[0][1] = '0'`.
   - Calls Down, Up, Right, Left -> All hit base cases.
   - `dfs(0, 1)` finishes!
6. **Back in `dfs(0, 0)`**:
   - Call `dfs(0, -1)` (Left) -> Out of bounds.
   - `dfs(0, 0)` finishes! Top-left island is completely erased.

Grid is now:
`0 0 0`
`0 0 0`
`0 0 1`

7. Loop continues until `r=2, c=2`.
   - `grid[2][2] == '1'`.
   - `island_count = 2`.
   - `dfs(2, 2)` sinks the bottom-right island.

Result: `2`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(R \times C)$ | $O(1)$ |
| **Average** | $O(R \times C)$ | $O(R \times C)$ |
| **Worst** | $O(R \times C)$ | $O(R \times C)$ |

The nested `for` loop checks all R x C cells. The `dfs` function visits each piece of land exactly once (and checks its neighbors). Therefore, every cell is processed a constant number of times. Time complexity is exactly $O(R x C)$.
Space complexity relies on the recursion Call Stack. In the worst-case scenario (the entire grid is one massive winding snake-shaped island), the DFS will go R x C levels deep into recursion before unwinding. Space complexity is $O(R x C)$.
*(If the grid is entirely water, DFS is never called, yielding $O(1)$ space).*

## Variants & optimizations

- **Word Search (`backtracking_04`):** When looking for a specific sequence of characters, you use DFS. But crucially, you must UN-SINK the island (backtrack: `grid[r][c] = original_char`) after exploring, because another word path might need to cross over that same letter later!
- **Union-Find (`graph_09`):** Number of Islands can also be solved iteratively in $O(R x C \cdot \alpha(N)$) time using a Disjoint Set structure, which connects adjacent '1's into graph components and counts the total distinct roots.

## Real-world applications

- **Minesweeper:** When you click a cell with "0" adjacent mines, the game automatically runs DFS/BFS to instantly expand and clear all connected "0" cells.

## Related algorithms in cOde(n)

- **[search_03 - BFS on a Grid](search_03_bfs-grid.md)** — The iterative, Queue-based sister algorithm used for finding shortest paths.
- **[graphs_01 - DFS](../graphs/graph_01_dfs.md)** — The exact same logic applied to generalized Nodes and Edges instead of a 2D matrix.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
