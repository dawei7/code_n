## General

Every substring start is a position in `s`, and the validity rule assigns a different character to each such position. Therefore, no valid partition can have more pieces than the number of distinct characters present in the string.

That upper bound is always attainable. The first piece necessarily begins at index zero. For every other distinct character, cut immediately before its first occurrence; order these first-occurrence positions from left to right. Each new piece begins with a character not used by an earlier piece, while the intervals between cuts remain nonempty and together cover the complete string. Hence the maximum number of pieces equals the number of distinct characters in `s`.

Scan the string once and record its seen letters. A 26-bit mask is sufficient: set the bit for each character, then count the set bits.

## Complexity detail

Let $n$ be the string length. The scan takes $O(n)$ time. Because the input alphabet contains exactly 26 lowercase letters, the bit mask occupies $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Hash set:** Inserting every character and returning the set size is equally linear; the set is still bounded by 26 entries.
- **Rescan every earlier prefix:** Testing whether each character appeared before without storing seen state is correct but can take $O(n^2)$ time.
- **Enumerate every partition:** Trying all $2^{n-1}$ choices of cut boundaries is correct but exponential and unnecessary once the upper-bound construction is recognized.
- **Repeated characters:** Later copies do not create additional possible starting letters, though they may appear anywhere inside a piece.
- **First character:** Its first occurrence is already position zero, so it accounts for the initial piece without an added cut.
- **Single-character string:** Its only complete partition has one piece, matching one distinct character.
- **All 26 letters:** Cutting before each first occurrence attains the alphabet-wide maximum of 26 pieces.
