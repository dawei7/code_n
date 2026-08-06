## General
**Whitespace-aware splitting performs normalization during extraction**

Call `s.split()` without a literal separator. It returns every maximal non-space word in original order while discarding leading and trailing spaces and omitting empty fields from repeated internal spaces. In contrast, `split(" ")` would retain empty strings between adjacent separators.

Reverse the extracted word sequence, not the characters inside each word, then join with one literal space. `join` inserts separators only between words, so it simultaneously guarantees exactly one internal space and no leading or trailing space.

The split sequence contains every source word exactly once and no separator artifacts. Reversing changes only word positions, and joining changes only normalized separators, so the result preserves all word content in precisely the required reverse order.

## Complexity detail
Let $n = \lvert s\rvert$. Splitting and joining inspect or copy a linear total number of characters, while reversed iteration visits the word references once, giving $O(n)$ time. The extracted word list and immutable returned string use $O(n)$ space.

## Alternatives and edge cases
- **Manual two-pointer scan:** offers explicit control and is useful for mutable buffers, but is more code than Python's whitespace-aware split requires.
- **Reverse all characters and then each word:** can meet the in-place follow-up with mutable storage, whereas Python strings still require allocation.
- **Literal `split(" ")`:** produces empty fields for repeated spaces and therefore does not normalize correctly by itself.
- A one-word string returns that word without surrounding spaces.
- Arbitrarily long legal space runs collapse to one separator.
- The source guarantees at least one word; broader all-whitespace input would naturally yield an empty string with this implementation.
