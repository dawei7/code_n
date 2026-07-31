## General

**Read the fixed-width endpoints**

The format always places the starting column at `s[0]`, starting row at
`s[1]`, ending column at `s[3]`, and ending row at `s[4]`. Convert the column
letters to character codes and the row characters to integers so both
inclusive intervals can be traversed directly.

**Make loop order match output order**

Use the column interval as the outer loop and the row interval as the inner
loop. For each coordinate pair, concatenate the current column letter and row
number and append that cell name. The nested-loop order is already
non-decreasing by column and then row, so no sorting step is needed.

Every iteration chooses one column within the horizontal bounds and one row
within the vertical bounds, hence produces a cell inside the rectangle.
Conversely, every pair from those two inclusive intervals appears in exactly
one nested-loop iteration. The output therefore contains all and only the
requested cells once, in the prescribed order.

## Complexity detail

The nested loops execute once for each of the $A=wh$ returned cells, taking
$O(A)$ time. The returned list and its cell strings require $O(A)$ space; the
loop state itself is constant.

## Alternatives and edge cases

- **Generate in reverse and prepend:** Traversing backward and rebuilding the
  result at the front preserves the final order but takes $O(A^2)$ time.
- **Generate then sort:** Enumerate cells in arbitrary order and apply a
  comparison sort. This adds unnecessary $O(A\log A)$ time.
- A one-cell range returns exactly its shared endpoint.
- A one-row range advances columns while keeping the row fixed.
- A one-column range advances rows within that column.
- Both endpoints are inclusive.
- Column order has priority over row order, so `K2` precedes `L1`.
