## General

**Reuse one row of minimum costs**

The array named `sum` stores dynamic-programming costs. Before updating column `j` in a later row, `sum[j]` is the minimum cost to the cell directly above, while `sum[j-1]` has already been updated to the minimum cost for the cell directly left in the current row.

The recurrence is therefore

`sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]`.

This implements the same two-dimensional DP while overwriting values that will never be needed again.

**Copy and initialize the first row**

`sum = list(grid[0])` creates a separate list, so later updates do not modify the input's first row. Initially it contains raw cell values, not path costs.

The first loop turns it into prefix sums. For every `j > 0`, only the left predecessor exists in row 0, so adding `sum[j-1]` produces the cost of the unique all-right path to that cell. `sum[0]` already equals the starting value and needs no change.

**Update the first column of each later row**

Before scanning the interior of row `i`, `sum[0] += grid[i][0]` extends the unique all-down path. There is no left predecessor in column 0, so retaining the above cost and adding the current cell is the only legal update.

This separate boundary step lets the interior loop start at column 1 without invalid indexing.

**Mix old-row and new-row values intentionally**

At interior column `j`, `sum[j]` has not yet been overwritten in this row and therefore represents the above cost. `sum[j-1]` was overwritten in the previous inner-loop iteration and represents the left cost. Taking their minimum and adding the current cell computes the current state.

After assignment, `sum[j]` changes meaning from previous-row cost to current-row cost. At the end of the row, all entries represent that row, ready to serve as above costs for the next iteration.

**Trace the rolling state**

For `[[1,3,1],[1,5,1],[4,2,1]]`, copying and prefixing the first row gives `[1,4,5]`. The second row updates to `[2,7,6]`: first column 2, then `min(2,4)+5=7`, then `min(7,5)+1=6`. The final row becomes `[6,8,7]`, and the last entry is returned.

**Why the recurrence produces a global minimum**

Every valid path to an interior cell ends with a down move from above or a right move from the left. The rolling invariant guarantees `sum` exposes the exact minimum for both predecessors at update time. Adding the current value to the cheaper one constructs the cheapest current path.

Any more expensive path reaching the same cell can be discarded because all future continuations from that coordinate are identical choices and add the same suffix costs. By induction across the row-major scan, the final array entry is the global minimum to the destination.

**The name `sum` shadows a built-in**

Using `sum` as a local variable hides Python's built-in `sum` function inside this method. The source never needs that built-in, so behavior is unaffected. A more descriptive name such as `dp` would reduce reader confusion but would not change the algorithm.

**Input and output behavior**

The first row is copied and all later arithmetic occurs in that copy. The original grid remains unchanged. The return value is the final scalar cost, not the rolling array.

Copying rather than aliasing the first row is important. If `sum` directly referred to `grid[0]`, prefix initialization would overwrite the caller's first-row cell values. `list(grid[0])` gives the DP state its own storage while still requiring only one row of memory.

## Complexity detail

The first-row prefix loop and later nested loops process each of the $mn$ cells at most once. Time is $O(mn)$.

The rolling list contains $n$ integers, while other variables are scalar. Auxiliary space is $O(n)$, matching the manifest. The source comment's $O(m+n)$ is a looser bound; no row-sized structure proportional to $m$ is stored.

## Alternatives and edge cases

- **Full DP table:** It preserves every intermediate value for visualization but uses $O(mn)$ space.
- **Use the shorter dimension:** With careful orientation, a rolling array of length $\min(m,n)$ can reduce memory further when the grid is very tall or wide.
- **In-place grid update:** Store minimum costs directly in `grid` for constant auxiliary space, at the cost of mutating input.
- **Memoized recursion:** It expresses the choice naturally but uses cached states and a call stack.
- **One cell:** The copied first entry is returned without either loop changing it.
- **One row:** Prefix accumulation computes the only possible route.
- **One column:** Each outer iteration updates only `sum[0]`.
- **Zero costs:** Minimum comparison and addition handle them naturally.
- **Non-negative guarantee:** It bounds behavior intuitively, though acyclic DP does not require it for correctness.
- **Built-in shadowing:** Local `sum` prevents calls to the built-in inside the method but causes no current defect.
