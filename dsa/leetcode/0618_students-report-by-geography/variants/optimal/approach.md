## General
**Assign an independent alphabetic rank**

Use `ROW_NUMBER()` partitioned by `continent` and ordered by `name`. Each continent starts at rank one, so equal ranks identify names that belong on the same output row. Equal names and fully duplicate rows still receive separate row numbers, which preserves their multiplicity in successive output positions.

**Pivot each rank with conditional aggregation**

Group the ranked relation by its row number. For each target continent, a `CASE` expression exposes that continent's name and nulls the others; `MAX` selects the one nonnull value for the group. If no student from a continent has that rank, all corresponding values are null and the output cell remains null.

**Why every name appears in the correct cell**

Within one continent, `ROW_NUMBER` assigns every name one unique position in alphabetic order. Grouping equal positions places exactly the kth name from every available continent together. Conditional aggregation sends a name only to its own continent column, so no name is duplicated, omitted, or moved across continents.

The primary test guarantee makes America at least as populous as Asia and Europe, so its ranks determine the complete output height. Because the query groups every rank present in any partition rather than starting from America explicitly, the same source also answers the follow-up where the largest continent is not known in advance.

## Complexity detail
For `R` students, partition ordering costs $O(R \log R)$ time and $O(R)$ execution space. The grouped pivot is linear after ranking, and ordering the at most `R` result ranks does not increase the bound.

## Alternatives and edge cases
- **Rank three filtered lists and join them:** separately number each continent and outer-join by rank; it is explicit but repeats similar logic and needs full-outer-join emulation in MySQL.
- **Session variables:** older MySQL solutions can maintain one counter per continent, but evaluation-order dependencies make them fragile compared with window functions.
- **Correlated rank count:** count preceding names for every student; it can take $O(R^2)$ time and, without a unique tie-breaker, cannot assign distinct ranks to fully duplicate source rows.
- A missing Asia or Europe population produces an entirely null column while America's names still appear.
- Unequal continent sizes produce nulls only after the shorter list is exhausted.
- Duplicate rows remain duplicate names at separate successive ranks.
- Input row order is irrelevant; names are ordered within each continent.
- Under the primary guarantee, the output row count equals America's population; the generalized query also equals the largest population for the follow-up.
