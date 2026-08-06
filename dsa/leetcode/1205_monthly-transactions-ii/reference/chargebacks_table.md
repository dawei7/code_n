## Chargebacks Table

The `Chargebacks` table has the following schema:

| Column Name | Type |
|---|---|
| `trans_id` | int |
| `trans_date` | date |

Each row records an incoming chargeback for an earlier transaction. `trans_id` is a foreign key referencing `Transactions.id`. The referenced transaction may have been either approved or declined.
