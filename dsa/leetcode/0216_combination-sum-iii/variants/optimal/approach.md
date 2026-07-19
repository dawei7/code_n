## General
Backtrack over the fixed candidates `1` through `9`, always choosing the next value strictly after the previous choice. The state consists of the next permitted candidate, the remaining number of slots, the remaining sum, and the current path.

Increasing choices serve two purposes at once: a digit cannot be reused, and one mathematical combination is generated in only one order. After choosing `3`, for example, recursion may consider `4..9` but never return to `1` or choose `3` again.

Accept a path only when it contains exactly `k` values and the remaining sum is zero. Several bounds can prune impossible branches early:

- A negative remaining sum cannot recover because all future values are positive.
- Fewer available candidates than remaining slots makes completion impossible.
- The sum of the smallest possible remaining choices may already exceed the target.
- The sum of the largest possible remaining choices may still fall short.

For $k = 3, n = 9$, the increasing paths that finish exactly are `[1,2,6]`, `[1,3,5]`, and `[2,3,4]`. Permutations such as `[6,2,1]` are never generated.

Every emitted path contains exactly `k` distinct values from `1..9`, is increasing, and has sum `n`, so it is valid. Conversely, every valid combination has one unique increasing ordering. At each depth, the recursion includes the branch choosing that ordering's next value; none of the sound pruning rules can remove it because its remaining choices prove the relevant bounds feasible. The recursion therefore reaches and emits every valid combination exactly once.

## Complexity detail
The fixed universe contains at most `C(9,k)` size-`k` subsets, and copying each successful path costs $O(k)$, giving the stated $O(\binom{9}{k}k)$ output-sensitive bound. The current path and recursion depth use $O(k)$ auxiliary space, excluding returned combinations.

## Alternatives and edge cases
- Generating permutations repeats each combination up to $k!$ times.
- Allowing the same candidate in recursive calls violates distinctness and solves a different Combination Sum variant.
- Dynamic programming can count possibilities but is unnecessary for enumerating this tiny fixed domain.
- Targets below the sum of `1..k` or above the sum of the largest `k` digits return empty.
- Selecting all nine values is possible only for sum `45`; impossible `k` values naturally yield no combinations.
