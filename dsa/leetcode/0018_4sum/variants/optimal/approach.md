## General
**Fix two values and leave a monotone two-sum problem**

Sort the values. Choose first index `i` and second index `j`, then place left and right pointers around the suffix after `j`. The remaining pair must equal `target - values[i] - values[j]`.

Sorted order makes that pair sum monotone. If the four-value total is too small, replacing the left value with a larger one is the only move that can increase it. If the total is too large, replacing the right value with a smaller one is the only move that can decrease it. Thus one suffix scan handles all candidate pairs for the fixed prefix.

**Enforce uniqueness at every selection level**

Skip `values[i]` when it equals the previous first value and likewise skip duplicate second values for a fixed `i`. After emitting a quadruplet, advance both pointers past all copies of their current values. This prevents duplicates without a result set.

Bounds from the four smallest or four largest available values can stop or skip fixed-index searches that cannot reach the target, improving constants without changing worst-case complexity.

**Prune only when sorted bounds prove impossibility**

For a fixed first index, the sum of it and the three smallest available successors is the smallest achievable quadruplet. If even that exceeds `target`, every later first value is at least as large, so the outer loop may stop. Conversely, if the first value plus the three largest values is still below `target`, this first value cannot succeed and may be skipped. Analogous bounds can be applied after choosing the second index.

These checks are optional constant-factor improvements. They must use four distinct valid positions and should be computed in a sufficiently wide integer type so the pruning arithmetic itself does not overflow.

**What the two pointers have ruled out**

For fixed `i` and `j`, every pair outside the pointer interval has been examined or ruled out by sorted monotonicity. Moving a pointer discards only sums that remain on the same wrong side of the target. Duplicate skips remove value-identical quadruplets, never a new combination.

**Trace a representative input**

Sorting `[1, 0, -1, 0, -2, 2]` gives `[-2, -1, 0, 0, 1, 2]`. Fixing `-2, -1` finds pair `1, 2`; fixing `-2, 0` finds `0, 2`; fixing `-1, 0` finds `0, 1`. Duplicate fixed and pointer values are skipped, leaving exactly three results.

**Why fixing two values covers every quadruplet once**

Every sorted quadruplet has a first and second value. The nested loops eventually choose that pair; skipping an equal fixed value loses no new value combination because the earlier identical choice had access to every later value that the repeated choice can use.

With the first two values fixed, the remaining target is a sorted two-sum problem. A sum that is too small can only be raised by moving the left pointer, and a sum that is too large can only be lowered by moving the right pointer, so the sweep cannot skip a matching pair. After a match, advancing over equal pointer values removes only repeated spellings of that same quadruplet. Every distinct solution is therefore found and emitted once.

## Complexity detail
Sorting costs $O(n \log n)$. The two fixed-index loops select $O(n^2)$ prefixes, and each launches an $O(n)$ two-pointer sweep, so worst-case time is $O(n^3)$. A copied sorted array uses $O(n)$ auxiliary space; in-place sorting has language-dependent stack or workspace costs. The result list is output space.

## Alternatives and edge cases
- **Four nested loops:** checks all index quadruples in $O(n^4)$ time and still needs value deduplication.
- **Pair-sum table:** can approach $O(n^2)$ expected work for detection, but maintaining distinct indices and unique quadruplets requires substantial $O(n^2)$ storage and careful normalization.
- **Recursive k-sum:** generalizes this pattern cleanly to other `k`; its two-sum base case is the same monotone pointer scan.
- Fewer than four inputs return an empty result. Repeated values can form a valid answer, as with four copies of `2`, but that value quadruplet must be emitted only once.
- In fixed-width languages, addends near the constraint limits should be promoted before summation to prevent overflow from reversing comparisons with `target`.
