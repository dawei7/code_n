## General
**Encode used bikes:** Represent an assignment prefix by a $B$-bit mask. Bit `j` is set exactly when bike `j` has already been assigned. Assign workers in index order, so `mask.bit_count()` is also the index of the next worker and no separate worker dimension is needed.

**Try every unused bike once per state:** For the next worker, consider each bike whose bit is clear. Add that worker-bike Manhattan distance to the optimal remaining cost for the mask with the bike bit set. The state value is the minimum of those choices. When $W$ bits are set, all workers have bikes and the remaining cost is zero.

**Memoize overlapping suffixes:** Different assignment orders can reach the same used-bike mask before assigning the same next worker. Cache the result for each mask so its remaining choices are solved once rather than once per partial permutation.

Every valid complete assignment begins with exactly one unused bike choice for the current worker, so the recurrence considers it. Conversely, every recurrence path assigns distinct bikes to workers in order and is valid. Taking the minimum over the first choice plus an optimal cached suffix therefore yields the globally minimum total distance.

## Complexity detail
There are at most $2^B$ masks, and each state examines up to $B$ bikes. Total time is $O(B2^B)$. The memo table stores at most one value per mask, and recursion depth is at most $W$, giving $O(2^B)$ auxiliary space.

## Alternatives and edge cases
- **Plain backtracking:** Enumerate every one-to-one assignment without caching. It is correct but can require factorial time when workers and bikes have equal counts.
- **Hungarian algorithm:** It solves larger rectangular assignment problems in polynomial time, but its machinery is unnecessary for the bound $B \le 10$.
- **Greedy nearest pair:** A locally shortest distance can reserve a bike needed much more by another worker, so greedy choices do not guarantee the minimum total.
- **More bikes than workers:** The recursion stops after $W$ selected bits; unused bikes need no special handling.
- **Single worker:** The recurrence simply chooses the nearest bike.
- **Equal total costs:** Only the minimum numeric sum is returned, so assignment tie breaking is irrelevant.
- **Zero Manhattan distance:** The uniqueness guarantee prevents a worker and bike from sharing a location, but the recurrence would still handle a zero-cost edge correctly.
