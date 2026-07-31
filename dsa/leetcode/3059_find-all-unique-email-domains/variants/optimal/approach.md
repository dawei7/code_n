## General

**Extract the complete domain before filtering.** Locate `@` in each email and
take the substring beginning immediately after it. Keeping this derived value
in a CTE gives the filter, grouping, projection, and ordering one consistent
definition of a domain.

**Test the suffix and aggregate once.** Retain extracted domains matching
`%.com`; because the pattern is anchored at the string end, domains such as
`shop.com.org` do not qualify. Group the remaining rows by the complete domain
and use `COUNT(*)` so every individual email contributes exactly once. Rename
the grouped key to `email_domain` and sort it ascending.

Every input row belongs to exactly one extracted domain. The suffix filter
therefore removes precisely the non-`.com` rows, and grouping the survivors
produces exactly one correctly counted row for each qualifying domain.

## Complexity detail

Let $S$ be the total email-character count and $g$ the number of qualifying
distinct domains. Domain extraction and suffix checks take $O(S)$ time.
Expected hash grouping is linear in the qualifying rows, and ordering the $g$
groups costs $O(g\log g)$, for $O(S + g\log g)$ time overall. The grouped
counts use $O(g)$ working space; database sort machinery may use comparable
additional storage.

## Alternatives and edge cases

- **Group by the full email:** This separates different individuals at the same domain and produces incorrect counts.
- **Search for `com` anywhere:** A containment test admits domains whose actual suffix is different, such as `shop.com.org`.
- **Correlated count per distinct domain:** This is correct but repeatedly scans extracted rows instead of aggregating them once.
- Multiple local parts before `@` can and should contribute to one domain count.
- If no domain ends in `.com`, return an empty result with the requested columns.
- Domain ordering is lexical ascending and independent of counts.
