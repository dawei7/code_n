# Team Scores in Football Tournament

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1212 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/team-scores-in-football-tournament/) |

## Problem Description

### Goal

The `Teams` table contains one row for each football team and uniquely identifies it by `team_id`. The `Matches` table records finished matches between two different registered teams, naming the host and guest team IDs and the goals scored by each side; `match_id` is unique.

Compute every team's tournament score after all matches. A win awards three points, a draw awards one point to each team, and a loss awards no points. Teams that played no match must still appear with zero points. Return `team_id`, `team_name`, and `num_points`, ordered by decreasing points and then by increasing `team_id` when scores tie.

### Function Contract

**Input tables**

- `Teams(team_id, team_name)`: `team_id` is unique and each row represents one team.
- `Matches(match_id, host_team, guest_team, host_goals, guest_goals)`: `match_id` is unique; host and guest are different IDs from `Teams`.
- Let $t$ be the number of teams and $m$ the number of matches.

**Return value**

- One row per team with columns `team_id`, `team_name`, and `num_points`, sorted by `num_points DESC, team_id ASC`.

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

Two teams that draw each receive one point.

**Example 3**

A team absent from both host and guest columns still appears with zero points.

### Required Complexity

- **Time:** $O(t+m)$
- **Space:** $O(t+m)$

<details>
<summary>Approach</summary>

#### General

**View every match from both sides.** Emit one point event for `host_team` and one for `guest_team`. A host event awards 3, 1, or 0 according to whether `host_goals` is greater than, equal to, or less than `guest_goals`. The guest event applies the symmetric comparison.

**Aggregate events by team ID.** Combining these two projections with `UNION ALL` preserves both teams' contributions from every match. Grouping by the emitted team ID and summing points produces exactly each participating team's total.

**Restore the complete team catalog.** Left join `Teams` to the point events before grouping, or to their totals afterward. A team with no event then has a null sum, which `COALESCE` converts to zero. Grouping with the catalog also supplies the team name.

**Apply the standings order.** Sort the final rows by total points descending. For equal totals, sort `team_id` ascending. This explicitly implements both levels of the required order rather than relying on group output order.

#### Complexity detail

The event stream contains exactly $2m$ rows. Building it, aggregating it, and joining the $t$ team rows take $O(t+m)$ logical time with hash aggregation and indexed or hash joins. The event and grouping state can occupy $O(t+m)$ space. Physical engines may choose different join or sort plans.

#### Alternatives and edge cases

- **Join with `team_id = host_team OR team_id = guest_team`:** This is concise and correct, but an optimizer may use a nested comparison of teams and matches, taking $O(tm)$ time.
- **Two separate aggregates joined to Teams:** Host and guest totals can be computed independently and added, but null handling becomes more verbose.
- **Idle team:** The left join and `COALESCE` are necessary to return zero points.
- **Draw:** Both perspective events must award one point.
- **Away win:** The guest event, not the host event, receives three points.
- **No negative scores:** A loss contributes zero rather than subtracting points.
- **Tied standings:** Smaller `team_id` comes first regardless of team name.

</details>
