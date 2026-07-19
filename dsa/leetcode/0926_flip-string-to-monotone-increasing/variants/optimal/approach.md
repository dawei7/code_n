## General
**Summarize the processed prefix**

Scan from left to right. Let `ones_seen` count the `1` characters in the original prefix, and let `flips` be the minimum flips that make that prefix monotone increasing.

A new `1` can remain at the end of any monotone prefix, so it adds no flip and only increments `ones_seen`. A new `0` creates exactly two relevant choices. Flip this current character to `1`, costing `flips + 1`, or keep it as `0` and flip every earlier `1` to `0`, costing `ones_seen`. Set `flips = min(flips + 1, ones_seen)`.

**Why the recurrence is complete**

For a prefix ending in `0` to be monotone, that zero must belong to the zero region, which forces every earlier one to be flipped. Otherwise the final zero itself must be flipped into the one region. These cases cover every monotone result and are disjoint at the current position. Since `flips` stores the best cost for the preceding prefix, choosing the smaller extension preserves the minimum by induction. After the final character, `flips` is the required answer.

## Complexity detail
The scan examines each of the $n$ characters once and performs constant work per character, so time is $O(n)$. The two counters use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Try every zero-one split:** For each boundary, count `1` characters to its left and `0` characters to its right. Recounting both sides for every boundary takes $O(n^2)$ time.
- **Prefix and suffix counts:** Precomputing the two mismatch counts makes every split test constant time and the total time linear, but uses $O(n)$ extra space.
- **Two-state dynamic programming:** Tracking the best prefix ending in `0` and the best ending in `1` is equivalent and linear, though the recurrence above compresses the same information into two counters.
- **All zeros or all ones:** The string is already monotone and needs no flips.
- **A single character:** Either possible character is monotone by itself.
- **Balanced counts:** Counts alone do not determine the answer; `"10"` needs one flip because order matters.
- **Several optimal results:** Only the minimum flip count is returned, not a particular transformed string.
