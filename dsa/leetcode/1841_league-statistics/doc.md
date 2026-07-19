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

### Required Complexity

- **Time:** $O(m + t\log t)$
- **Space:** $O(m + t)$

<details>
<summary>Approach</summary>

#### General

**Express every match from both perspectives**

A match row stores the home and away sides in different columns, but the requested aggregates are team-centric. Normalize each match with `UNION ALL`: its home perspective contains the home team, home goals as `goal_for`, and away goals as `goal_against`; its away perspective swaps those roles. `UNION ALL` is essential because both perspective rows must remain, even when their numeric values happen to match.

After this transformation, every participating team has exactly one normalized row per match played. The team identifier no longer needs home-versus-away conditionals, while comparing `goal_for` with `goal_against` consistently determines whether that row contributes three, one, or zero points.

**Aggregate the standings**

Join the normalized rows to `Teams`, group by team identity and name, and compute the six requested values. `COUNT(*)` gives matches played. Separate sums give points, goals for, and goals against, while summing each row's goal difference gives the same result as subtracting the two goal totals.

For every original match, normalization creates exactly one row for each participant with mutually reversed goal totals. Therefore each appearance is counted once, each goal enters the scorer's `goal_for` and the opponent's `goal_against`, and the score comparison awards precisely the specified points. Grouping those rows consequently produces exactly the league totals. The final three-key sort implements the complete tie-breaking order.

#### Complexity detail

Normalizing $m$ matches produces $2m$ rows, and joining and aggregating them takes $O(m+t)$ expected work with hash-based execution. Sorting the $t$ standings rows costs $O(t\log t)$, for $O(m+t\log t)$ total time. The normalized relation and grouped standings require $O(m+t)$ working space.

#### Alternatives and edge cases

- **Direct conditional aggregation:** Join a team whenever it appears in either match column and use `CASE` for every metric; this is correct but repeats home/away branching and an `OR` join can be harder to optimize.
- **Correlated subqueries per team:** Independently scan `Matches` for every aggregate and team; this can revisit the match table $O(tm)$ times.
- **`UNION` instead of `UNION ALL`:** Duplicate elimination can incorrectly remove one perspective when the projected rows coincide and adds needless sorting or hashing.
- **Away wins:** Goals and the win comparison must be reversed for the away perspective.
- **Draws:** Equal goal totals award one point to both participants, including `0-0`.
- **Negative difference:** `goal_diff` may be negative and must not be clamped.
- **Repeated opponents:** Reversed home and away fixtures are distinct because their ordered team pair differs.
- **Complete ordering:** Equal points use descending goal difference; only a remaining tie uses ascending team name.

</details>
