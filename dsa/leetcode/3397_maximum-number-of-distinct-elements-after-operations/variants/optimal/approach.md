## General

**Each element provides an interval of possible integer targets.** Original value `x` may receive any integer addition in `[-k,k]`, so it can become any integer in closed interval

$$
[x-k,x+k].
$$

The goal is to assign as many intervals as possible distinct integer points.

**Sort intervals by their original values.** All intervals have the same radius `k`. Sorting `nums` sorts both left endpoints `x-k` and right endpoints `x+k`. This is the natural order for greedily placing target points from left to right.

The source sorts `nums` in place, which changes caller-visible element order.

**Keep the last distinct assigned value.** `pre` starts at negative infinity, so the first interval has no effective lower restriction. For current interval, the smallest target that would be new is `pre+1`.

The smallest feasible new target is

$$
\max(x-k,\texttt{pre}+1).
$$

It cannot exceed the interval right endpoint, so the source clips it:

`cur = min(x + k, max(x - k, pre + 1))`.

**Count only when clipping remains above `pre`.** If `cur > pre`, it lies in the interval and is a new integer, so answer increases and `pre=cur`.

If `cur <= pre`, the interval ends before the next unused integer. It cannot receive any new value greater than `pre`. The element may duplicate some earlier assignment, but duplicates do not increase the objective, so `pre` stays unchanged.

**Why choosing the smallest feasible target is optimal.** Suppose a solution assigns the current interval a larger feasible value. Moving it down to the greedy value preserves distinctness from earlier assignments and remains inside the interval. It leaves at least as much numeric room for every later interval, whose endpoints are no smaller after sorting.

By exchanging each choice this way, an optimal solution can be transformed to use every greedy assignment without reducing its count.

**Why skipped intervals never need reconsideration.** Later intervals have right endpoints at least as large, but the skipped interval's own right endpoint is at most `pre`. No future change can create a point inside that expired interval greater than the already committed last assignment. Skipping is permanent and safe.

**Accepted assignments remain in sorted order.** Greedy targets are strictly increasing because a counted `cur` must exceed `pre`. They need not stay close to their original values in sorted order beyond interval membership; the operation acts independently on each element. Strict increase is merely a convenient certificate that every counted result is distinct.

**Trace duplicate values.** For four copies of four with `k=1`, every interval is `[3,5]`. Greedy assigns 3, 4, and 5. The fourth computes a clipped value five, not greater than `pre=5`, so it is skipped. Maximum distinct count is three.

**Trace `k=0`.** Each interval is a single original value. Sorting groups duplicates. The first copy of a value counts; later equal copies cannot exceed `pre`. The result becomes the number of distinct original values.

**Why only integer spacing one matters.** Targets must be integers. Once `pre` is used, the smallest larger distinct integer is exactly `pre+1`; no fractional choice exists between them.

**Why the count is exact.** Every accepted `cur` is a legal target and strictly increases, constructing that many distinct outputs. The exchange argument shows no optimal assignment can count more intervals than the earliest-point greedy process.

An uncounted element still receives some legal value—zero adjustment always leaves it at `x`—but that value may duplicate a counted result. Since the objective counts distinct values rather than requiring all elements distinct, skipped intervals do not make the construction invalid.

## Complexity detail

Sorting $n$ values costs $O(n\log n)$. The subsequent scan is $O(n)$, so total time is $O(n\log n)$.

Python's in-place Timsort can use $O(n)$ temporary space in the worst case; other local variables use $O(1)$. The manifest's $O(n)$ space is a safe Python bound. The input list is mutated by sorting.

## Alternatives and edge cases

- **Process from right to left:** Assign the largest feasible decreasing targets; the symmetric greedy also works.
- **Bipartite matching over all integers:** The coordinate range can be huge and is unnecessary for equal-radius intervals.
- **No adjustment `k=0`:** Answer is original distinct count.
- **Single element:** It always contributes one.
- **Many identical elements:** At most `2k+1` distinct integers fit their shared interval.
- **Negative assigned targets:** They are legal because the operation result has no positivity restriction.
- **Large `k`:** Python integers safely represent interval endpoints.
- **Clipped value equals `pre`:** It is a duplicate and does not count.
- **Skipped element:** It may keep its original value; only the distinct-count objective matters.
- **Gap between intervals:** Greedy jumps to the next interval's left endpoint.
- **Input sorting mutation:** Original order is not preserved.
- **Equal endpoints order:** Duplicate intervals may appear in any relative order without affecting the result.
- **At most once operation:** Choosing any point in the interval corresponds to one allowed addition.
- **Strictly increasing certificate:** Every accepted target is automatically distinct from all earlier accepted targets.
- **Zero addition:** Keeping `x` is included in the interval.
- **Infinity sentinel:** It makes the first interval choose its left endpoint.
