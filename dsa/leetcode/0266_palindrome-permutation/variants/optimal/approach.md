## General
**Only parity matters for mirrored pairs**

Toggle each character in a set: add it on an odd occurrence and remove it on the next occurrence. At completion the set contains exactly the characters with odd counts.

After every processed prefix, membership in the set is equivalent to having odd frequency in that prefix.

**At most one odd count can occupy the center**

Every noncentral palindrome position has a mirrored partner containing the same character, consuming occurrences in pairs. Thus all counts must be even except possibly one character assigned to the unique center of an odd-length result. This condition is also sufficient: place half of every pair on each side and put the lone odd character, if any, in the center.

## Complexity detail
One expected-constant-time toggle per character gives $O(n)$ time. At most `k` distinct characters are stored.

## Alternatives and edge cases
- **Count each character by rescanning the string:** can take $O(n^2)$.
- Empty and one-character strings qualify; character matching is case-sensitive.
