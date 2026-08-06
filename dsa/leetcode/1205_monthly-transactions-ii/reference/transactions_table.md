## Transactions Table

The `Transactions` table has the following schema:

| Column Name | Type |
|---|---|
| `id` | int |
| `country` | varchar |
| `state` | enum |
| `amount` | int |
| `trans_date` | date |

`id` contains unique values. Each row describes an incoming transaction, and `state` is one of `"approved"` or `"declined"`.
