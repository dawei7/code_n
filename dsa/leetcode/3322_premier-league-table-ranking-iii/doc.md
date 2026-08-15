# Premier League Table Ranking III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3322 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/premier-league-table-ranking-iii/) |

## Problem Description

### Goal

`SeasonStats` contains one row for each team participating in a season, including its match results and goals scored and conceded. Derive two performance measures for every row: `points`, where each win contributes three and each draw contributes one, and `goal_difference`, equal to goals scored minus goals conceded.

Rank teams independently within each season. Greater points take precedence; when points tie, greater goal difference takes precedence; when both measures tie, the alphabetically earlier team name takes precedence. Return every team with its derived measures and one-based position. Order the complete result by `season_id` ascending, then position ascending, then `team_name` ascending.

### Function Contract

**Inputs**

- `SeasonStats(season_id, team_id, team_name, matches_played, wins, draws, losses, goals_for, goals_against)`: One row per `(season_id, team_id)` pair, recording that team's results and goals for the season.

**Return value**

Return columns `season_id`, `team_id`, `team_name`, `points`, `goal_difference`, and `position`. Compute `points` as `wins * 3 + draws`, compute `goal_difference` as `goals_for - goals_against`, and restart position numbering for each season.

### Examples

#### Example 1

- **Input:** The 2021 rows include Manchester City with 29 wins and 6 draws, Liverpool with 28 wins and 8 draws, and three other clubs; the 2022 rows contain another five-club season.
- **Output:** Manchester City leads 2021 with 93 points and a goal difference of 73, Liverpool follows with 92 points, and Manchester City also leads 2022 with 89 points. Each season's remaining teams follow their prescribed ranking criteria.

The two seasons form independent ranking partitions even when the same club appears in both.
