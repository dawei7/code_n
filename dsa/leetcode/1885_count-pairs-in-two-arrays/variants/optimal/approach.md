## General

**Move both sides of the inequality into one value per index.** The required condition is

$$
\texttt{nums1}[i]+\texttt{nums1}[j]
>
\texttt{nums2}[i]+\texttt{nums2}[j].
$$

Subtracting the second-array terms gives

$$
(\texttt{nums1}[i]-\texttt{nums2}[i])
+
(\texttt{nums1}[j]-\texttt{nums2}[j])>0.
$$

The list comprehension constructs these differences as `nums`. The original four-value comparison is now simply a question of counting pairs in one list whose sum is positive. This transformation preserves every index occurrence, including duplicate difference values.

**Sorting makes successful partners contiguous.** After `nums.sort()`, if `nums[l] + nums[r] > 0` for some left index `l` and fixed right index `r`, then every index `k` with `l <= k < r` also works because `nums[k] >= nums[l]`. Conversely, values before the first successful `l` cannot pair successfully with `r`. Thus all valid left partners for a fixed right endpoint form one suffix of the indices before `r`, and their count is `r - l`.

**Use the largest remaining value as the right endpoint.** The pointers start at the smallest and largest sorted positions. For the current `r`, the inner loop advances `l` while `nums[l] + nums[r] <= 0`. The comparison uses `<=` because the problem requires a strict greater-than inequality; a zero sum must be rejected. When the loop stops, either `l == r` and no pair remains, or `nums[l] + nums[r] > 0` and every position from `l` through `r - 1` forms a valid pair with `r`.

The line `ans += r - l` counts all those pairs at once. The algorithm then decrements `r`, permanently removing that right endpoint. Every counted pair has a unique larger sorted position, so it will not be counted again.

**Why the left pointer never needs to move backward.** When `r` decreases, `nums[r]` can only stay the same or become smaller. The minimum left value needed to make a positive sum can therefore only stay in place or move right. Any index already rejected with a larger right value cannot become valid with a smaller one. This monotonic threshold is what turns repeated partner searches into one overall linear scan after sorting.

**Trace the first example.** Differences for `nums1 = [2, 1, 2, 1]` and `nums2 = [1, 2, 1, 2]` are `[1, -1, 1, -1]`, which sort to `[-1, -1, 1, 1]`. With `r = 3`, both `-1 + 1` sums are zero and fail the strict condition, so `l` moves to index two. Pairing `nums[2]` with `nums[3]` gives two, so `r - l = 1` is added. Decrementing `r` makes it equal to `l`, ending the loop. The single counted occurrence corresponds to the two original indices whose differences were both one.

**Sorting does not lose original index-pair counts.** The condition after transformation depends only on the two difference values, not on their original order. Sorting permutes element occurrences bijectively. Every unordered pair of original indices corresponds to exactly one unordered pair of sorted positions and keeps the same sum. Counting pairs with lower sorted position less than higher sorted position therefore counts the same number of original pairs satisfying `i < j`; the order constraint exists only to avoid counting each unordered pair twice.

**Why the batch count is exact.** At a fixed `r`, the inner loop proves all positions below `l` fail and sorted order proves all positions at least `l` and below `r` succeed. Adding `r - l` is thus neither missing nor overcounting any partner for that endpoint. Since `r` visits each possible higher position once and `l` only removes positions that can never work in the future, induction over descending `r` establishes the final total.

**Input arrays are preserved.** The source builds a new difference list and sorts that list. Neither `nums1` nor `nums2` is rearranged or modified. `zip` stops at the shorter input in general, but the contract guarantees equal lengths, so every index contributes one difference.

## Complexity detail

Let $n$ be the common array length. Constructing differences costs $O(n)$ time. Sorting them costs $O(n\log n)$. Pointer `r` moves left at most $n$ times, and `l` moves right at most $n$ times across all inner-loop executions, so the counting phase is $O(n)$. Total time is $O(n\log n)$.

The difference list requires $O(n)$ storage. Python's Timsort may also use $O(n)$ temporary memory in the worst case. The pointers and answer use constant additional state, so overall auxiliary space is $O(n)$, matching the manifest.

There can be $n(n-1)/2$ successful pairs, which is about five billion when $n=10^5$. Python integers handle this automatically. A fixed-width implementation must use a 64-bit counter even though individual input values fit comfortably in 32 bits.

## Alternatives and edge cases

- **Binary search for each right endpoint:** After sorting, find the first value greater than `-nums[r]` with an upper-bound search. This is correct but takes another $O(n\log n)$ counting phase, while the monotone pointer makes it linear.
- **Brute-force all index pairs:** Directly testing every `i < j` takes $O(n^2)$ time and is too slow for $10^5$ elements.
- **Fenwick tree over differences:** Coordinate compression and frequency queries can count earlier values above a threshold online, but add data-structure complexity without improving the sorting-based asymptotic bound.
- **Strict inequality:** Difference sums equal to zero do not qualify. The inner loop must use `<= 0`, not `< 0`.
- **All differences nonpositive:** The left pointer eventually meets the right pointer without adding any positive count, and zero is returned.
- **All differences positive:** The inner loop never moves `l`, and each right endpoint contributes all earlier positions, totaling $n(n-1)/2$.
- **Duplicate differences:** They remain separate occurrences. Sorting and the `r - l` count include every distinct index pair even when values are equal.
- **A single element:** `l == r` initially, the loop does not execute, and no pair exists.
- **Equal input lengths:** The source relies on the contract. If lengths differed, `zip` would silently ignore extra elements, so validation would be needed in a generalized API.
