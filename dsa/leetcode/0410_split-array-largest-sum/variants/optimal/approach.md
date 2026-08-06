## General
**Search the possible largest sum**

No group limit can be below `max(nums)`, because every element belongs to some group. A limit of `sum(nums)` always
works as one group and therefore also permits at most `k` groups. Binary-search this inclusive numeric interval. Let
$S = \texttt{sum(nums)} - \texttt{max(nums)} + 1$ be the number of integer candidate limits in it.

**Greedily count groups under a candidate limit**

Scan left to right, extending the current group while its sum stays within the limit. When the next value would exceed it, start a new group. Because values are nonnegative, delaying each cut as long as possible minimizes the number of groups needed under that limit.

**Use monotonic feasibility**

If the greedy scan needs at most `k` groups, the candidate is feasible: any group can be split further at element boundaries until exactly `k` nonempty groups exist, without increasing a sum. Every larger limit is also feasible. If more than `k` groups are necessary, every smaller limit is impossible.

**Why the converged bound is optimal**

Binary search discards only ranges proved entirely feasible or infeasible by the monotone predicate. When the bounds meet, that value is feasible and its predecessor is not, so it is exactly the minimum possible largest group sum.

## Complexity detail
Each feasibility check scans `n` values in $O(n)$ time. Binary search performs $O(\log S)$ checks over the range from the largest element to the total sum, giving $O(n \log S)$ time. Only scalar bounds and counters use $O(1)$ space.

## Alternatives and edge cases
- **Partition dynamic programming:** tries every prior cut for every group and endpoint, taking $O(kn^2)$ time and $O(n)$ optimized space.
- **Enumerate all cut combinations:** grows combinatorially.
- **Greedily balance group sums without a tested limit:** local equalization choices do not guarantee a global optimum.
- With $k = 1$, the answer is the total sum.
- With $k = n$, the answer is the largest element.
- Zero values allow cuts without increasing any group sum.
- Nonnegativity is what makes greedy feasibility and monotonic splitting valid.
