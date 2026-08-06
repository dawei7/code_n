## Function Contract

**Database Schema**

**`Transactions`**

| Column | Type | Meaning |
|---|---|---|
| `transaction_id` | int | Unique transaction identifier. |
| `day` | datetime | Date and time of the transaction. |
| `amount` | int | Amount of the transaction. |

**Return value**

Return a table with the single column `transaction_id`. Include every transaction whose `amount` is equal to the maximum amount among all transactions on the same calendar date (`DATE(day)`). Sort the output by `transaction_id` ASC.
