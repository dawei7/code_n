## Activity Table

| Column Name | Type |
|---|---|
| `user_id` | int |
| `session_id` | int |
| `activity_date` | date |
| `activity_type` | enum |

Duplicate rows are allowed. `activity_type` is one of `open_session`, `end_session`, `scroll_down`, or `send_message`. Each row records one activity on a social-media website, and every session belongs to exactly one user.
