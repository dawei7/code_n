# Design Tic-Tac-Toe

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 348 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/design-tic-tac-toe/) |

## Problem Description
### Goal
Design a stateful $n \times n$ Tic-Tac-Toe game for players `1` and `2`. Each valid `move(row, col, player)` marks a previously empty cell, and moves arrive in gameplay order with no calls after a winner has been declared.

After each move, return that player's number if the mark completes an entire row, an entire column, the main diagonal, or the opposite diagonal using only that player's marks. Otherwise return `0`. Only lines passing through the newly marked cell can become winners. Preserve board state across calls and determine the result efficiently without rescanning the full board after every move.

### Function Contract
**Inputs**

- `n`: the board dimension
- `moves`: for the app adapter, triples `[row, column, player]` replayed in order. Native LeetCode calls `move(row, col, player)` one move at a time.

**Return value**

- The app adapter returns the status after every move. Each status is `0` when nobody has won, or the winning player number `1` or `2`.

### Examples
**Example 1**

- Input: `n = 3, moves = [[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]`
- Output: `[0, 0, 0, 0, 0, 0, 1]`

**Example 2**

- Input: `n = 2, moves = [[0,0,1],[1,0,2],[0,1,1]]`
- Output: `[0, 0, 1]`

**Example 3**

- Input: `n = 1, moves = [[0,0,1]]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(m)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Encode each player's ownership with a sign**

A move can affect only its row, its column, and—when applicable—one or both diagonals. Storing the full board and rescanning those lines is unnecessary. Instead, maintain signed totals for every row and column plus two diagonal totals.

Represent player 1 by $+1$ and player 2 by $-1$. For a move at `(row, col)`, add that sign to `rows[row]` and `columns[col]`. Add it to the main diagonal when $r=c$, and to the anti-diagonal when $r+c=n-1$.

**Check only the lines touched by the move**

Because moves are valid and cells are never reused, a line total reaches `+n` exactly when all `n` cells belong to player 1, and `-n` exactly when they all belong to player 2. After updating the affected counters, check whether the absolute value of any of them equals `n`; if so, return the current player, otherwise return zero.

**Why opposing signs cannot hide a win**

Opposing moves cancel in a shared counter, but this cannot hide a win: a line containing both players cannot be complete for either player, while a line owned entirely by one player has no opposite signs to cancel. Every possible winning line is represented by exactly one maintained counter, so the constant-time check is both necessary and sufficient.

#### Complexity detail

Each `move` updates and checks at most four integers, taking $O(1)$ time. Replaying `m` moves therefore takes $O(m)$ total time. The row and column arrays use $O(n)$ space; the two diagonal counters are constant-sized. No `n x n` board is required.

#### Alternatives and edge cases

- **Store and rescan the board:** takes $O(n)$ time per move and $O(n^2)$ storage.
- **Separate counters per player:** also supports $O(1)$ moves but uses twice as many arrays; signed totals encode both players together.
- On a `1 x 1` board, the first move wins immediately.
- The center of an odd-sized board belongs to both diagonals and must update both diagonal counters.
- A move outside both diagonals changes only one row and one column.

</details>
