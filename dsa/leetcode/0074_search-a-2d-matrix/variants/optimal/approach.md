## General
**The row-boundary condition creates one virtual sorted array**

Values increase within each row, and the first value of every row is greater than the previous row's final value. Therefore row-major traversal is one strictly increasing sequence of length $m \cdot n$. Binary-search its flat indices without constructing or copying that sequence.

**Division and remainder map a flat midpoint to its cell**

For flat index `middle`, the row is `floor(middle / columns)` and the column is `middle % columns`. Compare that cell to `target` and discard the lower or upper half exactly as in ordinary binary search.

**Standard binary-search elimination crosses row boundaries safely**

If `target` exists, its flat index remains inside the inclusive search interval. Every discarded half contains values strictly below or strictly above the target based on the midpoint comparison.

**Trace a midpoint in the second row**

In a 3-by-4 matrix, flat index 5 maps to row 1, column 1. If that value is 11 and the target is 13, discard indices through 5 and continue in the upper flat half, seamlessly crossing row boundaries.

**Row-major indices form one sorted searchable sequence**

Values increase within each row, and each row's first value is greater than the preceding row's last. Concatenating rows in row-major order is therefore globally sorted.

The quotient-and-remainder mapping from flat index to `(row, column)` is a bijection over all `mn` cells, so no position is lost or repeated. Binary search on these virtual indices makes the same safe half-discard decisions as on a physical sorted array and finds exactly the contained targets.

## Complexity detail
The interval of `mn` cells is halved each iteration, giving $O(\log(mn))$ time. Only bounds and coordinates are stored, using $O(1)$ space.

## Alternatives and edge cases
- **Scan every cell:** takes $O(mn)$ time.
- **Binary-search a row, then that row:** also gives logarithmic time, but requires a separate row-selection argument.
- **Copy into a flat list:** preserves binary-search time but wastes $O(mn)$ space and copying work.
- A one-cell matrix is an ordinary one-element binary search. Targets below the first or above the last value exhaust the interval and return false.
- This flattening proof needs the cross-row ordering condition; matrices sorted only within rows require a different search strategy.
