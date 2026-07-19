## General
**Count the supply before consuming it**

The strings contain only lowercase English letters, so a fixed array of 26 counters represents the available magazine characters. Scan `magazine` and increment the counter at `ord(character) - ord("a")`.

**Consume one occurrence for each requirement**

Scan `ransom_note` and inspect the corresponding supply counter. If it is zero, every available occurrence of that character has already been used, so construction is impossible. Otherwise decrement it to reserve exactly one occurrence for the current position.

**Why completing the scan is sufficient**

Each decrement pairs one ransom-note occurrence with a distinct magazine occurrence of the same character. The algorithm returns early precisely when such a pairing is unavailable. Therefore, if every required character is processed, all positions have disjoint matching supplies and the note can be constructed.

## Complexity detail
Let `r` and `m` be the lengths of `ransom_note` and `magazine`. Each string is scanned once, for $O(r + m)$ time. The 26 counters occupy constant space because the alphabet size does not grow with the inputs.

## Alternatives and edge cases
- **Hash-map or Counter comparison:** expresses multiplicity directly and remains $O(r + m)$, but its storage scales with the number of distinct characters in a general alphabet.
- **Sort both strings:** can compare grouped characters but costs $O(r \log r + m \log m)$ time.
- **Search and remove per character:** is straightforward but repeated linear searches or string rebuilding can take $O(rm)$ time.
- An empty ransom note can always be constructed.
- A shorter magazine cannot supply a longer ransom note.
- Repeated letters must be counted by occurrence, not merely checked for membership.
- Extra magazine characters do not affect a successful result.
