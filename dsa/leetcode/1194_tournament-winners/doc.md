# Tournament Winners

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1194 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [tournament-winners](https://leetcode.com/problems/tournament-winners/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/tournament-winners/).

### Goal
For each tournament group, find the player with the highest total score across all matches. If several players in a group tie, choose the smallest `player_id`.

### Query Contract
**Input tables**

- `Players(player_id, group_id)`: Player group assignments.
- `Matches(match_id, first_player, second_player, first_score, second_score)`: Match results.

**Output columns**

- `group_id`
- `player_id`

### Examples
**Example 1**

`Players`

| player_id | group_id |
|---:|---:|
| 15 | 1 |
| 25 | 1 |
| 30 | 1 |
| 45 | 1 |
| 10 | 2 |
| 35 | 2 |
| 50 | 2 |
| 20 | 3 |
| 40 | 3 |

`Matches`

| match_id | first_player | second_player | first_score | second_score |
|---:|---:|---:|---:|---:|
| 1 | 15 | 45 | 3 | 0 |
| 2 | 30 | 25 | 1 | 2 |
| 3 | 30 | 15 | 2 | 0 |
| 4 | 40 | 20 | 5 | 2 |
| 5 | 35 | 50 | 1 | 1 |

Output:

| group_id | player_id |
|---:|---:|
| 1 | 15 |
| 2 | 35 |
| 3 | 40 |

---

## Solution
### Approach
Normalize match scores into one row per player per match using `UNION ALL`, then aggregate scores per player. Join to `Players` for the group, rank players inside each group by total score descending and `player_id` ascending, and keep rank `1`.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, match score rows are expanded and grouped by player.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
