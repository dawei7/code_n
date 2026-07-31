## General

**Turn minimum powers into threshold counts.** Sort `nums`. Within any selected subsequence, the minimum absolute difference between any pair is attained by two adjacent selected values in sorted order. Every positive power is therefore one of the positive pairwise differences in `nums`; power zero can occur through duplicates but contributes nothing to the requested sum.

Let the distinct positive differences be

$$
0 = d_0 < d_1 < d_2 < \dots < d_m,
$$

and let $C(d)$ be the number of length-$k$ subsequences whose power is at least $d$. A subsequence with power $p$ is counted by every $C(d_i)$ for which $d_i \le p$. Consequently, its total contribution across the intervals between consecutive attainable differences is exactly

$$
\sum_{i=1}^{m} (d_i - d_{i-1}) C(d_i).
$$

For a particular subsequence of power $p = d_j$, the coefficients telescope to $d_j-d_0=p$; subsequences of power zero appear in none of these positive-threshold counts. Thus, computing every $C(d_i)$ and adding these weighted contributions gives the required sum directly.

**Count one minimum-gap threshold.** Fix a positive difference $d$. After sorting, a selected subsequence has power at least $d$ exactly when every pair of consecutive selected values differs by at least $d$. For one chosen length, let `previous[i]` count valid subsequences of that length ending at sorted index `i`.

To build the next length and end at `right`, every predecessor `left < right` with `nums[right] - nums[left] >= d` is legal. As `right` increases, the eligible predecessor indices form a growing prefix. A pointer advances through that prefix once while a running sum accumulates the corresponding values from `previous`; the running sum becomes the count ending at `right`. Starting with one length-one subsequence at each index and repeating this transition through length `k` produces $C(d)$.

**Combine all attainable differences.** Generate and sort the distinct positive pair differences. For each one, run the threshold DP and add `(gap - previous_gap) * count` modulo $10^9+7$. Sorting preserves index multiplicity: equal values at different original indices still create separate DP choices, while the strict positive threshold correctly excludes selections whose power is zero.

## Complexity detail

There are at most $n(n-1)/2 = O(n^2)$ distinct positive pair differences. For one threshold, each of the $k-1$ DP layers moves both `right` and the eligibility pointer across $n$ indices, taking $O(kn)$ time. Across all thresholds, the total time is $O(kn^3)$; sorting costs only $O(n \log n)$ additional time. The difference set occupies $O(n^2)$ space, and the rolling DP layers occupy $O(n)$ space, so total auxiliary space is $O(n^2)$.

## Alternatives and edge cases

- **Direct predecessor transitions:** For every threshold, length, and ending index, scan all earlier indices instead of maintaining a prefix pointer. This remains correct but costs $O(kn^4)$ time because the threshold DP becomes quadratic in $n$.
- **Enumerate all subsequences:** Generate every length-`k` index combination and compute its minimum pair difference. This mirrors the definition but requires exponential work in the worst case.
- **Memoize the current minimum difference:** A choose-or-skip recursion can include the last selected index and current minimum gap in its state, but the $O(n^2)$ possible gap values multiply an already large index-and-length state space and make it substantially less efficient.
- **Duplicate values:** Any selected pair of equal values makes that subsequence's power zero. Those index choices are still distinct, but their numerical contribution is zero.
- **Choosing two elements:** When `k = 2`, each subsequence's power is simply that pair's absolute difference; the same threshold identity still applies.
- **Choosing every element:** When `k = n`, there is one index subsequence, whose power is the smallest adjacent gap after sorting.
- **Modulo arithmetic:** Counts and the accumulated weighted sum must be reduced modulo $10^9+7$ because the number and total power of valid subsequences can be large.
