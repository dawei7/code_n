## General
**Encode each player's ownership with a sign**

A move can affect only its row, its column, and—when applicable—one or both diagonals. Storing the full board and rescanning those lines is unnecessary. Instead, maintain signed totals for every row and column plus two diagonal totals.

Represent player 1 by $+1$ and player 2 by $-1$. For a move at `(row, col)`, add that sign to `rows[row]` and `columns[col]`. Add it to the main diagonal when $r=c$, and to the anti-diagonal when $r+c=n-1$.

**Check only the lines touched by the move**

Because moves are valid and cells are never reused, a line total reaches `+n` exactly when all `n` cells belong to player 1, and `-n` exactly when they all belong to player 2. After updating the affected counters, check whether the absolute value of any of them equals `n`; if so, return the current player, otherwise return zero.

**Why opposing signs cannot hide a win**

Opposing moves cancel in a shared counter, but this cannot hide a win: a line containing both players cannot be complete for either player, while a line owned entirely by one player has no opposite signs to cancel. Every possible winning line is represented by exactly one maintained counter, so the constant-time check is both necessary and sufficient.

## Complexity detail
Each `move` updates and checks at most four integers, taking $O(1)$ time. Replaying `m` moves therefore takes $O(m)$ total time. The row and column arrays use $O(n)$ space; the two diagonal counters are constant-sized. No `n x n` board is required.

## Alternatives and edge cases
- **Store and rescan the board:** takes $O(n)$ time per move and $O(n^2)$ storage.
- **Separate counters per player:** also supports $O(1)$ moves but uses twice as many arrays; signed totals encode both players together.
- On a `1 x 1` board, the first move wins immediately.
- The center of an odd-sized board belongs to both diagonals and must update both diagonal counters.
- A move outside both diagonals changes only one row and one column.
