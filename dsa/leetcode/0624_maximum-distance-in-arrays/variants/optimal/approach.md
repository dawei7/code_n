## General
**Only endpoints can be globally extreme**

Because each array is sorted, its first value is its minimum and its last value is its maximum. Any largest cross-array absolute difference must pair one array's minimum with another array's maximum; interior values cannot improve either endpoint.

**Keep extremes from earlier arrays**

Initialize `minimum` and `maximum` from the first array. For each later array, compare its maximum with the earlier minimum and compare its minimum with the earlier maximum. These two candidates cover both possible orientations of a cross-array extreme.

**Compare before updating**

Only after evaluating both candidates should the current endpoints extend the running `minimum` and `maximum`. This ordering guarantees that every candidate uses the current array on one side and a strictly earlier array on the other, so the forbidden same-array pair is never considered.

**Why one pass covers the optimum**

Take an optimal pair and consider whichever of its two arrays is processed later. When that later array is scanned, the earlier array's relevant endpoint is already represented by the running extreme. The algorithm evaluates a candidate at least as large as that optimal pair, while every evaluated candidate is legal, so the recorded maximum is exact.

## Complexity detail
Let `M` be the number of arrays. Reading two endpoints and performing constant work per array takes $O(M)$ time, independent of the total number of interior elements. The running extrema and answer use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Compare every pair of arrays:** evaluate their endpoint combinations directly; it is correct but costs $O(M^2)$ time.
- **Track the two global minima and maxima with source indices:** also solves the different-array restriction, but requires more state and tie handling than the streaming comparison.
- **Flatten and sort all values:** loses source identity unless every value retains its array index and also processes irrelevant interior values.
- The global minimum and maximum may belong to the same array; comparing before updating prevents using that illegal distance.
- Single-element arrays have the same minimum and maximum and need no special handling.
- Equal values across all arrays produce distance zero.
- Negative values work unchanged because the two directed endpoint differences are nonnegative candidates.
