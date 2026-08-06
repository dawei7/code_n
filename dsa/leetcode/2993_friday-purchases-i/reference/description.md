## Description

The `Purchases` table records a user, a purchase date, and an amount. Every
date lies between November 1 and November 30, 2023, inclusive, and the triple
`(user_id, purchase_date, amount_spend)` is unique.

For each Friday in that month having at least one purchase, sum all spending
on that date. Return its one-based `week_of_month`, the `purchase_date`, and
the `total_amount`. Weeks without a Friday purchase must not appear. Order the
result by week of month ascending.
