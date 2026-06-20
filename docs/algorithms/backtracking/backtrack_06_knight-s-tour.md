# Knight's Tour

| | |
|---|---|
| **ID** | `backtrack_06` |
| **Category** | backtracking |
| **Complexity (required)** | $O(8^(N^2)$) Time, $O(N^2)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Knight's tour](https://en.wikipedia.org/wiki/Knight%27s_tour) |

## Problem statement

Given an `N x N` empty chessboard, a knight starts at the first block `(0, 0)` and must make exactly `N^2 - 1` legal "L-shaped" moves to visit every single square on the board exactly once.
Find and return the matrix representing the exact sequence of moves the knight makes. The starting square should be marked `0`, the next square `1`, and so on. If no such tour exists, return an empty matrix.

**Input:** An integer `N`.
**Output:** An `N x N` matrix populated with integers from `0` to `N^2 - 1` representing the step numbers.

## When to use it

- To showcase pure exhaustion of a 2D constraint satisfaction problem.
- A classic theoretical CS problem that demonstrates how heuristics (Warnsdorff's Rule) can vastly optimize brute-force Backtracking.

## Approach

**1. The Decision Tree:**
At any square `(r, c)`, the knight has exactly 8 possible L-shaped jumps.
If a jump goes out of bounds, or lands on a square that already has a step number \ge 0, it is invalid and pruned.

**2. The Backtracking State:**
`backtrack(r, c, move_number)`:
- `r`, `c`: The current coordinates of the knight.
- `move_number`: An integer from `1` to `N^2 - 1` tracking the current depth of the tour.

**3. State Management (The Chessboard):**
We use an `N x N` matrix `board` initialized entirely to `-1`.
- **Make Choice:** `board[r][c] = move_number`.
- **Recurse:** Loop through all 8 valid jumps, calling `backtrack(next_r, next_c, move_number + 1)`. If ANY of those recursive calls returns `True`, it means the board is successfully completed! We instantly return `True` to bubble up the success.
- **Backtrack:** `board[r][c] = -1`. The knight lifts off the square so a different path can try it later.

**4. Base Case:**
When `move_number == N * N`, it means we have successfully placed the knight N^2 times! The tour is complete. Return `True`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for backtrack_06: Knight's Tour.

For a board of size n, find any sequence of knight moves that
visits every cell exactly once. Backtracking with Warnsdorff's
heuristic: at each step, prefer the move with the fewest
onward neighbours.
"""


def solve(n):
    if n <= 1:
        return [(0, 0)] if n == 1 else []
    if n < 5:
        return []
    visited = [[False] * n for _ in range(n)]
    path = []
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def degree(r, c):
        count = 0
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                count += 1
        return count

    def helper(r, c, step):
        visited[r][c] = True
        path.append((r, c))
        if step == n * n:
            return True
        candidates = []
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                candidates.append((degree(nr, nc), nr, nc))
        candidates.sort()
        for _, nr, nc in candidates:
            if helper(nr, nc, step + 1):
                return True
        visited[r][c] = False
        path.pop()
        return False

    if helper(0, 0, 1):
        return path
    return []
```

</details>

## Walk-through

*(Knight's Tour on N < 5 is mathematically impossible! We will conceptually walk through a dead end on N=3).*

`N = 3`. Start at `(0, 0)`. `board[0][0] = 0`.
`backtrack(0, 0, 1)`:
- Try jumps:
  - `i=0 (+2, +1)`: `nr=2, nc=1`. Valid!
    - `board[2][1] = 1`.
    - `backtrack(2, 1, 2)`:
      - Try jumps from `(2, 1)`:
        - `(-2, -1)` lands on `(0, 0)` -> Visited!
        - `(-2, +1)` lands on `(0, 2)`. Valid!
          - `board[0][2] = 2`.
          - `backtrack(0, 2, 3)`:
            - Try jumps from `(0, 2)`:
              - `(+2, -1)` lands on `(2, 1)` -> Visited!
              - All other 7 jumps go out of bounds. Loop ends.
          - Backtrack: `board[0][2] = -1`. Return False.
      - All jumps from `(2, 1)` exhausted.
    - Backtrack: `board[2][1] = -1`. Return False.
- All jumps from `(0, 0)` exhausted.
Return False.

Result: `[]` (No tour exists for a 3x3 board).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2)$ | $O(N^2)$ |
| **Average** | $O(8^(N^2)$) | $O(N^2)$ |
| **Worst** | $O(8^(N^2)$) | $O(N^2)$ |

At every square, the knight has up to 8 choices. The tour requires N^2 steps.
The brute force upper bound time complexity is an astronomical $O(8^{N^2})$. For an 8 x 8 board, 8^{64} is computationally impossible to solve via raw brute force without extreme luck in branch ordering.
Space complexity is $O(N^2)$ for the board and the recursion call stack depth.

## Variants & optimizations

- **Warnsdorff's Heuristic:** This is the magic trick that makes Knight's Tour solvable in real-time! Instead of blindly looping through the 8 jumps in a static order, you should **sort the 8 jumps** based on *how many onward jumps they have available*. You must greedily jump to the square that has the FEWEST onward options! By doing this, the knight is forced to visit the edges and corners first, preventing it from getting trapped. This drops the practical time complexity to near $O(N^2)$!

## Real-world applications

- **Cryptography:** Used in designing encryption algorithms and pseudo-random number generators where ensuring maximum spatial diffusion over a memory grid is required without repeating states.

## Related algorithms in cOde(n)

- **[backtrack_05 - Rat in a Maze](backtrack_05_rat-in-a-maze.md)** — The foundational 2D tracking problem with only 4 directions and static walls.
- **[backtrack_02 - Permutations](backtrack_02_permutations.md)** — Generating a Knight's Tour is mathematically equivalent to generating a specific permutation of the N^2 squares constrained by L-jumps.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
