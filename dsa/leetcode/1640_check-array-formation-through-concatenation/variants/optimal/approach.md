## General
**The next target value identifies at most one piece.** Because all flattened piece values are distinct, no two pieces can begin with the same integer. Build a map from each piece's first value to the complete piece. This converts choosing the next piece from a search into a direct lookup.

**Consume the target from left to right.** At target index `i`, `arr[i]` must be the first value of whichever piece appears next in a valid concatenation. Look up that piece and compare it with the target slice beginning at `i`. If no piece starts there or any internal value disagrees, no alternative piece can repair the mismatch, so return `false`. Otherwise advance by the entire piece length and repeat.

Reaching the end proves that the encountered pieces concatenate to `arr`. Since both sides contain $n$ distinct values in total, the successful scan cannot silently omit or reuse a piece: every target value is consumed once, and each matched piece is uniquely identified by its first value.

## Complexity detail
Building the first-value map visits each piece once. Across the scan, slice comparisons examine each of the $n$ target positions once because matched pieces do not overlap. Total time is $O(n)$, and the piece map uses $O(n)$ space in the maximum case of singleton pieces.

## Alternatives and edge cases
- **Search every remaining piece:** At each target boundary, scanning the full collection for a matching first value is correct but can take $O(n^2)$ time when many pieces are singletons.
- **Sort pieces by target positions:** A target-value-to-index map can order pieces by their first values, after which flattening and comparison works in $O(n\log n)$ time; sorting is unnecessary.
- **Try all piece permutations:** Permutation search ignores the distinct first-value property and grows factorially.
- A single piece succeeds only when its complete internal order equals `arr`.
- Singleton pieces may appear in any collection order because their concatenation order is chosen freely.
- Matching the first value is insufficient; every later value in that piece must match the consecutive target segment.
- The equal total lengths mean a successful complete scan uses all supplied values; no optional piece may be discarded.
- Distinctness is global across all flattened pieces, so first-value lookups are unambiguous.
