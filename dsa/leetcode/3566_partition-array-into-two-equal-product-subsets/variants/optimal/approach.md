## General

If both required subsets have product `target` and together contain every element, multiplying their products shows that the product of the entire array must be `target * target`. Reject immediately when this necessary condition fails.

Once the total product equals `target * target`, it is enough to find one nonempty subset whose product is `target`: the product of every excluded element is then the total divided by that subset product, which is also `target`. The positive distinct input and $n\ge3$ rule also prevent the only problematic whole-array case at target 1.

Use recursive include/exclude search to construct that first subset. A state records the current index, selected product, and whether at least one value has been selected. Accept when the product reaches `target` with a nonempty selection. Reject when all values have been considered, the product already exceeds `target`, or the current product does not divide `target`. The last test is safe because multiplying by further positive integers cannot remove a prime factor that the target does not contain.

Every subset corresponds to exactly one series of include/exclude decisions, so the search is complete. The early total-product condition then proves that any accepted subset has a valid nonempty complement with the required product.

## Complexity detail

There are at most $2^n$ include/exclude states in the recursion tree, and each state performs constant-time arithmetic under the problem's bounded integer model. The worst-case time is $O(2^n)$. The recursion depth is at most $n$, so auxiliary space is $O(n)$.

The benchmark size is $n$. Each tier has total product exactly `target * target` but no target-product subset, forcing the accepted search to resolve the subset decisions. The calibrated slower implementation enumerates the same masks but recomputes every subset product from all $n$ positions, adding a factor of $n$.

## Alternatives and edge cases

- **Recompute every bitmask product:** This is straightforward but costs $O(n2^n)$ because each mask scans the full array.
- **Meet in the middle:** Products of both halves can be enumerated in roughly $O(2^{n/2})$ stored states, but the extra machinery and exponential memory are unnecessary for $n\le12$.
- **Total product mismatch:** The answer is immediately false even if some subset alone has product `target`.
- **Value 1:** Including 1 does not change a product, but the element must still belong to exactly one subset.
- **Current product exceeds target:** With positive integers, later multiplication cannot bring it back down.
- **Current product does not divide target:** That branch contains an irreparable prime factor or exponent and can be discarded.
- **Nonempty subsets:** The search tracks whether it selected a value; the full-partition identity guarantees a nonempty complement for every feasible input.
- **Large target:** Implementations in fixed-width languages must avoid overflowing while checking the squared target or multiplying candidates.
