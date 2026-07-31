## General

Let $t$ be the number of rows in `TeamStats`.

**Calculate the ordering value once**

Use a common table expression to project each team's points as `wins * 3 + draws`. The `losses` and `matches_played` columns describe the record but do not change this formula.

**Use competition ranking, not dense ranking**

`RANK() OVER (ORDER BY points DESC)` assigns equal point totals the same position. When several rows tie, the next position skips the occupied row numbers: totals ordered as `20, 20, 18` receive positions `1, 1, 3`. That is the required competition-ranking behavior. `DENSE_RANK()` would incorrectly produce `1, 1, 2`, while `ROW_NUMBER()` would incorrectly separate the tied teams.

Only `points` belongs in the window ordering. Adding `team_name` there would break point ties and assign distinct positions.

The window ordering determines rank values but does not guarantee output presentation. Apply a final `ORDER BY points DESC, team_name ASC` so point totals descend and tied teams appear alphabetically without changing their shared position.

## Complexity detail

The points projection scans $t$ rows. Ranking and final ordering generally require sorting, for $O(t\log t)$ time and $O(t)$ working space. An optimizer may reuse a sort or exploit a suitable index, but the query does not depend on that optimization.

## Alternatives and edge cases

- **Dense ranking:** `DENSE_RANK()` shares ties but does not leave the required gaps after them.
- **Unique row numbering:** `ROW_NUMBER()` gives tied teams different positions and violates the contract.
- **Correlated higher-score count:** Computing `1 + COUNT(*)` of teams with more points can express competition rank, but may perform $O(t^2)$ comparisons without optimizer transformation.
- All teams with the same points receive position 1 and are ordered by name.
- A team with only losses has zero points.
- Three draws and one win both yield three points and therefore tie.
- `team_id` does not determine tie order; `team_name` does.
- `matches_played` is not recomputed and does not participate in ranking.
- A single team receives position 1.
