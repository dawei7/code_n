## General
**Use remaining needs as the complete state**

After any sequence of bundle purchases, future choices depend only on the quantities still required, not on the order used to reach them. Represent that state as an immutable tuple so equivalent subproblems share one memoized result.

**Keep individual purchases as a universal fallback**

For each state, buying every remaining item individually is always legal and gives an initial upper bound. Then try each bundle whose quantities do not exceed the remaining needs, subtract it componentwise, and combine its price with the optimal cost of the smaller state.

**Discard bundles that cannot improve a solution**

Ignore a bundle containing no items, which would not advance recursion. A bundle priced at least as high as its items bought individually is also unnecessary: replacing it with those individual purchases never costs more and preserves exact quantities.

**Why the recurrence finds the global minimum**

Any optimal plan either uses no further bundle, in which case the individual fallback matches it, or has a first bundle. That first bundle must fit the current needs, and the remainder of the plan is an optimal solution to the reduced state; otherwise it could be replaced by a cheaper remainder. Evaluating every legal first bundle and memoizing the minimum therefore covers and optimizes every valid plan.

## Complexity detail
There are at most $Π(\mathit{needs}_{i} + 1)$ remaining-quantity states. Each state checks `S` bundles across `M` item types, giving $O(SM \cdot \prod(needs_i + 1))$ time. Memo keys and recursion frames store `M` quantities per reachable state, using $O(M \cdot \prod(needs_i + 1))$ space.

## Alternatives and edge cases
- **Backtracking without memoization:** explores the same legal bundle sequences but recomputes equivalent remaining states exponentially many times.
- **Bottom-up multidimensional dynamic programming:** has the same state bound but is awkward to index when the number of item types varies.
- **Enumerate bundle usage counts:** bounding each offer independently creates a large Cartesian product and still needs exact-quantity checks.
- A bundle that exceeds any remaining quantity is illegal even when its price is attractive.
- Bundles may be reused as long as every application fits the remaining needs.
- Zero needs cost zero regardless of available offers.
- Non-discounted bundles may be ignored because individual purchases remain available.
- The modulus is not involved; return the exact minimum integer cost.
