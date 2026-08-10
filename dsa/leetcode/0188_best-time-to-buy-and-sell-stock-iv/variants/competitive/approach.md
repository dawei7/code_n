## General

**Identify which class is actually selected**

The file defines two classes. The platform entry named `Solution` is a greedy
valley/peak decomposition followed by randomized selection. `Solution2` is the
familiar $O(nk)$ dynamic program, but it is not the class LeetCode invokes for
the normal interface. Explaining only `Solution2` would therefore describe the
wrong implementation.

The primary algorithm is based on a less obvious fact: all achievable stock
profit can be decomposed into independent nonnegative marginal gains. Once
those gains are constructed correctly, the best result using at most `k`
transactions is the sum of the `k` largest gains.

**Extract maximal rising intervals**

The outer `while` repeatedly finds a valley index `v` and the following peak
index `p`. The first `for` advances until it sees `prices[v] < prices[v+1]`, so
`v` is the start of an upward move. If no increase remains, it uses the last
index. The second `for` advances while prices do not drop and stops at the end
of that nondecreasing run, making `p` its peak.

A simple valley-to-peak profit is `prices[p] - prices[v]`. If the transaction
limit were irrelevant, summing all positive rising runs would be optimal.
With a small limit, however, adjacent runs may need to be merged, and merely
discarding the smallest original run can miss the best answer.

**Maintain unresolved intervals on a monotonic stack**

`v_p_stk` stores valley/peak index pairs whose interactions with later rising
runs are not settled yet. The source comment states its value invariant: valley
prices increase while peak prices strictly decrease through the unresolved
structure. New intervals can violate either side of that pattern, causing old
intervals to be finalized or reorganized.

The stack contains indices rather than copied prices, so comparisons and profit
calculations always use the original array. Each interval is pushed once and
popped once, which is why the decomposition phase can remain linear despite
nested `while` loops.

**Finalize intervals cut off by a lower new valley**

If the most recent stored valley price is greater than the new valley price,
the old interval is popped and its full profit is appended to `profits`. The
new lower valley starts a better independent opportunity for future peaks; the
old time-ordered rise no longer needs to stay unresolved for a beneficial
overlap with this new interval.

This first popping loop may finalize several intervals, but none returns to the
stack. Across the entire input, its total number of iterations is therefore
bounded by the number of rising intervals.

**Reexpress overlapping intervals as marginal gains**

After lower-valley conflicts are removed, the second loop handles a new peak
that reaches or exceeds the previous stored peak. Let the previous interval be
`[last_v, last_p]` and the new one be `[v, p]`, with their time order fixed.

Two separate transactions would contribute:

`(prices[last_p] - prices[last_v]) + (prices[p] - prices[v])`

The algorithm rewrites the same total as a long merged transaction plus a
residual marginal gain:

`(prices[p] - prices[last_v]) + (prices[last_p] - prices[v])`

Expanding both sums shows they are equal. The code appends the residual
`prices[last_p] - prices[v]`, changes `v` to `last_v`, and keeps the long merged
interval available for further overlap. This transformation records both the
best one-transaction version and the extra gain obtained by allowing another
transaction.

Repeated pops apply the same identity through nested intervals. At the end,
all remaining stack intervals contribute their full valley-to-peak profits.
The resulting `profits` list consists of marginal gains whose largest choices
encode the best limited-transaction solution.

**Why choosing the largest gains enforces the limit**

The decomposition preserves the total profit available when all useful
transactions are allowed, but breaks it into increments arranged so that using
one more transaction adds one selected marginal gain. The overlap rewrite is
the key: the long interval represents a solution with fewer transactions, and
the residual represents the additional profit recovered by splitting it.

Consequently, selecting the largest `k` marginal profits maximizes the profit
obtainable with at most `k` transactions. If fewer than `k` components exist,
the code reduces `k` to their count. Components are nonnegative for the rising
intervals and overlap conditions, so using all available selected components
does not reduce profit.

**Partition instead of fully sorting**

The helper `nth_element` rearranges `profits` so the element at position
`k - 1` is in its descending-order partition and every earlier region contains
values at least as preferred by the comparison. It does not sort within the
top region because the final answer only needs their sum.

Each iteration chooses a random pivot, then `tri_partition` separates values
less than, equal to, and greater than that pivot according to the supplied
descending comparator. If the requested index lies in the equal region,
partitioning is sufficient. Otherwise, selection continues only in the
relevant side.

Random pivots give expected linear selection time. A sequence of unlucky
pivots can still cause quadratic worst-case time; the source comment notes that
a deterministic median-of-medians pivot could guarantee linear selection.

**Trace the conventional DP kept as `Solution2`**

Although unused by the selected entry point, `Solution2` is useful for contrast.
It stores `max_buy[j]`, the best balance while holding after using the $j$th
buy, and `max_sell[j]`, the best balance while empty after up to $j$
transactions. Each price updates these states in $O(k)$ time.

When `k >= len(prices) // 2`, its helper instead sums every positive adjacent
rise, because no strategy can complete more than $\lfloor n/2 \rfloor$
non-overlapping buy/sell pairs. This class matches the manifest's intended
$O(nk)$ time and $O(k)$ space, but it is not what `Solution.maxProfit` runs.

The `maxAtMostNPairsProfit` helper names its parameter `sprices` but reads the
enclosing `prices` variable. It happens to work for the only call shown, though
the unused parameter name is misleading.

**Boundary behavior of the primary source**

The Reference guarantees at least one price and `k >= 1`. These guarantees
matter. A nonincreasing array eventually creates a zero-length final interval,
yielding a zero marginal profit and correctly returning zero. If `k` were zero,
the call `nth_element(profits, k - 1, ...)` would use target `-1` and is not
designed for that case; the stated constraints avoid it.

Equal adjacent prices are absorbed into the rising-run scan until a drop or the
end. Zero-profit plateaus do not create profitable extra transactions. The
algorithm uses only completed valley-before-peak intervals, so it never models
simultaneous holdings.

## Complexity detail

Let $n$ be the number of days. Valley/peak discovery visits the price array in
forward-moving ranges. Every interval is pushed once and popped once, so stack
processing and profit decomposition take $O(n)$ time. Randomized
`nth_element` takes expected $O(n)$ time, making the selected primary method
expected $O(n)$ overall; its worst case is $O(n^2)$ under consistently poor
pivots. The stack and profit list use $O(n)$ space.

These are not the manifest's $O(nk)$ time and $O(k)$ space bounds. Those bounds
describe `Solution2`'s compressed DP, not the selected `Solution` class. This
source/manifest mismatch should be understood rather than hidden. Both methods
solve the same contract, but they have different resource profiles.

## Alternatives and edge cases

- **Compressed transaction DP:** `Solution2` is easier to verify, runs in $O(nk)$ time and $O(k)$ space, and directly matches the manifest.
- **Memoized state search:** The optimal variant explores day, remaining buys, and holding status in $O(nk)$ time but actually caches $O(nk)$ states.
- **Unlimited-transactions shortcut:** Sum positive adjacent differences when $k \ge \lfloor n/2 \rfloor$.
- **Full sorting of marginal gains:** Simpler than quickselect but costs $O(n\log n)$ time; only the largest `k` values are needed.
- **Deterministic selection:** Median of medians removes randomized quadratic worst cases at the cost of a more complex constant factor.
- **Nonincreasing prices:** The best profit is zero; no forced transaction is needed.
- **One price:** No buy can be followed by a later sell, so profit is zero.
- **Plateaus:** Equal prices add no marginal profit and are safely absorbed into interval boundaries.
- **`k` larger than useful gains:** Clamp it to the number of profit components, as the source does.
- **`k = 0`:** Outside the Reference constraints; the primary implementation would need an early return to support it safely.
- **Randomness:** Results are deterministic in value, but runtime and internal partition order depend on random pivot choices.
