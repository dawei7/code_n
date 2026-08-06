## General
**Store two generations in separate bits**

Every cell initially contains `0` or `1`, so its low bit can preserve the original state while the next bit records the
computed state. For each cell, inspect the eight neighboring coordinates that remain inside the board and add only
their low bits. Previously annotated cells therefore still contribute their original states.

Set the next bit exactly when the live-neighbor count is three, or when the count is two and the cell's original low
bit is set. This single condition represents both survival and birth; every other cell keeps a zero next bit and dies
or remains dead.

**Commit only after every next state is known**

After the first pass has annotated every cell, shift each value right once. The computed next bit becomes the new low
bit, so the board is updated in place without retaining a copy.

The low bit is never changed during the annotation pass. Consequently, every neighbor count is taken from the same
original generation regardless of traversal order. The next-bit condition implements all four transition rules, and
the final shifts expose all of those already-determined states simultaneously.

## Complexity detail
Let $m$ be the number of rows and $n$ the number of columns. Each of the $mn$ cells checks at most eight neighbors
and is shifted once, giving $O(mn)$ time. The two states share each existing integer, so the auxiliary space is
$O(1)$.

## Alternatives and edge cases
- **Copied original board:** computes the same simultaneous transition in $O(mn)$ time but uses $O(mn)$ auxiliary
  space.
- **Full-board rescanning per cell:** can remain correct but takes $O((mn)^2)$ time.
- **Borders and corners:** ignore coordinates outside the matrix, so they have fewer than eight possible neighbors.
- **Tiny or uniform boards:** the same rule handles a single cell, all-dead boards, and dense live regions without a
  special case.
