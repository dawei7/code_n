## Function Contract

**Database Schema**

**`Store`**

| Column | Type | Meaning |
|---|---|---|
| `bill_id` | int | Unique bill identifier. |
| `customer_id` | int | Customer identifier. |
| `amount` | int | Amount of the bill. |

**Return value**

Return a single-row table with column `rich_count`. `rich_count` is the count of distinct `customer_id` values having at least one bill with `amount > 500`.
