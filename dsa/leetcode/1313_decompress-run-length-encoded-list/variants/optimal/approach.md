## General
**Expand each pair directly into the result**

Visit even indices `0, 2, 4, ...`. At index `i`, create `nums[i]` copies of `nums[i + 1]` and extend the result list with that run. Appending each run to the same list preserves the pair order without revisiting any earlier output.

Every encoded pair is processed exactly once. For a pair `[freq, val]`, the method appends exactly `freq` copies of `val`; therefore, after processing the first $k$ pairs, the result equals the concatenation specified by those $k$ pairs. Extending this argument through all pairs proves the final list is the required decompression.

## Complexity detail
Reading the $n/2$ pairs takes $O(n)$ and materializing exactly $S$ output values takes $O(S)$, for $O(n+S)$ time. The returned list contains $S$ elements and uses $O(S)$ space; only constant state is used besides the output.

## Alternatives and edge cases
- **Repeated list concatenation:** Rebuilding the complete result for every run is correct, but copies all prior output repeatedly and can take quadratic time as the number and size of runs grow.
- **Element-by-element append:** Nested loops appending one value at a time have the same $O(n+S)$ bound and avoid constructing a temporary run list.
- **Frequency one:** The value appears exactly once; frequencies are never zero under the source contract.
- **Repeated adjacent values:** Separate pairs with the same value may remain separate in the encoding but become one visually continuous run in the output.
- **Maximum frequency:** A frequency of 100 contributes 100 copies while still using the same direct expansion rule.
- **Pair order:** Sorting or grouping encoded pairs would change the required decompressed list and is not allowed.
