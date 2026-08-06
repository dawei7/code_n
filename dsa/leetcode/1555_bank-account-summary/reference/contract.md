## Function Contract

**Inputs**

- `Users`: Table with columns `user_id` (int), `user_name` (varchar), `credit` (int).
- `Transactions`: Table with columns `trans_id` (int), `paid_by` (int), `paid_to` (int), `amount` (int), `transacted_on` (date).

**Return value**

Return a table with columns `user_id` (int), `user_name` (varchar), `credit` (int), and `credit_limit_breached` (varchar `"Yes"` or `"No"`).
