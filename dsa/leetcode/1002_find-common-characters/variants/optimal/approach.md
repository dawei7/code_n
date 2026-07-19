## General
**Track the smallest frequency seen for each letter:** Count the 26 lowercase letters in the first word. For each later word, build another 26-entry frequency array and replace every stored count with the smaller of its current value and the new word's count.

**Expand the final multiset:** After all words have been processed, the stored count for a letter is its minimum occurrence count over every word. Append that one-character string exactly that many times. Iterating letters alphabetically gives a deterministic order even though the contract accepts any order.

A character belongs to the multiset intersection exactly as many times as the least number of copies supplied by any input word. Taking componentwise minima therefore neither omits a universally available copy nor includes a copy missing from some word.

## Complexity detail
Counting scans all $S$ input characters once. Updating 26 minima for each of $W$ words costs $O(26W)$, which is bounded by $O(S)$ because every word is nonempty. The fixed-size frequency arrays use $O(1)$ auxiliary space; the returned list is output space.

## Alternatives and edge cases
- **Repeated list membership and removal:** Intersecting occurrence lists is intuitive, but removing from an array-backed list can shift many elements and lead to quadratic work per word.
- **Set intersection:** Sets discard duplicate occurrences and therefore fail the multiplicity requirement.
- **One input word:** Every character occurrence in that word belongs in the answer.
- **No common character:** Return an empty list.
- **High multiplicity:** Repeat a letter according to the minimum count, not its total count across all words.
