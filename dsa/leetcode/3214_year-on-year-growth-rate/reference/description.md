## Description

The `user_transactions` table records individual product purchases with a spend amount and timestamp. Aggregate all transactions for the same product and calendar year to obtain that product's current annual spend.

For every product-year row, report the preceding annual row's total spend for that product. Compute the year-on-year percentage change from the previous total to the current total and round it to two decimal places. A product's first annual row has no previous value, so both `prev_year_spend` and `yoy_rate` are `NULL`.

Return the rows in ascending `product_id` order and, within each product, ascending `year` order.
