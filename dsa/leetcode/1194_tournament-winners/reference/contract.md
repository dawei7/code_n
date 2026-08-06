## Function Contract

**Input tables**

- `Players(player_id, group_id)` supplies every player and that player's group.
- `Matches(match_id, first_player, second_player, first_score, second_score)` supplies both participants and their corresponding points for every match.

Each match contributes `first_score` to `first_player` and `second_score` to `second_player`. Contributions from repeated matches and from both participant positions all belong in the same player total. Match opponents are guaranteed to belong to the same group.

Let $p$ be the number of players, $m$ the number of matches, and $g$ the number of groups.

**Return value**

Return exactly one row per group with columns `group_id` and `player_id`. Select the maximum-total player independently within each group and break a maximum-total tie by the lowest `player_id`. The result rows may appear in any order.
