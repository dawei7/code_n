## General

**What the solver is actually deciding**

The board already contains fixed clues, and every `'.'` marks a decision that is still unknown. A legal completed board must satisfy three restrictions at the same time: a digit may appear only once in its row, only once in its column, and only once in its $3 \times 3$ sub-box. Checking only one or two of those restrictions is insufficient. For example, a `5` may be absent from a cell's row but already present in its column, so placing it would still be illegal.

There is an important difference between a **legal next placement** and a **placement that belongs to the solution**. A digit can obey all three restrictions now and nevertheless create a dead end several cells later. No local test can always recognize that future failure. The algorithm therefore combines fast legality checks with backtracking: make one legal choice, recursively try to finish the rest of the puzzle, and undo the choice's bookkeeping if that branch cannot be completed.

**Representing the three restrictions**

The solution builds three occupancy structures before searching:

- `row[i][v]` says whether row `i` already contains digit `v + 1`.
- `col[j][v]` says whether column `j` already contains digit `v + 1`.
- `block[i // 3][j // 3][v]` says whether the sub-box containing `(i, j)` already contains digit `v + 1`.

Digits are stored at indices `0` through `8`, so digit `1` corresponds to `v = 0` and digit `9` corresponds to `v = 8`. This conversion explains both `int(board[i][j]) - 1` during initialization and `str(v + 1)` during placement.

Integer division locates a cell's box. Rows `0`, `1`, and `2` all have `i // 3 == 0`; rows `3`, `4`, and `5` have value `1`; and rows `6`, `7`, and `8` have value `2`. Columns behave the same way. Thus `(i // 3, j // 3)` identifies one of the nine boxes without a special-case table.

The chained test `row[i][v] == col[j][v] == block[i // 3][j // 3][v] == False` is true only when all three flags are false. Consequently, each candidate check takes constant time. The solver does not have to rescan nine cells in the row, nine in the column, and nine in the box for every tentative digit.

**Separating clues from decisions**

One pass over the board records every fixed clue in the occupancy structures. Empty positions are appended, in row-major order, to `t`. This list matters because recursion can work with a single integer `k`: `t[k]` is the next cell to fill. Fixed cells never enter `t`, so the search can neither overwrite nor accidentally erase an original clue.

The input guarantee allows initialization to trust the clues. This implementation does not reject a malformed starting board containing duplicate fixed digits; that validation is unnecessary under the stated contract.

**The recursive state and its invariant**

At the start of `dfs(k)`, cells `t[0]` through `t[k - 1]` have been assigned along the current search branch. The three occupancy structures describe the original clues plus exactly those active assignments. Therefore, testing the flags for `t[k]` answers the precise question needed: would this next digit conflict with anything already chosen?

For the current cell `(i, j)`, the loop tries digits from `1` through `9`. When digit `v + 1` is available, the code performs three coordinated actions before recursing: it marks the digit occupied in the row, column, and box; writes the character to `board[i][j]`; and calls `dfs(k + 1)`. Marking before the recursive call is essential. Otherwise, a descendant could reuse the same digit in a shared row, column, or box because it would not know about the ancestor's choice.

After the recursive call returns, the code clears all three flags for this placement. That is the backtracking step. It restores the occupancy invariant for the parent branch so the next candidate is evaluated independently. The board character itself is not reset to `'.'`, which may initially look suspicious. It is safe for this exact implementation because unfilled-cell legality is determined exclusively by the occupancy arrays, and every revisited cell is overwritten before its next recursive call. If the successful branch has been found, retaining the written characters is exactly what leaves the answer in `board`.

**How success stops the search without erasing the answer**

When `k == len(t)`, every originally empty position has received a mutually compatible digit. The clues were recorded initially, and every new placement passed all three occupancy tests, so every row, column, and box is valid. The function sets the nonlocal flag `ok = True` and returns.

As recursion unwinds, each frame clears its temporary occupancy flags and then checks `ok`. Because `ok` is true, the frame returns immediately instead of trying another digit. Clearing these internal flags does not change the completed characters already written to `board`; the occupancy structures are no longer needed after the solution is known. The success flag therefore has two jobs: it distinguishes success from an ordinary failed recursive return, and it prevents later candidate trials from overwriting the completed board.

The guarantee of exactly one solution means this depth-first search will eventually reach that base case. More generally, uniqueness is not needed for the mechanics of backtracking; it only makes the first completed board unambiguous.

**Why the method is correct**

Every recursive placement is legal because the algorithm writes a digit only when the corresponding row, column, and box flags are all false. The flags are then set, so all deeper placements must respect that choice. Hence no search state accepted by the recursion contains a duplicate in any relevant unit.

The search is also complete. At each empty cell it considers every digit from `1` to `9` that is compatible with the preceding choices. If a candidate cannot lead to a completion, backtracking restores the parent state and tries the next candidate. Any valid solution has some digit in the first empty cell, some digit in the second, and so on; none of those solution digits can be rejected by the legality test when its prefix has been chosen. The depth-first enumeration therefore reaches the valid sequence. When the base case is reached, all empty cells are filled legally, which proves that the board left behind is a valid completed Sudoku.

## Complexity detail

Let $E$ be the number of empty cells in the input board. At each recursive level, at most nine digits are tried, so a direct worst-case upper bound is $O(9^E)$. Sudoku restrictions prune most branches much earlier: a cell often has only a few available digits, and an impossible partial board stops when some later cell has no candidate. That pruning is crucial in practice, but it does not change the conservative exponential worst-case bound recorded in the variant manifest.

Each candidate's legality test and each placement or removal update use a constant number of array accesses. Initialization visits all 81 cells once, which is $O(81)$ and therefore constant for the fixed board, or $O(N^2)$ if one describes a generalized $N \times N$ board. The exponential search dominates.

The empty-position list contains $E$ coordinate pairs, and recursion can be at most $E$ calls deep. These account for $O(E)$ auxiliary space. The row, column, and box tables contain a fixed 243 Boolean entries for a standard Sudoku and are $O(1)$ with respect to $E$. The board is modified in place rather than copied at every branch. Including the list and call stack gives the manifest's $O(E)$ space bound.

## Alternatives and edge cases

- **Rescan the row, column, and box for every candidate:** This removes the occupancy tables and is easy to derive, but every tentative placement performs repeated work. It remains a valid backtracking strategy on a $9 \times 9$ board, though the constant factor is worse.
- **Bit masks instead of Boolean tables:** Nine-bit integers can represent the digits used by each row, column, and box. Availability then becomes a few bitwise operations. This is compact and fast, but Boolean arrays make the digit-to-constraint relationship easier to inspect for a beginner.
- **Choose the most constrained empty cell first:** Rather than preserve row-major order in `t`, each level can select the unfilled cell with the fewest legal candidates. This minimum-remaining-values heuristic often shrinks the search tree dramatically, at the cost of extra selection logic and more complicated state management.
- **Copy the whole board at each recursive call:** Copies make rollback conceptually simple, but they allocate and copy 81 cells per branch. Updating one cell and three flags, then undoing those flags, is substantially cheaper.
- **Already solved board:** Then `t` is empty, so `dfs(0)` immediately sets `ok`. No clue is changed, and the method correctly returns `None` after leaving the board as it was.
- **A cell with no legal digit:** Its candidate loop makes no recursive call. The frame returns, causing its parent to undo the preceding choice and try another digit. This is the normal dead-end signal, not an exceptional condition.
- **Several locally legal digits:** The solver deliberately cannot commit based only on local validity. It explores one candidate to completion and backtracks if later constraints expose the mistake.
- **Stale characters after a failed branch:** Descendant cells can temporarily retain digits in `board`, but the occupancy tables—not those characters—govern candidate legality, and a descendant is overwritten before reuse. On the guaranteed-solvable input, the successful branch ultimately overwrites every position in `t` with its final digit.
- **Invalid or unsatisfiable input:** The official contract guarantees one solution. This source has no explicit failure return and does not restore every empty cell to `'.'` after total failure, so callers should not treat it as a validator for boards outside that contract.
- **In-place result:** The required outcome is the mutation of `board`. The absence of a returned grid is intentional; callers inspect the same nested list they passed in.
