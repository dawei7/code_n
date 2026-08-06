## Scores Table

| Column Name | Type |
|---|---|
| `player_name` | `varchar` |
| `gender` | `varchar` |
| `day` | `date` |
| `score_points` | `int` |

The pair (`gender`, `day`) is the primary key, so a gender has at most one score row on a given day. Each row records the points scored by the named player on that day. A gender of `F` identifies the female team, and `M` identifies the male team.
