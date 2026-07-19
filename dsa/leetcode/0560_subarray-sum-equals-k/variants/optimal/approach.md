## General
**Represent a subarray as a prefix difference**

Let the running prefix after the current element be `current`. A subarray ending here has sum `k` exactly when an earlier prefix equals `current - k`.

**Count every occurrence of an earlier prefix**

Store prefix sums in a frequency map rather than a set. If `current - k` has appeared several times, each occurrence starts a different valid subarray ending at the current index, so add its full frequency to the answer.

**Seed the prefix before the array**

Initialize sum zero with frequency one. This virtual prefix occurs before index zero and lets a prefix whose total is `k` count as a valid subarray beginning at the first element.

**Query before recording the current prefix**

Look up `current - k` before incrementing `current` in the map. This ensures the chosen earlier prefix is strictly before the subarray's end and prevents an empty subarray from being counted when $k = 0$.

**Why every valid subarray is counted once**

For a subarray from `left` through `right`, the prefix before `left` equals the prefix through `right` minus `k`. When the scan reaches `right`, that earlier prefix is already in the map and contributes one count. Conversely, every map occurrence added by the lookup identifies a unique earlier boundary whose difference is `k`, so it defines a valid non-empty subarray.

## Complexity detail
Each of the `n` elements performs constant expected-time hash lookups and updates, giving $O(n)$ time. At most $n + 1$ distinct prefix sums are stored, so space is $O(n)$.

## Alternatives and edge cases
- **Enumerate every start and extend a running sum:** is correct but examines $O(n^2)$ subarrays.
- **Precompute all prefixes then compare every pair:** keeps sum checks constant-time but still uses $O(n^2)$ pairs.
- **Sliding window:** is invalid when negative values can make the running sum decrease.
- **Target zero:** repeated equal prefix sums may create many valid subarrays.
- **All zeros:** every non-empty interval qualifies when $k = 0$.
- **Negative target:** uses the same prefix-difference equation without special handling.
- **Overlapping subarrays:** are distinct and must all be counted.
