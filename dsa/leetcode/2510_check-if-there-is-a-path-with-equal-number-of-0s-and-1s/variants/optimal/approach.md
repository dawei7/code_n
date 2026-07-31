## General

**Reject an impossible path length first**

Every path from `(0, 0)` to `(r - 1, c - 1)` makes exactly `r - 1` downward moves and `c - 1` rightward moves, so it visits $r+c-1$ cells. Equal counts of zeros and ones require this length to be even. If it is odd, no arrangement of values along a path can satisfy the goal.

For an even path length $L=r+c-1$, a valid path must contain exactly $L/2$ ones. This converts the question into a bounded reachability problem.

**Propagate reachable one-counts through the grid**

For each cell, retain the set of counts of ones attainable by some path ending there. Its predecessor can only be the cell above or the cell to the left, so combine the reachable sets from those two locations and add the current cell's binary value to every count. Counts above the target $L/2$ can be discarded because later cells can never decrease them.

Use one array of sets indexed by column. Before processing a cell, its slot still represents the cell above; after replacement it represents the current cell. The preceding slot already represents the cell to the left in the current row. This preserves exactly the same transitions as a full two-dimensional table while using only one row of state.

The initial cell begins from a virtual count of zero, then contributes its own value like every other cell. By induction over row-major order, a count belongs to a cell's set exactly when a legal path reaches that cell with that many ones. The destination contains the target precisely when a balanced path exists.

## Complexity detail

Each reachable set contains at most $O(r+c)$ distinct counts. Combining and advancing sets at all $rc$ cells takes $O(rc(r+c))$ time in the worst case. The rolling array holds $c$ sets, each with at most $O(r+c)$ counts, giving $O(c(r+c))$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every path:** Depth-first search without memoized count state is direct but can explore $\binom{r+c-2}{r-1}$ paths, which is exponential in the grid dimensions.
- **Three-dimensional boolean table:** Storing `reachable[row][col][ones]` gives the same transitions and time bound but uses $O(rc(r+c))$ space instead of rolling one row.
- **Difference instead of one-count:** Tracking `ones - zeros` is equivalent; the target becomes zero and the state range includes negative values.
- **Odd path length:** Equal integer counts cannot sum to an odd number, so the answer is immediately `False`.
- **Endpoint cells:** Both endpoints contribute to the count; initializing before the first cell avoids accidentally omitting `grid[0][0]`.
- **Repeated counts from different paths:** A set merges them safely because future transitions depend only on the count and current position, not on the route taken.
