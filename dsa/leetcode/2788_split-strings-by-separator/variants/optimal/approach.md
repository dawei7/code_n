## General

Process `words` from first to last. For each word, split it using the supplied `separator`; the language's string split operation returns the maximal substrings between delimiter occurrences in their left-to-right order. Append each non-empty substring to one result list.

**Why filtering after each split is sufficient**

A leading separator creates an empty first piece, a trailing separator creates an empty last piece, and consecutive separators create empty pieces between them. These are the only way empty pieces arise because every input word itself is non-empty. Testing each piece before appending therefore removes exactly the forbidden results without changing any valid text.

Each accepted piece is appended while its source word is being visited. The algorithm consequently preserves both orders that matter: pieces remain ordered within a word, and all pieces of an earlier word precede those of a later word. Since splitting removes the chosen delimiter and no other character is modified, the accumulated list is exactly the required output.

## Complexity detail

Let $S$ be the total number of characters across all strings in `words`. Splitting and inspecting every character takes $O(S)$ time. The returned strings and result list contain at most $O(S)$ total data, so the space complexity including the output is $O(S)$.

## Alternatives and edge cases

- **Nested list comprehension:** Flatten the per-word splits and filter falsey pieces in one expression. It has the same $O(S)$ bounds, but the explicit loops make the ordering and empty-piece rule easier to inspect.
- **Manual character scan:** Build each piece character by character and flush it at a separator. This avoids temporary split lists but requires more boundary bookkeeping and still takes $O(S)$ time.
- **Repeated prefix rebuilding:** Creating a fresh list and explicitly copying every previously collected piece before adding the next one is correct, but it requires quadratic work in the number of emitted pieces.
- **Leading, trailing, and adjacent separators:** All create empty split pieces, and every such piece must be discarded.
- **Other punctuation:** Only the selected `separator` divides a word; any other allowed punctuation remains part of its piece.
- **No non-empty pieces:** If every word consists only of separators, return an empty list.
