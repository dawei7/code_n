## General

**Sorted, strictly increasing arrays turn LCS into intersection**

In a general longest-common-subsequence problem, two shared values may appear in conflicting orders, so dynamic programming must decide which matches can coexist. Here every input array is strictly increasing. Any value that appears in several arrays has the same relative order in all of them: smaller common values always precede larger common values.

Each array also contains a value at most once. Therefore the longest common subsequence consists of exactly the values present in every array, listed in increasing order. No further ordering decision is needed.

The exact solution counts occurrences across all arrays. The constraints restrict values to $1$ through $100$, so `cnt = [0] * 101` supplies one counter for every possible value. For each `x` in each row, `cnt[x] += 1` records that this array contains `x`.

Because a row is strictly increasing, it cannot contribute twice to the same counter. Thus `cnt[x]` is not merely the total number of occurrences; it is exactly the number of different input arrays containing $x$.

**Select values found in every array**

There are `len(arrays)` input arrays. A value is common to all of them exactly when its counter equals that number. The result comprehension enumerates counters in numeric index order:

`[x for x, v in enumerate(cnt) if v == len(arrays)]`.

Enumeration automatically returns qualifying values from zero through 100 in increasing order. Index zero never qualifies because input values start at one and there are at least two arrays, but including its unused counter simplifies direct indexing.

For arrays `[2, 3, 6, 8]`, `[1, 2, 3, 5, 6, 7, 10]`, and `[2, 3, 4, 6, 9]`, the counters for two, three, and six become three. All other encountered values have smaller counts. The comprehension returns `[2, 3, 6]`.

**Why all common values can be included together**

Suppose $a<b$ are both present in every array. Strict increasing order forces $a$ to occur before $b$ in each array. Thus including $a$ never prevents including $b$. Applying this to every pair of common values shows that the complete sorted intersection is a subsequence of every array.

Any common subsequence can contain only values present in every array, so it cannot be longer than that intersection. Since the algorithm returns the entire intersection as a valid common subsequence, it is longest.

This also explains why no duplicate should appear in the result. Strictly increasing rows contain no duplicates, and the returned subsequence is itself strictly increasing.

**A complete correctness argument**

Every value returned has count equal to the number of arrays. Since each array can add at most one to that count, every array must contain it. Returned values are increasing because enumeration is increasing, so the returned list is a subsequence of every strictly increasing row.

Conversely, any value in a common subsequence appears in every row and increments its counter once per row, making its count equal to `len(arrays)`. The comprehension therefore returns it. The result contains all values that any common subsequence could use, so no longer common subsequence exists.

The solution exploits both special promises. Without strict uniqueness, a value could reach the array count through repeated occurrences in only some rows. Without sorted order, the common set might not be simultaneously usable as one subsequence.

## Complexity detail

Let $T$ be the total number of elements across all arrays and let $V=101$ be the counter-array length.

The nested loops visit each of the $T$ input elements exactly once. The final enumeration scans all $V$ counters. Total time is $O(T+V)$, which simplifies to $O(T)$ under the fixed value bound.

The counter array uses $O(V)$ space, and the returned list contains at most 100 values. Under the fixed constraints both are constant-sized; the manifest states the more explicit $O(V)$ auxiliary bound.

No sorting is performed because numeric counter indices already provide the required increasing order.

## Alternatives and edge cases

- **Set intersection:** Convert the first row to a set and repeatedly intersect it with later rows, then sort the result. This is correct but uses hashing and a final sort despite the small bounded value domain.
- **Repeated two-pointer intersection:** Merge the current common list with each sorted row. It takes linear time in the scanned data and does not rely on the value upper bound.
- **General LCS dynamic programming:** It would solve a much broader problem but waste time and memory because strict sorting eliminates order conflicts.
- **No common value:** No counter reaches the number of arrays, so the comprehension returns an empty list.
- **One shared value:** It is returned as a length-one subsequence.
- **Different row lengths:** Counts depend on membership, not row length, so no special handling is needed.
- **Value 100:** The counter has index 100 because its length is 101, so the upper bound is safely included.
- **Unused index zero:** It remains zero and cannot qualify because at least two arrays exist.
- **Strict-increase dependency:** Duplicate values in one row could falsely inflate a count; the exact method relies on the stated contract.
- **Sorted-order dependency:** In unsorted arrays, all common values need not form a common subsequence in sorted numeric order.
- **Result ordering:** Enumerating the counter array returns the required increasing sequence without a separate sort.
