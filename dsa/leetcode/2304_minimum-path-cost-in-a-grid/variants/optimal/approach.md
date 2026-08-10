## General

**Turn the grid into a sequence of row decisions**

A valid path chooses exactly one cell from every row. After choosing column `k` in row `i - 1`, the path may choose any column `j` in row `i`. The price of that one step has two new parts: the move price `moveCost[grid[i - 1][k]][j]` and the value `grid[i][j]` of the cell that has just been entered. The value of the previous cell must not be added again because it was already paid when that cell became part of the path.

This row-by-row structure is the reason dynamic programming fits. Once a path has reached a particular cell in the previous row, the exact sequence of still earlier columns no longer affects any future charge. Future move costs depend on the value of the current cell and on the next destination column, while all earlier charges can be summarized by one number: the cheapest total cost for reaching the current cell.

The solution stores those summaries in `f`. Before row `i` is processed, `f[k]` means:

> the minimum complete cost of a path that starts somewhere in row `0`, ends at `grid[i - 1][k]`, and includes every visited cell value and every move cost paid so far.

This definition is important because it tells us exactly what the transition still needs to add and prevents both missing and double-counting charges.

**Why the first row is the base case**

The path may begin in any first-row cell. Reaching that starting cell involves no move, so its cost is only its own value. Therefore the code initializes `f = grid[0]`. At that moment, `f[k] = grid[0][k]` is precisely the cheapest cost of a path ending in column `k` of the first row: there is only one such zero-move path.

This assignment initially makes `f` refer to the existing first row rather than to a copy. That is safe in this implementation because it never changes an entry of `f`. For each later row it creates a separate list `g`, fills `g`, and finally replaces the local reference with `f = g`. Consequently, the input grid is not modified.

**Compute every possible destination in the next row**

For each later row `i`, the code creates `g` with `n` entries initialized to infinity. Entry `g[j]` will become the minimum cost for reaching column `j` of this row.

To determine `g[j]`, every previous-row column `k` must be considered. There is no adjacency restriction: the statement permits a move from any cell in one row to any column in the following row. If the best path summarized by `f[k]` is extended from `grid[i - 1][k]` to `grid[i][j]`, its new total is

`f[k] + moveCost[grid[i - 1][k]][j] + grid[i][j]`.

Each term has a separate role:

- `f[k]` pays for the entire prefix through the previous cell.
- `moveCost[grid[i - 1][k]][j]` pays for this particular transition. Its row is selected by the value stored in the source cell, not by the source cell's row or column index.
- `grid[i][j]` pays for entering the destination cell.

The update keeps the minimum of this candidate and the current `g[j]`. After all `k` have been tried, `g[j]` is the cheapest way to reach that destination from any cell in the preceding row. After every destination `j` is complete, assigning `f = g` advances the dynamic-programming frontier by one row.

As a small conceptual trace, suppose the previous frontier is `f = [7, 4]` and the destination cell has value `5`. If the two relevant move costs are `3` and `9`, the two complete candidates are `7 + 3 + 5 = 15` and `4 + 9 + 5 = 18`. The smaller previous prefix does not necessarily produce the smaller new path because its move cost may be larger. That is why the algorithm must compare the full transition totals, not merely choose the smallest entry of `f`.

**Why keeping only one cost per cell is sufficient**

Consider any destination `grid[i][j]`. Every valid path reaching it must come from exactly one column `k` in row `i - 1`. For that fixed `k`, using anything other than the minimum-cost prefix represented by `f[k]` cannot help: the last move and destination value are identical no matter how the path reached `grid[i - 1][k]`, so a more expensive prefix remains more expensive after extension. It is therefore safe to discard all nonminimum prefixes ending at the same previous cell.

The inner loop explicitly evaluates the extension from every possible `k`. It consequently includes the final step of every possible path to `grid[i][j]` and selects the least expensive one. This proves that each newly computed `g[j]` satisfies the same meaning that `f[k]` had for the previous row. The base case satisfies that meaning in row `0`, so induction over the rows shows that the final `f[j]` is the minimum cost of any complete path ending at column `j` of the last row.

A complete path may end in any last-row column. Returning `min(f)` therefore compares all permitted endpoints and gives the minimum cost over all complete paths.

**A useful graph interpretation**

The grid can be viewed as a layered directed acyclic graph. Every cell is a vertex, and each cell in one row has an edge to every cell in the next row. An edge from source column `k` to destination column `j` carries the move charge plus the destination cell value. The first-row cell values act as starting distances. Processing rows from top to bottom is then shortest-path relaxation in topological order. The code does not build this graph because the grid and `moveCost` table already provide every edge weight when it is needed.

## Complexity detail

Let `m` be the number of rows and `n` the number of columns. There are `m - 1` transitions between consecutive rows. For each transition, the algorithm computes `n` destinations, and each destination examines all `n` possible source columns. Every candidate uses constant-time indexing, addition, comparison, and assignment. The running time is therefore `O((m - 1)n^2)`, which is written as `O(mn^2)`.

The algorithm does not store a dynamic-programming value for every grid cell at once. It retains only the previous frontier `f` and the new frontier `g`, each of length `n`. Thus the auxiliary space is `O(n)`. During the first iteration, `f` aliases `grid[0]`, but subsequent frontiers are newly allocated, and no input row is modified. The space occupied by the given `grid` and `moveCost` inputs is not counted as auxiliary space.

The numerical value infinity is only a safe initial sentinel for a minimum. Every destination has at least one possible predecessor, so each `g[j]` is replaced by a finite candidate before the row finishes. Python integers also grow as necessary, so adding the allowed nonnegative costs does not overflow.

## Alternatives and edge cases

- **Full two-dimensional dynamic programming:** Store the best cost for every cell in an `m` by `n` table. The recurrence is the same and the running time remains `O(mn^2)`, but the table consumes `O(mn)` space even though only the immediately preceding row is needed.
- **Explicit shortest-path graph:** Create all cell vertices and all `(m - 1)n^2` directed edges, then run a shortest-path procedure. This obscures the simple layered order and spends substantial memory materializing transitions that the nested loops can evaluate directly.
- **Greedily choosing the cheapest next cell or move:** A locally cheap destination can have expensive outgoing moves in later rows. Similarly, the cheapest prefix in `f` may have a costly transition to a particular destination. Only the full dynamic-programming comparison preserves enough information to make the global choice.
- **Using the source column as the move-cost row:** The lookup is `moveCost[grid[i - 1][k]][j]`. The source cell's value selects the row of `moveCost`; replacing it with `k` silently computes a different problem.
- **Forgetting the starting cell value:** The first row has no incoming move cost, but its selected cell still belongs to the path. Initializing every first-row state to zero would omit that required charge.
- **Adding the previous cell twice:** Its value is already included in `f[k]`. A transition adds only the move cost and the newly entered destination value.
- **Several equally cheap predecessors:** The minimum update may keep any one of them because the task asks only for the cost, not for the path itself. Equal candidates give the same state value and identical future possibilities from the destination cell.
- **One available destination per row:** Although the stated constraints provide at least two columns, the recurrence also naturally works for `n = 1`: each row has one predecessor and one destination.
- **Only one row:** The official constraints require at least two rows, but the initialization and final `min(f)` would still correctly return the smallest first-row value if a one-row input were supplied.
