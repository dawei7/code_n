## General
**Turn each call into its two country contributions**

Create a common table expression `call_endpoints` with `UNION ALL`. Its first branch emits `(caller_id, duration)` for every call, and its second emits `(callee_id, duration)`. `UNION ALL` is essential: caller and callee contributions are distinct observations, and duplicate call rows must remain duplicated.

The endpoint relation makes the averaging rule explicit. Each original duration occurs exactly twice overall. For a domestic call both copies later join to the same country; for an international call they join to different countries. This is precisely the required endpoint-weighted interpretation.

**Map endpoints through people to countries**

Join each endpoint to `Person` by person ID. Extract the first three characters of `phone_number` and join that prefix to `Country.country_code`. Keeping country codes as strings preserves leading zeroes such as `051`; numeric conversion is unnecessary and can obscure the fixed-width identity.

Group the joined endpoints by the country code and name. `AVG(duration)` within a group is then that country's required average because every incident endpoint contributes one row and no unrelated call contributes.

**Compare against the undoubled global average**

The scalar subquery `SELECT AVG(duration) FROM Calls` computes the global average across call records. Although the endpoint CTE contains every duration twice, doubling every call equally would produce the same global average; reading `Calls` directly states the contract more clearly and avoids needless expansion.

Use `HAVING`, not `WHERE`, to compare each completed country aggregate with that scalar value. The strict `>` operator excludes equality. An inner-join pipeline naturally omits countries with no endpoint, and aliasing `Country.name AS country` produces the exact requested schema.

For every returned group, the endpoint CTE supplies exactly its participants' call occurrences, so its aggregate is the defined country average. `HAVING` retains it exactly when that value exceeds the one global average. Conversely, every represented country forms one group and is retained whenever it meets that condition, proving both soundness and completeness.

## Complexity detail
The two CTE branches scan $L$ calls and materialize $E=2L$ endpoint rows. Joining those rows to the $P$ people and $C$ country codes and grouping them can be implemented with indexed or hash lookups plus a sort or grouped index traversal. The conservative portable bound is $O((P+C+E)\log E)$ time and $O(P+C+E)$ working space. Engines may choose an expected-linear hash plan when suitable indexes and memory are available.

The result contains at most $C$ rows. Duplicate `Calls` records are intentionally retained and do not alter the asymptotic bounds.

## Alternatives and edge cases
- **Join with an `OR` predicate:** Join `Person.id` to either `caller_id` or `callee_id` in one condition. It is concise, but disjunctive joins can inhibit index use and make the two endpoint contributions less explicit.
- **Two aggregated queries combined afterward:** Aggregate caller countries and callee countries separately, then merge sums and counts. This can be efficient but is longer and must combine both numerator and denominator correctly.
- **Correlated country subqueries:** Recompute incident-call averages separately for every country. It can repeatedly scan `Person` and `Calls`, producing quadratic scaling as the country count grows.
- **Use `UNION` instead of `UNION ALL`:** Deduplication incorrectly removes equal endpoint rows, including legitimate duplicate calls.
- **Average country-level averages:** Giving each country equal weight does not produce the global call average; compare every country with `AVG(Calls.duration)`.
- **Domestic call:** Its duration contributes twice to one country, matching its two participating endpoints.
- **International call:** Its duration contributes once to each endpoint's country.
- **Duplicate call rows:** Every stored row is an independent call occurrence and contributes twice.
- **Average equal to global:** Exclude it because the predicate is strictly greater, not greater than or equal.
- **Country with no calls:** It creates no endpoint group and must not appear.
- **Leading-zero country code:** Extract and compare the three-character string without numeric conversion.
- **Output ordering:** Any order is valid; an app-local `ORDER BY country` may provide deterministic presentation without changing membership.
