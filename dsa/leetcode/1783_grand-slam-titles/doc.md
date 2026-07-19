# Grand Slam Titles

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/grand-slam-titles/) |
| Frontend ID | 1783 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Players` table identifies tennis players by a unique `player_id` and records each player's name. The `Championships` table has one row per year. Its four tournament columns—`Wimbledon`, `Fr_open`, `US_open`, and `Au_open`—each store the `player_id` of that year's winner.

Report how many Grand Slam tournaments each player won across all years and all four tournament columns. A player who won several tournaments in one year receives credit for every title. Exclude players who never won a tournament, and return each remaining player's identifier, name, and total as `grand_slams_count`. The result rows may be in any order.

### Function Contract

**Inputs**

- `Players(player_id, player_name)`: one row per player; `player_id` is the primary key.
- `Championships(year, Wimbledon, Fr_open, US_open, Au_open)`: one row per year; `year` is the primary key, and each tournament column contains its champion's player ID.

Let $C$ be the number of championship rows and $K$ the number of distinct players who won at least one listed tournament.

**Return value**

- Return the columns `player_id`, `player_name`, and `grand_slams_count`.
- Include exactly the $K$ winning players. `grand_slams_count` counts occurrences of their ID across all four tournament columns and all years.
- Result order is unrestricted.

### Examples

**Example 1**

- Input: `Players = [[1,"Nadal"],[2,"Federer"],[3,"Novak"]]`, `Championships = [[2018,1,1,1,1],[2019,1,1,2,2],[2020,2,1,2,2]]`
- Output: `[[1,"Nadal",7],[2,"Federer",5]]`

Nadal's ID appears seven times and Federer's appears five times. Novak has no title and is omitted.

**Example 2**

- Input: `Players = [[7,"Serena"],[8,"Venus"]]`, `Championships = [[2021,7,7,7,7]]`
- Output: `[[7,"Serena",4]]`

Winning all four tournaments in one year contributes four titles.

**Example 3**

- Input: `Players = [[1,"A"],[2,"B"],[3,"C"],[4,"D"]]`, `Championships = [[2024,1,2,3,4]]`
- Output: `[[1,"A",1],[2,"B",1],[3,"C",1],[4,"D",1]]`

Each tournament column contributes its winner independently.
