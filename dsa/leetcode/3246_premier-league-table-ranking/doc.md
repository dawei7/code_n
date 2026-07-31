# Premier League Table Ranking

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3246 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/premier-league-table-ranking/) |

## Problem Description

### Goal

The `TeamStats` table contains one row per football team. For each team, calculate its league points as three points per win plus one point per draw; losses add no points.

Assign a competition position by descending points. Teams with equal point totals share the same position, and the next position must account for every preceding row. For example, two teams tied at position 1 are followed by position 3, not position 2.

Return `team_id`, `team_name`, `points`, and `position`. Sort the result by points from greatest to least, then alphabetically by `team_name` among tied teams.

### Function Contract

**Input table**

`TeamStats`

- `team_id`: The unique integer identifier of a team.
- `team_name`: The team's name.
- `matches_played`: Its number of matches.
- `wins`: Its number of wins.
- `draws`: Its number of draws.
- `losses`: Its number of losses.

**Return value**

- One row per team with columns `team_id`, `team_name`, `points`, and `position`, in the required points/name order.

### Examples

**Example 1**

- Input: `TeamStats = [(1,"Manchester City",10,6,2,2),(2,"Liverpool",10,6,2,2),(3,"Chelsea",10,5,3,2),(4,"Arsenal",10,4,4,2),(5,"Tottenham",10,3,5,2)]`
- Output: `[(2,"Liverpool",20,1),(1,"Manchester City",20,1),(3,"Chelsea",18,3),(4,"Arsenal",16,4),(5,"Tottenham",14,5)]`

**Example 2**

- Input: `TeamStats = [(1,"Alpha",3,0,3,0),(2,"Beta",1,1,0,0)]`
- Output: `[(1,"Alpha",3,1),(2,"Beta",3,1)]`

**Example 3**

- Input: `TeamStats = [(1,"Zulu",2,0,0,2),(2,"Ajax",2,0,0,2)]`
- Output: `[(2,"Ajax",0,1),(1,"Zulu",0,1)]`
