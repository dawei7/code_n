## General
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

## Complexity detail
The board dimensions and digit alphabet are fixed by the contract, so both the 81-cell scan and at most 27 nine-element sets are bounded constants: $O(1)$ time and space. For a generalized `N×N` board the same method would use $O(N^2)$ time and space.

## Alternatives and edge cases
- **Validate every unit separately:** is still constant for 9×9 boards but revisits cells and duplicates indexing logic.
- **Bit masks:** replace sets with integers for smaller constants while preserving the same invariant.
- **Attempt to solve the puzzle:** answers a stronger and different question; a valid partial board may still be unsolvable.
- A completely empty board is valid because no uniqueness rule is violated. Validity does not imply completeness or solvability.
- The contract guarantees a 9×9 shape and symbols `1` through `9` or `.`; structural and alphabet validation would be separate concerns.
- For a generalized `N×N` board, the scan and ownership storage are $O(N^2)$ even though the fixed 9×9 contract is $O(1)$.
