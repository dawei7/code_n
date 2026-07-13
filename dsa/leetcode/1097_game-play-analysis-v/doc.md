# Game Play Analysis V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1097 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [game-play-analysis-v](https://leetcode.com/problems/game-play-analysis-v/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/game-play-analysis-v/).

### Goal
For each install date, report how many players installed on that date and the day-one retention rate: the fraction of those players who logged in again exactly one day after their install date.

### Query Contract
**Input table**

- `Activity(player_id, device_id, event_date, games_played)`: Player activity records.

**Output columns**

- `install_dt`
- `installs`
- `Day1_retention`

### Examples
**Example 1**

`Activity`

| player_id | device_id | event_date | games_played |
|---:|---:|---|---:|
| 1 | 2 | 2016-03-01 | 5 |
| 1 | 2 | 2016-03-02 | 6 |
| 2 | 3 | 2017-06-25 | 1 |
| 3 | 1 | 2016-03-02 | 0 |
| 3 | 4 | 2018-07-03 | 5 |

Output:

| install_dt | installs | Day1_retention |
|---|---:|---:|
| 2016-03-01 | 1 | 1.00 |
| 2016-03-02 | 1 | 0.00 |
| 2017-06-25 | 1 | 0.00 |
| 2018-07-03 | 1 | 0.00 |

---

## Solution
### Approach
First find each player's install date with `MIN(event_date)`. Then left join those install rows to activity records for the same player on `install_dt + 1 day`. Group by install date, count installs, and divide retained players by installs.

The retention value should be rounded to two decimal places.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query groups activity by player and joins back to next-day activity.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
