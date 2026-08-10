## General

**Combine both operation budgets into reductions of absolute differences**

For index `i`, only `|nums1[i] - nums2[i]|` matters after squaring. One operation on either array can reduce a positive difference by exactly one by moving the appropriate value toward the other. Which array supplies the operation is irrelevant to the resulting difference.

Therefore the two budgets combine into `k = k1 + k2`, and the method builds the difference list `d`. Increasing a difference can never help minimize a sum of squares, so useful operations only lower positive entries.

If `sum(d) <= k`, every difference can be reduced to zero. Operations are optional, so any unused budget need not be spent and the answer is zero.

**Why the largest differences should be lowered first**

Reducing difference `v` by one changes its square from `v^2` to `(v-1)^2`, an improvement of `2v - 1`. This improvement is larger when `v` is larger.

Consequently, an optimal allocation keeps the remaining differences as level as the budget permits: it should not leave one value far above another while spending a reduction on the smaller one. The code finds the final leveling height with binary search.

**Binary-search the smallest affordable cap**

For a proposed cap `x`, lowering every difference above `x` down to `x` costs

`R(x) = sum(max(v - x, 0) for v in d)`.

As `x` increases, this required cost never increases. The predicate `R(x) <= k` is therefore monotone.

The search range is zero through the original maximum difference. If capping at `mid` fits the budget, the code moves `right` down because an even lower cap may fit. Otherwise it raises `left`. At termination, `left` is the smallest height to which all larger differences can be capped within `k` operations.

**Apply the cap and account for spent operations**

The first update loop replaces each difference `v` with `min(left, v)`. It subtracts `max(0, v - left)` from `k`, exactly the operations used to perform that cap.

Some budget may remain because lowering every capped value one more level would cost too much collectively. Minimality of `left` guarantees that the remaining budget is smaller than the number of entries currently equal to `left` that originated at or above it.

The second loop spends one remaining operation on distinct entries equal to `left`, lowering each to `left - 1` until `k` reaches zero. This produces the most balanced possible final multiset: values are at most `left`, with some of the top-level values one lower.

It never lowers an entry below `left - 1` while another remains at `left`, which would waste convex-square improvement.

**Why the final vector is optimal**

Suppose two positive remaining differences satisfy `a >= b + 2`. Moving one unit of reduction from `b` to `a` changes the squared total by

`(a-1)^2 + (b+1)^2 - (a^2 + b^2) = -2(a-b-1) < 0`.

So any allocation with a gap of at least two among reducible top values is not optimal. The cap and remainder construction leaves no such improvable imbalance among values affected by the budget.

Differences originally below the cap are left alone because reducing a higher value gives at least as much marginal benefit. Binary search finds the lowest globally affordable level, and the final single reductions distribute the remainder across the current maximum level. This is exactly the convex greedy optimum.

The final generator sums `v * v` for every adjusted difference.

## Complexity detail

Let `n` be the array length and `D = max(d)`. Building differences and each feasibility calculation are `O(n)`. Binary search performs `O(\log D)` calculations, so exact running time is `O(n \log D)`, followed by linear adjustment passes. Since `D <= 10^5`, this is also within the manifest's broader `O(n \log n)`-style performance expectation, though the actual logarithm is over the value range, not sorting.

The difference list uses `O(n)` auxiliary space. Generator expressions use constant incremental state. Inputs are not modified.

Python integers safely hold squared totals. No modulus is requested. The early zero case avoids binary search when the budget can eliminate every difference.

## Alternatives and edge cases

- **Max heap of differences:** Repeatedly pop, decrement, and reinsert the largest value. This is intuitive but can require up to `k` operations, which is too large when budgets reach `10^9`.
- **Sort and lower groups in batches:** Sort differences descending and level each top group toward the next height. This is `O(n \log n)` and also exploits convexity.
- **Frequency array by difference value:** With the bounded `10^5` range, counts can be lowered from high buckets. It uses value-range space and can be efficient, but binary search is compact.
- **Keep `k1` and `k2` separate:** Any useful unit operation on either side has the same effect on one absolute difference, so separation adds no constraint.
- **Spend operations after all differences reach zero:** Operations are allowed at most, not exactly, so extra budget is ignored.
- **Zero operation budget:** The binary cap becomes the original maximum and the final sum is the original squared difference.
- **All differences zero:** The early sum test returns zero immediately.
- **Budget equals total difference:** Every entry reaches zero exactly.
- **Several equal maximum differences:** Remaining operations are spread one per top entry before any receives a second, maximizing square reduction.
- **A single difference:** The method lowers it by up to `k` and squares the nonnegative remainder.
- **Negative array values after modification:** The contract permits them, supporting the abstract ability to keep moving values toward each other; only absolute differences matter.
- **Binary-search monotonicity:** A higher cap never needs more reductions. Reversing the predicate updates would find the wrong boundary.
- **Remainder proof:** Minimal `left` ensures fewer leftover operations than top-level entries, so one second-loop pass is enough.
- **Input preservation:** Only the newly created `d` list is changed.
