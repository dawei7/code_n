## General
**Every symmetric contribution is a matching pair**

Maintain a set of character kinds that currently have one unmatched occurrence. When a character is absent, insert it. When it is present, remove it and add two to the usable length; those two copies can occupy mirrored positions.

**Reserve at most one center**

After all occurrences are processed, a nonempty unmatched set means at least one odd leftover occurrence exists. A palindrome can use exactly one such character at its center, so add one regardless of how many unmatched kinds remain.

**Why greedy pairing loses nothing**

Every palindrome position outside the center must be paired with the same character on the opposite side. Taking every available pair is always beneficial and pairs of different characters do not compete. Conversely, no construction can use more than `floor(count / 2)` pairs of a character or more than one unpaired center, so the computed length is an upper bound that is achievable.

**Keep letter case distinct**

Uppercase and lowercase letters represent different character kinds. The set uses the original characters as keys, ensuring `"A"` cannot pair with `"a"`.

## Complexity detail
Each of the `n` characters triggers one constant-time expected set operation, for $O(n)$ time. At most 52 English letter kinds can remain unmatched, so space is $O(1)$ under the fixed alphabet.

## Alternatives and edge cases
- **Frequency array or counter:** sum the even part of every count and add one if any count is odd; it has the same bounds.
- **Sort the characters:** makes pairs adjacent but costs $O(n \log n)$ time.
- **Search explicitly for one unused mate per occurrence:** is correct but can take $O(n^2)$ time.
- A one-character string forms a palindrome of length one.
- Several odd counts contribute only one center character.
- All-even counts use every character.
- Uppercase and lowercase occurrences do not pair.
