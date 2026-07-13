# Valid Sudoku

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 36 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-sudoku/) |

## Problem Description
### Goal
You are given a partially filled $9 x 9$ Sudoku board. Filled cells contain digits `1` through `9`, while a dot represents an empty cell. Check the values already present against the standard Sudoku constraints.

No digit may appear twice in one row, one column, or one of the nine $3 x 3$ sub-boxes. Empty cells impose no conflict and do not need to be filled. Return whether the current board is valid; validity does not require proving that the unfinished puzzle has a solution.

### Function Contract
**Inputs**

- `board`: 9×9 `List[List[str]]` containing digits `1`–`9` or `.`

**Return value**

`True` when no filled digit is duplicated in any required unit; otherwise `False`.

### Examples
**Example 1**

- Input: the standard partially filled valid board shown in the cases
- Output: `True`

**Example 2**

- Input: the same board with a second `5` in its first row
- Output: `False`

**Example 3**

- Input: an empty 9×9 board
- Output: `True`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Every filled cell belongs to exactly three uniqueness units**

Maintain one set for each of nine rows, nine columns, and nine boxes. For a filled cell `(row, col)`, compute its box index as `(row // 3) * 3 + col // 3`: integer division identifies the box row and box column, and the multiplication flattens those coordinates to `0..8`.

If the digit already appears in any of the three associated sets, the board is invalid. Otherwise insert it into all three. Empty cells contribute no constraint and are skipped.

**A membership hit is a concrete duplicate witness**

Before each cell is processed, every set contains exactly the filled digits previously encountered in its unit, with no duplicates. A membership hit identifies the earlier equal digit in that same row, column, or box, so it is a concrete rule violation. Three successful insertions preserve the invariant for later cells.

**Trace row, column, and box conflicts independently**

If row zero already contains `5` at column zero and another `5` appears at column four, the row-zero set contains `5` when the latter cell is reached, so validation returns false immediately. A duplicate confined to a box or column is detected analogously by its corresponding set.

**Every duplicate has an unavoidable second encounter**

If two equal filled digits share a row, column, or box, one of them is scanned later. By then the earlier digit is present in the corresponding unit set, so the later occurrence forces rejection. No invalid duplicate can escape this second encounter.

Conversely, the algorithm rejects only when a digit is already recorded for the same row, column, or box, which is an actual rule violation. Finishing the board without rejection therefore means every filled digit is unique in all three required units.

#### Complexity detail

The board dimensions and digit alphabet are fixed by the contract, so both the 81-cell scan and at most 27 nine-element sets are bounded constants: $O(1)$ time and space. For a generalized `N×N` board the same method would use $O(N^2)$ time and space.

#### Alternatives and edge cases

- **Validate every unit separately:** is still constant for 9×9 boards but revisits cells and duplicates indexing logic.
- **Bit masks:** replace sets with integers for smaller constants while preserving the same invariant.
- **Attempt to solve the puzzle:** answers a stronger and different question; a valid partial board may still be unsolvable.
- A completely empty board is valid because no uniqueness rule is violated. Validity does not imply completeness or solvability.
- The contract guarantees a 9×9 shape and symbols `1` through `9` or `.`; structural and alphabet validation would be separate concerns.
- For a generalized `N×N` board, the scan and ownership storage are $O(N^2)$ even though the fixed 9×9 contract is $O(1)$.

</details>
