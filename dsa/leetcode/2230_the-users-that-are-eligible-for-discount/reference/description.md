## Description

The `Purchases` table records each user's purchase timestamp and paid amount. Its composite primary key is (`user_id`, `time_stamp`), so a user cannot have two rows at the same instant.

Given `startDate`, `endDate`, and `minAmount`, report every user who made at least one purchase both within the inclusive interval from `startDate` through `endDate` and for an amount of at least `minAmount`. Each date parameter denotes the start of its day: in particular, the upper boundary is `endDate` at `00:00:00`, not the end of that calendar day. Return qualifying IDs once in ascending order.
