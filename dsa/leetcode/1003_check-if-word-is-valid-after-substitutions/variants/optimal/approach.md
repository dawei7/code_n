## General
**Reverse insertions by deleting completed triples:** If a string was created by inserting `"abc"`, reversing the final insertion removes some contiguous `"abc"`. Repeatedly removing such triples must eventually produce the empty string. A stack performs these removals online without rescanning earlier characters.

**Reduce as soon as a suffix becomes `"abc"`:** Append each input character to the stack. Whenever the final three entries are `'a'`, `'b'`, and `'c'`, pop all three. This immediate reduction is safe: those characters form a complete inserted block, and removing it exposes exactly the surrounding text that existed before that insertion.

Every reduction corresponds to reversing a legal insertion. If the stack is empty after the scan, reversing the reductions constructs `s` from the empty string. If characters remain, no sequence of legal reverse operations can eliminate them, so the string is invalid.

## Complexity detail
Each of the $N$ characters is pushed once and popped at most once. The scan therefore takes $O(N)$ time, and the unreduced stack can contain $O(N)$ characters.

## Alternatives and edge cases
- **Repeated string replacement:** Removing one or all visible `"abc"` substrings in repeated full-string passes is correct but can take $O(N^2)$ time for deeply nested insertions.
- **Character counts alone:** Equal numbers of `'a'`, `'b'`, and `'c'` are necessary but do not enforce the required nesting and order.
- **Single `"abc"`:** It reduces directly to the empty stack and is valid.
- **Length not divisible by three:** Such a string cannot consist entirely of inserted triples.
- **Premature `'b'` or `'c'`:** It remains unreduced unless a valid `"abc"` suffix is formed in the correct order.
