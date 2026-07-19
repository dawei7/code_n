## General
**Maintain the active line**

Begin with one line of width zero. For each character, use its alphabet index to retrieve the width. If adding it would exceed 100, start a new line whose initial width is that character's width; otherwise, add it to the current line.

The two maintained values describe the layout of the processed prefix. When the next character fits, appending it preserves that layout. When it does not, the writing rule requires a line break immediately before that character, and the update creates exactly that next line. Induction over the string makes the final line count and width exact.

**Preserve exact capacity**

The comparison must be `current_width + character_width > 100`. Equality means the character still fits, so using `>=` would create an extra line for exact fills.

## Complexity detail
For a string of length `n`, each character causes one table lookup and constant arithmetic, giving $O(n)$ time. The width table belongs to the input, and the scan stores only two counters, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Accumulate then subtract overflow:** Add each width first and, when the total exceeds 100, increment the line count and reset to the current character; this is equivalent when the overflowing character is retained correctly.
- **Re-layout every prefix:** Simulating the string again for each growing prefix is correct but takes $O(n^2)$ time.
- **Build physical line strings:** Grouping characters into strings uses unnecessary $O(n)$ storage when only counts and widths are needed.
- **Exact width 100:** Keep the character on the current line.
- **First character:** It always occupies the initially counted first line.
- **Single character:** Return one line and that character's width.
- **Width lookup:** Index by `ord(character) - ord('a')` so the supplied alphabet-order table is respected.
