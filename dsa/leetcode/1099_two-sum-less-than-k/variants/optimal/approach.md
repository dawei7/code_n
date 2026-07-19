## General
**Sort to expose monotonic choices.** Work with a sorted copy of `nums`. Place `left` at the smallest value and `right` at the largest. The current pair is the widest remaining combination, but its sum determines which endpoint can safely be discarded.

**Advance the smaller endpoint after a valid sum.** If `values[left] + values[right] < k`, record it as a candidate. Keeping the same left value while moving `right` inward cannot improve that sum, so every pair using this left endpoint is no better. Increment `left` to seek a larger candidate.

**Reduce the larger endpoint after an invalid sum.** If the current sum is at least `k`, pairing `values[right]` with any index between `left` and `right` only keeps or increases the sum. Therefore this right endpoint cannot participate in a valid remaining pair and can be decremented.

Each step discards one endpoint only after proving that it cannot yield a better valid answer. The pointers eventually cover all potentially optimal pair boundaries, and the best recorded candidate is consequently the maximum valid pair sum. If no candidate is recorded, no valid pair exists.

## Complexity detail
Sorting the $n$ values costs $O(n \log n)$ time, and the two pointers make one $O(n)$ pass. The sorted copy uses $O(n)$ auxiliary space; the pointer state itself is constant-size.

## Alternatives and edge cases
- **Check every pair:** A double loop is direct and correct but takes $O(n^2)$ time.
- **Sorting plus binary search:** For each left value, binary-search the largest compatible right value, also giving $O(n \log n)$ time.
- **Strict threshold:** A pair summing exactly to `k` is invalid and must force the right pointer inward.
- **Duplicate values:** Equal values may form a pair when they occupy different indices.
- **Fewer than two elements:** No pair exists, so the result is `-1`.
- **All sums too large:** The initialized `-1` remains unchanged.
