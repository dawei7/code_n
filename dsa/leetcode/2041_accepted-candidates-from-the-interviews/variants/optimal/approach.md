## General

**Join candidates to all rounds of their interview**

The candidate row contains `interview_id` but not the individual scores. The `Rounds` table contains those scores under the same identifier. The query uses

`Candidates JOIN Rounds USING (interview_id)`

to create one joined row for each matching candidate-round combination.

`JOIN` without another qualifier is an inner join. A candidate whose interview has no matching round contributes no joined row and therefore cannot appear in the final grouped result.

`USING (interview_id)` is shorthand for equality of the two tables' identically named `interview_id` columns. It also exposes one merged join column rather than two separately qualified copies.

**Apply the experience requirement before aggregation**

`WHERE years_of_exp >= 2` removes candidates with fewer than two years of experience.

The boundary is inclusive: a candidate with exactly two years passes. Filtering before grouping is appropriate because `years_of_exp` is a property of the candidate row, not an aggregate of interview rounds.

Once an inexperienced candidate is removed, none of that candidate's joined round rows contribute to later grouping.

**Group all round rows by candidate**

`GROUP BY 1` uses an ordinal reference to the first selected expression. The only selected expression is `candidate_id`, so this means “group by candidate identifier.”

Every joined round belonging to the same candidate enters that candidate's group. The composite primary key on `Rounds` ensures each interview round identifier occurs at most once for an interview, so a single round row is not duplicated within `Rounds` itself.

If two candidate rows happen to reference the same interview identifier, they still have different `candidate_id` groups. Each candidate is evaluated separately, which is consistent with reporting candidate IDs.

**Filter groups with `HAVING`**

The total interview score does not exist on one row; it is `SUM(score)` across the candidate's joined rounds. Aggregate conditions belong in `HAVING`, which is evaluated after grouping.

The query retains a candidate only when

`SUM(score) > 15`.

The comparison is strict. A total of exactly fifteen does not qualify, while sixteen does.

Using `WHERE SUM(score) > 15` would be invalid because `WHERE` runs before group aggregates have been formed.

**Trace the example**

Candidate 9 has six years of experience, so the `WHERE` condition keeps the candidate. Interview 104 joins to scores 6, 7, 2, and 7. Their group sum is 22, which passes the strict threshold, so candidate ID 9 is selected.

Candidate 6 has sufficient experience but interview 109 totals only ten. The candidate survives `WHERE` but fails `HAVING`.

Candidate 11 has a total score of sixteen but only one year of experience. Their joined rows are removed by `WHERE` before the score group can qualify.

Both requirements must hold for the same returned candidate.

**Why selecting only the ID is enough**

The requested result has one column, `candidate_id`. Candidate identifiers are unique in `Candidates`, and grouping produces at most one result row per identifier.

No `DISTINCT` is required after grouping. The group itself collapses all round rows for one candidate into a single output row.

**Why no output ordering is needed**

The contract permits any order. Without `ORDER BY`, SQL does not guarantee a particular order, but that is acceptable here.

Adding a sort would impose extra work without satisfying any missing semantic requirement.


Every returned row comes from a candidate with `years_of_exp >= 2` because otherwise all of that candidate's joined rows would have been filtered out. Its group also satisfies `SUM(score) > 15` by the `HAVING` clause. Thus every returned identifier is accepted under both rules.

Conversely, consider a candidate satisfying both rules and having matching round rows. The inner join creates those rows, the experience filter retains them, grouping collects them under that candidate's unique ID, and their sum passes `HAVING`. The ID is returned.

The query therefore returns all and only candidates satisfying the stated experience and total-score conditions.

**Physical execution is database-dependent**

The logical query states what must be computed, while the database optimizer chooses how. It may hash the join and grouping, use indexes on `interview_id`, or sort intermediate rows.

The manifest includes a sorting term, but the SQL source does not explicitly request an output sort. Complexity should therefore be understood in terms of the selected execution plan rather than as a fixed language-level loop count.

## Complexity detail

Let $C$ be candidate rows, $R$ round rows, and $J$ the number of joined candidate-round rows after matching interview IDs. With hash-based join and aggregation, expected work is $O(C+R+J)$ and working space is $O(C+R)$ in a broad upper-bound description.

A sort-based grouping plan can cost $O(J\log J)$ time and $O(J)$ intermediate space. Under a data model where joined volume is proportional to the source rows, this is consistent with a scan-plus-group or scan-plus-sort bound. Indexes and optimizer choices can improve constants or avoid materializing some rows. There is no explicit `ORDER BY` cost.

## Alternatives and edge cases

- **Aggregate rounds first:** Build one total per `interview_id`, filter totals above fifteen, then join to experienced candidates; often reduces join volume.
- **Correlated subquery:** Sum rounds for each candidate, but without good indexing it can repeat work.
- **`WHERE` for experience:** Correct because experience is a row attribute evaluated before grouping.
- **`HAVING` for score total:** Required because the threshold applies to an aggregate.
- **Exactly two years of experience:** Included by `>= 2`.
- **Exactly fifteen total points:** Excluded by strict `> 15`.
- **No matching rounds:** Excluded by the inner join and cannot form a qualifying total.
- **Several rounds:** All matching `score` values are added.
- **Shared interview identifier:** Candidates remain separate because grouping uses `candidate_id`.
- **Duplicate candidate output:** Prevented by one group per primary-key identifier.
- **Any row order:** No `ORDER BY` is necessary.
- **`GROUP BY 1`:** Refers to the first selected expression, `candidate_id`; naming the column explicitly would be clearer but equivalent.
- **Null score outside the stated model:** `SUM` ignores null values; an all-null group would not pass the comparison.
