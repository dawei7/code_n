## General
**Map each letter to its keyboard row**

Build one lookup from every lowercase keyboard letter to row index zero, one, or two. This turns a row-membership question into a constant-time lookup.

**Use the first letter as the required row**

For each word, lowercase its first letter and record that row. The word qualifies only if every remaining lowercase letter maps to the same row. Append the original word rather than the normalized copy.

**Why this test is sufficient**

If every letter's row equals the first letter's row, all letters share one row and the word is valid. If any row differs, no single keyboard row can contain both that letter and the first, so the word must be rejected.

## Complexity detail
Let `c` be the total number of characters across all words. Each character is normalized and checked once, so time is $O(c)$. The fixed 26-letter lookup is $O(1)$ auxiliary space; the returned words and lowercase temporary strings use up to $O(c)$ space.

## Alternatives and edge cases
- **Three row sets:** convert each word to a lowercase set and test whether it is a subset of any keyboard-row set; this is also linear.
- **Compare every character pair:** is correct but can take quadratic time for a long word.
- **Regular expressions:** one pattern per keyboard row works, but is less explicit and adds matching overhead.
- **Mixed case:** normalize only for membership and preserve the original word in the result.
- **Single letter:** always belongs to exactly one row.
- **Repeated letters:** remain valid when their row matches.
- **Input order:** filtering must not sort qualifying words.
