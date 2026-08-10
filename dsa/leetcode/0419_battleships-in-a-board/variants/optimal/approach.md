## General

**Count one canonical cell per ship**

A battleship may occupy many `'X'` cells, so counting every `'X'` would count its length rather than the number of ships. Flood-filling each ship would work, but the placement rules provide a simpler one-pass signature.

Every valid horizontal or vertical ship has exactly one beginning cell when the board is read from top to bottom and left to right:

- a horizontal ship's beginning is its leftmost `'X'`; and
- a vertical ship's beginning is its topmost `'X'`.

A one-cell ship is both its leftmost and topmost cell. The algorithm counts an `'X'` only when there is no `'X'` immediately above it and no `'X'` immediately to its left. That condition identifies exactly these beginning cells.

**Scan every board coordinate once**

The nested loops visit rows `0` through `m-1` and columns `0` through `n-1`. If `board[i][j] == '.'`, the cell is empty and cannot represent a ship, so the code immediately continues.

For an `'X'`, the test

`i > 0 and board[i - 1][j] == 'X'`

asks whether the ship continues from the cell above. If so, the current cell is not the top of a vertical ship and has already been represented by an earlier cell in that ship.

The next test

`j > 0 and board[i][j - 1] == 'X'`

asks whether the ship continues from the left. If so, the current cell is not the left end of a horizontal ship.

Only an occupied cell with neither predecessor increments `ans`.

The boundary checks `i > 0` and `j > 0` must precede neighbor access. A cell in the top row has no above neighbor, and a cell in the leftmost column has no left neighbor. In Python, using index `-1` without these guards would wrap around to the opposite edge and could falsely connect unrelated ships.

**Why every ship contributes at least once**

Take a horizontal ship. Its leftmost cell has no `'X'` to its left by definition. The separation guarantee also prevents an unrelated vertical ship from placing an `'X'` immediately above it; adjacent ships are not allowed. Because the ship itself extends only horizontally, this beginning cell has no same-ship cell above. It passes both predecessor tests and is counted.

Take a vertical ship. Its topmost cell similarly has no `'X'` above. It has no same-ship cell to the left, and the separation rule prevents another ship there. It is counted.

A single-cell ship has no occupied predecessor in either direction and is counted as well. Thus no valid battleship is missed.

**Why no ship contributes more than once**

Every non-leftmost cell of a horizontal ship has an `'X'` immediately to its left, so it fails the left-neighbor test. Every non-topmost cell of a vertical ship has an `'X'` immediately above, so it fails the above-neighbor test. Hence all cells after the canonical beginning are skipped.

Because ships are straight `1 x k` or `k x 1` segments and are separated, there are no branching shapes or crossings that could contain two cells with neither predecessor. Exactly one cell per ship increments `ans`, proving that the final total is correct.

**A concrete example**

Consider

`[["X",".",".","X"], [".",".",".","X"], [".",".",".","X"]]`.

At `(0,0)`, the cell is occupied and has no above or left coordinate, so it starts the one-cell horizontal ship and is counted. At `(0,3)`, the same predecessor condition holds, so the vertical ship is counted. Cells `(1,3)` and `(2,3)` each see an `'X'` above and are skipped. The result is two even though the board contains four occupied cells.

**Why scanning order does not carry hidden state**

The reasoning refers to an earlier top or left cell, but the code does not need to remember whether that cell was counted. The board's immutable local pattern is enough: the presence of an occupied predecessor proves that the current cell is a continuation. Therefore the algorithm would make the same decision for each coordinate regardless of the order in which coordinates are visited, although row-major order makes the “beginning” intuition natural.

No board cell is modified. This satisfies the follow-up and avoids needing restoration or a visited matrix.

## Complexity detail

Let $r=m$ be the number of rows and $c=n$ the number of columns. The nested loops inspect all $rc$ cells. Each occupied cell triggers at most two constant-time neighbor checks. Total time is $O(rc)$.

The algorithm stores only dimensions, loop indices, and the integer answer. It uses $O(1)$ auxiliary space and does not modify `board`. The input matrix itself is not counted as extra space.

Inspecting every cell is asymptotically necessary in the general case: an unread coordinate could contain an isolated ship that changes the answer. Thus the linear-in-board-size time is optimal.

## Alternatives and edge cases

- **Flood fill each unvisited ship:** Start DFS or BFS at an unvisited `'X'`, mark its connected cells, and increment once. This is $O(rc)$ time but needs $O(rc)$ visited space in the worst case or modifies the board, both unnecessary under the placement guarantees.
- **Erase ships in place:** On finding an `'X'`, walk through and replace its cells with `'.'`. It uses little auxiliary space but violates the follow-up's requirement not to modify `board`.
- **Count transitions along rows and columns separately:** This can work but risks double-counting single-cell ships and needs careful orientation logic. The no-above-and-no-left signature treats all lengths uniformly.
- **Count all occupied cells:** This is incorrect whenever a ship has length greater than one because it counts cells rather than connected straight segments.
- **Top-row ship:** The guarded above check treats the missing neighbor as empty; only a left continuation can suppress counting.
- **Left-column ship:** The guarded left check similarly leaves the above neighbor to determine whether it is a continuation.
- **Single-cell board containing `'.'`:** The cell is skipped and the result is zero.
- **Single-cell board containing `'X'`:** It has no predecessor and contributes exactly one.
- **One long horizontal ship:** Only its first column is counted; every later cell sees the previous `'X'`.
- **One long vertical ship:** Only its first row is counted; every later cell sees the above `'X'`.
- **Several separated ships:** The required empty separation ensures each beginning cell is not rejected because of an unrelated adjacent ship.
- **Invalid touching or L-shaped arrangements:** The proof relies on the contract's straight, separated placement. If arbitrary connected `'X'` shapes were permitted, a graph traversal and an explicit definition of a ship would be necessary.
- **Python negative indexing:** Omitting `i > 0` or `j > 0` would read the last row or column from a first-edge cell. The explicit guards are correctness conditions, not merely optimizations.
