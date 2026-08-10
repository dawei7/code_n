## General

**Use the smallest possible group lengths**

If `k` groups have strictly increasing positive lengths, the least total number of placements they can use is achieved by lengths

$$
1,2,\ldots,k,
$$

whose sum is `k(k+1)/2`. Any larger length choice consumes more usage capacity without increasing the number of groups. Therefore a maximum-count construction may be reasoned about using these minimal target sizes.

The second restriction is that one number cannot appear twice inside one group. A number with usage limit `u` can contribute to at most `u` different groups, and never more than the number of groups being built.

**Sort capacities from small to large**

The exact solution sorts `usageLimits` in place. Processing small limits first exposes scarce numbers early, while larger limits later can absorb accumulated unmet placement capacity.

Sorting is part of the real implementation. The Optimal manifest instead describes clamping and counting sort with linear time; that is a different algorithm. The source's initial `usageLimits.sort()` determines an `O(n log n)` time bound.

**Interpret the current entry as a pooled surplus**

Variable `k` is the number of groups already proven constructible with minimal lengths `1..k`.

As processing advances, the code carries unused capacity from earlier sorted entries into the next entry:

`usageLimits[i + 1] += usageLimits[i]`.

Thus the current value is not always one original usage limit. It becomes a pool of capacity available among processed numbers after the placements already committed to existing groups have been accounted for.

This capacity transfer is accounting, not a literal claim that one number's usage may be reassigned to another. The sorted greedy theorem says only the cumulative usable capacity matters at this stage, while processing one new distinct number per index ensures no group count exceeds the number of available labels.

**Decide whether one more group can be formed**

With `k` existing groups, the next minimal group must have length `k + 1`. The condition

`usageLimits[i] > k`

is equivalent to saying the current pool has at least `k + 1` units available.

If true:

1. Increment `k`, so it now equals the new group length.
2. Subtract `k` from the pool to pay for that group's placements.

Only one new group is created at a given index. After processing `i + 1` distinct numbers, no group can have length greater than `i + 1`, so the group count cannot jump by more than one when introducing one more number.

Any capacity left after paying for the new group is carried forward.

**A walkthrough**

For `usageLimits = [1, 2, 5]`, sorting changes nothing.

- At the first entry, pool 1 is greater than current `k = 0`. Form group length one, set `k = 1`, and spend one, leaving zero.
- At the second entry, pool 2 is greater than one. Form group length two, set `k = 2`, and spend two.
- At the third entry, pool 5 is greater than two. Form group length three, set `k = 3`, and spend three.

Three groups of lengths one, two, and three are feasible.

For `[1, 1, 100]`:

- The first one forms a length-one group.
- The second pool is not greater than `k = 1`, so it cannot fund length two by itself; its one unused unit is carried into the final entry.
- The final pool becomes 101, easily funding the length-two group.

Carry allows capacities from multiple small limits to jointly satisfy later total demand.

**Connection to cumulative triangular thresholds**

A common equivalent solution maintains cumulative capacity `total` and creates group `k + 1` when total reaches the next triangular requirement:

$$
1+2+\cdots+(k+1).
$$

The exact code subtracts each newly paid group length from the carried pool. Consequently, its current pooled value equals cumulative processed capacity minus all already committed minimal group sizes. Condition “pool at least `k+1`” is exactly the triangular-threshold test written in residual form.

Sorting and the one-increment-per-new-label rule handle the distinct-number feasibility that a total-sum check alone could obscure.

**Why the greedy choice is safe**

Whenever enough residual capacity exists for the smallest legal next group, creating it immediately cannot hurt a future maximum. Delaying it would preserve the same capacity but would not reduce the size required by any later group; future group lengths must only increase.

Paying the minimum `k + 1` placements leaves as much surplus as possible for later groups. If the pool is too small, no group of any valid next length can be formed yet, so carrying all capacity forward is optimal.

With sorted capacities, this residual process is the standard feasibility characterization for assigning distinct labels across groups. It produces the greatest `k` for which all minimal placement demands can be scheduled within individual usage limits.

**Mutation is part of the storage strategy**

The input list is used as the carry array. Sorting reorders it, subtracting consumes group costs, and addition transfers residual capacity. The original usage limits are not preserved.

This allows the core greedy scan to use only scalar extra state after sorting, but callers that need the original order or values must supply a copy.

## Complexity detail

Let `n` be the number of usage limits. Python sorting takes `O(n log n)` time. The subsequent scan performs constant work per index, taking `O(n)`. Total time is `O(n log n)`.

The manifest's `O(n)` time belongs to a different clamped counting-sort method and does not match `usageLimits.sort()` in the exact solution.

The scan itself uses `O(1)` scalar auxiliary space and reuses the input list. Python's Timsort can allocate `O(n)` temporary memory in the worst case, so implementation-level auxiliary space is `O(n)`. The list is modified in place.

## Alternatives and edge cases

- **Cumulative-sum threshold:** After sorting, accumulate limits and increment groups when total reaches the next triangular number. It is an equivalent and often more immediately recognizable formulation.
- **Binary search on group count:** Feasibility can be tested with capped capacities, but repeated checks add logarithmic overhead and complexity.
- **Counting sort after clamping limits to `n`:** Because no number can appear in more than `n` groups, this can realize the manifest's linear-time strategy with `O(n)` space.
- **Skip sorting:** Scarce and abundant capacities cannot be pooled safely in arbitrary order under this greedy update.
- **One number:** At most one group can exist because a group cannot repeat the same label.
- **Huge usage limit:** It cannot alone fill multiple positions in one group; group count remains bounded by the number of distinct labels.
- **All limits equal one:** Total capacity may be large, but distinct minimal groups consume triangularly; the greedy stops at the largest feasible count.
- **Pool exactly `k`:** It is one short of the required next length `k + 1`, so strict `> k` correctly waits.
- **Unused surplus:** It is carried forward and can help pay for later groups.
- **Large integer limits:** Python integers hold cumulative sums without overflow.
- **Input mutation:** Sorting and residual carry destroy original values and order.
- **Manifest mismatch:** Real source uses comparison sorting, so its time is `O(n log n)` rather than `O(n)`.
