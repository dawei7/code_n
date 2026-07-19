## General
**Fix how many digits come from each source**

If `take` digits come from `nums1`, then exactly `k - take` must come from `nums2`. Only splits satisfying `0 <= take <= n` and `0 <= k - take <= m` are feasible. Enumerating that interval covers every valid final sequence because each sequence has one definite source count.

For each split, solve two independent tasks: choose the maximum subsequence of the requested length from each array, then merge those two subsequences as strongly as possible. Keep the greatest candidate over all splits.

**A monotonic stack chooses the best fixed-length subsequence**

To select `r` digits from one array, exactly `len(nums) - r` digits may be dropped. Scan left to right. While drops remain and the current digit is larger than the stack top, remove that smaller earlier digit; replacing it improves the first position where the subsequences differ. Then append the current digit. If unused drops remain after the scan, truncate them from the end.

The stack never changes the order of retained digits. A smaller top is removed only when enough deletion budget remains, so the requested length is always achievable. When the scan finishes, every possible earlier improvement has been taken, making the retained subsequence lexicographically maximal for that length.

**Equal leading digits require comparing the complete remaining suffixes**

During the merge, choosing the larger current digit is easy. When the digits are equal, the next choice must come from whichever remaining suffix is lexicographically larger. Looking only one digit ahead is insufficient because equal runs may continue for many positions.

Compare suffixes by advancing temporary indices across their common prefix. If one suffix ends first, the other is larger; otherwise the first unequal digit decides. Append from the winning source and repeat. This greedy choice fixes the largest possible next digit without disturbing either source order. By induction over output positions, the merge is the largest interleaving of the two chosen subsequences.

Together, the maximum-subsequence proof handles every fixed split, the suffix-aware merge handles every interleaving for that split, and enumerating all feasible splits handles every source allocation. The best candidate is therefore globally optimal.

## Complexity detail
There are at most $k + 1$ feasible splits. For one split, the two monotonic scans cost $O(n + m)$. A merge emits `k` digits, and a suffix comparison may scan $O(k)$ equal digits at each emission, giving $O(k^2)$ in the worst case. Total time is $O(k(n + m + k^2))$. Stacks, candidates, and the merged result use $O(k)$ auxiliary space.

## Alternatives and edge cases
- **Compare only the current digits while merging:** fails on ties such as suffixes `[6,7]` and `[6,0,4]`; the left `6` must win because $7 > 0$ later.
- **Choose the globally largest `k` digits:** can violate the relative order within a source.
- **Enumerate all subsequences or interleavings:** is correct but grows combinatorially.
- One feasible split may take all digits from one source. Repeated equal digits stress suffix comparisons but do not change correctness, and $k = n + m$ requires retaining every input digit while still choosing the best merge.
