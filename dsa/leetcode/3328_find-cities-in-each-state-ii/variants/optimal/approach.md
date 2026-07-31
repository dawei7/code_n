## General

Each output row summarizes one state, so group the source rows by `state`. Within each group, `GROUP_CONCAT` collects every city. Its internal `ORDER BY city` is essential: the final output order of states does not impose any order on the names inside an aggregate string. Use `SEPARATOR ', '` to match the required formatting exactly.

Count matching initials during the same aggregation. In MySQL, the comparison `LEFT(city, 1) = LEFT(state, 1)` evaluates to $1$ when true and $0$ when false, so summing it gives `matching_letter_count` without another join or scan.

The two eligibility requirements are group properties and therefore belong in `HAVING`, after aggregation. `COUNT(*) >= 3` enforces the minimum number of cities, while `matching_letter_count >= 1` excludes states with no matching initial. MySQL permits the aggregate alias in `HAVING`, allowing the computed count to be reused directly.

Finally order qualifying groups by `matching_letter_count DESC` and then `state ASC`. This secondary key is required even when two states share the same count; relying on an engine's incidental group order would not satisfy the contract.

The remotely verified native query uses MySQL's inline `GROUP_CONCAT(city ORDER BY city SEPARATOR ', ')` form. The app-local adapter runs in SQLite, so it first orders rows in a CTE and then calls `GROUP_CONCAT(city, ', ')`. Its case-insensitive sort key removes spaces before comparison to reproduce MySQL's dictionary-style ordering for names such as `Newark` and `New York City`. Both artifacts implement the same ordering, separator, grouping, filtering, and output contract in their source-native dialects.

## Complexity detail

Let $n$ be the number of rows in `cities`. Grouping and scanning the rows is linear under ordinary database aggregation, while ordering city names inside groups and sorting the output groups gives an $O(n\log n)$ worst-case time bound. The grouped strings, aggregate state, and sorting workspace can require $O(n)$ space. The database optimizer may use indexes or external sorting, but those physical choices do not change the query's logical requirements.

## Alternatives and edge cases

- **Correlated subqueries per state:** Separate queries for city count, matching count, and concatenation repeat work and are harder for the optimizer than one grouped aggregation.
- **Filter matching cities in `WHERE`:** Doing so would remove nonmatching cities from both the city list and total city count; all cities must remain in the group even though only some contribute to the conditional sum.
- **Use `WHERE COUNT(*)`:** Aggregate predicates are unavailable before grouping and must be expressed with `HAVING`.
- **Omit the aggregate ordering:** `GROUP_CONCAT(city)` alone does not guarantee alphabetical city names.
- **Exactly three cities:** The state qualifies because the threshold is inclusive, provided at least one initial matches.
- **No matching initial:** A state is excluded even when it has many cities.
- **Tied matching counts:** State name ascending is the mandatory deterministic tiebreaker.
