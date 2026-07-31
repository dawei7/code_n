## General

**Represent each case with one bit per letter.** English letters form a fixed alphabet of 26 possibilities. Use one integer mask for lowercase appearances and another for uppercase appearances. When a character is lowercase, convert its offset from `a` into a bit position and set that bit in the lowercase mask. Do the analogous operation relative to `A` for uppercase characters. Setting an already-set bit changes nothing, which naturally prevents duplicates from being counted more than once.

**Intersect the two presence sets.** Bit $i$ is set in both masks exactly when the corresponding letter appears in both lowercase and uppercase. A bitwise AND retains precisely those shared bits, and the population count of the result is therefore the number of special letters. Every input character updates the correct presence mask, so after the scan the intersection contains all and only the letters required by the definition.

## Complexity detail

Let $n$ be the length of `word`. The scan processes each character once, and the final operations are on fixed-width 26-bit masks, so the time complexity is $O(n)$. The two integer masks use $O(1)$ auxiliary space because the alphabet size is fixed.

## Alternatives and edge cases

- **Two character sets:** Store every lowercase and uppercase character separately, then count lowercase letters whose uppercase form is present. This is also $O(n)$ time and $O(1)$ space under the fixed alphabet, but the two masks encode the same state more compactly.
- **Pairwise character search:** For every occurrence, scan the whole string for its opposite case and deduplicate successful letters. It is correct but can take $O(n^2)$ time.
- **Single case only:** A letter appearing repeatedly in lowercase or repeatedly in uppercase is not special without its other case.
- **Duplicate pairs:** Any number of occurrences of the same two cases contributes exactly one because the requested count is over distinct letters.
- **Alphabet endpoints:** Offsets for `a`/`A` and `z`/`Z` map to bit positions 0 and 25 without special handling.
