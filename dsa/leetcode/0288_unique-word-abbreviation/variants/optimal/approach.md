## General
**Canonicalize the abbreviation once**

Words of length two or less abbreviate to themselves. Longer words use first character, number of omitted middle characters, and last character.

**Record identity, not occurrence count**

For each abbreviation, store its sole distinct word while all insertions agree. If a different word shares it, mark the abbreviation ambiguous.

Each map value is either the only distinct dictionary word with that abbreviation or an ambiguity marker representing at least two distinct words.

**Absence or matching identity is exactly uniqueness**

If an abbreviation is absent, no dictionary word conflicts with the query. If it maps to the query word itself, repeated occurrences still represent only that identity and also cause no conflict. A stored different word or ambiguity marker proves that some distinct dictionary word shares the abbreviation. These cases exhaust the definition of uniqueness.

## Complexity detail
Building scans total dictionary characters `c`; each query abbreviation and hash lookup is constant relative to its word length, for total query characters `q`. The map stores at most one entry per distinct abbreviation.

## Alternatives and edge cases
- **Scan the dictionary for every query:** takes $O(cq)$ in aggregate.
- Empty dictionaries accept every query; short words remain uncompressed; duplicate dictionary entries count as one identity.
