## Examples

**Example 1**

- **Input:** Qualifying orders in September, October, and December 2020 and January 2021, together with invoices of `20` or less.
- **Output:**
  | month | order_count | customer_count |
  | --- | --- | --- |
  | 2020-09 | 2 | 2 |
  | 2020-10 | 1 | 1 |
  | 2020-12 | 2 | 1 |
  | 2021-01 | 1 | 1 |
- **Explanation:** Invoices equal to `20` are excluded, and the two December orders belong to one customer.

**Example 2**

- **Input:** Three qualifying orders from one customer in the same month.
- **Output:**
  | month | order_count | customer_count |
  | --- | --- | --- |
  | 2020-11 | 3 | 1 |
- **Explanation:** `order_count` is 3 while `customer_count` is 1.

**Example 3**

- **Input:** Only orders whose invoices are at most `20`.
- **Output:** An empty table with headers `month`, `order_count`, `customer_count`.
- **Explanation:** Months with no qualifying orders do not appear.
