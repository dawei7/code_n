## Spending Table

| Column Name | Type |
|---|---|
| `user_id` | int |
| `spend_date` | date |
| `platform` | enum |
| `amount` | int |

The triple `(user_id, spend_date, platform)` is the composite primary key. Each row records a user's spending through one of the website's applications on one date. `platform` is an enum containing exactly `desktop` and `mobile`.
