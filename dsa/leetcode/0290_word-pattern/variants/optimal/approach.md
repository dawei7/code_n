## General
**A pattern match requires a bijection, not one map**

Split the sentence and reject a length mismatch. For each character-word pair, require any existing character mapping to match the word and any existing word mapping to match the character; otherwise install both mappings.

After every processed position, the two maps are inverses over all character-word pairs seen so far.

**The inverse maps enforce both directions**

A forward conflict would assign two words to one pattern character; a reverse conflict would assign one word to two characters. Rejecting both kinds makes the relation one-to-one and consistent. If every aligned pair passes and the sequence lengths match, the two maps form exactly the required bijection over all positions.

## Complexity detail
Each of `n` positions performs expected-constant-time hash operations, and at most `k` distinct mappings are stored.

## Alternatives and edge cases
- **Compare first-occurrence indices by rescanning:** can take $O(n^2)$.
- A word-count mismatch fails immediately; repeating both the character and its word is valid.
