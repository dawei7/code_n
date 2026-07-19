## General
**Group relationships by the followed user**

Group the table by `user_id`. Every row in one group represents one distinct follower relationship because the composite primary key forbids duplicates. `COUNT(follower_id)` therefore gives exactly that user's number of followers.

No separate users table participates in the query, so the result contains precisely the `user_id` values represented by at least one relationship. A user absent from `Followers` cannot be inferred and does not produce a zero-count row.

**Name and order the result explicitly**

Alias the aggregate as `followers_count`, then order the grouped rows by `user_id ASC`. The declared primary key begins with `user_id`, allowing an engine to scan relationships in grouping and output order, but the explicit `ORDER BY` remains necessary to make the result contract deterministic.

## Complexity detail
Every one of the $R$ relationships must be inspected because any row can change one user's count. Hash aggregation performs expected constant work per row and stores at most $U$ counters, taking $O(R)$ time and $O(U)$ space. An ordered scan of the composite primary-key index can instead aggregate consecutive users while already producing ascending order.

## Alternatives and edge cases
- **Correlated count per user:** Selecting distinct users and rescanning `Followers` for each one can take $O(RU)$ time without a suitable index.
- **Window count plus deduplication:** A window function can attach the group count to every relationship, but an additional distinct step is needed to return one row per user.
- **Single relationship:** Its user receives a follower count of one.
- **Shared follower:** One `follower_id` may follow several users and contributes once to each corresponding group.
- **Nonconsecutive identifiers:** Grouping and numeric ordering do not assume contiguous user IDs.
- **Duplicate relationship:** The primary key rules it out, so ordinary `COUNT` is sufficient; `COUNT(DISTINCT follower_id)` is unnecessary.
- **Missing users:** With no separate user table, users having zero recorded followers do not appear.
