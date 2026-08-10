## General

**Search for the median value instead of building all subarray values**

An array of length $n$ has

$$
m=\frac{n(n+1)}2
$$

nonempty subarrays. Explicitly computing the distinct count for every one and sorting those $m$ values would be too expensive when $n$ reaches $10^5$.

The lower median is the element at one-based rank

$$
q=\left\lceil\frac m2\right\rceil=\frac{m+1}{2}\text{ rounded down}.
$$

Rather than generate the sorted uniqueness array, ask a threshold question:

“Are there at least $q$ subarrays containing at most `mx` distinct values?”

If the answer is true for some `mx`, it remains true for every larger threshold. This monotonic false-then-true behavior makes binary search possible. The first threshold for which the count reaches $q$ is exactly the lower median.

**Count subarrays with at most mx distinct values**

Helper `check(mx)` uses a sliding window. At each right endpoint `r`:

1. Add `nums[r]` to frequency map `cnt`.
2. While the map contains more than `mx` keys, move left endpoint `l` rightward, decrementing frequencies and removing a key when its count becomes zero.
3. Once the window `nums[l..r]` has at most `mx` distinct values, add `r - l + 1` to `k`.

Why add that many? Every subarray ending at $r$ and starting at an index from $l$ through $r$ is a suffix of the valid window, so it also has at most `mx` distinct values. There are exactly $r-l+1$ such starts.

Any start before $l$ is invalid at the moment the shrinking loop stops. The window was shrunk only while it had too many distinct values, and $l$ is the smallest remaining valid start. Thus the helper counts all qualifying subarrays ending at $r$ exactly once.

The count `k` is cumulative across right endpoints. As soon as it reaches `(m + 1) // 2`, the helper returns `True`; the exact total is unnecessary because binary search needs only the yes/no predicate.

**How the binary search call works**

The expression

`bisect_left(range(n), True, key=check)`

treats `range(n)` as candidate thresholds 0 through $n-1$. Python applies `check` as the key and sees a conceptual Boolean sequence such as

`[False, False, True, True, ...]`.

`bisect_left` returns the first position whose keyed value is at least `True`, which is the first true threshold.

Distinct counts of nonempty subarrays range from 1 to at most $n$. For $n>1$, the median is below $n$ because all $n$ length-one subarrays have distinct count 1 and only one subarray can reach $n$ distinct values; the searched range contains the answer. For $n=1$, `check(0)` is false and `bisect_left` returns the insertion position 1, which is the correct median even though 1 lies just beyond the sole candidate index.


For any integer $v$, `check(v)` is true exactly when at least $q$ entries of the uniqueness multiset are no greater than $v$. In a sorted list, the value at rank $q$ is the smallest value with that property. Binary search returns precisely that smallest threshold, so it returns the requested lower median.

For `nums = [1,2,3]`, there are six subarrays and $q=3$. At threshold 1, exactly the three length-one subarrays qualify, so `check(1)` is true. Threshold 0 qualifies none. The first true value is 1.

## Complexity detail

Let $n$ be the array length and let $D$ be the number of distinct values in the whole array.

Inside one `check` call, the right pointer advances $n$ times. The left pointer also advances at most $n$ times over the entire call, not $n$ times per right endpoint. Expected hash-map operations are $O(1)$, so one check costs $O(n)$ expected time.

The exact code binary-searches `range(n)`, not the narrower range 0 through $D$. It therefore makes $O(\log n)$ predicate calls and takes $O(n\log n)$ expected time. The manifest says $O(n\log D)$, which would apply if the search upper bound were explicitly $D$; that is not what the exact source does. Since $D\le n$, both bounds coincide in the worst case, but they differ when $D$ is much smaller than $n$.

The frequency map contains at most $D$ keys and usually at most `mx` keys after shrinking, so auxiliary space is $O(D)$. The lazy `range` object uses $O(1)$ storage.

The total number of subarrays can be $O(n^2)$, but Python integers safely store `m` and `k`. Early return can save work on some checks without changing worst-case complexity.

## Alternatives and edge cases

- **Build and sort the uniqueness array:** Counting all $O(n^2)$ subarrays and sorting their values is too slow and requires quadratic storage.
- **Search only through D:** Compute the whole-array distinct count first and binary-search 0 through $D$. This realizes the manifest's $O(n\log D)$ time but adds an initial set construction.
- **Two-pointer counting by exact distinct count:** Counting subarrays with exactly $k$ distinct values can be obtained from two “at most” counts, but finding the median still benefits from threshold search.
- **Fenwick-tree/offline methods:** More advanced formulations exist, but the monotone sliding-window predicate is simpler and meets the constraints.
- **Lower median for even m:** The target rank is `(m + 1) // 2`. Using `m // 2 + 1` would choose the upper middle when $m$ is even.
- **Single element:** The search returns insertion index 1 after `check(0)` is false, correctly reporting uniqueness 1.
- **All values equal:** Every subarray has exactly one distinct value, so threshold 1 immediately has all $m$ subarrays and the answer is 1.
- **All values distinct:** A window's distinct count equals its length; the predicate still counts valid suffixes correctly.
- **Removing zero-frequency keys:** Leaving a zero-count key in `cnt` would make `len(cnt)` overstate the number of distinct values and break the window invariant.
- **Threshold zero:** No nonempty subarray qualifies. The shrinking loop moves `l` beyond each `r`, contributing zero.
- **Hash-map complexity:** The stated linear check time is expected under ordinary dictionary behavior; pathological collision behavior is outside the standard analysis.
- **Predicate monotonicity:** Raising `mx` can only add qualifying subarrays, never remove them, which is the exact property `bisect_left` requires.
