## General

A bomb placed in an empty cell attacks in four straight directions. A wall stops the blast; enemies do not. Therefore the score of an empty cell is the number of enemies in its wall-delimited horizontal segment plus the number in its wall-delimited vertical segment.

The brute-force temptation is to start at every empty cell and scan left, right, up, and down. Large open segments would then be scanned repeatedly. The exact solution removes that repetition with four complete directional sweeps. It allocates a matrix `g` where each cell accumulates the number of visible enemies found from the left, right, above, and below.

**What the running counter means.**

During a left-to-right row sweep, `t` is the number of enemies encountered since the most recent wall. A wall resets `t` to zero because nothing on its left can be hit from a position on its right. An enemy increments `t`. The current value is added into `g[i][j]`.

At an empty cell, that contribution equals exactly the number of enemies visible to its left. At an enemy cell, the running value also includes that enemy itself; at a wall, it is zero. Those latter values do not matter because the final answer examines only empty cells.

The same pattern can be reused in every direction. Reset on a wall, increment on an enemy, and add the running count at each position.

**First horizontal pass: enemies on the left.**

For each row `i`, the source sets `t = 0` and visits columns from `0` through `n - 1`. When it reaches an empty cell `(i, j)`, `g[i][j]` receives the number of enemies between that cell and the nearest wall or boundary to its left.

Enemies farther left than a wall are deliberately absent because the reset discarded them. Empty cells do not change `t`, so every empty cell in the same uninterrupted portion sees the same already-passed enemies.

**Second horizontal pass: enemies on the right.**

The counter is reset and the same row is scanned from `n - 1` down to `0`. At an empty cell, this pass contributes enemies between the cell and the nearest right-side wall or boundary.

After both row passes, an empty cell's `g` value equals all horizontally visible enemies. No enemy is counted in both horizontal directions for the same empty cell: every other column lies strictly either left or right of it.

**Two vertical passes.**

The source then processes one column at a time. A top-to-bottom pass counts visible enemies above each empty cell. A bottom-to-top pass counts those below. Walls again reset the running counter.

After all four sweeps, for every empty `(i, j)`, `g[i][j]` is

$$
\text{left enemies}+\text{right enemies}+\text{up enemies}+\text{down enemies}.
$$

The horizontal and vertical counts do not overlap because their only intersection is the bomb cell itself, and that cell is empty. Thus simple addition gives the exact number killed.

**A trace through a row segment.**

Consider the row `['E', '0', 'E', 'W', 'E', '0']`. In the left-to-right pass, the counter values added at the first empty and final empty are `1` and `1`. The wall resets the count, so the last empty does not see either enemy from the first segment.

In the right-to-left pass, the first empty receives one more count from the enemy to its right before the wall. The final empty receives zero from its right. Their horizontal totals become two and one respectively, exactly matching the blast rule.

**Why four passes are sufficient.**

Take any empty cell and any enemy in its row. If the enemy is to the left and no wall separates them, it contributes to the running counter when the left-to-right sweep reaches the empty cell. If a wall separates them, a reset removes it. The right-to-left sweep gives the symmetric result for enemies on the right. The vertical passes establish the same fact above and below.

Every killable enemy lies in exactly one of these four directional groups, and every enemy counted by a group has an unobstructed segment to the bomb. Therefore the accumulated score contains all and only the enemies that would be killed.

**Selecting a legal bomb position.**

The final list comprehension collects `g[i][j]` only where `grid[i][j] == '0'`. Enemy and wall scores are ignored because bombs may be planted only on empty cells. `max(..., default=0)` returns the best score and handles a grid with no empty cell by returning zero.

The grid is guaranteed nonempty and rectangular, so reading `len(grid[0])` is safe. The method never changes `grid`; all accumulated data goes into `g`.

**The exact source differs from the manifest's space description.**

The manifest summary says row and column segment totals are cached while evaluating cells and advertises $O(n)$ space. That describes the editorial's rolling row count plus one column-count array. The checked-in solution instead stores an entire $m\times n$ matrix and later creates a list of all empty-cell scores for `max`. Its time remains optimal, but its actual auxiliary space is $O(mn)$, not $O(n)$.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns.

The two horizontal sweeps visit every cell twice in total, and the two vertical sweeps visit every cell twice more. The final comprehension visits every cell once to find legal candidates. This is a constant number of complete grid traversals, so total time is $O(mn)$.

The `g` matrix contains $mn$ integer entries, requiring $O(mn)$ space. The final list comprehension may contain one value for every cell when the grid is entirely empty, requiring another $O(mn)$ temporary list. These coexist during the `max` call, so peak auxiliary storage remains $O(mn)$. The manifest's $O(n)$ space does not match the exact source.

Each directional counter uses $O(1)$ space. The output is a single integer, so none of the matrix storage can be classified as required output space.

## Alternatives and edge cases

- **Rolling row and column segment counts:** Recompute a row-segment total only after a wall and keep one cached total per column. This reaches $O(mn)$ time with $O(n)$ space and matches the manifest, but it is not the checked-in implementation.

- **Brute force from every empty cell:** Scan four directions until walls. It uses $O(1)$ extra space but can require $O(mn(m+n))$ time in a wall-free grid.

- **Precompute four separate direction matrices:** This is conceptually direct but uses four $m\times n$ tables instead of accumulating all directions into one.

- **No empty cells:** The candidate list is empty and `default=0` produces the only sensible result, since no bomb can be placed.

- **No enemies:** Every running counter stays zero, so every legal bomb score is zero.

- **All cells in one open segment:** Every empty cell sees all enemies in its row segment and column segment; the sweeps reuse these counts without rescanning from each empty.

- **Adjacent wall:** A wall immediately beside an empty cell blocks everything beyond it because the directional counter resets at that wall.

- **Enemies do not block the blast:** Encountering `'E'` increments rather than resets the counter, allowing farther enemies in the same segment to be counted too.

- **Bomb cell is empty:** Horizontal and vertical contributions cannot double-count an enemy at their intersection because the intersection contains `'0'`.

- **One row:** Vertical passes contribute zero to empty cells, and the two horizontal passes still give the correct answer.

- **One column:** The symmetric reasoning applies; horizontal contributions are zero and vertical sweeps solve the problem.

- **Input preservation:** `grid` remains unchanged. The separate matrix makes the method easy to reason about but accounts for its larger space cost.
