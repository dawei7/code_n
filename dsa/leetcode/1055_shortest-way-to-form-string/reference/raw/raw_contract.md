## Function Contract

**Inputs**

- `source`: a nonempty string of lowercase English letters.
- `target`: a nonempty string of lowercase English letters.

Each selected piece may delete different characters from a fresh use of `source`, but every retained piece must preserve `source` order. Their concatenation must equal all of `target` exactly.

**Return value**

- The smallest number of subsequences of `source` whose concatenation is `target`, or `-1` when construction is impossible.
