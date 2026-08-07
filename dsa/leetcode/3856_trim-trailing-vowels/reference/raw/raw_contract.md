## Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

Let $j$ be the largest index whose character is not one of `a`, `e`, `i`, `o`, or `u`. If no such index exists, no character belongs to the retained prefix.

Only the contiguous vowel suffix after $j$ is removed. A vowel at or before a later consonant is not trailing and must remain.

**Return value**

Return `s[:j + 1]` when a non-vowel exists, or the empty string when all characters are vowels.
