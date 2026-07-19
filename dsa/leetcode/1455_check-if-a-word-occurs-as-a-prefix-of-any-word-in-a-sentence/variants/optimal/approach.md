## General
**Visit only word starts**

Keep `start`, the character index of the current word, and a 1-based
`word_index`. The first word begins at zero. Find the next space to locate the
current word's exclusive end; if no space remains, the sentence length is the
end of the final word.

Compare `searchWord` with `sentence` beginning exactly at `start`, but only
when the current word is at least as long as the search string. This boundary
condition prevents a match from continuing through the separating space. It
also ensures that an occurrence in the middle of a word is never considered.

**Return immediately on the first match**

Words are visited from left to right. The first successful prefix comparison
therefore has the minimum possible 1-based word index, so return it immediately.
If the word does not match, move `start` to the character after its following
space and increment `word_index`. Exhausting the sentence without returning
proves that no word has the prefix, so return `-1`.

**Why the scan implements the definition exactly**

At every iteration, `start` is the first character of precisely the word named
by `word_index`, because it is initially zero and later moves only to the
character following a separator. The length check and `startswith` comparison
are true exactly when the complete `searchWord` occupies that word's leading
characters. Thus every returned index is valid. Every word start is examined
in increasing order, so no earlier valid word can be missed, and reaching the
end establishes that none exists.

## Complexity detail
Let $N$ be the sentence length. Searches for successive spaces cover disjoint
portions of the sentence. Prefix comparisons inspect characters within their
respective words, so total work is $O(N)$. The scan retains only indices and an
end position, using $O(1)$ auxiliary space without materializing a word list.

## Alternatives and edge cases
- **Split then enumerate:** `sentence.split()` followed by `startswith` is a
  concise $O(N)$ solution, but it allocates $O(N)$ storage for the word list.
- **General substring search:** Finding `searchWord` anywhere and then checking
  boundaries can inspect irrelevant middle-of-word occurrences and complicate
  selection of the first word index.
- **First word matches:** Return `1` immediately.
- **Several words match:** Return the earliest index, not the total count or
  the last match.
- **Whole word equality:** A word is a prefix of itself, so equality qualifies.
- **Search word longer than a candidate:** That candidate cannot match; do not
  compare across its following space.
- **Middle occurrence:** In `"hamburger"`, `"burger"` is not a prefix.
- **Single-word sentence:** Test that one word and return either `1` or `-1`.
- **No match:** Return the integer `-1` exactly.
