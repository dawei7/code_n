## General

**Reduce all possible pairs to neighboring dates**

For one user, imagine sorting all purchase rows by `purchase_date`. The requirement asks whether any two dates differ by at most seven days. It may seem necessary to compare every pair, but sorted order makes only neighboring dates necessary.

Suppose two non-neighboring dates `a` and `b` are at most seven days apart. Every date between them lies inside the same seven-day interval. In particular, an adjacent pair somewhere from `a` through `b` has a gap no larger than `b - a`, and therefore no larger than seven days. Thus, the existence of any qualifying pair guarantees a qualifying adjacent pair.

The reverse is immediate: an adjacent pair is still a pair of purchases. If its gap is at most seven, the user qualifies. Checking consecutive sorted dates is therefore both sufficient and necessary.

**Use a window function to find each previous purchase**

The common table expression `t` selects every `user_id` and computes

`LAG(purchase_date, 1) OVER (PARTITION BY user_id ORDER BY purchase_date)`.

`PARTITION BY user_id` creates a separate ordered sequence for each user. Purchases from different users never become neighbors. `ORDER BY purchase_date` puts that user's rows in chronological order, and `LAG(..., 1)` returns the date from the immediately preceding row.

For a user's earliest purchase, no preceding row exists, so `LAG` returns `NULL`. That row cannot establish a pair and should not qualify anyone by itself.

When several purchases occur on the same date, their tie order is immaterial. At least one tied row follows another tied row, producing a zero-day gap. The unique `purchase_id` is not needed as a secondary order key because every order among equal dates yields the same date difference.

**Turn neighboring dates into day gaps**

The expression `DATEDIFF(purchase_date, previous_date)` subtracts the previous date from the current date and returns the number of calendar days. Because the rows are sorted ascending, this value is nonnegative.

The CTE names the result `d`. A same-day pair has `d = 0`, purchases exactly one week apart have `d = 7`, and both satisfy the “at most seven days” wording.

For the first row in each partition, the previous date is `NULL`, so `DATEDIFF` also yields `NULL`. In SQL's three-valued logic, `NULL <= 7` is not true, and the later `WHERE` clause discards it automatically.

**Filter qualifying gaps and return one row per user**

The outer query reads the computed rows and applies `WHERE d <= 7`. Each surviving row proves that its user has a purchase and an immediately preceding purchase within the allowed gap.

A user might have several qualifying neighboring pairs. `SELECT DISTINCT user_id` collapses those multiple proof rows to one output row, as required. Finally, `ORDER BY user_id` produces increasing IDs.

**Why every output user qualifies**

Any returned ID came from a CTE row with `d <= 7`. That row has a non-null previous purchase from the same `user_id` because `LAG` never crosses partitions. The two purchase dates are in chronological order and differ by at most seven days. They are two table rows, so the user satisfies the contract.

**Why every qualifying user is returned**

Take a user with any two qualifying purchases. Sort all of that user's purchase dates. If the qualifying pair is adjacent, its later row directly has `d <= 7`. If other purchases lie between them, at least one neighboring gap within that interval is no greater than the total qualifying gap. That later neighboring row passes the filter.

The user's ID therefore appears among the filtered rows and survives `DISTINCT` exactly once. No qualifying user is missed.

**Trace the example**

User `2` has dates March 13, March 20, and June 8 after sorting. The first gap is seven days, so the March 20 row passes. The much larger later gap does not matter because one valid pair is enough.

User `7` has two purchases on June 19. One tied row receives the other as its lag date and produces `DATEDIFF = 0`, so user `7` passes. User `5` has only one row; its lag is null and it does not pass.

The CTE is not materialized by every database engine; it is a logical way to name the window result so the outer query can filter it.

## Complexity detail

Let `r` be the number of rows in `Purchases`. Computing `LAG` requires rows to be ordered by `user_id` partitions and `purchase_date`. Without a supporting index or already useful physical order, sorting dominates at `O(r \log r)` time. Window evaluation, filtering, and scanning are linear after ordering.

`DISTINCT` and final ordering can also require sorting or hashing, bounded by `O(r \log r)` time in the worst case. The overall declared complexity is `O(r \log r)`.

The database may use `O(r)` working space for sorting, window state, and distinct processing. Exact physical memory and disk-spill behavior depend on MySQL's execution plan and indexes, but `O(r)` is the logical auxiliary bound used by the manifest.

## Alternatives and edge cases

- **Self-join every user's purchases:** Join two rows on equal `user_id` and a date gap at most seven. It is straightforward but can generate quadratically many row pairs for a user with many purchases.
- **Correlated existence subquery:** Test each row for another qualifying row. An optimizer and suitable index may execute it well, but the window formulation directly exploits sorted adjacency.
- **Compare only minimum and maximum dates:** A user can have a close pair amid a much wider overall span, so the extremes alone are insufficient.
- **Same-day purchases:** `DATEDIFF` is zero, and zero is correctly within seven days.
- **Exactly seven days:** The inclusive comparison `<= 7` admits the boundary.
- **Eight days:** It fails the condition.
- **Only one purchase:** `LAG` is null and the user is absent.
- **Many qualifying pairs:** `DISTINCT` ensures one output row per user.
- **Equal-date tie ordering:** Any order among tied rows creates a zero gap between neighboring tied purchases, so no secondary key is required for correctness.
- **Partition boundary:** `PARTITION BY user_id` prevents one user's last purchase from becoming another user's previous date.
- **First row null:** SQL does not treat null as zero; `WHERE d <= 7` discards it.
- **Required ordering:** `DISTINCT` alone does not guarantee order. The final `ORDER BY user_id` is necessary.
