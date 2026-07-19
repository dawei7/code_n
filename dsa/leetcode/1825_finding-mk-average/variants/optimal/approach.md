## General
**Represent the moving window and its value distribution**

Use a deque to retain arrival order for eviction. Over values 1 through $U$, maintain one Fenwick tree of occurrence counts and another of occurrence sums. Insertion adds one count and the value to the corresponding trees. When the deque exceeds `m`, remove its front value with inverse updates.

**Obtain sums by sorted rank without materializing a sort**

To compute the sum of the smallest `t` elements, use binary lifting on the count tree to find the value containing rank `t`. The sum tree gives the complete contribution of smaller values, and any remaining occurrences at the boundary contribute `remaining * value`. Duplicate values are therefore split correctly when a trim boundary passes through them.

**Extract the middle and floor its average**

The sum of sorted ranks `k + 1` through `m - k` is `sumSmallest(m - k) - sumSmallest(k)`. Divide that exact middle sum by `m - 2*k`. Neither calculation mutates the deque or trees, so repeated queries return the same result until another addition.

## Complexity detail
Initializing the two trees costs $O(U)$. Each insertion and possible eviction performs a constant number of Fenwick updates in $O(\log U)$ time. Each full-window calculation performs two order-statistic searches and prefix-sum queries, also $O(\log U)$; an early calculation is $O(1)$. Across $q$ calls, total time is $O(U+q\log U)$. The deque stores at most $m$ values and the two trees store $O(U)$ entries, giving $O(m+U)$ space.

## Alternatives and edge cases
- **Sort the window for every query:** It is simple and correct but costs $O(m\log m)$ per full calculation.
- **Three balanced multisets:** Maintaining the lowest `k`, middle, and highest `k` groups with the middle sum also gives logarithmic updates, but requires careful duplicate-aware rebalancing.
- **Before warm-up:** Return `-1` until exactly `m` values have been added.
- **Duplicate trim boundaries:** Remove occurrences, not distinct values; Fenwick counts preserve multiplicity.
- **Eviction:** Only the oldest of the previous `m` values leaves when one new value arrives.
- **Flooring:** Use integer floor division after summing all retained values.
- **Repeated calculation:** Do not remove, reorder, or otherwise mutate window state.
- **Extreme values:** Values 1 and $10^5$ are ordinary Fenwick indices and may appear repeatedly.
