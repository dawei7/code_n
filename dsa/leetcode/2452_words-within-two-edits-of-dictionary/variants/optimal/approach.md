## General

Changing characters does not alter their positions, and all words have equal length. Therefore, the minimum edits needed to turn one word into another are exactly their Hamming distance: the number of positions containing different letters.

Process queries in their given order. For each query, compare it with each dictionary word and count mismatched positions. Stop that pairwise comparison immediately when a third mismatch appears, because later positions cannot make it qualify. If a comparison finishes with at most two mismatches, append the query once and stop checking further dictionary words.

Every appended query has an explicit dictionary witness at distance at most 2, so it is valid. Conversely, a query is omitted only after every dictionary comparison has found at least three mismatches, proving that no allowed sequence of two substitutions can create a match. Appending during the original scan also preserves the required order.

## Complexity detail

Let $Q=\lvert\texttt{queries}\rvert$, $D=\lvert\texttt{dictionary}\rvert$, and $n$ be the shared word length. In the worst case every query-dictionary pair requires all $n$ character comparisons, giving $O(QDn)$ time.

Apart from the returned list, the scan stores only counters and current references, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Wildcard signatures:** Indexing dictionary words by patterns with one or two omitted positions can accelerate repeated lookup, but creates many signatures and is unnecessary under the bounds.
- **Trie traversal with an edit budget:** A trie can explore matching and substituted edges, though branching and implementation overhead outweigh its benefit for at most 100 dictionary words.
- **Recompute prefix distances:** Recounting all mismatches from the beginning at every position is correct but takes $O(QDn^2)$ time.
- **Exact match:** A Hamming distance of zero qualifies because the limit is at most two edits.
- **Exactly two mismatches:** The boundary value qualifies; only the third mismatch permits rejection.
- **One-character words:** Every query is within one edit of every dictionary word, so all queries qualify.
- **Multiple witnesses:** A query appears only once even if several dictionary words are close enough.
- **Query order and duplicates:** The scan preserves every qualifying occurrence in the same order supplied.
