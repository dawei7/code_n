## General

**For a fixed right endpoint, valid starts form one suffix**

Fix `r` and compare windows `nums[l..r]` as `l` moves right.

Removing elements from the left cannot increase the maximum, cannot decrease the minimum, and shortens the length. Therefore both nonnegative factors in

$$
(\max-\min)(r-l+1)
$$

stay the same or decrease. The cost cannot increase when the window shrinks.

Consequently, for each right endpoint there is a smallest valid start `l`. Every start from `l` through `r` is valid, while every earlier start is invalid.

This suffix property is what allows a sliding window. Once the smallest valid `l` is known, the number of valid subarrays ending at `r` is simply

$$
r-l+1.
$$

**The left boundary never needs to move backward**

When a new rightmost value is appended, the window length grows and its range `max - min` cannot decrease. Therefore the cost for an unchanged left boundary cannot decrease.

If some start was too far left for the previous right endpoint, it cannot become valid after extending farther right. The minimum valid `l` is monotone nondecreasing across the scan.

This proves that one left pointer can serve all right endpoints without restarting.

**Maintain the maximum with a decreasing deque**

`q1` stores indices whose values decrease from front to back. Its front is the maximum value in the current window.

Before appending new index `r` with value `x`, the source removes indices from the back while

`nums[q1[-1]] <= x`.

Any such older value can never again be the maximum while `x` remains in the window: `x` is at least as large and lies later, so it also expires later as `l` advances. The older index is dominated and can be discarded.

After appending `r`, `nums[q1[0]]` is the window maximum.

Using `<=` rather than only `<` keeps the latest occurrence among equal maxima. That is safe and simplifies expiration because the latest equal value survives longer.

**Maintain the minimum with an increasing deque**

`q2` is symmetric. Its values increase from front to back, so the front is the current minimum.

Before appending `r`, the source pops from the back while

`nums[q2[-1]] >= x`.

The later `x` is no larger and expires later, so every removed index is dominated as a future minimum.

After appending, `nums[q2[0]]` is the window minimum.

Together the deque fronts provide the range in constant time:

`nums[q1[0]] - nums[q2[0]]`.

**Shrink until the current window becomes valid**

After updating both deques, the source tests:

`(nums[q1[0]] - nums[q2[0]]) * (r - l + 1) > k`.

While the cost is too large and `l < r`, it increments `l`. Any deque-front index that now lies before `l` is removed.

The deques always store indices in increasing order. Before one increment, no stored front is older than the current `l`. Since `l` advances by exactly one, at most one front in each deque can cross outside during that increment, so the source's single `if q[0] < l` removal is sufficient.

The loop stops at the first valid start. If shrinking reaches `l == r`, the window contains one value. Its maximum equals its minimum, so cost is zero. Since `k >= 0`, a singleton is always valid; the `l < r` guard safely prevents unnecessary further shrinking.

**Count all valid subarrays ending at r**

When shrinking stops, `nums[l..r]` is valid and `l` is the earliest valid start.

Every later start `s > l` produces a shorter window whose range cannot be larger, so it is also valid. There are `r - l + 1` choices:

`[l..r], [l+1..r], ..., [r..r]`.

The source adds that number to `ans`. Every subarray has exactly one right endpoint, so counting valid endings at each `r` counts every valid subarray exactly once.

**Trace the first example**

For `nums = [1,3,2]` and `k = 4`:

At `r = 0`, the singleton `[1]` costs zero, contributing 1.

At `r = 1`, the maximum is 3 and minimum is 1. The length-2 cost is $(3-1)\cdot2=4$, so `l` remains 0 and both endings `[1,3]` and `[3]` contribute 2.

At `r = 2`, window `[1,3,2]` has range 2 and length 3, cost 6, so it is invalid. Incrementing `l` to 1 leaves `[3,2]` with cost $(3-2)\cdot2=2$. It is the earliest valid ending window, so `[3,2]` and `[2]` contribute 2.

The total is $1+2+2=5$.

**Why deque removals lose no future answer**

An index removed from a deque back is dominated by a later index with an equally or more extreme value. As long as the older index could belong to a window, the later one also belongs and supplies at least the same maximum or minimum. Once the later index leaves, the older one must have left even earlier.

An index removed from the front is outside the current window and, because `l` never decreases, can never belong to a future window.

Thus each removal discards only information that can no longer affect any current or future cost.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Every index is appended once to each deque. It can be removed at most once from each deque, from either the back as dominated or the front as expired. The left pointer advances at most $N-1$ times.

All nested-loop iterations across the full scan are therefore $O(N)$, giving total time $O(N)$.

Each deque can hold up to $N$ indices in a monotone input, so auxiliary space is $O(N)$. The answer may be as large as $N(N+1)/2$; Python integers store it exactly.

## Alternatives and edge cases

- **Enumerate every subarray:** Updating minimum and maximum incrementally still requires $O(N^2)$ pairs, which is too slow for $N=10^5$.
- **Balanced multiset window:** An ordered multiset can provide min and max in $O(\log N)$ per insertion/removal, yielding $O(N\log N)$ time. Monotonic deques exploit one-directional movement for linear time.
- **Two heaps with lazy deletion:** This also maintains extrema but is more complicated and logarithmic; stale-entry bookkeeping is unnecessary here.
- **k equals zero:** A valid window must have maximum equal to minimum, so the method counts exactly constant-valued subarrays.
- **All values equal:** Every range is zero, no shrinking occurs, and the answer is all $N(N+1)/2$ subarrays.
- **Single-element input:** Its cost is zero and the function returns 1.
- **Strict failure versus inclusive success:** The loop shrinks only when cost is `> k`, so a cost exactly equal to `k` is counted.
- **Duplicate maxima or minima:** Back removal keeps the newest equal occurrence, which remains available longer and preserves the correct extreme.
- **Large products:** The maximum range and length can create values above 32-bit limits, but Python multiplication is exact.
- **Earliest valid start:** Cost monotonicity under left-shrinking guarantees that all later starts are valid and justifies adding `r - l + 1` at once.
