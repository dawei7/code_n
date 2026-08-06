## Function Contract

**Inputs**

- `arr`: The initial array of $n$ integers.

Each daily update must compare only values from the previous day. In particular, a change at position `i` cannot affect the decision for `i + 1` until the following day. Comparisons are strict, so equality with either neighbor prevents that peak-or-valley update.

Let $C$ be the total number of individual increments and decrements performed before stabilization.

**Return value**

Return the stable array reached when a complete simultaneous day produces no changes. Positions `0` and `n - 1` must equal their original values.
