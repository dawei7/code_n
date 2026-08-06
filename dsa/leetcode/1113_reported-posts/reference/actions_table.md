## Actions Table

| Column Name | Type |
|---|---|
| `user_id` | int |
| `post_id` | int |
| `action_date` | date |
| `action` | enum |
| `extra` | varchar |

Duplicate rows are permitted. The `action` value is one of `view`, `like`, `reaction`, `comment`, `report`, or `share`. The optional `extra` value supplies action-specific information, such as a report reason or reaction type.
