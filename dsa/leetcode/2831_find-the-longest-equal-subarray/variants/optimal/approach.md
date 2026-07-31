## General

Fix a value $x$ and list the original indices at which it occurs:

$$
p_0 < p_1 < \dots < p_{m-1}.
$$

If occurrences $p_l$ through $p_r$ are to form one equal subarray, every non-$x$ value strictly between their endpoints must be deleted. The inclusive original span contains `p_r - p_l + 1` elements, while $r-l+1$ of them equal $x$. The required deletion count is therefore

$$
(p_r-p_l+1)-(r-l+1)=p_r-p_l-(r-l).
$$

The task for one value is consequently to find the widest interval of its position list for which this quantity is at most `k`.

Scan each position list from left to right with two pointers. Extend `right` for every occurrence. While the required deletions exceed `k`, advance `left`; once the window is legal, its $r-l+1$ positions are equal values that can be made contiguous. Record the largest such count over every value.

**Why shrinking is safe**

For a fixed `right`, the deletion cost cannot increase when `left` moves right. Thus the loop stops at the earliest feasible left endpoint and retains the longest feasible window ending at that occurrence. If a window is infeasible, adding later occurrences cannot make its existing gap cost smaller, so discarding its leftmost occurrence cannot remove a future optimum that still uses that endpoint.

Every recorded window is attainable: delete precisely the nonmatching elements between its first and last occurrences. Conversely, any equal subarray in a resulting array corresponds to some consecutive range in the original position list of its value. All nonmatching elements between the two endpoint occurrences must have been deleted, so that range satisfies the same inequality and is examined by the sliding window. The maximum recorded length is therefore exactly the requested answer.

## Complexity detail

Let $n$ be the length of `nums`. Building all position lists takes $O(n)$ time and $O(n)$ space. Across all lists, `right` visits each array occurrence once and `left` advances at most once per occurrence. The total sliding-window work is $O(n)$, so the complete algorithm uses $O(n)$ time and $O(n)$ auxiliary space.

The benchmark uses $n$ as `size`, alternates two values, and gives enough deletion budget that a quadratic endpoint-enumeration method must inspect every pair of equal occurrences.

## Alternatives and edge cases

- **Window on the original array:** Maintain frequencies inside an original-index window and its maximum frequency. A legal span has at most `k` non-target values, and returning the largest retained frequency also gives an $O(n)$ method, though the stale-maximum invariant is less direct to explain.
- **Binary search per occurrence:** For every right endpoint, binary-search the earliest feasible position in the same value list. This is correct but takes $O(n \log n)$ time.
- **Enumerate equal endpoints:** Try every pair of positions holding the same value and compute the intervening deletion cost. It is correct but can require $O(n^2)$ time.
- **Zero deletions:** Only occurrences already consecutive in `nums` can belong to the same answer.
- **Deletions outside the span:** Values before the first chosen occurrence or after the last one do not consume the budget because the resulting equal subarray need not cover the entire array.
- **Unused budget:** The operation allows at most `k` deletions; an optimal answer never needs to spend the full budget.
- **All values equal:** No deletions are necessary, and the answer is $n$.
- **Single element:** The nonempty input always permits an equal subarray of length $1$, even though the definition also permits an empty subarray.
