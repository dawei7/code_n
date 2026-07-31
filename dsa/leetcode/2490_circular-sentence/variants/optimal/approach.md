## General

**Every required comparison is visible at a boundary.** At an internal word boundary, the sentence contains the earlier word's final character, then a space, then the next word's first character. Thus a space at index `i` is valid exactly when `sentence[i - 1] == sentence[i + 1]`. The input guarantees single separators and no leading or trailing spaces, so both neighboring indices always exist.

The only boundary not represented by a space is the cycle's closing edge. Check `sentence[-1] == sentence[0]` first. Then scan the string and test the two characters surrounding every space. If any comparison fails, the sentence cannot be circular; if the wraparound and all internal boundaries pass, every condition in the definition has been verified.

This direct scan is also correct for a one-word sentence: there are no spaces to inspect, and the wraparound comparison checks whether that word ends with its starting character.

## Complexity detail

Let $n = \lvert\texttt{sentence}\rvert$. The algorithm scans the sentence once, taking $O(n)$ time, and stores only an index and the current character, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Split into words:** Comparing `words[i][-1]` with the next word's first character is clear and remains $O(n)$ time, but it allocates $O(n)$ additional storage for the split representation.
- **Repeatedly split or rescan:** Rebuilding the word list for each boundary is correct but can take $O(n^2)$ time.
- **Single word:** Only its last and first characters are compared; a one-character word is always circular.
- **Case sensitivity:** Uppercase and lowercase forms of the same letter are different and must not be normalized.
- **Wraparound failure:** Matching all spaces is insufficient when the last sentence character differs from the first.
- **Early internal failure:** Returning immediately is safe because one mismatched adjacent pair disproves circularity.
