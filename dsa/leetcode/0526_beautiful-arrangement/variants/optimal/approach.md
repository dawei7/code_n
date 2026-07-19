## General
**Build only arrangements that can remain valid**

Fill the permutation from position `1` toward position `n`. At a position, try only unused values for which either the value divides the position or the position divides the value. Rejecting an incompatible value immediately avoids generating complete invalid permutations.

**Represent the chosen values with a bitmask**

Bit `value - 1` records whether `value` has already been placed. The number of set bits determines the next position, so the used-value mask completely describes a subproblem; the order that produced the mask cannot affect which continuations are legal.

**Memoize each remaining subproblem**

Different valid prefixes can select the same set of values in different orders. Cache the number of completions for each mask so those prefixes share one calculation. For a mask, sum the cached completion counts reached by placing every compatible unused value. The full mask contributes one completed arrangement.

**Why the sum counts every beautiful arrangement exactly once**

Every explored branch adds one unused value at the next fixed position and checks that position's condition, so a branch reaching the full mask is valid. Conversely, each valid permutation selects one of the explored compatible values at every position and therefore follows a unique root-to-leaf branch. Summing the child counts neither omits nor duplicates a valid permutation.

## Complexity detail
There are at most $2^{n}$ masks. Each mask examines up to `n` candidate values, giving $O(n \cdot 2^n)$ time. The memo table stores at most one count per mask for $O(2^n)$ space; the recursion depth is $O(n)$ and is dominated by the cache.

## Alternatives and edge cases
- **Bottom-up subset dynamic programming:** propagates counts between masks with the same $O(n \cdot 2^n)$ bounds, but may visit masks that the divisibility restrictions make unreachable.
- **Backtracking without memoization:** prunes incompatible placements but recomputes identical remaining-value subproblems and can approach factorial time.
- **Generate every permutation:** checks conditions only after or during generation and has an $O(n!)$ search space without state reuse.
- **Place constrained positions first:** can reduce branching in plain backtracking, but the position is no longer implied by the mask and the ordering must be tracked carefully.
- **$n = 1$:** the only permutation is valid because one divides itself.
- **Value equal to position:** always passes both divisibility directions.
- **Divisibility direction:** the condition is inclusive OR; either `value % position = 0` or `position % value = 0` is sufficient.
