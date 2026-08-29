## General

**An optimal removal may be treated as one contiguous block**

The score is determined only by the smallest and largest removed indices. If some characters between those endpoints were originally kept, removing them too does not increase the score because the endpoints remain the same. Removing additional characters from `t` also cannot destroy the fact that the remaining string is a subsequence of `s`.

Therefore, an optimal solution can remove one contiguous block `t[k:k+x]` of length $x$. The kept string consists of a prefix `t[:k]` followed by a suffix `t[k+x:]`. The problem becomes finding the smallest $x$ for which some split $k$ lets both kept pieces appear in `s` in the correct order.

Length zero represents removing nothing. Length `len(t)` represents removing all of `t`, leaving the empty string, which is always a subsequence.

**Record the earliest match for every prefix endpoint**

Let $m=|s|$ and $n=|t|$. The array `f` has one entry per index of `t`. A left-to-right greedy scan matches `t` against `s`. Whenever `s[i] == t[j]`, it sets `f[j] = i` and advances $j$.

Thus, when finite, `f[p]` is the earliest position in `s` where the prefix `t[:p+1]` can finish. Greedily using the earliest possible match is optimal because it leaves the largest remaining suffix of `s` available for whatever must come afterward.

Entries for unmatched prefix characters remain `inf`. Such a prefix cannot be embedded in `s`.

**Record the latest match for every suffix start**

The array `g` is built symmetrically from right to left. When `s[i] == t[j]`, the scan sets `g[j] = i` and moves to the preceding character of `t`.

When valid, `g[q]` is the latest position in `s` where the suffix `t[q:]` can begin. Taking suffix matches as late as possible leaves the largest amount of room before them for a kept prefix.

Entries that cannot start a fully matched suffix remain $-1$.

**Check one candidate removal length**

For a proposed length $x$, `check(x)` tries every starting index $k$ from $0$ through $n-1$. The removed block is `t[k:k+x]`.

The kept prefix ends at index `i = k - 1` in `t`. If that prefix is empty, its conceptual finish position in `s` is $-1$. Otherwise its earliest finish is `f[i]`.

The kept suffix begins at index `j = k + x`. If that suffix is empty because $j\ge n$, its conceptual start position is `m + 1`. Otherwise its latest start is `g[j]`.

The two pieces can be combined exactly when

$$
l<r,
$$

where $l$ is the prefix finish and $r$ is the suffix start. Strict inequality guarantees that their matched positions do not overlap or reverse order.

The sentinels make empty pieces natural. An empty prefix ending at $-1$ comes before any real suffix match. An empty suffix beginning at $m+1$ comes after any real prefix match. Unmatched real pieces retain `inf` or $-1$, causing the inequality to fail.

**Why earliest prefix plus latest suffix is decisive**

If even the earliest possible completion of the prefix is not before the latest possible start of the suffix, no other choices can work. Every alternative prefix match ends at the same place or later, and every alternative suffix match begins at the same place or earlier.

Conversely, if `f[k-1] < g[k+x]`, concatenate the greedy prefix match and greedy suffix match. All prefix positions precede all suffix positions, and both parts preserve character order internally. Their concatenation is a valid subsequence of `s`.

Thus `check(x)` returns true exactly when some length-$x$ block can be removed successfully.

**Binary-search the first feasible length**

If removing $x$ consecutive characters works, removing a block of length $x+1$ can also work: extend the successful removed interval by one position on either available side. The kept string only loses a character, so it remains a subsequence. Feasibility is monotone in $x$.

The call `bisect_left(range(n + 1), True, key=check)` searches lengths $0$ through $n$ and returns the first true one. The `range` is lazy and occupies constant space. Removing all $n$ characters always works, so the search has a guaranteed true endpoint.

For `s = "abacaba"` and `t = "bzaa"`, removing the one-character block `"z"` leaves `"baa"`. The earliest prefix match for `"b"` ends before a valid suffix match for `"aa"` begins, so `check(1)` succeeds. `check(0)` fails because the whole `t` is not a subsequence, making the answer one.

## Complexity detail

Building `f` and `g` takes $O(m+n)$ time because each two-pointer scan advances through each string only once. One `check(x)` call loops over up to $n$ split positions and costs $O(n)$ time. Binary search calls it $O(\log n)$ times.

The exact checked-in implementation therefore takes $O(m+n\log n)$ time, not the manifest's stated $O(m+n)$. A different coordinated two-pointer method can achieve the linear bound, but it is not the code here. Arrays `f` and `g` use $O(n)$ space, while the remaining state is constant.

## Alternatives and edge cases

- **Linear two-pointer optimization:** Prefix and suffix match information can be combined in one monotone sweep to find the minimum gap in $O(m+n)$ time, matching the manifest but differing from this implementation.
- **Try every removed interval:** There are $O(n^2)$ intervals, and checking each subsequence separately is much too slow.
- **General subsequence dynamic programming:** A two-dimensional table over both strings is unnecessary and can require $O(mn)$ time or space.
- **Already a subsequence:** `check(0)` succeeds, and binary search returns score zero.
- **No shared useful characters:** Only removing all of `t` works, so the answer is $n$.
- **Empty kept prefix:** The $-1$ sentinel ensures a valid suffix alone can satisfy the check.
- **Empty kept suffix:** The `m + 1` sentinel ensures a valid prefix alone can satisfy the check.
- **Unmatched prefix or suffix:** `inf` and $-1$ deliberately make `l < r` false for an impossible real piece.
- **Repeated characters:** Greedy earliest prefix matches and latest suffix matches preserve maximum separation even when many choices exist.
- **Lazy search range:** `range(n + 1)` does not allocate an $O(n)$ list of candidate lengths.
