## General
**Increasing choices give each set one construction path**

Keep a path and `start`, the smallest value allowed next. After choosing `value`, recurse with `value + 1`. The path is therefore strictly increasing, which is the unique canonical ordering of its set; permutations such as `[2,1]` are never explored separately from `[1,2]`.

**Reserve enough larger values to complete the path**

If the path still needs `r = k - len(path)` values, choosing next value `v` leaves $n - v$ larger values. Completion is possible only when that supply can fill the remaining $r - 1$ positions, which rearranges to $v \le n - r + 1$. Restricting the loop to this inclusive bound avoids every doomed short branch.

**Backtracking restores the shared prefix**

On entry, the path is strictly increasing and contains the fixed prefix for this subtree. Every completion uses only values at least `start`, so sibling next-value branches are disjoint. Append a choice, recurse, and pop it so the next sibling sees the exact same parent prefix.

**Trace the pruned choice ranges**

For $n = 4, k = 2$, a path beginning with 1 may choose 2, 3, or 4, producing three combinations. Backtracking then begins with 2 and chooses 3 or 4, and finally begins with 3 and chooses 4.

**Increasing order is the canonical path for a combination**

Every path chooses values from `1..n` in strictly increasing order and is emitted only at length `k`, so each leaf is a valid combination of distinct values.

Any valid combination has one unique increasing representation. The search permits each next value after the previous choice, so it follows that representation's branch. A different branch differs at its first distinct choice and cannot produce the same set, proving complete duplicate-free enumeration.

## Complexity detail
There are `C(n,k)` outputs and copying each costs $O(k)$, establishing the output-tight $O(k \cdot \binom{n}{k})$ time bound. The path and recursion use $O(k)$ auxiliary space, excluding returned combinations.

## Alternatives and edge cases
- **Generate all permutations then deduplicate:** performs vastly more work and loses the canonical-order invariant.
- **Enumerate all $2^{n}$ subsets then filter by size:** ignores `k` and can be much slower when few subsets have the requested size.
- **Iterative lexicographic generation:** achieves comparable output-sensitive complexity but has less direct state reasoning.
- $k = n$ has one path containing every value; $k = 1$ emits one singleton for each value.
- Copy the path at length `k`; storing the mutable path reference would corrupt completed results during backtracking.
