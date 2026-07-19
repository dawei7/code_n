## General
**Encode each unit's forbidden digits in a nine-bit mask**

Build nine row masks, column masks, and box masks from the clues. Bit $d - 1$ is set when digit `d` is already used. For cell `(row, col)`, flatten its 3×3 box coordinates to `(row // 3) * 3 + col // 3`.

Let `FULL = (1 << 9) - 1`. The legal-candidate mask for an empty cell is:

```text
FULL & ~(row_mask[row] | col_mask[col] | box_mask[box])
```

The union identifies every forbidden digit, complementing exposes unused digits, and the final `FULL` mask discards irrelevant higher bits. A candidate digit can be extracted one at a time with `bit = candidates & - candidates` and removed with `candidates -= bit`.

**Branch on the cell with the fewest legal candidates**

Collect the empty coordinates once. At recursion depth `position`, inspect only coordinates from `position` onward and compute each candidate mask. Select the cell with the fewest set bits and swap it into `empties[position]`. This **minimum remaining values** heuristic does not remove any choice; it merely chooses the order in which variables are assigned.

A zero-candidate cell proves the current partial assignment impossible and should fail immediately. A one-candidate cell is forced and avoids unnecessary branching. These early discoveries are why MRV is much faster than always taking the first empty cell on difficult boards.

Try each candidate bit in turn: convert its bit position to the corresponding character, write the board cell, and set the bit in its row, column, and box masks. If recursion fails, clear exactly those three bits and restore the board cell to `.` before trying the next candidate. Restore the empty-coordinate swap as well when backtracking if the implementation relies on list order outside the successful path.

**Transactional state changes make backtracking safe**

Before every recursive call, all filled cells obey Sudoku constraints; masks exactly encode those cells; positions before the recursion index are assigned; and later empty positions remain unassigned. Candidate masking permits only assignments absent from all three owning units, so setting one candidate preserves validity.

Each attempted assignment is a transaction across four representations: the board and three masks. On failure, undoing all four returns precisely to the parent state. This exact restoration is essential—leaving a stale bit would incorrectly hide valid candidates in sibling branches.

**Trace forced propagation before branching**

If an empty cell's row has digits 1–7, its column contains 8, and its box does not contain 9, the candidate mask contains only bit 9. MRV selects such a forced cell before branching elsewhere, writes 9, and propagates that restriction through its masks.

**Candidate branching preserves every possible completion**

The candidate mask contains exactly the digits absent from the selected cell's row, column, and box. Writing one of those digits preserves all Sudoku constraints, and restoring the cell and masks on failure returns the search to the identical prior state.

Consider any valid completion extending the current partial board. Its digit at the selected cell must appear in the candidate mask, so the search includes that branch regardless of the MRV choice. Repeating the argument at each deeper cell shows that backtracking retains a path to every valid completion. A filled board reached through legal candidates is itself valid and preserves every original clue; the solvability guarantee ensures one such path succeeds.

## Complexity detail
With `E` empty cells, the loose worst-case search tree has at most nine branches per level, $O(9^E)$. Masks and MRV dramatically prune real puzzles but do not change that exponential worst case. Recursion and the empty-cell list use $O(E)$ space; the fixed masks are constant.

## Alternatives and edge cases
- **First-empty backtracking:** correct but can explore far more branches before encountering a contradiction.
- **Sets instead of masks:** clearer to some readers but performs more allocations and set operations.
- **Exact cover / Algorithm X:** offers a powerful general formulation but requires substantially more infrastructure for a fixed 9×9 puzzle.
- An already solved valid board has $E = 0$ and succeeds immediately without changing clues.
- The contract guarantees a solvable board, so the public operation need not define an error result. The search itself should still return failure internally to drive backtracking.
- MRV changes exploration order but not the solution set. If multiple completions were allowed, it would return whichever valid completion its candidate order finds first.
