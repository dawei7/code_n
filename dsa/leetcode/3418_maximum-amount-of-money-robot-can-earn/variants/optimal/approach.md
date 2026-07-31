## General

For each cell, distinguish paths by the exact number of robbers already neutralized: zero, one, or two. A state stores the greatest profit reaching that cell with that count. The predecessor for each count is the larger of the state directly above and the state directly to the left.

Entering the current cell normally adds its value to every reachable predecessor state. If the value is negative and fewer than two neutralizations have been used, a second transition moves from state `used` to `used + 1` without adding the negative value. Keeping both transitions matters because saving a neutralization for a later, larger loss may be better.

Only the previous row and the already-computed prefix of the current row are needed. In a single array indexed by column, `dp[column]` still represents the cell above before it is overwritten, while `dp[column - 1]` represents the cell to the left. The start cell receives an imaginary predecessor with profit zero and no neutralizations, so its positive, negative, and neutralized possibilities follow the same transition.

Every path to a cell must arrive from above or left, and its treatment of the current negative cell is either normal or neutralized. The recurrence considers exactly these exhaustive choices and retains the best profit for every neutralization count. Induction in row-major order therefore proves each state optimal, and the largest of the three destination states is the answer for *at most two* neutralizations.

## Complexity detail

Let the grid contain $m$ rows and $n$ columns. Each of the $mn$ cells performs constant work for three states, so time is $O(mn)$. The row-compressed array stores three values for each of $n$ columns, using $O(n)$ auxiliary space.

The benchmark defines `size` as the cell count $mn$ and uses $4\times4$, $10\times10$, and $20\times20$ grids, spanning 25x. The accepted topological dynamic program is linear in `size`. A correct generic relaxation method that scans cells in reverse order for $m+n-1$ passes takes $O(mn(m+n))$ time and must fail only the scaling verdict.

## Alternatives and edge cases

- **Greedily neutralize the first two robbers:** A later robber may impose a much larger loss, so neutralization usage belongs in the DP state.
- **Keep only the best profit regardless of neutralizations:** A slightly worse prefix with an unused ability can dominate after a future negative cell.
- **Enumerate all monotone paths:** The number of routes is combinatorial in $m+n$ and is infeasible for 500-by-500 grids.
- **Repeated generic relaxation:** It eventually finds the same optimum but ignores the grid's known topological order and performs unnecessary passes.
- **Negative start or destination:** Either cell may be neutralized, and the uniform transition handles both.
- **All-positive grid:** The zero-neutralization state remains best; using fewer than two abilities is allowed.
- **All-negative grid:** Exactly two selected losses can become zero, but the result may still be negative.
- **Single row or column:** Each cell has only one possible predecessor, and the same recurrence applies.
