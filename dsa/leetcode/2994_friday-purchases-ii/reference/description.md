## Description

The `Purchases` table records a user, a purchase date, and an amount. Every
date is between November 1 and November 30, 2023, inclusive, and the triple
`(user_id, purchase_date, amount_spend)` is unique.

Report total user spending on each Friday of November 2023. All four Fridays
must appear: when no purchase occurred on a Friday, its total is `0`. Return
the one-based `week_of_month`, the Friday `purchase_date`, and `total_amount`,
ordered by week ascending.
