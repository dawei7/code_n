## General
**Turn a subarray sum into a difference of prefixes**

Let the running prefix through index `i` be `P`. A subarray starting after index `j` and ending at `i` sums to `k` exactly when `P - prefix[j] = k`, or equivalently `prefix[j] = P - k`.

Maintain a hash table from each prefix sum to the earliest index where it occurred. At each position, update the running sum and look for `running - k`. If present at index `j`, the subarray from $j + 1$ through the current position is valid, so compare its length with the best seen.

Seed the table with prefix sum zero at index `-1`. This represents the empty prefix before the array and lets a valid subarray beginning at index zero use the same formula.

**Preserve the earliest occurrence of every prefix**

When a prefix value repeats, do not replace its stored index. For a fixed ending index, the earliest matching prefix produces the longest subarray. A later occurrence can never yield a better length for this or any future end.

For `[1,-1,5,-2,3]` with target three, prefix zero is first stored at `-1` and appears again after `-1`; the earlier index is retained. At index three the running sum is three, so matching prefix zero gives length four for `[1,-1,5,-2]`.

Every reported interval is correct because subtracting its stored prefix from the current prefix equals `k`. Conversely, if an optimal interval ends at `i`, its preceding prefix sum is `running - k`; that value was stored when its earliest occurrence was scanned. The lookup therefore considers an interval at least as long as the optimum ending at `i`, proving the global maximum is found.

## Complexity detail
The scan performs one expected-constant-time lookup and insertion per element, giving $O(n)$ expected time. At most $n + 1$ distinct prefix sums are stored, using $O(n)$ space.

## Alternatives and edge cases
- **Enumerate every start and end:** is correct but takes $O(n^2)$ time even when rolling sums avoid a third loop.
- **Sliding window:** is not valid when negative values can make expansion decrease the sum or contraction increase it.
- **Overwrite repeated prefix indices:** can preserve correctness but lose the longest possible interval.
- Target zero and repeated zero prefixes are handled naturally. A whole-array match uses the seeded index `-1`, and no match leaves the answer at zero.
