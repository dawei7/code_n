## General

**Keep only the earliest useful occurrence.** For any fixed value, only its earliest occurrence in each array can participate in the minimum index sum. Replacing either occurrence by a later duplicate never decreases $i+j$.

Scan `nums1` and store the first index of each value, leaving an existing entry unchanged when a duplicate appears. Then scan `nums2`. Whenever its current value exists in the map, combine the current index with the stored earliest index and update the global minimum.

**Take the minimum across common values.** The scan considers the earliest `nums1` occurrence with every `nums2` occurrence. In particular, it considers the earliest occurrence in both arrays, which is the best pair for that value. Taking the minimum across values therefore yields the best good pair overall. If no lookup succeeds, return `-1`.

## Complexity detail

Both arrays are scanned once. Expected time is $O(n)$ under expected constant-time hash-table operations, and the map stores at most $n$ distinct values for $O(n)$ space.

The benchmark defines its size as the common length $n$. It places the only common value at both final positions. The accepted lookup method stays linear, while a calibrated correct alternative examines every cross-array index pair and grows quadratically.

## Alternatives and edge cases

- **Enumerate all index pairs:** It is direct and correct but takes $O(n^2)$ time.
- **Sort value-index pairs:** Sorting can group common values in $O(n\log n)$ time, but hashing avoids the extra logarithmic factor.
- **Duplicate values:** Retain only the earliest index; later duplicates cannot improve a sum for the same value.
- **Immediate match:** A shared value at index 0 in both arrays gives the globally minimum possible answer 0.
- **Tied values:** Several distinct common values may attain the same minimum; only the numeric sum is returned.
- **Negative elements:** Hash keys handle them exactly like non-negative values.
- **No common value:** Preserve the sentinel and return `-1`.
- **Singleton arrays:** Equal singleton values return 0, while unequal ones return `-1`.
