## General
**Remove duplicate listening facts first**

Create `DistinctListens` from distinct `(user_id, song_id, day)` triples. This prevents repeated log rows for one song from inflating the common-song threshold.

**Qualify pairs within one day**

Self-join the distinct facts on equal `day` and `song_id`, requiring the first user ID to be smaller than the second. Each joined row represents one distinct song shared by one unordered user pair on one day. Group by both user IDs and `day`, retaining only groups with at least three rows.

Keeping `day` in this grouping is essential: songs shared across different dates cannot be accumulated into one qualifying count. Project the qualifying user IDs with `DISTINCT` afterward so a pair that qualifies on several days is still represented once.

**Exclude friends and emit both directions**

Because candidate pairs are already canonicalized with the smaller user first, one left join to `Friendship` checks the stored orientation exactly. Keep pairs without a friendship row. Emit the canonical direction and its reversal with `UNION ALL`; the two branches are distinct because the user IDs differ.

## Complexity detail
In the worst case, the self-join can produce $O(L^2)$ shared-listening rows, and grouping those rows uses $O(L^2)$ intermediate state. Friendship exclusion adds $O(F)$ build or lookup work under normal indexed/hash execution. The worst-case time is therefore $O(L^2+F)$ and space is $O(L^2)$.

This bound is output-optimal in the worst case. If $U$ users all listen to the same three songs on one day and none are friends, then $L=3U$ while the required directed output contains $U(U-1)=\Theta(L^2)$ rows.

## Alternatives and edge cases
- **Group only by user pair:** This is incorrect because common songs from different days can accumulate to three.
- **Count raw `Listens` rows:** Duplicate listening logs can falsely satisfy the distinct-song threshold.
- **Correlated pair subqueries:** Recounting shared songs separately for every user pair repeats work and is harder to optimize.
- **Exactly three songs:** The pair qualifies; the threshold is inclusive.
- **Multiple qualifying days:** Emit each directed recommendation only once.
- **Existing friendship:** Suppress both recommendation directions.
- **Unidirectional output wording:** The relationship is evaluated as an unordered pair, but both directed rows are required.
