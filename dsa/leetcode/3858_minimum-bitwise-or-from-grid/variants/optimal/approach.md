## General

**Translate zero result bits into row feasibility**

Suppose a mask records bits that the final OR must keep zero. A row can respect that mask exactly when it contains at least one value with `(value & mask) == 0`. Because rows are selected independently, the entire grid can respect the mask if and only if this condition holds for every row: choose any compatible value from each row, and none of the forbidden bits appears in their OR.

**Decide bits from most significant to least significant**

Numerical minimization of nonnegative integers is lexicographic by bits: clearing a more significant bit is preferable to every possible choice of lower bits. Process the bits from the highest bit present in the grid down to zero. Tentatively add the current bit to the forbidden mask and scan every row for a compatible value.

If all rows remain feasible, keep the bit forbidden. The mask itself proves that a joint selection exists with every accepted higher bit and the current bit equal to zero. If some row has no compatible value, then every selection that preserves the already-forbidden higher bits must set the current bit somewhere; record that bit in the answer instead.

Inductively, after each decision, the fixed answer prefix is the smallest feasible prefix. Once all bits are processed, the recorded bits form the minimum possible OR.

## Complexity detail

Let $M$ and $N$ be the row and column counts, and let $B$ be the bit length of the maximum cell value. Each of the $B$ feasibility checks scans at most all $MN$ cells, so the time complexity is $O(BMN)$. The source bound `grid[i][j] <= 100000` gives $B\le17$. The algorithm stores only masks and loop state, using $O(1)$ auxiliary space.

The benchmark defines size as the row count with two choices per row. Each new row can independently contribute a new bit. The accepted feasibility scan is $O(BMN)$; the correct slower control materializes every reachable OR after each row, growing to exponentially many states on these tiers.

## Alternatives and edge cases

- **Reachable-OR dynamic programming:** Combine every existing OR state with every value in the next row and deduplicate the results. It is correct but can retain exponentially many masks before the fixed 17-bit ceiling is reached.
- **Enumerate row selections:** Trying all $N^M$ combinations is a direct oracle only for tiny grids.
- **Minimize each row independently:** Choosing the numerically smallest value in every row can be suboptimal because different values may avoid overlapping high bits more effectively.
- **Test bits independently:** A different value might clear each bit separately, yet no single value clears all previously accepted bits; feasibility must use the entire accumulated forbidden mask.
- **One row:** The result is simply that row's smallest value, which the bit-greedy checks recover.
- **One column:** Every row's sole value must be selected, so the answer is their ordinary bitwise OR.
- **Positive cells:** The result cannot be zero because every valid selection includes at least one positive value.
