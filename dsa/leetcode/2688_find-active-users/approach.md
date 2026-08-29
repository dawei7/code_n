## General

**Sort each user's purchases chronologically**

An active user needs at least one pair of purchases no more than seven days apart.

The window expression:

`LAG(created_at, 1) OVER (PARTITION BY user_id ORDER BY created_at)`

examines purchases separately for each user and orders that user's rows by timestamp. For every row except the first in its partition, it exposes the immediately preceding purchase time as `prev_created_at`.

Partitioning prevents a purchase from one user being compared with another user's purchase.

**Why checking only adjacent purchases is sufficient**

At first, “within seven days of any other purchase” sounds as though every pair must be tested.

Suppose some earlier purchase $A$ and later purchase $B$ are within seven days. Let $P$ be the purchase immediately before $B$ in chronological order. Because $P$ is no earlier than $A$:

$$
B-P\le B-A\le7\text{ days}.
$$

Therefore $B$ and its immediate predecessor also form a qualifying pair.

Conversely, any adjacent pair within seven days is plainly a pair of the user's purchases. So adjacent comparison detects existence exactly and avoids a quadratic self-join.

**Build a derived table because the lag value is computed**

The inner query returns `user_id`, `created_at`, and the window result `prev_created_at` for every purchase row.

The surrounding derived table is named `t`. The next query level can then filter using the computed alias.

This layering is useful in MySQL because a window-function result is conceptually produced after the ordinary `WHERE` phase of the same query block and cannot simply be filtered there as though it were a base column.

**Measure the calendar-day gap**

`DATEDIFF(created_at, prev_created_at)` returns the difference in days between the current and previous timestamp's dates.

Because rows are ordered ascending inside each user partition, the current row is not earlier than its predecessor. The relevant differences are nonnegative.

The predicate uses `<= 7`, so a gap of exactly seven days qualifies. A same-day repeated purchase has difference zero and also qualifies.

**Why the first purchase is ignored**

The first chronological row for a user has no predecessor, so `LAG` returns `NULL`.

`DATEDIFF(created_at, NULL)` is `NULL`, and the comparison `NULL <= 7` is unknown rather than true. That row is excluded automatically.

A user with only one purchase therefore cannot appear in the active set.

**Deduplicate active user IDs**

A user may have several adjacent pairs within seven days. The inner filtering could therefore produce the same `user_id` multiple times.

The outermost query uses `SELECT DISTINCT user_id` so each active user appears once.

The problem permits any output order, so no `ORDER BY` is needed.

**What the outer `IN` query does**

The middle subquery produces the set of user IDs having at least one qualifying adjacent gap.

The outer query scans `Users` and retains rows whose `user_id` belongs to that set, then `DISTINCT` collapses repeats.

The same output could be selected directly from the derived table, but the exact source uses membership. It remains correct because every ID in the active set necessarily exists in `Users`.

**Trace an active user**

Suppose user 6 purchased on September 10 and September 14.

After ordering, the September 10 row has no predecessor. The September 14 row receives September 10 as `prev_created_at`.

`DATEDIFF` is four, which satisfies `<= 7`. User 6 enters the membership set and appears once in the final output.

**Trace a non-active user**

Suppose user 4 purchased on September 2 and September 13.

The adjacent gap is 11 days, so it fails. With no other purchases, no row for user 4 survives the middle filter, and the outer membership test excludes that user.

**Duplicate records and equal timestamps**

The table may contain duplicate records. Two purchases for the same user at the same timestamp appear as adjacent rows after ordering.

Their gap is zero, so the user is active. This matches the row-based purchase interpretation: a second purchase occurred within seven days, even if all recorded fields happen to match.


For each user, `LAG` pairs every purchase after the first with its immediate chronological predecessor. The adjacent-pair lemma proves that some pair lies within seven days exactly when at least one of these predecessor gaps is at most seven.

The middle filter identifies precisely those witnessing rows, the membership subquery identifies precisely their users, and `DISTINCT` returns each such user once. Therefore the output is exactly the active-user set.

## Complexity detail

Let $R$ be the number of purchase rows. Partition ordering can require sorting the rows, giving $O(R\log R)$ time in the absence of a suitable index. Window evaluation, filtering, and deduplication are linear or sorting/hash-based within that bound.

The ordered window result and deduplication state can require $O(R)$ space. A database engine may instead exploit indexes, external sorting, hashing, or disk spill, but $O(R)$ is the safe logical bound.

## Alternatives and edge cases

- **Self-join every user's purchase pairs:** Correct but can create $O(R^2)$ candidate pairs for a prolific user.
- **Correlated existence subquery:** Expresses the condition directly but may repeat searches without an effective index.
- **Select directly from the lag-derived table:** Can eliminate the outer `IN` scan while preserving the same adjacent-gap reasoning.
- **User with one purchase:** Has no predecessor and is not active.
- **Gap exactly seven days:** Qualifies because the predicate is inclusive.
- **Gap greater than seven days:** Does not qualify.
- **Same timestamp:** Difference zero, so duplicate purchase rows make the user active.
- **Many qualifying pairs:** `DISTINCT` emits the user only once.
- **Different users with nearby dates:** Never compare because `PARTITION BY user_id` separates them.
- **First partition row:** Its null predecessor is naturally filtered out.
- **Datetime values:** MySQL `DATEDIFF` compares date portions in calendar days.
- **Any output order:** No final sorting is required.
