## General

Every legal movement goes either right or down. Therefore, reaching cell `(i, j)` can happen only from `(i - 1, j)` or `(i, j - 1)`. This one-way structure turns the grid into a directed acyclic graph and makes dynamic programming sufficient: once the cheapest costs for the upper and left neighbors are known, no other earlier cell can enter `(i, j)` directly.

The alternating movement-and-wait rule initially seems to require a time-parity state. It does not. Every path to `(i, j)` uses exactly `i + j` moves, because each move increases one coordinate by one. More importantly, the schedule is forced: after entering an intermediate cell on an odd-numbered movement second, the traveler must pay that cell's waiting cost before taking the next move. There is no choice to wait extra seconds, skip a wait, or change the parity.

**Which cells pay waiting cost**

The path pays the entrance cost of every visited cell, including `(0, 0)` and the destination. Waiting costs have two exceptions:

- no waiting cost is paid at `(0, 0)` before the first move;
- no waiting cost is paid at the destination because the trip ends immediately upon reaching it.

Every other visited cell is an intermediate stopping point, so its wait cost is mandatory.

The source handles the destination exception with a convenient accounting technique. During the DP, it adds both the entrance and waiting cost for every non-start cell, including the destination. After finishing, it subtracts `waitCost[-1][-1]` exactly once. This produces the true arrival cost without needing a special branch inside the nested loop.

**A full-table recurrence**

Imagine first that `best[i][j]` stores the minimum cost to reach `(i, j)` and, for a non-start cell, also pay the wait associated with staying there until the next move. Then:

$$
\textit{best}[0][0]=1,
$$

because entering `(0, 0)` costs `(0+1)(0+1)=1` and no initial wait is due.

For every other cell:

$$
\textit{best}[i][j]
=
\min(\textit{best}[i-1][j],\textit{best}[i][j-1])
+(i+1)(j+1)
+\textit{waitCost}[i][j],
$$

where a predecessor outside the grid is treated as infinity. The first additional term is the cell's entrance cost, and the second is the provisionally included wait.

The final result is:

$$
\textit{best}[m-1][n-1]-\textit{waitCost}[m-1][n-1].
$$

**Compressing the table to one row**

The source does not allocate `m * n` DP entries. When processing one row from left to right, only two predecessor values are needed:

- `dp[column]` still holds the value from the previous row, so it is `from_above`;
- `dp[column - 1]` has already been updated for the current row, so it is `from_left`.

After calculating the current cell, assigning the result back to `dp[column]` safely discards the no-longer-needed value from above. At the end of a row, the same array represents that completed row.

The top boundary naturally works because all entries except `dp[0]` start at infinity. The left boundary uses infinity explicitly when `column == 0`. The loop skips `(0, 0)` so its initialized cost of 1 is not overwritten.

**Why the grid may be transposed conceptually**

A rolling row normally needs one value per column, giving `O(n)` space. To guarantee `O(\min(m,n))` space, the source chooses the smaller dimension as `width`:

- if `n <= m`, it traverses the original orientation with `height = m` and `width = n`;
- if `n > m`, it uses `height = n` and `width = m`, treating the grid as transposed.

When transposed, an internal position `(row, column)` corresponds to original position `(column, row)`. The assignment

`original_row, original_column = (column, row)`

performs that mapping before reading `waitCost` or calculating the entrance cost.

Transposition preserves the problem. A right move in the internal grid may represent a down move in the original grid, and an internal down move may represent an original right move, but both are legal and have the same cost determined by the mapped destination cell. Start and destination remain opposite corners.

**Following the 2-by-2 example**

The initial rolling state is `[1, infinity]`. At original cell `(0, 1)`, the only finite predecessor is the left cell, so the provisional value becomes:

`1 + 2 + waitCost[0][1] = 1 + 2 + 5 = 8`.

At `(1, 0)`, the only finite predecessor is above:

`1 + 2 + waitCost[1][0] = 1 + 2 + 2 = 5`.

At destination `(1, 1)`, the cheaper predecessor is 5. Adding entrance cost 4 and provisional destination wait 4 gives 13. The return statement subtracts that last wait, yielding 9. This corresponds to entering the start, moving down, waiting at `(1, 0)`, and moving right into the destination.

**Why taking the cheaper predecessor is correct**

Consider an optimal path to a non-start cell. Its last move must come from above or left. Before that last move, the prefix of the path must itself be a cheapest valid path to that predecessor. If it were not, replacing it with a cheaper predecessor path would preserve the forced schedule and reduce the total cost, contradicting optimality.

The recurrence examines both possible final moves and adds exactly the costs caused by entering and then provisionally waiting at the current cell. By induction in row-major traversal order, every stored DP value is optimal. Subtracting the destination's artificial wait leaves exactly the requested arrival cost.

## Complexity detail

Let the grid contain `m` rows and `n` columns. The nested loops visit each of the `mn` cells once, and every visit performs constant-time arithmetic, comparisons, and array access. Time complexity is `O(mn)`.

The rolling array has length `width = \min(m,n)`. All other state consists of scalar variables, so auxiliary space is `O(\min(m,n))`. The input `waitCost` is read but never copied or modified.

The numeric costs can grow with the path length and cell values. Python integers expand as needed, so the implementation has no fixed-width overflow. Under the usual unit-cost arithmetic model used by the manifest, this does not change the stated bounds.

## Alternatives and edge cases

- **Full two-dimensional DP:** It uses the same recurrence and is easier to visualize, but requires `O(mn)` space instead of the source's `O(\min(m,n))`.
- **Shortest-path algorithm:** Dijkstra would work on a suitable state graph, but the right/down movement graph is acyclic and the waiting schedule is fixed, so a heap adds unnecessary overhead.
- **Add explicit parity to the state:** Parity is determined by the number of moves and no optional waiting is allowed, making such a state redundant.
- **Special-case the destination in the loop:** Omitting its wait during recurrence is valid. The source's add-then-subtract method keeps every non-start transition uniform.
- **One row:** The only possible path repeatedly moves right; the rolling recurrence uses only `from_left` after the start.
- **One column:** The only possible path repeatedly moves down; if transposed, it is processed exactly like a one-row grid.
- **Two cells:** The traveler moves directly to the destination and pays no wait. Adding and then subtracting the destination wait gives the correct result.
- **Zero waiting costs:** They simply contribute nothing; the recurrence still applies unchanged.
- **Very large waiting cost:** The DP may choose a geographically different monotone path to avoid that intermediate cell.
- **Equal predecessor costs:** Either last move is optimal, and storing only the value is sufficient because the path itself is not requested.
- **Entrance cost at the start:** `dp[0] = 1` includes it exactly once.
- **No wait at the start:** The initialization deliberately excludes `waitCost[0][0]`.
- **No wait at the destination:** The final subtraction removes exactly the provisional charge.
- **Conceptual transposition:** Coordinate mapping must be applied to both entrance and wait costs; the source computes both using `original_row` and `original_column`.
- **Input preservation:** Only the one-dimensional DP array is mutated. `waitCost` remains unchanged.
