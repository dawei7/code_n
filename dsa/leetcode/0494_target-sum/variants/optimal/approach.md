## General
**Store counts for reachable partial sums**

Begin with one way to make sum zero before processing any values. A mapping associates every reachable sum with the number of sign assignments that produce it.

**Apply both sign choices**

For each value, create a fresh mapping. Every prior sum with count `ways` contributes `ways` assignments to `sum + value` and another `ways` assignments to `sum - value`. Replacing the old mapping prevents one array element from being used more than once.

**Why the counts are exact**

After processing the first `k` values, induction shows the mapping counts precisely all $2^{k}$ sign assignments grouped by their sum. Extending each assignment once with plus and once with minus creates every assignment for value $k + 1$ exactly once. The target's final count is therefore the requested answer.

**Zeros still create distinct expressions**

For a zero, adding and subtracting reach the same numeric sum, but they are different sign choices. Performing both updates doubles the stored count as required.

## Complexity detail
Let `total = sum(nums)`. At most `2 * total + 1` sums are reachable after each of `n` values, so time is $O(n \cdot total)$ and the two mappings use $O(total)$ space.

## Alternatives and edge cases
- **Subset-sum transformation:** assigning plus signs to a subset reduces the problem to counting subsets with sum `(total + target) / 2`; it has the same pseudo-polynomial bounds.
- **Memoized recursion:** caches `(index, current_sum)` states and matches the dynamic-programming complexity.
- **Unmemoized recursion:** is correct but explores all $2^{n}$ sign assignments.
- **Target outside `[ - total, total]`:** has zero assignments.
- **Parity mismatch:** the subset-sum form must reject a nonintegral transformed target.
- **Zeros:** double every existing count.
- **Negative target:** requires no special case in the signed-sum mapping.
