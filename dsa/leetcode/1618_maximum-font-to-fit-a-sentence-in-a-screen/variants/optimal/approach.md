## General
**Compress repeated metric queries.** Count how often each character appears in `text`. For a candidate font, request each distinct character width once, multiply it by that character's frequency, and sum the products. This produces exactly the sentence width while using at most $\sigma$ width queries instead of one query per character. Reject immediately when the font height exceeds `h`.

**Exploit monotone fit across the available sizes.** Both height and every character width are non-decreasing with font size. Therefore the predicate “this font fits within `w` and `h`” is true for an initial prefix of `fonts` and false thereafter. Binary-search that boundary. When the middle font fits, record it and search to the right; otherwise search to the left.

At termination, every font to the right of the recorded answer has been excluded directly or by monotonicity, while the recorded font passed both exact dimension checks. If no middle font ever fits, the initialized answer `-1` correctly represents an empty feasible prefix.

## Complexity detail
Building the frequency map takes $O(n)$ time and $O(\sigma)$ space. Binary search tests $O(\log f)$ fonts, with one height query and at most $\sigma$ width queries per test, for $O(n+\sigma\log f)$ total time. The interface-call count is also $O((\sigma+1)\log f)$.

## Alternatives and edge cases
- **Scan fonts from smallest to largest:** Reusing character frequencies gives $O(n+\sigma f)$ time, but ignores the monotone boundary and may query every font.
- **Query every character occurrence:** Width summation without frequency compression takes $O(n\log f)$ calls and can exceed the interactive query budget on repeated text.
- **Scan fonts from largest downward:** This may find the answer early, but in the worst case no font fits and all $f$ sizes are tested.
- A font whose dimensions equal `w` or `h` still fits because both limits are inclusive.
- A height failure is sufficient to reject a font without making any width queries.
- The answer is an available font value, not its index in `fonts`.
- If the smallest font fails, monotonicity proves that the correct result is `-1`.
