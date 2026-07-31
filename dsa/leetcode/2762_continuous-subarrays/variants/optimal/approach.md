## General

The pairwise condition is governed entirely by the extreme values: every pair differs by at most $2$ if and only if the window maximum minus the window minimum is at most $2$. This property is monotone under removing values, so maintain the longest valid window ending at each right index.

Two monotonic deques provide the window extremes in constant amortized time. `maximums` stores indices whose values decrease from front to back; before appending a new value, remove every smaller or equal value from its back. Its front is therefore the current maximum. Symmetrically, `minimums` stores increasing values and discards larger or equal values, leaving the minimum at its front. Replacing equal values with their newer index is safe because the newer occurrence remains in the window at least as long.

After inserting `nums[right]`, advance `left` while the two front values differ by more than $2$. Whenever the departing index is at a deque's front, remove it. Once the window is valid, every subarray ending at `right` and starting at an index from `left` through `right` is also valid. There are exactly `right - left + 1` such subarrays, so add that number to the answer.

This counts each valid subarray exactly once by its right endpoint. No start before `left` can work because `left` stopped at the earliest valid boundary after eliminating the violating extreme, while every later start removes elements from an already valid window and cannot enlarge its range.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each index is appended once to each deque and removed at most once from each end, so the total time is $O(n)$.

The accepted implementation discards equal values from the deque backs. A valid window of integers with range at most $2$ contains at most three distinct values, so each deque keeps at most one index per level. Immediately before shrinking, the newly inserted value adds at most one further level. Thus the auxiliary space is bounded by a constant, $O(1)$.

The benchmark tiers contain only three repeating values, making every subarray valid. The monotonic window processes them linearly, while a correct implementation that expands every start and maintains its extrema performs quadratic work.

## Alternatives and edge cases

- **Expand every left endpoint:** Updating a running minimum and maximum for each possible start is correct and uses constant extra space, but takes $O(n^2)$ time on long valid arrays.
- **Ordered multiset or frequency map:** Maintaining sorted keys supports window extremes, but introduces $O(\log n)$ updates or extra bookkeeping when two monotonic deques suffice.
- **Heap pair with lazy deletion:** Min- and max-heaps can track extremes, but stale indices complicate removal and require $O(n)$ storage.
- **All values equal:** Every non-empty subarray is continuous, producing $n(n+1)/2$ and demonstrating why the answer needs more than 32 bits.
- **Difference exactly two:** The upper bound is inclusive, so a range of exactly $2$ remains valid.
- **Large jump:** A new value more than $2$ away from an existing extreme may move `left` several positions; each discarded position is still processed only once overall.

