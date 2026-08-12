# Su Doku - Optimal Approach

## Algorithm Explanation

Solve $50$ Sudoku puzzles from `sudoku.txt` and return the sum of the $3$-digit numbers formed by the top-left cells `grid[0][0..2]` of each solution.

### Constraint Satisfaction & MRV Backtracking:
To solve all $50$ grids rapidly:
1. Parse $50$ $9 \times 9$ integer matrices from `sudoku.txt`.
2. Employ **Minimum Remaining Values (MRV)** heuristic search:
   - For every empty cell $(r, c)$, compute the set of valid digits compliant with row, column, and $3 \times 3$ sub-box constraints.
   - Select the empty cell with the fewest available candidate choices.
   - If a cell has $0$ valid choices, prune the search tree immediately (dead end).
3. Recursively fill cells using depth-first backtracking.
4. Extract `grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]` for each completed grid and sum across all $50$ solutions.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(50 \times T)$ where $T \le 100$ recursive states per grid. Runs in $< 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary recursion stack memory.
