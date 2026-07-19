## General
**Match target characters across source-block boundaries**

Scan one copy of `s1` at a time while keeping `target_index`, the next needed position in `s2`. Each match advances that index; reaching the end of `s2` increments the number of completed target copies and resets the index to zero. This naturally permits one target copy to begin in one source block and finish in a later block.

**A block-boundary index determines the future**

At the end of a source block, the only state affecting future matches is `target_index`. If the same index appears after two different source-block counts, processing between those boundaries is a cycle: it consumes a fixed number of source blocks and completes a fixed number of `s2` copies.

**Fast-forward whole cycles**

Record for each boundary index the source-block count and completed-target count where it first appeared. On repetition, compute the cycle's two deltas and skip as many whole cycles as fit in the remaining `n1` blocks. Then directly simulate the short leftover suffix.

**Convert target copies into requested groups**

The scan counts individual copies of `s2`. Every output unit requires `n2` such copies, so integer-divide the completed count by `n2`. Any incomplete group cannot contribute to the answer.

**Reject an impossible alphabet immediately**

If `s2` contains a character absent from `s1`, no amount of source repetition can form even one target copy, so return zero before simulation.

## Complexity detail
There are only `abs(s2)` possible boundary indices before one repeats. Detecting the cycle and simulating the leftover blocks each scan at most a constant multiple of those states, with $O(|s1|)$ work per block, for $O(|s1| \cdot |s2|)$ time independent of a huge `n1`. The boundary-state map uses $O(|s2|)$ space.

## Alternatives and edge cases
- **Scan all `n1` source blocks:** uses constant state and is correct but costs $O(n1 \cdot |s1|)$ when `n1` is large.
- **Precompute every target-index transition:** builds a finite-state transition table, then applies cycle detection or binary lifting.
- **Materialize repeated strings:** wastes memory proportional to repetition counts and is infeasible at the limits.
- **Missing target character:** makes the answer zero regardless of repetition counts.
- **Cross-block match:** preserve the target index between source copies; resetting it would miss valid subsequences.
- **Incomplete final `s2` or group:** only fully matched target copies and complete groups count.
- **Cycle with leftover blocks:** skip only whole cycles and simulate the remainder to avoid overcounting.
