## Function Contract

**Inputs**

- `NPV(id, year, npv)` contains $P$ stored values keyed by `(id, year)`.
- `Queries(id, year)` contains $Q$ requested pairs keyed by `(id, year)`.

**Return value**

Return exactly the columns `id`, `year`, and `npv`, with one row for every `Queries` row:

- if the same `(id, year)` exists in `NPV`, return its stored `npv`;
- otherwise, return `0` for `npv`.

Both key columns participate in the lookup, so equal IDs in different years remain independent. Unrequested `NPV` rows must not appear. A stored value of zero is returned as zero just like the missing-row fallback, and result order is unrestricted.
