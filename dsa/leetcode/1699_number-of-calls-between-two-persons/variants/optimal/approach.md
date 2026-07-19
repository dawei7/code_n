## General
**Canonicalize direction before grouping**

For every call row, compute `person1` as the smaller of `from_id` and `to_id`, and `person2` as the larger. SQL `CASE` expressions implement this portably. Both directions between the same participants now yield the identical key `(person1, person2)`, while the strict identifier inequality guarantees the two projected values differ.

**Aggregate every call row in its canonical pair**

Group by the two canonical expressions. `COUNT(*)` gives the number of calls, including duplicate source rows, and `SUM(duration)` gives their combined duration. Do not apply `DISTINCT`: identical rows still represent multiple table records and must contribute multiple times.

Each source row maps to exactly one unordered pair, and every pair present in the input has a group. Canonicalization makes opposite directions share that group, so its count and sum cover exactly all calls between those two people. The problem permits any result order, so sorting is unnecessary.

## Complexity detail
A hash aggregation examines each of the $R$ call rows once, computes a constant-size canonical key, and updates two aggregates in expected $O(1)$ time, for expected $O(R)$ total time. There can be at most $R$ distinct pairs, so the aggregation state uses $O(R)$ space.

## Alternatives and edge cases
- **Union both directions:** duplicating rows with reversed endpoints before grouping is unnecessary and would double-count unless followed by extra correction.
- **Group by directed IDs:** grouping directly on `(from_id, to_id)` incorrectly separates calls in opposite directions.
- **Correlated subqueries per row:** repeatedly scanning for the reverse pair can take quadratic time and still needs deduplication of output pairs.
- **Duplicate call rows:** every row counts as a call and contributes its full duration; no `DISTINCT` belongs in either aggregate.
- **Only reverse-direction rows:** canonical expressions still place the smaller ID in `person1`.
- **Several partners for one person:** each distinct second participant forms its own unordered pair group.
- **Output order:** any row order is valid and is compared as an unordered table.
