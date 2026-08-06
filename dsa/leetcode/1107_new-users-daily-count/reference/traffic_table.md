## Traffic Table

| Column Name | Type |
|---|---|
| `user_id` | int |
| `activity` | enum |
| `activity_date` | date |

Duplicate rows are permitted. The `activity` value is one of `login`, `logout`, `jobs`, `groups`, or `homepage`; `activity_date` records the date of that event for the identified user.
