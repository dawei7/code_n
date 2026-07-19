## General
**Expose word boundaries once:** Split `text` on its guaranteed single spaces. This produces the words in their original order without empty tokens.

**Inspect each possible triple:** For every index `i` from zero through `len(words) - 3`, compare `words[i]` with `first` and `words[i + 1]` with `second`. When both match, append `words[i + 2]`. Overlapping occurrences are handled because the index advances by one rather than skipping past a match.

Every appended word follows a matching adjacent pair by the two comparisons. Conversely, every valid three-word occurrence begins at one inspected index, so its third word is appended exactly once and in sentence order.

## Complexity detail
Splitting and scanning process $N$ characters in $O(N)$ time. The word list and returned strings require $O(N)$ space in total. There are $W-2$ candidate triples when $W \ge 3$.

## Alternatives and edge cases
- **Regular expression:** A lookahead can capture overlapping matches, but careful word boundaries and escaping make it less direct than token scanning.
- **Repeated prefix reconstruction:** Rebuilding or rescanning a prefix for every candidate remains correct but can take quadratic time.
- **Fewer than three words:** No word can follow a complete bigram, so the answer is empty.
- **Bigram at the end:** A final `first second` pair contributes nothing because no `third` word follows it.
- **Overlapping matches:** A reported third word may also begin the next matching bigram and must not be skipped.
- **Repeated output words:** Preserve every occurrence; do not deduplicate the result.
