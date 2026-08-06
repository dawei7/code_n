## Description

The system runs one independent task every day. Each task has one of two outcomes: it either fails or succeeds.

Within the inclusive period from `2019-01-01` through `2019-12-31`, divide the recorded days into continuous intervals that share the same outcome. Report an interval's `period_state` as `failed` when all of its tasks failed and as `succeeded` when all of its tasks succeeded. Represent each interval by its first date, `start_date`, and its last date, `end_date`.

Return the intervals in ascending order of `start_date`.
