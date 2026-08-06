## Transactions Table

| Column Name | Type |
|---|---|
| `user_id` | `int` |
| `transaction_date` | `date` |
| `amount` | `int` |

Duplicate rows are allowed because each row represents a separate transaction. Every transaction is guaranteed to belong to a recorded visit: `Visits` contains the pair (`user_id`, `transaction_date`).
