## General

**Drive the result from the requested keys.** Place `Queries` on the left side of a `LEFT JOIN`. This preserves every requested pair even when `NPV` has no matching row. An inner join would silently discard precisely the missing-key rows that need the zero fallback.

**Match the complete composite key.** Join on both `id` and `year`. Each table makes that pair a primary key, so an exact match supplies at most one stored row and each query produces exactly one output row. Matching only `id` would confuse different years and could multiply a query when the inventory has several stored years.

**Replace only missing values.** For a matched key, select `n.npv`; for an unmatched key, the outer-joined value is `NULL`, so `COALESCE(n.npv, 0)` supplies the required zero. A genuine stored `npv = 0` remains zero. The candidate does not sort because the source explicitly permits any order: omitting unnecessary ordering keeps the data flow to one composite-key lookup per query and preserves the required linear expected-time bound.

The join therefore establishes a one-to-one correspondence with `Queries`. Every output row carries the exact requested key, receives its unique stored value if present, and receives zero otherwise; no unrequested `NPV` row can be introduced.

## Complexity detail

Let $P$ be the number of `NPV` rows and $Q$ the number of `Queries` rows. Building a hash lookup for the stored composite keys and probing it once per query takes expected $O(P+Q)$ time. The lookup structure and returned rows require $O(P+Q)$ space under the branch contract. A database may instead use the `NPV` primary-key index and avoid materializing a separate hash table.

## Alternatives and edge cases

- **Correlated scalar lookup:** Looking up `NPV` separately for every query is concise, but without a composite-key index it can rescan all stored rows and take $O(PQ)$ time.
- **Inner join:** This incorrectly drops requested pairs that have no stored value instead of returning them with zero.
- **Join on `id` only:** Different years for the same inventory can attach the wrong value or duplicate a query row.
- **Unnecessary ordering:** Sorting an unrestricted result adds no semantic value and can introduce $O(Q\log Q)$ work beyond the required $O(P+Q)$ bound.
- **Stored zero:** A real zero and the fallback zero display identically, but `COALESCE` preserves the correct value in either case.
- **Empty `NPV`:** Every query survives the left join and receives zero.
- **Empty `Queries`:** The result is empty even when stored values exist.
- **Unrequested values:** Rows that occur only in `NPV` never appear because `Queries` drives the join.
- **Repeated ID across years:** Each year is looked up independently through the full composite key.
