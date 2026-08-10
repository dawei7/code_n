## General

**Replace each bag by its filling cost**

For bag `i`, the only relevant quantity is how many additional rocks it needs:

$$
d_i = \texttt{capacity}[i] - \texttt{rocks}[i].
$$

Two bags with the same deficit cost the same to complete, regardless of their absolute capacities or current rock counts. Completing a bag is an all-or-nothing benefit of one: partially filling it does not increase the number of full bags.

The first loop computes every deficit in place with `capacity[i] -= x`, where `x` is the corresponding value from `rocks`. After that loop, `capacity` no longer contains capacities; it contains filling costs.

The constraints ensure `rocks[i] \le capacity[i]` before mutation, so every deficit is nonnegative.

**Choose the cheapest bags first**

`capacity.sort()` orders the deficits from smallest to largest. If the goal is to buy as many unit-value items as possible with a fixed budget, choosing cheaper items before expensive ones is optimal.

An exchange argument proves this. Suppose a plan fills a bag with deficit `y` but omits another bag with deficit `x \le y`. Replacing `y` by `x` does not use more rocks and keeps the same number of full bags. Repeating such exchanges transforms any size-`k` feasible plan into the `k` smallest deficits without increasing cost.

Therefore, for every possible count `k`, the minimum number of additional rocks needed to fill any `k` bags is the sum of the first `k` sorted deficits. The largest affordable prefix length is the global optimum.

**Spend the budget along the sorted prefix**

The second loop visits each sorted deficit `x` and performs `additionalRocks -= x`. If the result remains nonnegative, the current bag can be completed in addition to all earlier bags.

If the subtraction makes the budget negative at index `i`, exactly `i` earlier deficits were affordable. The current deficit is the smallest remaining one, so every later deficit is at least as large. No alternative choice among the unfilled bags can add another full bag to the already optimal cheapest prefix. Returning `i` is therefore correct.

The code checks after subtraction rather than before. On failure, the local budget temporarily becomes negative, but the method returns immediately, so that temporary value has no later effect.

**Count already-full bags naturally**

A bag already at capacity has deficit zero. Sorting places zero deficits first. Subtracting zero leaves the budget unchanged, yet the loop index advances, so every already-full bag is counted.

No separate initial count is needed. Zero-cost bags are simply the cheapest prefix entries.

**Return all bags when the budget suffices**

If no subtraction makes `additionalRocks` negative, every deficit has been paid. The loop finishes and the method returns `len(capacity)`.

Unused additional rocks are allowed. The algorithm does not try to distribute leftover rocks after all bags are full, because doing so cannot increase the answer.

**Trace the first example**

For `capacity = [2, 3, 4, 5]` and `rocks = [1, 2, 4, 4]`, the in-place deficits become `[1, 1, 0, 1]`. Sorting gives `[0, 1, 1, 1]`.

With two additional rocks:

- deficit zero is counted at no cost;
- the first deficit one leaves one rock;
- the second deficit one leaves zero;
- the next deficit one makes the budget negative.

The failing index is three, so three bags can be full.

**Why partial allocation to an expensive bag cannot help**

Every completed bag contributes exactly one to the objective, and an incomplete bag contributes zero. Moving rocks from a completed cheap bag into an incomplete expensive bag would lose one full bag before potentially gaining one, never improving the count. Spreading the budget among several unfinished bags is likewise useless until one reaches its full deficit.

This discrete unit reward is what makes sorting deficits sufficient. If bags provided partial value, a different optimization model would be needed.

**Account for the exact input mutation**

The method reuses `capacity` as working storage and then sorts it. The caller's capacity values and original ordering are destroyed. `rocks` is only read.

This saves allocating a separate deficit list, but it is an observable side effect. A version required to preserve inputs should build `[cap - rock for cap, rock in zip(capacity, rocks)]` instead.

**Why the returned prefix length is correct**

Every prefix the loop successfully pays is feasible, so the returned count is attainable. If it fails at `i`, the sum of the `i+1` smallest deficits exceeds the budget. Any set of `i+1` bags costs at least that much by sorted-order minimality, so no plan can fill more than `i` bags. The attainable lower bound and impossible upper bound coincide.

## Complexity detail

Let `n` be the number of bags. Computing deficits in place takes `O(n)` time. Sorting dominates at `O(n \log n)`, and the budget loop takes at most `O(n)`. Total time is `O(n \log n)`.

The explicit algorithm allocates no separate deficit array, but Python's in-place Timsort may use `O(n)` temporary memory in the worst case. Including sorting internals, auxiliary space is `O(n)`, matching the manifest. Apart from sorting workspace, the method uses `O(1)` variables.

Both input arrays contain `n` entries. Only `capacity` is mutated.

## Alternatives and edge cases

- **Separate deficit list:** It preserves `capacity` while using explicit `O(n)` additional storage and the same time bound.
- **Min-heap:** Heapifying deficits and repeatedly extracting the cheapest can also find the answer, but sorting is simpler and has the same worst-case order here.
- **Counting sort:** Capacities reach `10^9`, so a frequency array over all possible deficits is impractical.
- **Fill bags in original order:** It can spend rocks on a costly bag while several cheaper bags could yield a larger count.
- **Partial filling:** It provides no benefit unless the bag reaches capacity, so the greedy algorithm commits whole deficits.
- **Already-full bag:** Its zero deficit is counted without consuming budget.
- **All bags already full:** Every deficit is zero and the method returns `n`.
- **Budget fills every deficit:** The loop completes and returns the full list length, even if rocks remain unused.
- **Budget fails on the first positive deficit:** The returned index counts any preceding zero deficits and no unaffordable bag.
- **Equal deficits:** Their order is irrelevant because they cost the same and give the same unit reward.
- **Very large capacity values:** Only differences and a running budget are stored; Python integer arithmetic is safe.
- **Post-subtraction check:** A negative local budget is harmless because the function returns immediately.
- **Array-length correspondence:** The source guarantee lets `enumerate(rocks)` safely index the matching capacity entry.
- **Capacity mutation:** Values are replaced by deficits and then reordered; callers must not expect the original list afterward.
- **Rocks preservation:** The `rocks` list is never changed.
