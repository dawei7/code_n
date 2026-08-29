## General

**Replace the round trip with two simultaneous forward paths**

The original journey goes from the top-left to the bottom-right and then returns by moving up or left. Reverse the return path in time. It becomes a second path from the top-left to the bottom-right that moves down or right.

This transformation is exact:

- Any legal outbound and return journey becomes two legal forward paths after reversing the return.
- Any two legal forward paths can be interpreted as the outbound path and the reverse of the return path.
- A cherry visited by both paths must be counted only once, matching the rule that the first visit removes it.

The problem is therefore to choose two down/right paths simultaneously and maximize the cherries in the union of their visited cells.

**Synchronize both travelers by step count**

After `k` moves from `(0, 0)`, a traveler at row `i` must be at column

`j = k - i`,

because every move increases row or column by one. Both travelers have made the same number of moves, so their columns are determined once their two row coordinates are known.

The exact solution defines `f[k][i1][i2]` as the maximum cherries collected after `k` moves when traveler one is at row `i1` and traveler two is at row `i2`. Their complete positions are `(i1, k - i1)` and `(i2, k - i2)`.

This reduces four position coordinates to the step number plus two rows.

**Initialize the shared starting cell**

At step zero, both travelers occupy `(0, 0)`. Its cherry, if present, may be collected only once, so

`f[0][0][0] = grid[0][0]`.

Every other state starts at negative infinity. That sentinel means the state is unreachable and ensures an invalid predecessor can never beat a real score.

**Reject positions outside the grid or on thorns**

For each layer `k` and row pair, the solution derives `j1 = k - i1` and `j2 = k - i2`. A state is skipped if either column is outside `0` through `n - 1` or either current cell contains `-1`.

Rows already come from `range(n)`, so only derived columns need explicit range validation.

**Count the current cells once or twice**

The layer’s new reward begins as `grid[i1][j1]`. If `i1 != i2`, the travelers occupy distinct cells and the second cell is added.

At equal step `k`, equal rows imply equal columns because both columns equal `k - row`. Therefore `i1 == i2` is exactly the same-cell condition; no separate column comparison is necessary.

Grid values on valid cells are zero or one, so this adds precisely the newly collected cherries at the two current positions without double-counting a meeting cell.

**Enumerate the four move combinations**

To reach current row `i` at step `k`, the previous row at step `k - 1` is either:

- `i`, meaning the traveler moved right and kept the same row.
- `i - 1`, meaning the traveler moved down.

The loops over `range(i1 - 1, i1 + 1)` and `range(i2 - 1, i2 + 1)` enumerate the four combinations of right/down moves for the two travelers. Negative previous rows are rejected.

For every valid pair `(x1, x2)`, the transition is

`f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][x1][x2] + t)`.

If a predecessor is unreachable, its negative-infinity score remains unreachable after adding the finite reward.

**Why no mutable cherry-removal grid is needed**

The state scores the union of two complete paths. Every time layer adds the two current cells, counting one when positions coincide. Because down/right paths visit each step layer once, the same path cannot revisit a cell. The only possible duplicate between paths occurs when they occupy the same cell at the same step, which the equality check handles.

Thus the DP directly counts unique collected cherries without modifying `grid` or remembering which individual cherries were removed.

**Final state and impossible paths**

Both travelers need exactly `2n - 2` moves to reach `(n - 1, n - 1)`. The final table entry is `f[-1][-1][-1]`.

If no valid path exists, that entry remains negative infinity. The problem requires zero in that case, so the method returns `max(0, final_score)`.

**Why the DP is correct**

Each state considers exactly every pair of valid synchronized partial paths ending at its positions. Its four predecessor combinations cover every possible final move pair, and the induction hypothesis supplies the best score for each predecessor. Adding the current distinct-cell reward extends those paths exactly.

Conversely, every transition follows legal right/down moves and skips thorns and out-of-bounds positions, so it represents valid paths. Induction over `k` proves every state stores the optimum for its endpoint pair. The final endpoint pair represents every possible outbound/return choice under the path reversal, so the returned score is globally optimal.

## Complexity detail

There are `2n - 1 = O(n)` step layers. Each layer loops over `n^2` row pairs and checks four predecessor pairs, a constant. Time complexity is `O(n^3)`.

The exact implementation allocates all `(2n - 1) * n * n` states, so its literal auxiliary space complexity is `O(n^3)`. The often-cited `O(n^2)` bound uses rolling layers because layer `k` depends only on `k - 1`. That optimization is not present in the stored source and should be described as an alternative.

## Alternatives and edge cases

- **Roll two DP layers:** Retain only the previous and current `n x n` tables. This preserves `O(n^3)` time and reduces auxiliary space to `O(n^2)`.

- **Simulate outbound choices and mutate cherries:** Trying every first path and then optimizing the return is exponential and can make a locally attractive first path block a better combined result. The simultaneous formulation optimizes both together.

- **Four-dimensional positions:** Track both rows and columns explicitly. The synchronized step identity makes two coordinates redundant and avoids an `O(n^4)` state space.

- **Count a meeting cell twice:** This violates cherry removal. Equal rows at the same step mean the exact same cell, so its reward must be added once.

- **Single-cell grid:** Both travelers start and finish together. The initialized value is returned, zero or one.

- **No valid complete path:** The final state remains unreachable and `max(0, ...)` returns zero.

- **Thorn at a candidate position:** That entire state is skipped, so no path can pass through the blocked cell.

- **Paths cross or share segments:** Sharing is allowed. Every shared cell is counted once at its synchronized visit layer.
