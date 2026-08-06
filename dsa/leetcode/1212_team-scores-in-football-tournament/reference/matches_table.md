## Matches Table

The `Matches` table has the following schema:

| Column Name | Type |
|---|---|
| `match_id` | int |
| `host_team` | int |
| `guest_team` | int |
| `host_goals` | int |
| `guest_goals` | int |

`match_id` contains unique values. Every row describes one finished match between two different teams. `host_team` and `guest_team` identify rows in `Teams` by `team_id`; `host_goals` and `guest_goals` are the respective goal totals.
