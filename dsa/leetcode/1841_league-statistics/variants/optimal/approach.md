## General

**Turn every match into one row per team perspective.** A row in `Matches` contains both teams, but league statistics are grouped by a single team. The common table expression `Scores` normalizes each match into two rows:

- The first `SELECT` describes the home team.
- The second `SELECT` describes the away team.

`UNION ALL` combines them without deduplication. This matters because two rows with equal numeric statistics can still represent two real match appearances and must both be counted.

**Home-team perspective.** The first branch selects `home_team_id AS team_id`. Its `CASE` assigns three points when home goals exceed away goals, zero when they are lower, and one otherwise, which means a draw. It also renames home goals to `goals` and away goals to `away_goals`. From this row’s team perspective, those are goals for and goals against.

**Away-team perspective.** The second branch selects `away_team_id`. Its outcome logic is reversed: a home win gives the away team zero, a home loss means the away team won and receives three, and equality gives one. Away goals become `goals`, while home goals become `away_goals`.

After the union, every row has the same interpretation regardless of venue:

- `team_id` identifies the team whose appearance is described.
- `score` is that team’s points for the match.
- `goals` is what that team scored.
- `away_goals` is what its opponent scored, despite the slightly misleading column name for home-perspective rows.

This normalization removes the need for venue-dependent conditional expressions in the final aggregation.

**Join names after normalizing.** `Scores AS s JOIN Teams AS t ON s.team_id = t.team_id` attaches the team name to every match appearance. The query then groups by `s.team_id`. Because `team_id` is unique in `Teams`, one team identifier determines one team name under MySQL’s functional-dependency rules, allowing `team_name` to be selected.

**Aggregate the six requested columns.** Within each team group:

- `COUNT(1)` counts perspective rows. There is exactly one such row for each match the team played, whether home or away.
- `SUM(score)` adds league points across wins, draws, and losses.
- `SUM(goals)` totals goals for.
- `SUM(away_goals)` totals goals against.
- `SUM(goals) - SUM(away_goals)` computes goal difference.

The query does not compute separate win, draw, or loss counts because the output does not request them.

**Apply the ranking order after aggregation.** `ORDER BY points DESC` places higher point totals first. `goal_diff DESC` resolves equal points in favor of the better goal difference. Finally, `team_name` uses ascending order by default, producing lexicographical order for any remaining tie.

These aliases refer to aggregate result columns, so sorting occurs after team totals have been calculated.

**Trace one match.** For Ajax at home against Dortmund with score zero to one, the home branch produces Ajax with zero points, zero goals for, and one goal against. The away branch produces Dortmund with three points, one goal for, and zero goals against. Each team receives one match appearance. Repeating this conversion for all sample matches and summing yields the displayed standings.

**Why every played match is counted correctly.** Fix a match. `UNION ALL` emits exactly two rows, one for each participant. Each branch’s `CASE` matches the league’s three-zero or one-one scoring rule, and its goal aliases match that participant’s perspective. Therefore that match contributes exactly the correct increment to both teams’ aggregates. Grouping sums all and only a team’s appearance rows, proving the totals for participating teams.

**Material exact-query limitation for teams with no matches.** The final query starts from `Scores` and uses an inner `JOIN` to `Teams`. A team that has not appeared in any `Matches` row has no perspective row in `Scores` and is absent from the result entirely. The local description asks for league statistics and does not explicitly guarantee that every listed team has played.

If zero-match teams are intended to appear with zeros, this exact query does not fully satisfy that case. A solution for that broader contract would need to start from `Teams`, left join normalized match rows, and replace null aggregates with zero. The checked-in query is correct for teams with at least one played match or under an unstated guarantee that every team appears.

**Why `UNION` would be wrong.** Plain `UNION` removes duplicate rows. If a team had two match appearances producing identical `team_id`, score, goals, and opponent-goals values, one could disappear, reducing matches played and totals. `UNION ALL` preserves event multiplicity and is the required form.

## Complexity detail

Let `m` be the number of matches and `t` the number of teams. The CTE produces `2m` rows. Scanning matches and calculating perspective fields is `O(m)` logical work. Joining teams can be near linear with an index or hash plan, grouping processes the perspective rows, and final ordering of up to `t` participating teams costs `O(t log t)`. A representative overall bound is `O(m + t log t)`, subject to the database optimizer and available indexes.

The normalized rows, grouping state, and sort can require `O(m + t)` working space. MySQL may materialize, stream, hash, or externally sort parts of the plan, so physical memory and disk behavior is engine-dependent.

## Alternatives and edge cases

- **Conditional aggregation without a union:** Join each team to matches where it is home or away and use `CASE` for perspective. It avoids doubling through a CTE but makes every aggregate expression more complex.
- **Start from `Teams` with a left join:** This is necessary if teams with zero matches must appear with zero statistics.
- **Plain `UNION`:** It can erase distinct match appearances that happen to produce identical projected values and must not replace `UNION ALL`.
- **Draw:** Both perspective rows receive score one, and each side’s goals for equal the other side’s goals against.
- **Home win:** Home receives three and away zero; the second branch deliberately reverses the comparison outcome.
- **Away win:** Away receives three and home zero.
- **Repeated scorelines:** `UNION ALL` retains all appearances, so identical match statistics still count separately.
- **Negative goal difference:** Subtracting aggregate goals against naturally produces a negative value and descending sorting ranks it below a larger difference.
- **Complete standings tie:** Team name ascending supplies the final deterministic order.
- **Team with no matches:** The exact inner-join query omits it rather than returning zeros.
- **Unique team name dependency:** Grouping by `team_id` relies on its unique Teams row to determine `team_name`; stricter SQL modes or other engines may prefer grouping by both.
- **Indexes:** Indexes on team identifiers help joins, but they do not change the query’s logical result.
