## General
**Index every feature before reading responses**

Create maps from each feature to its original index and to an initial popularity count of zero. Hash lookup then distinguishes exact feature words from unrelated tokens such as `"lock"` and `"locker"` in constant expected time.

**Deduplicate within each response**

Split one response into words and convert those words to a set. Visit each distinct word once; if it is a feature, increment that feature's count. The set enforces the definition that one response contributes at most one vote to a feature, regardless of repetition.

**Sort with the complete ranking key**

Sort the feature array using the pair `(-popularity, original_index)`. Negating the count places more popular features first, while the increasing original index implements the required stable tie rule explicitly rather than depending on hash-map iteration order.

Every count is incremented once for exactly those responses whose word set contains the feature, so it equals the stated popularity. The sorting key orders unequal counts descending and equal counts by their original positions. Consequently, the returned permutation satisfies both ranking rules and includes every feature once.

## Complexity detail
Splitting and deduplicating all responses examines $W$ word occurrences in $O(W)$ expected time. Sorting $F$ features takes $O(F\log F)$ time, for $O(W+F\log F)$ total. The feature maps use $O(F)$ space, and the temporary set for one response uses at most $O(U)$ space.

## Alternatives and edge cases
- **Scan every response for every feature:** This is correct but can take $O(FW)$ time and repeatedly tokenize the same text.
- **Count raw word occurrences:** A global frequency counter is incorrect because repeated mentions within one response must count only once.
- **Stable sort by count alone:** This works in languages guaranteeing stable sorting, but an explicit original index makes the tie contract portable and visible.
- **Repeated mention in one response:** It contributes one popularity point, not the repetition count.
- **Exact words only:** A feature is not mentioned merely because it is a substring of another response word.
- **No mentioned features:** Every count stays zero and the original feature order is returned.
- **Equal positive popularity:** Original order still breaks the tie.
- **Response with unrelated words:** Those tokens are ignored after the hash lookup.
