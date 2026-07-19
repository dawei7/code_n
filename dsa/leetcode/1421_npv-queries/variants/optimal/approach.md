## General
**Keep every query row.** Use `Queries` as the left side of a `LEFT JOIN` to `NPV`. Match on both `id` and `year`; matching only the identifier could attach a value from the wrong year or duplicate a request.

For a matched row, select the stored `npv`. For an unmatched row, the joined value is `NULL`, so replace it with zero using `COALESCE`. Ordering by the two key columns is not required by the source relation but makes local results deterministic.

The left join emits exactly one row for each unique query key. The composite join condition supplies its value if and only if that exact stored key exists, and `COALESCE` handles precisely the remaining unmatched case. Therefore every requested pair receives the required value without adding unrelated NPV rows.

## Complexity detail
With a hash table or composite-key index for the stored rows, building or reading the lookup and probing all requests takes $O(P+Q)$ time. The join structures and returned rows require $O(P+Q)$ space under the stated bound.

## Alternatives and edge cases
- **Correlated scalar subquery:** Look up `NPV` separately for every query row. It is concise but can degrade to $O(PQ)$ without a composite index.
- **Inner join:** This incorrectly discards requested pairs that lack a stored value.
- **Join on id only:** Different years for one identifier would match incorrectly.
- **Stored zero:** A real `npv = 0` and a missing row both display zero, as required.
- **Empty NPV table:** Every query still appears with zero.
- **Deterministic order:** Sorting is useful for fixtures even though relational result order is otherwise unspecified.
