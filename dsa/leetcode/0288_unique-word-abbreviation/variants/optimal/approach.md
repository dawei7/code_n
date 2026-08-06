## General

**Canonicalize the abbreviation once**

Words of length two or less abbreviate to themselves. Longer words use the first character, number of omitted middle
characters, and last character.

**Record identity, not occurrence count**

For each abbreviation, store its sole distinct word while all insertions agree. If a different word shares it, store
`None` as an ambiguity marker.

Each map value is therefore either the only distinct dictionary word with that abbreviation or an ambiguity marker
representing at least two distinct words. Repeated copies of the same word leave the sole identity unchanged.

**Absence or matching identity is exactly uniqueness**

If an abbreviation is absent, no dictionary word conflicts with the query. If it maps to the query word itself,
repeated occurrences still represent only that identity and also cause no conflict. A stored different word or
ambiguity marker proves that some distinct dictionary word shares the abbreviation. These cases exhaust the definition
of uniqueness. The app candidate constructs this object as `validator` and applies the same lookup to every query.

## Complexity detail

Let

$$
c = \sum_{w \in \texttt{dictionary}} \lvert w \rvert
\qquad\text{and}\qquad
q = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

Building the abbreviation map takes $O(c)$ time, and all query abbreviations and lookups take $O(q)$ time, for
$O(c + q)$ overall. The map stores at most one abbreviation and one word reference per distinct key, bounded by $O(c)$
space.

## Alternatives and edge cases

- **Scan the dictionary for every query:** takes $O(cq)$ in aggregate.
- **Map abbreviations to occurrence counts:** is insufficient because repeated copies of one word must not create a
  conflict; distinct identity, not count, controls the result.
- **Short words:** lengths one and two remain unchanged, so they cannot collide through an inserted number.
- **Repeated dictionary word:** any number of identical copies still makes that word's own query unique.
- **Ambiguous abbreviation:** once two distinct words share a key, every query for that key is false, including either
  dictionary word.
- **Defensive empty dictionary:** every query is unique, although the source contract requires at least one dictionary
  entry.
