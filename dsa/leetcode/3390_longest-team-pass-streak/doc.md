# Longest Team Pass Streak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3390 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-team-pass-streak/) |

## Problem Description

### Goal

The `Teams` table assigns every match participant to a team. The `Passes` table records each attempted pass through its sender, receiver, and `time_stamp`. A pass is successful for the sender's team when both players belong to that same team; receiving the ball on another team is an interception.

For each team, consider only passes sent by that team's players and place them in chronological order. Successful passes extend the current streak, while an interception ends it. Passes sent by another team do not interrupt this team's sequence. Return the greatest positive streak attained by every team that completes at least one successful pass, omitting teams whose outgoing passes are all intercepted, and order the rows by `team_name` in ascending order.

### Function Contract

**Inputs**

- `Teams(player_id, team_name)`: One row per player. `player_id` is unique, and `team_name` identifies the player's team.
- `Passes(pass_from, time_stamp, pass_to)`: One row per pass. `(pass_from, time_stamp)` is unique, both player columns identify rows in `Teams`, and `time_stamp` uses the match-minute format `MM:SS` from `00:00` through `90:00`.

Let $t$ be the number of player rows and $p$ the number of pass rows.

**Return value**

- A table with columns `team_name` and `longest_streak`, ordered by `team_name` in ascending order. Only teams with a positive successful-pass streak appear.

### Examples

#### Example 1

`Teams`

| player_id | team_name |
|---:|---|
| 1 | Arsenal |
| 2 | Arsenal |
| 3 | Arsenal |
| 4 | Arsenal |
| 5 | Chelsea |
| 6 | Chelsea |
| 7 | Chelsea |
| 8 | Chelsea |

`Passes`

| pass_from | time_stamp | pass_to |
|---:|:---:|---:|
| 1 | 00:05 | 2 |
| 2 | 00:07 | 3 |
| 3 | 00:08 | 4 |
| 4 | 00:10 | 5 |
| 6 | 00:15 | 7 |
| 7 | 00:17 | 8 |
| 8 | 00:20 | 6 |
| 6 | 00:22 | 5 |
| 1 | 00:25 | 2 |
| 2 | 00:27 | 3 |

Output

| team_name | longest_streak |
|---|---:|
| Arsenal | 3 |
| Chelsea | 4 |
