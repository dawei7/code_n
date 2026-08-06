## Matches Table

The `Matches` table has the following schema:

| Column Name | Type |
|---|---|
| `match_id` | int |
| `first_player` | int |
| `second_player` | int |
| `first_score` | int |
| `second_score` | int |

`match_id` is the table's primary key. Each row identifies a match's two participants through `first_player` and `second_player`, then records their respective point totals in `first_score` and `second_score`. Both players in any one match belong to the same group.
