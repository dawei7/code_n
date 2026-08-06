## Hint

**Hint 1:** Integral prices have only one possible rounded value. Subtract those values from the target to reduce the problem.

**Hint 2:** For a non-integral price, subtracting its floor leaves a binary choice: contribute either `0` by rounding down or `1` by rounding up.

**Hint 3:** The reduced task is to choose a `0` or `1` contribution at each remaining position so their sum reaches the reduced target while the corresponding error changes are minimized. This formulation can be solved with dynamic programming.
