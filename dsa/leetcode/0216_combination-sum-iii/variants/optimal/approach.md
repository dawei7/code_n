## General
Backtrack over the fixed candidates `1` through `9`, always choosing the next value strictly after the previous choice. The state consists of the next permitted candidate, the remaining number of slots, the remaining sum, and the current path.

Increasing choices serve two purposes at once: a digit cannot be reused, and one mathematical combination is generated in only one order. After choosing `3`, for example, recursion may consider `4..9` but never return to `1` or choose `3` again.

Accept a path only when it contains exactly `k` values and the remaining sum is zero. At each depth, candidates are
visited in ascending order. As soon as a candidate exceeds the remaining sum, it and every larger candidate are
impossible, so the loop stops. The protected source intentionally does not add minimum-sum, maximum-sum, or
available-slot bounds; the fixed nine-value universe keeps the direct search small.

For $k = 3, n = 9$, the increasing paths that finish exactly are `[1,2,6]`, `[1,3,5]`, and `[2,3,4]`. Permutations such as `[6,2,1]` are never generated.

Every emitted path contains exactly `k` distinct values from `1..9`, is increasing, and has sum `n`, so it is valid. Conversely, every valid combination has one unique increasing ordering. At each depth, the recursion includes the branch choosing that ordering's next value; none of the sound pruning rules can remove it because its remaining choices prove the relevant bounds feasible. The recursion therefore reaches and emits every valid combination exactly once.

## Complexity detail
The recursion can visit at most all $2^9$ subsets of the fixed digit universe. If $R$ combinations are returned, copying
their paths costs $O(Rk)$, where $R \le \binom{9}{k}$. The stated $O(2^9 k)$ bound safely includes traversal and output
copying. The current path and recursion depth use $O(k)$ auxiliary space, excluding returned combinations. Because the
contract fixes the universe at nine digits and $2 \le k \le 9$, honest asymptotic runtime scaling is unavailable; the
bounded-domain certificate records the replacement proof.

## Alternatives and edge cases
- **Permutation generation:** It repeats each combination up to $k!$ times.
- **Candidate reuse:** Allowing the chosen digit in recursive calls violates distinctness and solves a different
  Combination Sum variant.
- **Stronger arithmetic bounds:** Minimum-sum, maximum-sum, and available-slot checks can prune more calls, but do not
  materially improve the fixed nine-digit search domain.
- **Dynamic programming:** It can count possibilities but is unnecessary when the task must enumerate the combinations.
- **Impossible target bounds:** Targets below the sum of `1..k` or above the sum of the largest `k` digits return empty.
- **All digits:** Selecting all nine values is possible only for sum `45`.
