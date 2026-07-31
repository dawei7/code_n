## General

Removing one interval leaves a prefix and a suffix. The result is strictly
increasing exactly when both retained pieces are internally strictly
increasing and, if neither is empty, the prefix's last value is smaller than
the suffix's first value.

**Find the usable prefix boundary.** Advance `left` across the longest initial
strictly increasing run. If it covers the entire array, all $N(N+1)/2$
non-empty subarrays are valid removals. Otherwise, the `left + 2` choices of an
empty prefix or a prefix ending from `0` through `left` pair with an empty
suffix, so count the removals that reach the array's end first.

**Grow suffixes while shrinking compatibility.** Begin `right` at the last
element and move it left only while the suffix remains strictly increasing.
For each suffix, decrease `left` until the prefix is empty or
`nums[left] < nums[right]`. The compatible prefix endings are then `-1`
through `left`, contributing `left + 2` removals.

The prefix pointer never moves right: extending an increasing suffix leftward
introduces a smaller first value, so the bridge condition can only become more
restrictive. Every counted removal therefore joins two valid pieces, and every
valid removal is counted once by its unique retained prefix and suffix.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each pointer crosses the array at most once,
so the algorithm takes $O(N)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate endpoint pairs:** Prefix/suffix validity tables allow each interval to be checked in constant time, but there are $O(N^2)$ intervals.
- **Rebuild each remainder:** Copying and scanning the retained values for every interval takes $O(N^3)$ time.
- **Already strictly increasing:** Every non-empty subarray is incremovable, producing the triangular count.
- **Empty retained side:** An empty prefix, suffix, or entire remainder is strictly increasing without a bridge comparison.
- **Equal values:** Equality violates strict increase both within a retained piece and across the deletion boundary.
- **Large answer:** The count can reach $N(N+1)/2$, so fixed-width implementations need a 64-bit return type.
