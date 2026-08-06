## Description

A bank wants a distribution of how many transactions occur during a visit. A transaction belongs to a visit only when both its `user_id` and date match that visit. For each visit, first determine its transaction count, including zero for a visit with no transactions.

Then report how many visits have each count. The output must contain every integer `transactions_count` from `0` through the largest count achieved by any visit. If no visit has a required intermediate count, its `visits_count` is `0`. Return these buckets in ascending `transactions_count` order.
