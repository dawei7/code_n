## Description

The `Purchases` table records retailer transactions. Each row has a unique `purchase_id`, the `user_id` that made the purchase, and its `purchase_date`.

Report every user who has at least one pair of distinct purchases whose dates are at most seven days apart. Purchases on the same date qualify, as does a pair exactly seven days apart. Return each qualifying `user_id` once, with the result ordered by `user_id`.
