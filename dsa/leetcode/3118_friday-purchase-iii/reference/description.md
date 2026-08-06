## Description

The `Purchases` table records a user, a November 2023 purchase date, and the amount spent. Its composite primary key is (`user_id`, `purchase_date`, `amount_spend`). The `Users` table maps each unique `user_id` to one of the membership categories `Standard`, `Premium`, or `VIP`.

For each of the four Fridays in November 2023, calculate the total amount spent separately by `Premium` and `VIP` members. Every Friday-membership pair must appear even when its total is zero. Return `week_of_month`, `membership`, and `total_amount`, ordered by `week_of_month` and then by `membership`, both in ascending order.
