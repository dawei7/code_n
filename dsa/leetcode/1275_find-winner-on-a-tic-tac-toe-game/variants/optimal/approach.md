## General

**Only the last player can be the winner**

The move list is guaranteed valid, and play stops as soon as someone wins. Therefore, if a winner exists, that winner made the final recorded move. Player A uses even move indices and player B uses odd indices. The exact source exploits this fact by examining only indices with the same parity as `n - 1`:

`range(n - 1, -1, -2)`.

Starting from the last move and subtracting two visits every move made by the last player and none made by the opponent. It is unnecessary to represent opponent marks because a valid finished game cannot contain an opponent win followed by another move.

**Eight counters represent all winning lines**

The $3$ by $3$ board has three rows, three columns, one main diagonal, and one anti-diagonal. Array `cnt` has eight entries. For move `(i, j)`, `cnt[i]` counts the chosen player's marks in row `i`, while `cnt[j + 3]` counts marks in column `j`.

If `i == j`, the cell lies on the main diagonal and `cnt[6]` increases. If `i + j == 2`, it lies on the anti-diagonal and `cnt[7]` increases. The center cell satisfies both conditions and correctly contributes to both diagonals.

After each processed mark, `any(v == 3 for v in cnt)` checks all eight possible lines. A count of three means the last player owns all three cells of that line because the input contains no repeated moves and only that player's moves were counted.

Although traversal goes backward in time, line membership is independent of ordering. Once all three marks of a winning line have been encountered, the counter reaches three. All visited indices have the same parity, so returning `"B" if k & 1 else "A"` identifies the last player. `k & 1` is one for an odd index and zero for an even index.

**Why ignoring the other player is safe**

Suppose player A had won before B's final move. The rules would have ended the game immediately, making B's later move invalid. The valid-input guarantee rules this out. Thus, when the list ends on B's move, only B can possibly be the winner; symmetrically, a list ending on A's move can only have A as winner.

If the last player has a winning line, the loop eventually counts its three cells and returns that player. If the loop finishes without a counter reaching three, the last player did not win, and validity implies the opponent did not win either.

For the first example, the last move index is four, so the loop counts A's moves at indices four, two, and zero. Those coordinates fill the main diagonal, making counter six reach three and returning A.

**Distinguish draw from pending**

If no winner is found, all nine cells being filled means a draw. The variable `n` is the number of recorded moves, not the board dimension, so `n == 9` tests board fullness. With fewer than nine valid moves and no winner, empty squares remain and the answer is `"Pending"`.

The method does not allocate the board. Validity guarantees coordinates are in range and never repeated, so counters alone contain enough information.

## Complexity detail

Let $m$ be the number of moves. The loop visits only one player's moves, at most $\lceil m/2\rceil$. Updating counters is constant work, and checking eight entries is also constant because the board size is fixed. Total time is $O(m)$.

The counter array always has eight integers, so auxiliary space is $O(1)$. No output structure or board copy is created.

For this problem $m\le9$, but the linear notation describes dependence on the supplied move list. The exact constant factors are very small.

## Alternatives and edge cases

- **Process both players with signed counters:** Add one for A and minus one for B to rows, columns, and diagonals. An absolute value of three identifies a winner and supports checking moves forward.
- **Build the full board:** Mark each move and scan its row, column, and diagonals. It is intuitive but stores more state and may rescan cells.
- **Count only the last player without valid-input guarantee:** This would be unsafe if moves could continue after an earlier win. The optimization depends on the stated validity.
- **Center move:** It increments its row, column, main diagonal, and anti-diagonal counters.
- **Corner move:** It belongs to one row, one column, and one or possibly both relevant diagonals according to the tests.
- **Winning final move:** Backward counting finds the completed line regardless of the order in which that player's earlier marks are encountered.
- **Nine moves without a winner:** Every square is occupied, so the result is `"Draw"`.
- **Fewer than nine moves without a winner:** At least one legal move remains, so the result is `"Pending"`.
- **Odd final index:** The last mover is B; every loop index is odd and the parity expression returns `"B"`.
- **Even final index:** The last mover is A and the parity expression returns `"A"`.
- **No repeated coordinates:** This guarantee prevents one cell from inflating a line counter more than once.
