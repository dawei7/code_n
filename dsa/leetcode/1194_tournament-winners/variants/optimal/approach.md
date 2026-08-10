## General

Every match stores two score contributions in different columns. The query first converts those role-specific columns into one common stream of `player_id`, `score`, and `group_id` rows. It then totals each player’s points, ranks players inside their groups, and retains rank one.

**Expand each match into two score rows**

The first common table expression, `s`, has two branches joined by `UNION ALL`.

The first branch selects `first_player AS player_id` and `first_score AS score`. It joins `Matches` to `Players` on the first player ID to attach that player’s `group_id`.

The second branch does the symmetric work for `second_player` and `second_score`.

`UNION ALL` is crucial. Two identical score rows can come from different matches or roles and must both contribute to the total. Plain `UNION` would remove duplicates and could undercount a player.

The guarantee that both players in a match belong to the same group is consistent with either role’s join. Attaching the group from the player table also avoids trying to infer membership from opponents.

**Aggregate all roles and matches per player**

The next CTE, `t`, groups the score stream by `player_id` and calculates `SUM(score) AS scores`. A player who appeared as first player in some matches and second player in others now has all contributions in one total.

The query also selects `group_id`. Player IDs are unique in `Players`, so one player belongs to exactly one group and `player_id` functionally determines `group_id`. Under the intended MySQL semantics, grouping by the player ID therefore has one unambiguous group value. Writing `GROUP BY group_id, player_id` would make this dependency explicit and be more portable under strict grouping rules.

**Rank independently within every group**

The `p` CTE computes:

`RANK() OVER (PARTITION BY group_id ORDER BY scores DESC, player_id)`.

`PARTITION BY group_id` restarts ranking for each group. Ordering `scores DESC` places the largest total first. Adding `player_id` in ascending order implements the tie rule: among equal totals, the lower player ID comes first.

Because `player_id` is unique, no two rows in one partition can tie on both ordering keys. Consequently, exactly one row receives rank one in each represented group. `RANK` works here, although `ROW_NUMBER` would communicate the one-winner intention more directly.

The outer query keeps `WHERE rk = 1` and returns only `group_id` and `player_id`. Result ordering is unspecified, which is allowed.

**Following the example’s first group**

Player 15 receives three points as a first player and zero as a second player, totaling three. Player 30 receives one plus two, also totaling three. Player 25 totals two and player 45 totals zero. The window order places players 15 and 30 first by their tied score, then resolves that tie by the lower ID. Player 15 receives rank one and is selected.

For group two, players 35 and 50 both total one. The same secondary ordering selects 35. For group three, player 40’s five points exceed player 20’s two, so no tie-break is needed.

**Why the selected row is the required winner**

The expanded stream contains one row for each player-side contribution from every match. `UNION ALL` preserves all of them, and grouping adds exactly those values by player. Thus `scores` is each participating player’s total.

Within a group, descending score makes any maximum-total player precede every lower-total player. Among maximum-total players, ascending ID makes the smallest ID precede the others. The unique first row therefore satisfies both winner rules, and filtering rank one returns it.

The exact query derives candidate players from `Matches`. A player who never appears in any match does not enter `s` or later CTEs. Its completeness therefore depends on the source data ensuring that every group’s relevant candidates participate in at least one match. If entirely inactive players were permitted and needed to compete with a zero total, a more defensive query would start from all `Players` rows and left-join score totals with zero filling. The local table description shown here does not independently state that participation guarantee, so this dependency is material.

## Complexity detail

Let $m$ be the number of matches, $p$ the number of players, and $r$ the number of players represented in the match stream.

The two `UNION ALL` branches emit $2m$ contribution rows. With indexed primary-key joins, attaching group IDs is expected linear in the emitted rows. Aggregating them costs expected $O(m)$ time under hashing and stores up to $r$ totals.

The window function must order the $r$ player totals within group partitions. A general comparison-sort bound is $O(r\log r)$ overall, or more precisely the sum of $O(r_g\log r_g)$ across group sizes. Thus a realistic logical bound is $O(m+r\log r)$ time, not purely $O(p+m)$ unless ordering is supplied or treated specially by the engine.

The score stream, aggregates, window state, and result can require $O(m+p)$ intermediate and output space. Actual MySQL plans may materialize CTEs, hash, sort, or exploit indexes differently; `EXPLAIN` is needed for physical-plan claims.

## Alternatives and edge cases

- **`ROW_NUMBER` instead of `RANK`:** With the complete score-and-ID ordering, `ROW_NUMBER() = 1` directly selects one winner. It avoids relying on the uniqueness of the final ordering key to make rank one unique.
- **Correlated maximum query:** Compare each player against better players in the same group. This can express the rule but is often harder to optimize and read.
- **Start from all players:** Left-join aggregated scores and use zero for missing totals when players with no matches must remain eligible.
- **Use `UNION` instead of `UNION ALL`:** This is incorrect because equal score contributions from different matches are separate facts and must not be deduplicated.
- **Player appears in both roles:** Both branches contribute, and grouping correctly combines all points.
- **Tie on total score:** Ascending `player_id` makes the lower ID win.
- **No tie:** Descending score alone places the unique maximum first.
- **One player in a group:** That represented player receives rank one automatically.
- **Inactive player:** The exact query omits it because candidates originate in `Matches`; correctness requires the participation assumption described above or a query redesign.
- **Grouping portability:** Selecting `group_id` while grouping only by `player_id` relies on the functional dependency. Grouping by both columns would be clearer across strict SQL systems.
- **Any result order:** The outer query has no `ORDER BY` because the contract permits arbitrary row order.
