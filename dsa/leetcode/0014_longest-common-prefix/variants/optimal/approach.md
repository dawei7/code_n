## General
**Keep only the surviving prefix length**

Use the first string as the prefix candidate and keep an integer `common` denoting how many of its leading characters are still known to match every processed string. For each subsequent word, compare from index zero only while the index is below both `common` and that word's length. Replace `common` with the number of successful comparisons.

Delay slicing until the end. This avoids constructing and repeatedly trimming intermediate prefix strings.

**Intersect the candidate with each new word**

Before a word is processed, `strs[0][:common]` is exactly the longest common prefix of all earlier words. Comparing it with the new word finds exactly their shared initial segment. Any character beyond the first mismatch can never return to the common prefix, so reducing `common` preserves the invariant.

If `common` becomes zero, no later word can create a shared prefix and the result can be returned immediately.

**Trace how the candidate can only shrink**

Begin `flower`, `flow`, `flight` with `common = 6`. Comparing `flow` reduces it to 4. Comparing only the first four positions with `flight` matches `f` and `l`, then differs at index 2, so `common = 2` and the result is `fl`.

**Why the shrinking prefix remains maximal**

Before a new string is considered, the retained length describes the longest prefix shared by every earlier string. Comparing that prefix with the new string keeps exactly their common initial segment. Anything removed fails in the new string, while anything beyond the old boundary had already failed among earlier strings.

The updated prefix is therefore both shared by the enlarged collection and impossible to extend. Repeating this intersection across all strings leaves the unique longest common prefix, not merely some prefix that happens to work.

## Complexity detail
Let `S` be the total number of characters across all input strings. A word is compared only up to its length and the current candidate length, so total comparisons are $O(S)$. Apart from the returned slice, only indices are stored.

## Alternatives and edge cases
- **Repeated `startswith` while trimming:** compact, but adversarial long near-matches can rescan the same prefix characters and become quadratic.
- **Sort the strings:** only the lexicographic minimum and maximum then need comparison, but sorting costs $O(k \log k)$ string comparisons and may mutate input.
- **Trie:** useful when many prefix queries reuse the same corpus, but allocates storage proportional to all characters for a single query.
- A single input string is its own longest common prefix. If an empty string occurs, the answer becomes empty immediately.
- Character comparison is case-sensitive unless the surrounding challenge contract explicitly normalizes case.
