# All the Matches of the League

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2339 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/all-the-matches-of-the-league/) |

## Problem Description

### Goal

The `Teams` table contains the unique name of every team in a league. Every two distinct teams play twice: once with the first team at home and once with the second team at home.

Generate all directed matchups. Each result row names a `home_team` and a different `away_team`, and every ordered pair of distinct teams must appear exactly once. The result rows may be returned in any order.

### Function Contract

**Inputs**

- `Teams`: A table whose `team_name` column contains unique team names.

**Return value**

Return columns `home_team` and `away_team` containing every ordered pair of different teams exactly once. Output order is unrestricted.

### Examples

**Example 1**

- Input: `Teams = [("Leetcode FC"),("Ahly SC"),("Real Madrid")]`
- Output: `[("Real Madrid","Leetcode FC"),("Real Madrid","Ahly SC"),("Leetcode FC","Real Madrid"),("Leetcode FC","Ahly SC"),("Ahly SC","Real Madrid"),("Ahly SC","Leetcode FC")]`

Three teams produce six directed matches because each of the three unordered pairs is played in both home-away orientations.
