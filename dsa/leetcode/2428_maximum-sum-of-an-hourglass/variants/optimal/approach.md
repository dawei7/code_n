## General

**Anchor the fixed shape by its top-left corner.** An hourglass beginning at `(row, column)` selects offsets `(0,0)`, `(0,1)`, `(0,2)`, `(1,1)`, `(2,0)`, `(2,1)`, and `(2,2)`. Its top-left corner may use rows `0` through `m - 3` and columns `0` through `n - 3`.

Visit every legal anchor. Add the three top cells, the middle center, and the three bottom cells explicitly, then retain the largest sum. Because all grid values are non-negative, zero is a valid initial maximum.

Every contained, unrotated hourglass has one unique top-left corner in those ranges, and the seven-term expression selects exactly its cells. The scan therefore evaluates every candidate once, so the retained maximum is the requested result.

## Complexity detail

There are $(m-2)(n-2)$ placements, and each uses exactly seven reads and a constant number of arithmetic operations. The running time is $O(mn)$. Only loop indices and two sums are stored, so the auxiliary space is $O(1)$.

This time bound is asymptotically optimal. A constant fraction of matrix cells can independently change at least one hourglass sum, so arbitrary legal inputs require $\Omega(mn)$ inspection in the worst case.

## Alternatives and edge cases

- **Two-dimensional prefix sums:** Rectangle sums become constant-time, but the missing middle-row side cells still require adjustment; preprocessing costs $O(mn)$ time and space without improving the asymptotic bound.
- **Convolution with a seven-cell mask:** This expresses the same scan and retains $O(mn)$ work, while adding abstraction or library overhead.
- **Exactly `3 x 3`:** There is one placement.
- **Rectangular grids:** The row and column anchor ranges are independent.
- **Excluded middle corners:** `(row + 1, column)` and `(row + 1, column + 2)` must never contribute.
- **All zeros:** The maximum is 0.
- **Overlapping placements:** Shared cells contribute independently to each candidate sum.
- **No rotation:** Sideways hourglass patterns are outside the contract.
