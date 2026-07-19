## General
**Recognize only at an ampersand.** An entity can begin only where the current character is `&`. At such a position, compare the remaining input with the six fixed entity spellings. When one matches, append its decoded character and advance past the whole spelling. If none matches, copy the ampersand and advance once.

All non-ampersand characters are copied directly. Each step therefore either consumes one input character or consumes one complete recognized entity. Because the parser's index always advances over original input, an output `&` created from `&amp;` is never reconsidered. This is why `&amp;gt;` becomes `&gt;`, rather than `>`.

The fixed lookup table contains every recognized spelling and no others. A matched span is replaced exactly as required; an unmatched position is copied unchanged. Processing disjoint spans from left to right therefore produces precisely the requested parse.

## Complexity detail
Let $n$ be the length of `text`. At most six constant-length spellings are checked at any ampersand, so the scan takes $O(n)$ time. The result buffer can contain $O(n)$ characters and therefore uses $O(n)$ space.

## Alternatives and edge cases
- **Chained global replacements:** Repeated `replace` calls are concise, but replacement order can incorrectly decode newly produced text such as `&amp;gt;`.
- **Find the next semicolon:** Extracting candidate tokens into a hash map also works, provided unknown or incomplete tokens remain unchanged and the scan never skips a later valid ampersand.
- **Unknown entity:** Text such as `&ambassador;` must be copied exactly.
- **Incomplete spelling:** A trailing `&amp` has no semicolon and is not decoded.
- **Adjacent entities:** Each complete spelling is consumed independently without inserting separators.
- **Nested-looking text:** Decoding happens once against the original character stream.
