## General

**Why backtracking is necessary**

Every `'.'` on the board must become a digit from `1` through `9`, but a candidate is allowed only if it duplicates no digit in the same row, column, or $3 \times 3$ box. These restrictions let the solver reject many candidates immediately. They do not, however, guarantee that a currently legal digit can be extended to a complete solution. A choice may look valid now and leave some later cell with no possible digit. The competitive solution handles that uncertainty with depth-first backtracking: try a legal digit, solve the remaining board recursively, and erase the digit if the remainder cannot be solved.

**Finding the next decision**

Each call to `solver(board)` scans the grid in row-major order. It stops at the first cell whose value is `'.'`. All earlier empty cells in this ordering have already been assigned by ancestor calls, so this first dot is the next unresolved decision on the current branch.

For that cell, the code tries the characters `1` through `9` in increasing order. It constructs them as `chr(ord('1') + k)`, where `k` ranges from `0` to `8`. The candidate is written to the board before validation because `isValid` compares the current cell's value with the surrounding cells. If the candidate is legal and the recursive call solves everything after it, `solver` immediately returns `True`. Otherwise, the cell is reset to `'.'` before the next digit is tried.

That reset is essential. Without it, the next iteration would no longer be testing an empty cell from the same parent state, and a failed candidate could incorrectly constrain a sibling branch. Backtracking is precisely this pairing of a reversible choice with restoration after failure.

**How `isValid` checks a tentative digit**

The helper receives the newly filled coordinates `(x, y)`. It first scans all nine rows at column `y`. The condition excludes `i == x` so the candidate is not compared with itself; if any other cell equals `board[x][y]`, the column contains a duplicate and the helper returns `False`.

It then scans all nine columns at row `x`, similarly excluding `j == y`. A match means the row contains a duplicate. Notice that variable names in the loops do not change the geometric meaning: `board[i][y]` varies the row index and therefore scans a column, while `board[x][j]` varies the column index and therefore scans a row.

Finally, it scans the candidate's $3 \times 3$ box. With integer division, `x / 3` identifies which group of three rows contains `x`, and multiplying by three gives that group's starting row. The same computation finds the starting column from `y`. The two `while` loops cover exactly three row indices and three column indices. The `(i != x or j != y)` condition skips only the candidate cell itself; every other box cell is compared with it.

If no duplicate is found in any of the three units, `isValid` returns `True`. This means the placement is locally consistent, not necessarily that the entire branch is solvable. The recursive `solver` call answers the latter question.

**Success and failure signals**

If the nested scan finds no `'.'` anywhere, every cell has a digit. Each digit inserted by the search passed the row, column, and box checks at the moment it was inserted, while the original clues are assumed valid by the problem contract. The board is therefore complete and valid, so `solver` returns `True`.

If the first empty cell has been tried with all nine digits and none leads to success, the function returns `False`. It is correct to return immediately after exhausting that cell instead of scanning for another empty cell: a complete solution must put some legal digit in the first unresolved position. If no such digit can lead to a completion, changing a later position cannot rescue the current prefix. Control must go back to an earlier choice.

At the public-method level, `solveSudoku` ignores the Boolean returned by `solver`. That Boolean is an internal control signal for recursive frames. Under the guarantee that the input has one solution, the initial call succeeds and leaves the completed digits in the shared `board`. The required method itself returns no value because the contract asks for in-place mutation.

**Why the enumeration finds the solution**

Every accepted placement is safe at the time it is made: `isValid` has checked all other cells in the candidate's row, column, and box, so it creates no duplicate. Recursive calls preserve this property for all subsequent placements. Therefore, reaching a board with no dots implies a valid Sudoku, not merely a full grid.

The enumeration is complete as well. Consider the first empty cell in any search state. Every possible completed board extending that state must assign one of the digits `1` through `9` to this cell. The loop examines all nine. It discards a digit only if it already violates a Sudoku rule or if exhaustive recursion proves that the remaining board cannot be filled after that choice. Thus the digit belonging to the guaranteed solution is never permanently skipped. Repeating the argument at each depth shows that the successful sequence of assignments will eventually be visited.

**A Python-version defect in the selected source**

The intended algorithm relies on integer division when it computes box boundaries. The selected implementation writes `x / 3` and `y / 3`. That expression performs integer division for integer operands in Python 2, which is the environment this older competitive source targets. In Python 3, `/` produces a floating-point value. Consequently, `i` and `j` become floats, and an expression such as `board[i][j]` raises a `TypeError` because list indices must be integers.

The algorithm described above is therefore the intended behavior, but this exact file is not Python 3-compatible unchanged. Replacing those divisions with `x // 3` and `y // 3` would preserve the intended box calculation. The protected solution is not altered here; documenting the mismatch is necessary so a learner does not mistake a runtime failure for a flaw in backtracking itself.

## Complexity detail

Let $E$ be the number of initially empty cells. Each recursive level may try as many as nine digits, giving a conservative search-tree bound of $O(9^E)$. Sudoku constraints usually reject most candidates and make the practical tree much smaller, but adversarial partial boards can still require extensive backtracking.

For each candidate, `isValid` examines nine row positions, nine column positions, and nine box positions, which is $O(9)$ and therefore constant for standard Sudoku. Each recursive call also scans up to all 81 cells to find the first dot. Both factors are fixed constants on a $9 \times 9$ board, so the manifest records $O(9^E)$ rather than multiplying by 81. A generalized analysis that allowed board dimensions to grow would need to retain the validation and scanning factors instead of calling them constant.

The algorithm stores no row, column, or box cache. Its main auxiliary cost is the recursion stack, whose depth cannot exceed $E$, so space is $O(E)$. It mutates and restores the same input board rather than cloning it. A few loop indices and candidate characters occupy constant space per frame. The comment in the source claims constant space, but that omits the recursive call stack; the manifest's $O(E)$ is the safer accounting.

The Python 3 division defect prevents the exact source from completing once box validation is reached, but it does not change the complexity of the intended Python 2 algorithm.

## Alternatives and edge cases

- **Cached row, column, and box occupancy:** Boolean tables, sets, or bit masks make each legality test constant-time without rescanning surrounding cells. They require careful updates and rollback but generally outperform this scan-based version.
- **Minimum-remaining-values ordering:** Selecting the empty cell with the fewest candidates often detects contradictions earlier than always choosing the first dot. The search becomes faster on difficult puzzles, though candidate counting adds code and bookkeeping.
- **Exact-cover or Algorithm X formulation:** Sudoku can be represented as an exact-cover problem and solved with dancing links. That is powerful and systematic, but substantially less approachable than direct constraint-aware backtracking.
- **Python 3 execution:** The expressions based on `x / 3` and `y / 3` yield floats and lead to invalid list indexing. Integer floor division `//` is required to express the intended box boundaries in Python 3.
- **Already complete board:** The scan finds no dot, so `solver` returns `True` immediately. No cell is changed.
- **First empty cell has no legal candidate:** All nine trials fail, the cell is restored after each one, and the function returns `False` to make the preceding recursive frame reconsider its choice.
- **A legal candidate later fails:** Passing `isValid` proves only that no duplicate exists now. The recursive `False` result is what reveals that the candidate cannot participate in a full solution, after which the dot restoration makes the next trial safe.
- **Original clues:** The solver never selects a non-dot cell as a decision, so it preserves every clue. It assumes those clues are mutually consistent, as guaranteed by the problem statement.
- **Unsolvable input outside the contract:** The internal call would eventually return `False` and restore tried cells, but the public method discards that status. Callers receive no explicit failure indication.
- **Multiple solutions outside the contract:** Candidate order makes the algorithm stop at the first solution it encounters. The official uniqueness guarantee means that this ordering does not affect the required final board.
- **In-place mutation:** The successful path deliberately does not erase its digits while unwinding, so the caller's original list becomes the solved grid even though `solveSudoku` returns `None`.
