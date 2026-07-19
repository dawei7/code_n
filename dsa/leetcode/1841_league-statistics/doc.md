# League Statistics

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/league-statistics/) |
| Frontend ID | 1841 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Teams` table identifies the clubs in a league, while `Matches` records each played fixture, its home and away participants, and both goal totals. A team earns three points for a win, one point for a draw, and no points for a loss.

Build the standings from every played match. For each participating team, report its name, number of appearances, total points, goals scored, goals conceded, and goal difference. Rank teams by points descending, then goal difference descending, and finally team name in lexicographical order.

### Function Contract

**Inputs**

- `Teams(team_id, team_name)`:
  - `team_id` is the table's primary key.
  - `team_name` identifies the team.
- `Matches(home_team_id, away_team_id, home_team_goals, away_team_goals)`:
  - `(home_team_id, away_team_id)` is the table's composite primary key.
  - Each row gives the participants and final goal totals for one played match.
- Let $t$ be the number of participating teams and $m$ the number of matches.

**Return value**

- Return the columns `team_name`, `matches_played`, `points`, `goal_for`, `goal_against`, and `goal_diff`, in that order.
- Count a match once for each of its two teams.
- Award three points for a win, one for a draw, and zero for a loss.
- For each team, `goal_diff` equals `goal_for - goal_against`.
- Order rows by `points` descending, then `goal_diff` descending, then `team_name` ascending.

### Examples

**Example 1**

`Teams`

| team_id | team_name |
|---:|---|
| 1 | Ajax |
| 4 | Dortmund |
| 6 | Arsenal |

`Matches`

| home_team_id | away_team_id | home_team_goals | away_team_goals |
|---:|---:|---:|---:|
| 1 | 4 | 0 | 1 |
| 1 | 6 | 3 | 3 |
| 4 | 1 | 5 | 2 |
| 6 | 1 | 0 | 0 |

Output:

| team_name | matches_played | points | goal_for | goal_against | goal_diff |
|---|---:|---:|---:|---:|---:|
| Dortmund | 2 | 6 | 6 | 2 | 4 |
| Arsenal | 2 | 2 | 3 | 3 | 0 |
| Ajax | 4 | 2 | 5 | 9 | -4 |

Dortmund's two wins produce six points. Arsenal and Ajax both have two points, so Arsenal's higher goal difference places it first.

**Example 2**

If Alpha defeats Beta `2-0`, Alpha has one match, three points, and goal difference $2$; Beta has one match, no points, and goal difference $-2$.

**Example 3**

When two teams draw `0-0`, each receives one point and has goal difference $0$. Their names break the remaining standings tie.
