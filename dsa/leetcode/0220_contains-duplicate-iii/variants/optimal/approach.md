## General

**Separate the two conditions with a moving index window**

When the scan is at index `i`, a prior index `j` satisfies the index condition
exactly when `i - indexDiff <= j < i`. If the data structure contains only
values from those prior positions, every stored value already has an acceptable
index distance. The remaining task is to ask whether any stored value lies
within `valueDiff` of the current value.

The exact solution maintains those values in a `SortedSet` named `s`. Unlike an
ordinary hash set, a sorted set supports order queries. For current value `v`,
the acceptable numeric interval is

$$
[v-\texttt{valueDiff},\;v+\texttt{valueDiff}].
$$

The method finds the first stored value not smaller than the interval's lower
endpoint. If that smallest candidate is also no greater than the upper
endpoint, a valid pair exists.

**What the set contains before each search**

Before processing index `i`, `s` contains values belonging to the most recent
`indexDiff` prior indices, or all prior indices if fewer have been seen. The
current value is not inserted yet. Consequently any match found in `s` comes
from a distinct earlier index and automatically satisfies
$\lvert i-j\rvert \le \texttt{indexDiff}$.

After the query, the source inserts `v`. If `i >= indexDiff`, it then removes
`nums[i - indexDiff]`. At the current iteration, that old position is still
allowed because its distance from `i` is exactly `indexDiff`, so removal must
happen after the search, not before it. For the next index `i + 1`, its distance
would become `indexDiff + 1`, so removing it now prepares the precise next
window.

For example, with `indexDiff = 3`, the search at index 5 must consider indices
2, 3, and 4. After testing index 5, the algorithm adds its value and removes
the value at index 2. The set then represents indices 3, 4, and 5 for the
search at index 6.

**Use one lower-bound query to test the value interval**

`s.bisect_left(v - valueDiff)` returns the insertion position `j` of the lower
bound. If `j == len(s)`, every stored value is smaller than the lower bound, so
none can qualify. Otherwise `s[j]` is the smallest stored value that is at
least `v - valueDiff`.

Only this one candidate needs to be checked. If `s[j] <= v + valueDiff`, then
it lies inside the full closed interval and its difference from `v` is at most
`valueDiff`. If `s[j]` is already above the upper endpoint, every later sorted
value is even larger and also fails. Values before position `j` are below the
lower endpoint by the definition of `bisect_left`.

The endpoints are inclusive. Using `bisect_left` includes a value exactly
equal to `v - valueDiff`, and the `<=` comparison includes one exactly equal to
`v + valueDiff`, matching the required “at most” relation.

**Trace a successful exact-duplicate case**

For `nums = [1, 2, 3, 1]`, `indexDiff = 3`, and `valueDiff = 0`, the set before
index 3 contains `{1, 2, 3}`. The numeric interval for current value 1 is
`[1, 1]`. `bisect_left(1)` points to stored value 1, which is no greater than
the upper endpoint 1. The method returns true. That stored 1 came from index 0,
whose distance from index 3 is exactly the permitted maximum.

For `nums = [1, 5, 9, 1, 5, 9]`, `indexDiff = 2`, and `valueDiff = 3`, every
search examines only the previous two positions. Equal values recur three
positions apart, after their old occurrences have left the window, while the
values that remain differ by more than 3. Every interval query fails and the
method returns false.

**Why a set is safe even though windows usually need multiplicities**

A plain set normally cannot represent two active equal values separately. In
this algorithm, that situation never needs to survive an iteration. If the
current `v` equals a value already in the active set, then it is inside the
allowed interval for every nonnegative `valueDiff`, so the method returns true
before attempting insertion. Along any execution that continues, all active
window values are therefore distinct.

That fact also makes `s.remove(nums[i - indexDiff])` safe: the leaving value has
exactly one representative in the set. A multiset would be necessary only if
the algorithm continued past a detected active duplicate or if the query
semantics required counting rather than immediate existence.

**Why a true result satisfies both requirements**

The returned candidate lies in `s`, so it comes from an earlier active-window
index and satisfies the index-distance limit. The lower-bound construction and
upper comparison place it between `v - valueDiff` and `v + valueDiff`, which is
equivalent to an absolute value difference at most `valueDiff`. Because current
`v` has not yet been inserted, the two indices are distinct.

**Why exhausting the scan proves no pair exists**

Consider any hypothetical valid pair and focus on its later index. At that
iteration, the earlier index has not yet been evicted because its distance is
at most `indexDiff`; its value is present in `s`. The value condition places it
inside the current query interval. The lower-bound candidate is no larger than
that qualifying value while still at or above the lower bound, so it too lies
inside the interval, and the method would return true. Therefore completing all
iterations without returning rules out every valid pair.

**The exact source is an ordered-window method, not the manifest's buckets**

The manifest describes constant-expected-time buckets of width
`valueDiff + 1`. The exact solution uses `SortedSet` and ordered binary search.
Its actual time is $O(n\log w)$ for active-window size
$w = \min(n,\texttt{indexDiff})$, not $O(n)$. Its space bound agrees with the
manifest. This document follows the executable source and does not attribute a
bucket algorithm's time bound to a balanced ordered container.

`SortedSet` is supplied by the third-party `sortedcontainers` package, but the
source file does not import it. It also expects `List` to be available in the
execution environment.

## Complexity detail

Let $n$ be `len(nums)` and
$w = \min(n,\texttt{indexDiff})$. The set contains at most $w$ values.
`bisect_left`, ordered indexing, insertion, and removal take logarithmic time
in the window size under the `SortedSet` abstraction. Each input element causes
a constant number of these operations, so total time is
$O(n\log w)$. When the set is empty or has one entry, the logarithm is
understood with the usual constant lower bound.

The active set stores at most one value per index in the window and therefore
uses $O(w)$ auxiliary space. The algorithm reads `nums` without changing it.

## Alternatives and edge cases

- **Width-`valueDiff + 1` buckets:** Map each active value to a floor-divided bucket, then check its own and adjacent buckets. This matches the manifest and gives expected $O(n)$ time with $O(w)$ space, but negative-value bucket arithmetic and eviction must be handled carefully.
- **Balanced multiset:** Store counts as well as order. It supports the same lower-bound query and is robust if duplicate values must coexist, at the cost of slightly more bookkeeping than this early-return problem needs.
- **Linear scan of the previous window:** Compare `v` with each of up to `indexDiff` prior values. It uses constant extra space but takes $O(nw)$ time in the worst case.
- **`valueDiff = 0`:** The interval collapses to `[v,v]`, so the method detects exact duplicates within the index window.
- **`indexDiff = 1`:** Before each search, the set contains only the immediately preceding value. Removal after the query maintains that one-element window.
- **Maximum index window:** If `indexDiff >= n - 1`, every earlier index remains eligible, and the set can grow to $O(n)$ distinct values.
- **A pair exactly on either boundary:** Distance exactly `indexDiff` is tested before eviction, and numeric difference exactly `valueDiff` passes the inclusive comparisons.
- **Negative values:** Ordered comparison and subtraction work normally; unlike a bucket method, this source needs no floor-division convention.
- **Repeated value outside the window:** Its old representative has already been removed, so equality alone does not produce a false positive.
- **Large magnitudes:** Python integers do not overflow when computing `v - valueDiff` or `v + valueDiff`; fixed-width implementations should use a sufficiently wide type.
- **Input preservation:** Only the ordered set changes. The array and its ordering remain intact.
