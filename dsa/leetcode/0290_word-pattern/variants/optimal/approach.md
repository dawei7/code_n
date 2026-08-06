## General
**A pattern match requires a bijection, not one map**

Split the sentence into words and reject it immediately if the number of words differs from the number of pattern
characters. Scan the aligned character-word pairs once while maintaining both a character-to-word map and a
word-to-character map.

For each pair, an existing forward mapping must name the current word, and an existing reverse mapping must name the
current character. If both checks pass, assign the pair in both maps. After every processed position, the two maps are
inverses over all pairs seen so far.

**The inverse maps enforce both directions**

A forward conflict would assign two words to one pattern character; a reverse conflict would assign one word to two
characters. Rejecting both kinds makes the relation one-to-one and consistent. Conversely, if every aligned pair
passes, both occurrences of every character-word association agree, so the complete sequences follow the required
bijection.

## Complexity detail
Let $n$ be the combined number of characters in `pattern` and `s`. Splitting and scanning consume $O(n)$ time, and
the expected total cost of hashing the words is also $O(n)$. The word list and the two maps retain at most $O(n)$
characters and references, so the auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Pairwise consistency checks:** comparing every pair of positions is correct but takes quadratic time.
- **One directional map:** misses the case where two different pattern characters map to the same word.
- **Length mismatch:** fails before `zip` could silently discard unmatched characters or words.
- **Repeated association:** repeating both a character and its established word is valid and leaves the maps
  unchanged in meaning.
