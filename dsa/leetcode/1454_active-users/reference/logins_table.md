## Logins Table

`Logins` records the account ID and calendar date for each login event.

| Column Name | Type |
|---|---|
| `id` | `int` |
| `login_date` | `date` |

Duplicate rows are allowed. In particular, one user may log in more than once
on the same day.
