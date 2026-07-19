## General
**Every endpoint offers a restart-or-extend decision**

For each value, the best nonempty subarray ending at that position has only two possible forms: start a new subarray with the current value, or extend a subarray ending one position earlier. Among all extensions, extending the best previous endpoint sum is optimal, so update with `max(value, ending_here + value)`.

This choice discards a negative accumulated prefix exactly when carrying it forward would make every future extension worse than starting at the current position.

**Separate the best ending here from the best seen anywhere**

After index `i`, `ending_here` is the largest sum of a nonempty subarray whose right endpoint is exactly `i`. `best` is the largest sum over every nonempty subarray ending at or before `i`. Update the endpoint value first and then use it to update the global value.

Initialize both from `nums[0]`, not zero. A zero initialization would incorrectly allow the forbidden empty subarray and return zero for an all-negative input.

**Trace a harmful prefix being discarded**

Across `[-2, 1, -3, 4, -1, 2, 1]`, the ending sums become `-2, 1, -2, 4, 3, 5, 6`. Restarting at 4 discards a harmful prefix, and extending through `-1, 2, 1` produces the optimum 6.

**Endpoint optima cover every possible subarray**

Any nonempty subarray ending at index `i` either starts at `i` or extends a subarray ending at $i - 1$. Among all extensions, the one using the greatest previous ending sum is never worse than extending any other prefix. This gives the exact best sum ending at each index.

Every contiguous subarray has one final index, so it appears among the candidates summarized by that endpoint's optimum. Taking the maximum over all endpoint optima therefore yields the best subarray anywhere, including the largest single value when every number is negative.

## Complexity detail
The algorithm visits each number once and performs constant work, yielding $O(n)$ time. It stores two running sums, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate every interval:** can update each interval sum incrementally but still takes $O(n^2)$ time.
- **Prefix sums:** make any fixed interval sum constant-time, yet examining all intervals remains quadratic.
- **Divide and conquer:** combines prefix, suffix, and crossing maxima in $O(n \log n)$ time and is useful for deriving segment-tree variants, but is not optimal for one query.
- A one-element array returns that element. For all-negative input, the least negative singleton becomes the optimum.
- If endpoint indices were also required, record a candidate start whenever the recurrence restarts and save endpoints whenever `best` improves.
