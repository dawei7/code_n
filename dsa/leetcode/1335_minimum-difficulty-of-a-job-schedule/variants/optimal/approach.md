## General
**Represent the best schedule for each remaining suffix**

For one remaining day, every remaining job must be done together. Build an array `dp` in which `dp[i]` is therefore the maximum difficulty in the suffix beginning at index `i`.

Then add days one at a time. When scheduling the suffix at `i` across `day` days, choose the final job `cut` assigned to the first of those days. Its segment is `job_difficulty[i:cut + 1]`, while `dp[cut + 1]` already stores the optimum for the remaining jobs across one fewer day. Only cuts leaving at least one job for each later day are legal.

As `cut` moves right, maintain the maximum difficulty of the current first-day segment. The candidate cost is that running maximum plus `dp[cut + 1]`; the least candidate becomes the new state for `i`. Every valid schedule has exactly one such first boundary, and combining that boundary with an optimal remaining suffix cannot be worse than the same boundary with any other suffix schedule. Taking the minimum over all legal boundaries thus yields the global optimum.

Use a fresh array for each day count so transitions read only states from the preceding layer. After building through `d` days, `dp[0]` covers every job.

## Complexity detail
For each of the $d$ layers, there are $O(n)$ suffix starts and $O(n)$ legal cut positions. Updating the segment maximum is constant time, so the total is $O(dn^2)$. Two one-dimensional state arrays use $O(n)$ space.

## Alternatives and edge cases
- **Top-down memoization:** Recursing on the next job and remaining days gives the same $O(dn^2)$ states and transitions, but adds recursion and cache overhead.
- **Recompute every segment maximum:** Calling `max(job_difficulty[i:cut + 1])` for each transition is correct but raises the worst-case time to $O(dn^3)$.
- **Too few jobs:** Return `-1` immediately when $n<d$.
- **One day:** The answer is the maximum difficulty in the complete array.
- **One job per day:** When $n=d$, every boundary is forced and the answer is the sum of all difficulties.
- **Zero difficulties:** Daily maxima may be zero; initialization must not treat zero as an absent job.
- **Fixed order:** Jobs cannot be reordered to group large values more conveniently.
