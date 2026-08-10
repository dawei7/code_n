## General

**Derive the two football metrics directly from each row.** Every `SeasonStats` row already represents one team in one season. Points are three per win plus one per draw, so `wins * 3 + draws` is exact; losses contribute zero and need not appear. Goal difference is `goals_for - goals_against`.

The query selects both expressions with aliases `points` and `goal_difference`. It does not need grouping because the documented unique key `(season_id, team_id)` guarantees at most one statistics row for that team-season pair.

**Rank each season independently.** The window function partitions by `season_id`. Rows from different seasons never compete, and rank restarts at one for every season.

Inside a partition, the ordering tuple is:

`wins * 3 + draws DESC, goals_for - goals_against DESC, team_name`.

This repeats the metric expressions because aliases defined in the same select list are not generally available inside another select expression's window clause. Descending points implements the primary criterion. Descending goal difference implements the secondary criterion, including negative differences. The omitted direction for `team_name` defaults to ascending, producing alphabetical order.

**What `RANK` means with the complete tie order.** Because team name is included in the window order, two teams with equal points and goal difference but different names receive different positions in alphabetical sequence. If team names are unique within a season, the ordering tuple is unique and `RANK` behaves like row numbering from one with no gaps.

If duplicate team names with the same metrics are possible, `RANK` assigns them the same position and leaves a gap afterward. The schema guarantees unique team IDs, not explicitly unique names. The statement's alphabetical final criterion cannot distinguish identical names, so returning a tie is defensible; a unique position would require another tie-break such as `team_id` and perhaps `ROW_NUMBER`.

**Order the displayed result separately from computing rank.** The final `ORDER BY 1, 6, 3` uses select-list positions: first `season_id`, then sixth column `position`, then third `team_name`. All default to ascending. This matches the requested presentation.

Window ordering determines each rank value, while final ordering determines row display. Keeping these roles separate is important: final sorting cannot retroactively change a computed position, and a correct window rank does not guarantee the rows are returned in that order without `ORDER BY`.

**Why every output is correct.** For any team row, the arithmetic expressions give the specified point and goal-difference values. Partitioning limits comparisons to its season. The ordered window counts how many teams precede it under the complete priority sequence, assigning the corresponding rank. The final sort groups seasons and presents teams by position and name. Every source row appears once because there is no filtering or join.

The query intentionally ignores `matches_played` and `losses` beyond their implicit relation to wins and draws. Neither affects points except that losses add zero, and neither is a tie criterion.

## Complexity detail

Let $n$ be the number of `SeasonStats` rows. Computing arithmetic expressions is $O(n)$. A general execution plan sorts rows within seasons for the window function and may sort again for final output, giving $O(n\log n)$ time in the worst case. Suitable indexes or optimizer reuse can reduce physical sorting work.

Window-sort buffers and result materialization can require $O(n)$ space. Database complexity is plan-dependent, but the manifest's $O(n\log n)$ time and $O(n)$ space are reasonable general bounds.

## Alternatives and edge cases

- **`ROW_NUMBER` instead of `RANK`:** It guarantees unique sequential positions but needs a deterministic final tie-break, such as `team_id`, when names also tie.
- **`DENSE_RANK`:** It would avoid gaps after complete ties but still assign the same position to identical ordering tuples; the statement does not request that behavior specifically.
- **CTE for derived metrics:** Computing points and goal difference in a CTE can avoid repeating expressions in the window order and improve readability without changing semantics.
- **Equal points:** Goal difference decides the higher team.
- **Equal points and goal difference:** Alphabetically smaller team name receives the earlier position.
- **Identical names and metrics:** Exact `RANK` ties them and may create a later rank gap because no team-ID tie-break exists.
- **Negative goal difference:** Descending numeric order correctly treats $-1$ as better than $-5$.
- **No wins:** Draws still contribute one point each.
- **Losses:** They add zero and are correctly absent from the point expression.
- **Several seasons:** `PARTITION BY` restarts positions, while final order groups seasons ascending.
- **Positional final order:** `ORDER BY 1, 6, 3` is valid but fragile if projection order changes; named aliases are clearer.
- **One team in a season:** It receives position one regardless of metrics.
- **No aggregation:** The unique team-season row already contains totals, so grouping would be redundant.
- **Team names and collation:** Alphabetical comparison follows the database column's configured collation. Case, accents, and locale rules could affect order outside the example, so SQL “alphabetical” order is not necessarily raw byte order.
- **Repeated expressions:** Points and goal difference are calculated again inside the window order. This is logically consistent with the displayed aliases, though a CTE would make future formula changes less error-prone.
