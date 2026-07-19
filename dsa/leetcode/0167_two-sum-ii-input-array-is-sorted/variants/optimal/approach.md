## General
Sorting changes Two Sum from a lookup problem into an elimination problem. Put `left` at the smallest value and `right` at the largest, then inspect their sum.

- If the sum equals `target`, these are the required positions.
- If the sum is too small, increment `left`. Keeping that left value and choosing any smaller right endpoint could only decrease the sum, so the current left position cannot belong to a solution inside the remaining interval.
- If the sum is too large, decrement `right`. Keeping that right value and choosing any larger left endpoint could only increase the sum, so the current right position cannot belong to a solution.

The key is that each comparison eliminates an entire row or column of possible pairs, not just one pair. For `[2, 7, 11, 15]` and target `9`, $2 + 15$ is too large, so `15` is discarded; $2 + 11$ is also too large, so `11` is discarded; $2 + 7$ matches. Convert the zero-based pointer positions to the required one-based result `[1, 2]`.

Throughout the scan, the promised solution remains between `left` and `right`. When a boundary is removed, monotonic order proves that the boundary value cannot pair with any still-eligible position to reach the target. Because a valid pair is guaranteed, the pointers must encounter it before crossing.

Suppose the current sum is below the target. Every candidate partner for `numbers[left]` within the remaining interval is at most `numbers[right]`, so all such sums are at most the already-too-small current sum. Discarding `left` cannot discard a solution. The symmetric argument proves that a too-large sum allows `right` to be discarded safely. Thus every update preserves the valid pair in the candidate interval. When the current sum equals the target, the two distinct boundary indices form the required pair, so returning them is correct.

## Complexity detail
Each pointer moves only inward and can move at most $n - 1$ times. The total running time is $O(n)$, and the two indices plus current sum use $O(1)$ auxiliary space.

## Alternatives and edge cases
- A hash map also finds complements in $O(n)$ time, but uses $O(n)$ space and ignores the sorted-order guarantee.
- Binary-searching for each complement uses constant auxiliary space but costs $O(n \log n)$ time.
- Nested loops test $O(n^2)$ pairs.
- Equal values may form the answer when they occupy different positions; the pointer condition naturally preserves distinct indices.
- Negative values and boundary pairs need no special handling.
- The output indices are one-based even though most implementations use zero-based pointers internally.
