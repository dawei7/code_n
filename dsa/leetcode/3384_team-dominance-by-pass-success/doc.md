# Team Dominance by Pass Success

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3384 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/team-dominance-by-pass-success/) |

## Problem Description

### Goal

The `Teams` table assigns every player in a match to a team. The `Passes` table records the player sending each pass, its `time_stamp`, and the player receiving it.

Score every recorded pass for the sender's team. A pass received by a teammate contributes $+1$; a pass received by a player on another team contributes $-1$. Compute these contributions separately for the first half, from `00:00` through `45:00` inclusive, and the second half, from `45:01` through `90:00` inclusive.

Return one row for every team and half that has at least one recorded outgoing pass. Each row contains the team name, half number, and summed dominance score. Sort the result by `team_name` and then `half_number`, both in ascending order.

### Function Contract

**Inputs**

- `Teams(player_id, team_name)`: One row per player. `player_id` is unique, and `team_name` identifies that player's team.
- `Passes(pass_from, time_stamp, pass_to)`: One row per recorded pass. `(pass_from, time_stamp)` is unique; both player columns refer to `Teams.player_id`, and the timestamp uses the fixed `MM:SS` match-minute format from `00:00` through `90:00`.

Let $t$ be the number of player rows, $p$ the number of pass rows, and $g$ the number of resulting team-half groups.

**Return value**

- A table with columns `team_name`, `half_number`, and `dominance`, ordered by the first two columns in ascending order.

### Examples

**Example 1**

`Teams`

| player_id | team_name |
|---:|---|
| 1 | Arsenal |
| 2 | Arsenal |
| 3 | Arsenal |
| 4 | Chelsea |
| 5 | Chelsea |
| 6 | Chelsea |

`Passes`

| pass_from | time_stamp | pass_to |
|---:|:---:|---:|
| 1 | 00:15 | 2 |
| 2 | 00:45 | 3 |
| 3 | 01:15 | 1 |
| 4 | 00:30 | 1 |
| 2 | 46:00 | 3 |
| 3 | 46:15 | 4 |
| 1 | 46:45 | 2 |
| 5 | 46:30 | 6 |

Output

| team_name | half_number | dominance |
|---|---:|---:|
| Arsenal | 1 | 3 |
| Arsenal | 2 | 1 |
| Chelsea | 1 | -1 |
| Chelsea | 2 | 1 |
