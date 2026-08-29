## General

**Move both robots synchronously.** After the same number of moves, both robots are always on the same row. Their complete state at row `i` is therefore determined by two columns `j1` and `j2`. Tracking their paths separately would lose the interaction when they occupy the same cell.

Define `f[i][j1][j2]` as the maximum cherries collected through row `i` when robot one ends that row at column `j1` and robot two ends at column `j2`. A value of `-1` marks an unreachable state. This sentinel is safe because all grid values are nonnegative, so every reachable total is at least zero.

**Initialize the mandated starting positions.** On row zero, robot one is at column zero and robot two at column `n - 1`. The source sets only `f[0][0][n - 1]`. Since the grid has at least two columns, those starting cells differ and their cherry values are added.

All other row-zero column pairs remain unreachable. This prevents the DP from inventing a different starting placement.

**Count the current row once per occupied cell.** For a candidate state `i, j1, j2`, `x` begins with `grid[i][j1]`. If the robots use different columns, it also adds `grid[i][j2]`. If they meet, the second contribution is zero because the cell becomes empty after one robot collects it.

The current-row reward depends only on the two columns, not on how they arrived there. That is why a maximum predecessor total is sufficient state.

**Enumerate the nine predecessor movements.** A robot that ends at column `j1` could have been at `j1 - 1`, `j1`, or `j1 + 1` on the previous row. The loop over `y1` covers these possibilities. The analogous loop over `y2` covers robot two, giving at most nine predecessor pairs.

The bounds check rejects columns outside zero through `n - 1`. The reachability check `f[i - 1][y1][y2] != -1` rejects position pairs that could not arise from the required starts.

For each valid predecessor, the new total is its best collected amount plus `x`. Taking a maximum records the best way to reach the current pair. Different histories leading to the same state have identical future options, so only their greatest total matters.

**Why predecessor direction is correct.** The movement rule says a robot may change its column by minus one, zero, or plus one while moving down one row. That relation is symmetric: if `j1` is reachable from `y1`, then `y1` lies within one of `j1`. Looking backward with `range(j1 - 1, j1 + 2)` therefore enumerates exactly the legal previous columns.

**Take the best ending pair.** Both robots must reach the bottom row, but no particular final columns are required. The generator over `product(range(n), range(n))` examines every pair on the last layer, and `max` returns the best reachable total.

Some bottom states may remain `-1`, but at least one legal movement sequence exists and has a nonnegative score, so unreachable sentinels cannot win.

**A row-level trace.** At a state where the robots occupy distinct columns with values five and two, `x` is seven. Each reachable predecessor represents a pair of positions on the row above. If the best such predecessor has accumulated twelve cherries, this state becomes nineteen. If the robots both occupy the five-cherry cell, `x` is five rather than ten.

**Why the recurrence is correct.** Every legal pair of robot paths reaching state `i, j1, j2` has one unique predecessor column pair on row `i - 1`, and that pair appears in the nine-way loops. By induction, its table value is the best score for that predecessor state. Adding the correctly deduplicated current reward gives the path's score.

Conversely, every transition accepted by the bounds and reachability checks is a legal simultaneous move from an actual state. Thus the maximum contains no impossible path. Induction across rows proves all states are optimal, and maximizing the final layer yields the global answer.

**Be precise about storage.** The manifest advertises `O(C^2)` space using rolling row layers. The exact source allocates all `R` layers in `f`, each with `C^2` entries. Its actual auxiliary space is `O(RC^2)`. Only the immediately previous layer is read, so compression is possible but not implemented here.

## Complexity detail

Let `R` be the row count and `C` the column count. There are `RC^2` states. Each state checks at most nine predecessor pairs, a fixed constant, so filling the table takes `O(RC^2)` time. The final maximum checks `C^2` states and is absorbed by that bound.

The three-dimensional list stores `RC^2` values, giving `O(RC^2)` auxiliary space for this exact source. Loop variables and the temporary product iterator add only constant state.

Keeping just the previous and current `C by C` layers would reduce storage to `O(C^2)`, matching the manifest, without changing time.

Nonnegative grid values justify `-1` as unreachable. If negative rewards were allowed, a lower sentinel such as negative infinity would be necessary.

## Alternatives and edge cases

- **Rolling two layers:** Retain only row `i - 1` and the row being built. This is the direct way to achieve the manifest's `O(C^2)` space.
- **Top-down memoization:** Recursively explore nine next-position pairs and cache row-column states. It has the same time class but may store only reached states.
- **Move one robot to the bottom first:** This loses the necessary interaction between paths and would require remembering consumed cells. Synchronous movement gives the compact joint state.
- **Treat robots independently:** Maximizing two separate paths can double-count shared cells and miss globally better coordination.
- **Robots meet:** The current cell's cherries are added once through the `j1 == j2` condition.
- **Robots cross:** Their column order may reverse between rows. The DP allows all legal pairs and does not require `j1 <= j2`.
- **Edge columns:** Bounds checks remove moves left of zero or right of `C - 1`.
- **All zeros:** Reachable states remain zero and the answer is zero.
- **One high-value shared cell:** Both may use it, but its reward contributes only once.
- **Different final columns:** All bottom pairs are considered; no endpoint is prescribed.
- **Unreachable states:** The `-1` sentinel prevents them from creating transitions.
- **Nonnegative-value guarantee:** It distinguishes every reachable score from the sentinel.
- **Minimum two columns:** Starting robots occupy distinct cells, so initialization may safely add both.
- **Nine movement combinations:** Each of two robots has three choices, and all combinations must be considered.
- **Space reporting:** Use `O(RC^2)` for this exact table and `O(C^2)` only for a rolling implementation.
