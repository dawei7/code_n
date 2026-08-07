## Function Contract

**Input tables**

- `Teams(team_id, team_name)` supplies the complete team catalog.
- `Matches(match_id, host_team, guest_team, host_goals, guest_goals)` supplies each finished match, its two distinct participants, and their respective scores.

Let $t$ be the number of teams and $m$ the number of matches.

**Return value**

Return exactly one row per team with columns `team_id`, `team_name`, and `num_points`, where `num_points` is that team's sum of three-point wins and one-point draws across all matches.

Sort the result by `num_points` in decreasing order. When totals tie, sort those rows by `team_id` in increasing order.
