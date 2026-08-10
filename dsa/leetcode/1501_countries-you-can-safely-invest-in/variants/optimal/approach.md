## General

**Why each call must be viewed from both endpoints**

A country's average is based on calls involving people in that country, whether those people were callers or callees. The join

`Person JOIN Calls ON id IN (caller_id, callee_id)`

matches a call row to its caller's person row and separately to its callee's person row. Because the contract guarantees different caller and callee IDs, each call produces exactly two endpoint rows when both people exist.

This duplication is intentional. A call between two countries contributes its full duration once to each country's endpoint statistics. A call within one country contributes twice to that country's sum and count, once for each participating person. The sample explanation follows precisely this endpoint interpretation.

Duplicate rows in `Calls` remain separate events. Each duplicate also generates two endpoint rows and therefore retains its multiplicity in every average.

**Mapping a person to a country**

Phone numbers begin with a three-character country code and may contain leading zeroes. `LEFT(phone_number, 3)` extracts those first three characters as text. Joining that value to `Country.country_code` preserves codes such as `051` that would be damaged by numeric conversion.

The alias `c` refers to `Country`, and `c.name AS country` gives the result column its required name. An inner join means a person whose prefix has no country row contributes to no country group.

**Building each country's average**

The derived table groups endpoint rows by the selected country. `AVG(duration) AS duration` computes the arithmetic mean of every incident call endpoint for that country.

`GROUP BY 1` is positional syntax meaning group by the first selected expression, which is `c.name AS country`. Grouping by an explicit column expression would be more descriptive, but the positional form is valid MySQL syntax.

For a cross-country call of duration thirty, each involved country receives one thirty-minute endpoint. For a domestic call of duration thirty, the same country receives two thirty-minute endpoints. Duplicating a value twice does not change that individual call's value, but it gives appropriate weight to both residents participating under the endpoint definition.

Countries with no call endpoint never appear in the person-call join and therefore never form a group.

**Comparing against the global average**

The outer query filters the country aggregates with

`duration > (SELECT AVG(duration) FROM Calls)`.

The scalar subquery computes the average over original call rows, counting each stored row once. The comparison is strict, so a country equal to the global average is not selected.

Why is comparing endpoint-based country averages to a once-per-call global average coherent? If every call were duplicated once for each endpoint globally, both the total duration and number of observations would double, leaving the same average. Thus the scalar average equals the average over all call endpoints.

The derived-table alias `t` makes its averaged `duration` available to the outer `WHERE`. The final query selects only `country` and has no ordering clause because any order is allowed.

**Why the result is correct**

Any returned country has at least one endpoint row, and its derived average is strictly greater than the global call average because it passed the outer predicate. Its group includes callers and callees whose three-character phone prefix matches that country.

Conversely, every country with incident call endpoints forms a group containing all of them. The aggregate computes its exact endpoint average. If that average is strictly above the scalar global average, the outer filter retains it. Therefore, every and only qualifying country name is returned.

**Important SQL-name behavior**

The unqualified `id` in the first join refers to `Person.id` because the other participating table has `caller_id` and `callee_id` rather than a column literally named `id`. Similarly, unqualified `duration` comes from `Calls` inside the derived query.

Using `IN` in a join predicate is concise, though some optimizers may handle two explicit endpoint branches more efficiently. This is a logical join condition, not a membership lookup in a prebuilt application set.

## Complexity detail

Let $P$ be the number of people, $C$ the number of countries, and $E$ the number of call rows. The endpoint join can produce up to $2E$ person-call matches before country grouping. A plan using indexes or hash structures can process the base rows and joins near linearly, while grouping may use hashing or sorting.

The manifest's $O((P+C+E)\log E)$ time and $O(P+C+E)$ space are reasonable conservative logical bounds for join and sort-based aggregation. Actual database complexity depends on indexes, statistics, chosen join algorithms, materialization, memory limits, and whether intermediate data spills to disk.

`id IN (caller_id, callee_id)` can make index use less straightforward than two equality joins or a union of caller and callee endpoints. `LEFT(phone_number, 3)` is a function expression and may also need an expression index to support a direct seek. The scalar global average requires a scan of `Calls` unless the engine shares or precomputes equivalent work.

## Alternatives and edge cases

- **UNION ALL endpoint normalization:** Produce caller-duration rows and callee-duration rows separately, combine them with `UNION ALL`, then join people and countries. This makes the two-endpoint semantics explicit and can improve optimizer options.
- **UNION instead of UNION ALL:** It is wrong because it could remove duplicate endpoint rows, while every call row and both endpoints must retain their weight.
- **Conditional joins:** Joining calls to caller and callee people in separate aliases can work but requires reshaping both endpoints before one country aggregation.
- **Domestic call:** It contributes twice to the same country, once per distinct participant.
- **International call:** Its duration contributes once to each endpoint country.
- **Duplicate call rows:** They count independently and must not be deduplicated.
- **Country with no calls:** It has no group and is absent rather than treated as having average zero.
- **Average equal to global:** Strict greater-than excludes it.
- **Leading-zero country code:** Text prefix extraction preserves the zeros.
- **Null durations:** SQL `AVG` ignores nulls; the reference presents duration values but does not specify null semantics.
- **Unrestricted output order:** No `ORDER BY` is needed or implied.
