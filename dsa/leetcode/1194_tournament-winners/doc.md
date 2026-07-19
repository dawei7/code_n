# Tournament Winners

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1194 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/tournament-winners/) |

## Problem Description

### Goal

The `Players` table assigns every uniquely identified player to a tournament group. The `Matches` table records two players and their respective point totals for each match; both participants in a match always belong to the same group.

Within each group, add all points scored by each player across every match. The group winner is the player with the greatest total score. When several players share that maximum, the player with the smallest `player_id` wins. Return the winning player for every group in any order.

### Function Contract

**Input tables**

- `Players(player_id, group_id)`: `player_id` is the primary key, and each row assigns that player to one group.
- `Matches(match_id, first_player, second_player, first_score, second_score)`: `match_id` is the primary key; the two player columns identify same-group opponents, and the score columns give the points they earned in that match.
- Let $p$ be the number of players, $m$ the number of matches, and $g$ the number of groups.

**Return value**

- One row per group with columns `group_id` and `player_id`, identifying the maximum-total scorer and using the smallest `player_id` to break a tie.

### Examples

**Example 1**

`Players`

| player_id | group_id |
|---:|---:|
| 15 | 1 |
| 25 | 1 |
| 30 | 1 |
| 45 | 1 |
| 10 | 2 |
| 35 | 2 |
| 50 | 2 |
| 20 | 3 |
| 40 | 3 |

`Matches`

| match_id | first_player | second_player | first_score | second_score |
|---:|---:|---:|---:|---:|
| 1 | 15 | 45 | 3 | 0 |
| 2 | 30 | 25 | 1 | 2 |
| 3 | 30 | 15 | 2 | 0 |
| 4 | 40 | 20 | 5 | 2 |
| 5 | 35 | 50 | 1 | 1 |

Output:

| group_id | player_id |
|---:|---:|
| 1 | 15 |
| 2 | 35 |
| 3 | 40 |

**Example 2**

If two players in one group finish with equal total scores, the smaller `player_id` is returned.

**Example 3**

Scores earned as `first_player` and as `second_player` both contribute to the same player's total.
