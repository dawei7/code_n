## General

With $g$ groups, a particular number can appear at most once in each group and therefore at most $g$ times. Also, $g$ can never exceed the $n$ available numbers because the largest group needs at least $g$ distinct members. Consequently, replacing every limit by $min(	exttt{limit}, n)$ cannot remove any useful occurrence.

Build a frequency table for these clamped limits. Its indices run only from $1$ through $n$, so iterating the table processes all numbers in non-decreasing limit order without comparison sorting.

Maintain `available`, the cumulative effective capacity processed so far, and `groups`, the maximum supported group count. The smallest strictly increasing lengths for $g$ groups are $1,2,\ldots,g$, which require

$$
T_g = \frac{g(g+1)}{2}
$$

placements. After adding one number's limit, test whether `available` reaches $T_{g+1}$. If it does, increase `groups` by one.

**Why one threshold test per number preserves distinctness**

Introducing one additional number can raise the group count by at most one: a construction of $g+1$ groups needs at least $g+1$ distinct numbers in its largest group. Processing limits from smallest to largest exposes the restrictive numbers first, so a large limit cannot stand in for a missing distinct number. Capacity beyond the current triangular requirement remains available as later numbers are introduced and more groups make another occurrence of each earlier number usable.

If the next triangular threshold is not met, there are not even enough total legal placements among the processed numbers, so another group is impossible. If it is met, the non-decreasing limits let the existing placements be redistributed so that the new number helps extend the group-length sequence by one. Thus each increment is feasible, and every skipped increment is forced. The final count is maximal.

## Complexity detail

Let $n$ be the length of `usageLimits`. Clamping and counting visit every input once, and scanning the $n$ frequency buckets plus all $n$ represented numbers is linear. The running time is $O(n)$. The frequency table contains $n+1$ integers, so the space complexity is $O(n)$.

## Alternatives and edge cases

- **Comparison sorting plus greedy accumulation:** Sort the limits and apply the same triangular thresholds. This is the conventional $O(n \log n)$ solution and uses up to $O(n)$ sorting space in Python.
- **Binary search on the group count:** Test candidate counts using a capacity-feasibility procedure. It is valid with a careful distinctness check, but adds logarithmic search and more complicated proof obligations.
- **Explicit group construction:** Repeatedly assign numbers to materialized groups. It obscures the capacity invariant and may take quadratic time or worse.
- **Limits larger than $n$:** Clamp them to $n$ because no number can appear more than once in each of at most $n$ groups.
- **One available number:** Regardless of its limit, only one group can exist because a second, longer group would need another distinct number.
- **All limits equal to one:** The answer is the largest $g$ satisfying $g(g+1)/2 \le n$.
- **Large arithmetic:** The cumulative capacity can reach $10^{14}$ before clamping, so fixed-width implementations should use a 64-bit integer for totals and triangular values.
