# Year on Year Growth Rate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3214 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/year-on-year-growth-rate/) |

## Problem Description

### Goal

The `user_transactions` table records individual product purchases with a spend amount and timestamp. Aggregate all transactions for the same product and calendar year to obtain that product's current annual spend.

For every product-year row, report the preceding annual row's total spend for that product. Compute the year-on-year percentage change from the previous total to the current total and round it to two decimal places. A product's first annual row has no previous value, so both `prev_year_spend` and `yoy_rate` are `NULL`.

Return the rows in ascending `product_id` order and, within each product, ascending `year` order.

### Function Contract

**Inputs**

The `user_transactions` table contains:

- `transaction_id`: An integer uniquely identifying the transaction.
- `product_id`: The integer product identifier.
- `spend`: The transaction's decimal spend amount.
- `transaction_date`: The transaction timestamp.

Let $t$ be the number of transaction rows and $g$ the number of distinct product-year groups.

**Return value**

- Columns `year`, `product_id`, `curr_year_spend`, `prev_year_spend`, and `yoy_rate`, ordered by `product_id` and `year` ascending.
- For a nonzero previous total $P$ and current total $C$, `yoy_rate` is $\operatorname{round}(100(C-P)/P,2)$.

### Examples

#### Example 1

For product `123424`, annual spends of `1500.60`, `1000.20`, `1246.44`, and `2145.32` from 2019 through 2022 produce:

| year | product_id | curr_year_spend | prev_year_spend | yoy_rate |
|---:|---:|---:|---:|---:|
| 2019 | 123424 | 1500.60 | NULL | NULL |
| 2020 | 123424 | 1000.20 | 1500.60 | -33.35 |
| 2021 | 123424 | 1246.44 | 1000.20 | 24.62 |
| 2022 | 123424 | 2145.32 | 1246.44 | 72.12 |
