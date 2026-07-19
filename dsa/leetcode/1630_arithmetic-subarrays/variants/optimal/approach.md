## General
**Derive the only possible common difference.** For a query of length $k$, find its minimum and maximum. If the values can form an arithmetic progression, those extremes occupy its endpoints, so the common difference must be

$$
d=\frac{\max-\min}{k-1}.
$$

If the span is not divisible by $k-1$, no integer ordering can work. If the span is zero, every value equals the minimum and the query succeeds immediately.

**Check each required position exactly once.** For positive $d$, every value must equal $\min+jd$ for an integer position $j$ from 0 through $k-1$. Scan the subarray, reject a value whose offset from the minimum is not divisible by $d$, and reject a position that appears twice. Since there are $k$ values and exactly $k$ possible positions, distinct valid positions imply that every required progression value appears once.

The extrema argument proves that no other difference needs consideration. A successful occupancy scan supplies every element of the unique candidate progression, so sorting by position yields a valid arithmetic sequence. Every rejection identifies a missing, duplicated, or off-grid value that no rearrangement can repair.

## Complexity detail
For a length-$k$ query, slicing, finding extrema, and checking positions take $O(k)$ time. Summed across all queries, this is $O(S)$. The current slice and its occupied-position set use $O(k)\subseteq O(n)$ auxiliary space and are discarded before the next query.

## Alternatives and edge cases
- **Sort every range:** Sorting each selected slice and comparing adjacent differences is straightforward but takes $O(k\log k)$ per query rather than linear time.
- **Boolean occupancy array:** A length-$k$ array can replace the hash set with the same asymptotic bounds and predictable indexing.
- **Try every permutation:** Permutation enumeration is unnecessary and grows factorially.
- Every two-element range is arithmetic because its sole adjacent difference is automatically constant.
- Equal values are valid only when the common difference is zero; duplicates invalidate a positive-step candidate.
- Negative values do not change the offset-and-divisibility reasoning because the minimum anchors nonnegative offsets.
- Overlapping queries must be answered independently without modifying `nums`.
