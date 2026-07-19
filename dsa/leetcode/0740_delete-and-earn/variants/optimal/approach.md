## General
**Combine all copies of the same value**

If value `x` is chosen once, every other copy of `x` can also be chosen: doing so earns more points and introduces no additional forbidden values. Aggregate all copies into `points[x] = x * frequency(x)`. The decision is now whether to take each distinct value's entire point total.

**Recognize the house-robber structure on values**

Taking `points[x]` forbids only `points[x-1]` and `points[x+1]`. Lay the totals out by numeric value, inserting zero for absent values. This is exactly the maximum-weight selection of nonadjacent positions.

**Carry take and skip states across the value axis**

Before processing a value, `take` is the best score that selected the previous value and `skip` is the best score that did not. For the current total, selecting it requires the old `skip`, so new `take = skip + points[x]`. Skipping it permits either old state, so new `skip = max(skip, take)`. The answer is the larger final state.

**Why aggregation and the recurrence are complete**

Any valid original sequence corresponds to a set of chosen values with no consecutive integers, and taking all copies of every chosen value can only improve it. Conversely, every nonadjacent value set is realizable because choosing those values never deletes one another. The two-state recurrence considers exactly the take-or-skip alternatives for every value and keeps the best compatible prefix score, so its final maximum equals the optimal earning total.

## Complexity detail
Let `n` be the list length and `m = max(nums)`. Aggregating the input takes $O(n)$ time, and scanning point totals from `0` through `m` takes $O(m)$, for $O(n+m)$ time. The point array uses $O(m)$ space; the recurrence itself uses constant additional state.

## Alternatives and edge cases
- **Sort only distinct values:** aggregate in a hash map, sort its `u` keys, and handle gaps explicitly in $O(n+u \log u)$ time and $O(u)$ space; this is attractive when values are sparse.
- **Memoized recursion:** the same take-or-skip recurrence can be written top down, but the iterative form avoids call-stack overhead.
- **Explore choices without memoization:** branching on each adjacent value group repeats subproblems and grows exponentially.
- **One distinct value:** take every copy, earning their full sum.
- **Gaps larger than one:** both sides may be taken because they do not delete each other.
- **Many duplicates:** aggregate their total before making any adjacency decision.
- **Heavier neighboring combination:** two outer values may together beat the total at the value between them.
- **Maximum value:** allocating through `max(nums)` includes the upper constraint safely.
