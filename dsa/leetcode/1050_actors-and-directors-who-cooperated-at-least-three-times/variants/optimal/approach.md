## General
**Form one group per pair:** Group rows by both `actor_id` and `director_id`. Grouping by only one column would mix collaborations with different partners and answer a different question.

**Count collaboration rows:** Apply `COUNT(*)` to each pair's group. The unique timestamp ensures rows are distinct events, but its numeric value and ordering do not affect the count.

**Filter at the inclusive threshold:** Retain groups with `COUNT(*) >= 3`. Selecting the grouping columns produces one result row per qualifying pair. The final ascending order is used only for stable local fixtures.

Every output pair owns at least three source rows because it passes the `HAVING` predicate. Conversely, all rows for any pair are collected into one group, so a pair with at least three collaborations has a count of at least three and cannot be omitted.

## Complexity detail
For $R$ rows, a sort-based grouping plan takes $O(R log R)$ time and $O(R)$ execution space in the worst case. Hash aggregation can reduce expected grouping time to $O(R)$, while indexes may alter the physical plan.

## Alternatives and edge cases
- **Correlated count:** Select distinct pairs and count matching rows in a correlated subquery. It is correct but can rescan all $R$ rows for each source row, taking $O(R^2)$ time.
- **Self-join three copies:** Join three distinct timestamps for the same pair to prove at least three events. It creates many combinations when a pair collaborates often.
- **Window count:** Compute `COUNT(*) OVER (PARTITION BY actor_id, director_id)`, filter, and deduplicate. It is valid but less direct than grouped aggregation.
- **Exactly three rows:** The pair qualifies because the threshold is inclusive.
- **Two rows:** The pair does not qualify.
- **Same actor, different directors:** Each actor-director combination is counted independently.
- **Same director, different actors:** These are also separate groups.
- **Timestamp values:** Only their uniqueness distinguishes events; gaps or input order do not matter.
