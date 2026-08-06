## Actions Table

| Column Name | Type |
|---|---|
| `user_id` | int |
| `post_id` | int |
| `action_date` | date |
| `action` | enum |
| `extra` | varchar |

`Actions` may contain duplicate rows. `action` is an enum containing `view`, `like`, `reaction`, `comment`, `report`, and `share`. `extra` supplies optional action details, such as a report reason or reaction type.
