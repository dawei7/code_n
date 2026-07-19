## General
**Reject multiplicities that cannot be separated**

Each value may appear at most once in any of the `k` subsets. If some value occurs more than `k` times, at least one subset would receive two copies by the pigeonhole principle, so return `-1` immediately. Otherwise a bitmask can distinguish the individual array occurrences even when their values match.

**Precompute every legal completed subset**

Enumerate masks over the $n$ indices. A mask is a legal group only when it selects exactly $m$ indices and their values are all distinct. Store its incompatibility, `max(values) - min(values)`, in a table indexed by the mask. Invalid masks retain a sentinel cost.

**Build the partition with subset dynamic programming**

Let `best(used)` be the minimum additional incompatibility needed after the indices marked in `used` have already been assigned to complete groups. Enumerate submasks of the remaining indices; each precomputed legal submask can become the next group, adding its cost to `best(used | group)`.

Always require the next group to contain the first unused index. Every completed partition has exactly one group containing that index, so this restriction removes only permutations of the same groups, never a distinct partition. It greatly reduces duplicate transitions while keeping the state determined solely by `used`.

For any state, the recurrence considers every possible legal group containing its anchor. Choosing one such group leaves a smaller instance on precisely the unselected occurrences. By induction, the recursive value supplies the minimum cost partition of that remainder, so adding the current incompatibility gives the best partition beginning with that group. Taking the minimum over all anchored legal groups therefore gives the optimum for the state. The empty mask begins with no assigned elements, and the full mask has zero remaining cost; consequently `best(0)` is exactly the minimum total.

## Complexity detail
Precomputing group costs takes $O(n2^n)$ time in the direct mask scan. Across all dynamic-programming states, enumerating submasks yields the standard $O(3^n)$ bound, which dominates for this exponential domain. The group-cost table and memoized state values each have $2^n$ entries, and recursion depth is at most `k`, giving $O(2^n)$ space.

## Alternatives and edge cases
- **Backtracking into labeled groups:** can be pruned by duplicate states, but without bitmask memoization it repeatedly explores equivalent group orders and may grow much faster.
- **Valid-group lists by anchor index:** avoids enumerating invalid submasks during transitions, but duplicating each group across its indices uses additional storage.
- **One subset:** all values must be distinct, and the answer is the overall maximum minus minimum; any duplicate makes the partition impossible.
- **One element per subset:** every incompatibility is zero, and duplicates are harmless because they occupy different subsets.
- **Frequency exactly `k`:** the repeated value must occur once in every subset but does not by itself make the partition impossible.
- **Occurrence identity:** equal values at different indices need separate mask bits even though the legality check compares their values.
