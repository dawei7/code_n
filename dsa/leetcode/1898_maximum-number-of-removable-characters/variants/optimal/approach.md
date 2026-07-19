## General
**Turn removal order into a threshold.** Build an array `removal_time` aligned with `s`. If original index `i` is the $j$-th entry of `removable`, store $j$; for an index that is never removable, store $r$. Under a candidate prefix length $k$, the character at index `i` remains exactly when `removal_time[i] >= k`. This avoids constructing a new string or repeatedly shifting indices.

**Test one prefix with two pointers.** Scan `s` from left to right while tracking the next unmatched character of `p`. Ignore positions removed before $k$. Whenever a retained character equals the current character of `p`, advance the pattern pointer. The test succeeds if that pointer reaches the end of `p`. Because matches are taken in increasing original-index order, success is precisely the definition of `p` being a subsequence.

**Binary-search the last successful prefix.** If `p` survives $k$ removals, it also survives any smaller prefix because restoring characters cannot invalidate a subsequence. Conversely, once a prefix fails, every larger prefix fails. This monotone true-then-false predicate lets an upper-midpoint binary search retain the greatest successful $k$, including the boundary answers $0$ and $r$.

## Complexity detail
Let $n = \lvert s \rvert$ and $r = \lvert\texttt{removable}\rvert$. Constructing `removal_time` costs $O(n + r)$ time and $O(n)$ space. Each subsequence test scans at most $n$ positions, and binary search performs $O(\log(r + 1))$ tests. The total time is $O((n + r)\log(r + 1))$, with $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Rebuild the retained string for every candidate:** This preserves correctness but performs extra allocation and may repeatedly copy $O(n)$ characters; a removal-time array supports the same test in place.
- **Try every prefix in increasing order:** Rechecking the subsequence after each removal can require $O(nr)$ time when `p` survives nearly every prefix.
- **Empty `removable`:** The only legal choice is $k = 0$, and the initial subsequence guarantee makes it valid.
- **All listed removals are harmless:** The answer can equal $r$ even though the constraints require $r < n$.
- **Original indices:** Entries in `removable` never shift after earlier deletions; treating them as indices into a shortened string changes the problem.
- **Repeated characters:** A greedy left-to-right subsequence match is necessary because retaining the right counts alone does not preserve relative order.
