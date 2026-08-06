## Description

The `Transactions` table records individual purchases. Every `transaction_id` is unique, and each customer-date pair is unique, so a customer has at most one transaction on a calendar day.

For each customer, divide their transaction dates into maximal streaks in which every date is exactly one day after the preceding date. Find the greatest streak length across the entire table and return the `customer_id` attached to every streak having that length, sorted by `customer_id` in ascending order. The judge preserves one row per winning streak; therefore, if one customer owns multiple separate globally longest streaks, that identifier appears multiple times.

The transaction `amount` does not affect whether dates are consecutive.
