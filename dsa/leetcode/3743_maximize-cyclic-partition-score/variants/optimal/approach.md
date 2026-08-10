## General

**Represent one subarray range by two ordered extrema**

For any part, its range is

$$
\max-\min.
$$

Along the cyclic traversal, whichever extreme appears first determines an ordered contribution:

- If the maximum appears first, open with `+value` and close at the minimum with `-value`.
- If the minimum appears first, open with `-value` and close at the maximum with `+value`.

Thus each positive-range part can be represented by one non-overlapping ordered pair of positions contributing either `first-second` or `second-first`. Elements between or around the chosen extrema may belong to the part without affecting its range.

A one-element or constant part has range zero and never increases the score. Because the partition may use fewer than `k` parts, zero-range parts need not consume DP capacity. Every positive-range part needs at least two positions, so at most

$$
q=\min\left(k,\left\lfloor\frac n2\right\rfloor\right)
$$

such pairs matter. The source names this `limit` and returns zero immediately when it is zero.

**Linear non-wrapping pair states**

The first DP pass handles positive-range parts whose selected extrema do not wrap across the array boundary.

`completed[p]` is the maximum score after completing `p` ordered extrema pairs.

`open_positive[p]` stores the best value after `p` completed pairs and opening a new pair with `+value`. Closing it at a later value subtracts that value.

`open_negative[p]` stores the corresponding state opened with `-value`, ready to close by adding a later value.

At each array value, copied arrays preserve the option to skip that position. Transitions use only the old arrays, so one position cannot both open and close a pair.

An open pair closes through:

`old_positive[p] - value`

or

`old_negative[p] + value`,

updating `completed[p+1]`.

A completed state opens a new pair through `old_completed[p]+value` or `old_completed[p]-value`.

Because a new pair starts only from a completed state, selected pairs are disjoint and ordered. Any unselected positions can be assigned to neighboring partition parts without changing their extrema.

`completed[0]=0` represents choosing no positive-range part. All impossible states begin at a very negative sentinel, preventing them from winning a maximum.

**Why a second DP is needed for the cyclic boundary**

Cutting the cycle into the input's linear order can split at most one partition part across the boundary. All other positive-range parts lie inside the complementary linear interval. The source separately models that one wrapping “outer” part.

`outer_sign` is tried as `-1` and `+1`, covering whether the first encountered outer extreme is its minimum or maximum.

`outer_open[p]` stores the contribution of the first outer endpoint together with `p` completed inner pairs. The statement

`outer_open[0] = max(outer_open[0], outer_sign * value)`

may choose the current value as that first endpoint.

While the outer pair remains open, the algorithm can open and close ordinary inner pairs:

- `inner_positive[p]` and `inner_negative[p]` represent an inner pair currently open.
- Closing an inner pair updates `outer_open[p+1]`, preserving the earlier outer endpoint and adding the inner range.
- Opening an inner pair starts from `old_outer[p]`.

The condition `inner_pairs + 1 < limit` reserves capacity for the still-unfinished outer pair.

Finally,

`old_outer[p] - outer_sign * value`

closes the wrapping pair at a later linear position and updates `cyclic_completed[p+1]`. The two outer endpoints delimit the complementary interval containing the inner pairs; on the cycle, the outer part itself travels through the array boundary.

Trying both signs yields the absolute difference between the outer part's maximum and minimum regardless of which appears first in linear order.

**Why ordered pairs correspond to a legal partition**

Starting from any partition, choose one occurrence of the minimum and maximum inside every positive-range part. Traversing the cycle gives disjoint ordered pairs, with at most one pair wrapping the chosen array boundary. The two DP phases can reproduce their contributions.

Conversely, completed noncrossing pairs can be expanded into consecutive parts: place cuts in the unused gaps between pairs, and include intervening unselected elements with the relevant pair. Those elements stay between that part's actual minimum and maximum or can only make the represented range at least as large; the DP's chosen extrema contribution is therefore attainable, and an optimal representation can choose true extrema.

The maximum across ordinary `completed` states and both `cyclic_completed` arrays covers zero through `q` useful parts and every possible boundary behavior.

For `[1,2,3,3]` with two parts, one pair can represent range one for `[2,3]` and the wrapping pair range two for `[3,1]`, totaling three.

## Complexity detail

Let `q=min(k,floor(n/2))`. The linear pass processes `q` states per element. Each of the two outer-sign passes also processes `q` states per element with constant transition work. Total time is $O(nq)$.

Every state array has length `q` or `q+1`. A constant number of old and new arrays coexist, so auxiliary space is $O(q)$. Copying arrays each iteration contributes to the stated time but not a larger peak-space order.

## Alternatives and edge cases

- **Enumerate cyclic cut sets:** There are exponentially many partitions as `k` grows. Pair-state DP avoids choosing every cut explicitly.
- **Try every rotation and run a linear DP:** This adds a factor of `n`. The outer-pair states handle the single wrapping part in two passes.
- **Force exactly `k` positive parts:** Zero-range parts add nothing, and fewer parts are allowed. The answer takes the maximum over all completed pair counts.
- **Allow crossing pairs:** Crossing extrema would not correspond to disjoint consecutive parts. Opening only from completed states prevents crossings in the linear case.
- **Use one outer sign:** The maximum may occur before or after the minimum in linear order. Both signs are required.
- **One element:** `q=0` and every possible partition score is zero.
- **`k=1`:** One pair captures the range of the whole cycle.
- **All values equal:** Every opened pair closes with contribution zero, so the answer remains zero.
- **Repeated extrema:** Any occurrence can serve as the selected endpoint; maxima naturally retain the best.
- **Very large values:** The negative sentinel is far below every possible real score under the constraints.
- **Fewer than two positions per useful part:** Impossible for positive range, which justifies the `n//2` cap.
