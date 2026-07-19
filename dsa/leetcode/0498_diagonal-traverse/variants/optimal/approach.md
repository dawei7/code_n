## General
**Group cells by coordinate sum**

Every cell on one top-right-to-bottom-left diagonal has the same `row + col`. The possible sums run from zero through `rows + cols - 2`, which fixes the order in which diagonals appear.

**Enumerate one diagonal without scanning the matrix**

For a sum `d`, start at row `max(0, d - cols + 1)` and column `d - row`. Increase the row and decrease the column until leaving the matrix. This visits exactly the cells of that diagonal.

**Reverse alternating diagonals**

The direct enumeration moves downward-left. Odd-numbered diagonals keep that order, while even-numbered diagonals are reversed to move upward-right. Append each oriented diagonal to the answer.

**Why every cell appears once**

Each matrix coordinate has one unique sum and is therefore assigned to exactly one diagonal. The bounded row-and-column walk reaches every coordinate with that sum once, and parity changes only its order, not its membership.

## Complexity detail
Every matrix cell is collected and appended once, giving $O(rows \cdot cols)$ time. The returned list and the largest temporary diagonal together use $O(rows \cdot cols)$ space, with $O(\min(rows, cols))$ auxiliary storage beyond the output.

## Alternatives and edge cases
- **Direction simulation:** move a cursor upward-right or downward-left and change direction at boundaries with the same linear bounds.
- **Scan all cells for every diagonal:** is correct but takes $O(rows \cdot cols \cdot (rows + cols))$ time.
- **Map sums to lists:** simplifies grouping but stores all cells in an additional dictionary of diagonals.
- **Single row:** returns left-to-right order.
- **Single column:** returns top-to-bottom order.
- **Rectangular matrix:** diagonal lengths grow only to the shorter dimension, then shrink.
- **Parity:** diagonal zero is traversed in the upward-right orientation, though it contains one cell.
