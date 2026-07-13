# Team Scores in Football Tournament

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1212 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [team-scores-in-football-tournament](https://leetcode.com/problems/team-scores-in-football-tournament/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/team-scores-in-football-tournament/).

### Goal
Compute the tournament standings for every team. Each match gives 3 points to the winner, 1 point to each team in a draw, and 0 points to the loser. Teams with no matches must still appear with 0 points.

### Query Contract
**Input tables**

- `Teams(team_id, team_name)`: Team identifiers and names.
- `Matches(match_id, host_team, guest_team, host_goals, guest_goals)`: Finished games with the two team ids and their goals.

**Output columns**

- `team_id`
- `team_name`
- `num_points`

### Examples
**Example 1**

`Teams`

| team_id | team_name |
|---:|---|
| 10 | Leetcode FC |
| 20 | NewYork FC |
| 30 | Atlanta FC |
| 40 | Chicago FC |
| 50 | Toronto FC |

`Matches`

| match_id | host_team | guest_team | host_goals | guest_goals |
|---:|---:|---:|---:|---:|
| 1 | 10 | 20 | 3 | 0 |
| 2 | 30 | 10 | 2 | 2 |
| 3 | 10 | 50 | 5 | 1 |
| 4 | 20 | 30 | 1 | 0 |
| 5 | 50 | 30 | 1 | 0 |

Output:

| team_id | team_name | num_points |
|---:|---|---:|
| 10 | Leetcode FC | 7 |
| 20 | NewYork FC | 3 |
| 50 | Toronto FC | 3 |
| 30 | Atlanta FC | 1 |
| 40 | Chicago FC | 0 |

**Example 2**

If two teams have equal points, the smaller `team_id` is listed first.

**Example 3**

A team with no hosted or guest matches is still returned with `num_points = 0`.

---

## Solution
### Approach
Convert each match into two point rows: one from the host team's perspective and one from the guest team's perspective. Award points with a `CASE` expression based on the two goal counts, aggregate by team, and left join that aggregate to `Teams` so teams without matches receive 0.

Finally order by `num_points DESC, team_id ASC`.

### Complexity Analysis
- **Time Complexity**: Database dependent; logically linear in the number of match-team rows plus the team rows after grouping.
- **Space Complexity**: Database dependent; the grouped point totals store one aggregate row per team that appeared in a match.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
