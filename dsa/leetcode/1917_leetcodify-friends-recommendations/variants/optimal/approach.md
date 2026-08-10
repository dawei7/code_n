## General

**Make existing friendship directional.** Recommendations must contain both directions, but existing friendships must block both directions. CTE `T` keeps every stored `user1_id -> user2_id` pair and unions its reversal. A correlated lookup can then test an ordered candidate pair directly.

**Pair listen rows sharing one song and day.** The comma-separated `Listens AS l1, Listens AS l2` is a self cross join constrained by the `WHERE` clause. Requiring equal `day` and `song_id` retains pairs of users who listened to the same song on the same date. `l1.user_id != l2.user_id` excludes pairing a user with themselves.

Because the join is directional, a match between users one and three generates both `1 -> 3` and `3 -> 1`. This naturally supplies the unidirectional output requirement.

**Exclude already-friends pairs.** The correlated `NOT EXISTS` searches `T` for the exact ordered pair. If found, the candidate is removed before aggregation. Since `T` contains both directions, storage order in `Friendship` cannot let a friend pair slip through.

**Group by day before counting common songs.** `GROUP BY l1.day, l1.user_id, l2.user_id` creates one group for a directed user pair on one date. This is crucial: three common songs spread across different days do not qualify. `HAVING COUNT(DISTINCT l1.song_id) >= 3` requires at least three distinct shared songs within that single day.

The `Listens` table may contain duplicates. A raw count would let repeated rows for one song inflate the threshold, and the self join could multiply duplicates from both users. `COUNT(DISTINCT ...)` collapses all such copies to one common song.

**Remove repeated recommendations across qualifying days.** A pair may share three songs on several dates. Grouping produces one qualifying row per day, but the final result must contain the directed recommendation only once. `SELECT DISTINCT l1.user_id, l2.user_id` removes those cross-day duplicates.

**Trace the example.** Users one and three share songs 10, 11, and 12 on March 15 and are absent from friendship `T`, so both directions survive and meet the distinct-song count. Users one and two share the same songs but their directed pairs exist in `T` and are excluded. User five listened on another day, so equal-day join conditions prevent a match.

**Why every result is valid.** A returned group contains two distinct nonfriends, at least three distinct equal song IDs, and one common day. Conversely, any ordered nonfriend pair meeting the definition creates self-join rows for those songs, survives the anti-friend test, satisfies `HAVING`, and appears after deduplication.

**Understand the two levels of deduplication.** `COUNT(DISTINCT l1.song_id)` deduplicates evidence *inside one day-specific group* so repeated listens do not fake three songs. Outer `SELECT DISTINCT` deduplicates the *recommendation row across groups* so several qualifying days do not repeat the same directed pair. Neither operation can replace the other because they solve different duplication problems.

**Why grouping includes both user directions.** The self join labels one side `l1` and the other `l2`. Swapping those aliases produces a separate directed group, even though shared-song evidence is symmetric. That is intentional: the output demands both recommendations. Friendship exclusion is also checked directionally against symmetric CTE `T`, so both candidate directions are removed together for existing friends.

**SQL null behavior is harmless here.** Both sources are ordinary `Listens` rows from a cross join, not optional joins, so day, song, and user values participating in successful equality predicates are concrete under the intended table data. The inequality prevents a user from generating recommendations to themselves even if duplicate rows exist.

**Any row order is acceptable.** The query has no `ORDER BY` because the contract permits any order.

## Complexity detail

Let $L$ be the number of listen rows and $F$ the number of friendships. Symmetrizing friendship costs $O(F)$ plus constant-factor duplicate elimination. A broad self-join can consider $O(L^2)$ row pairs before equality filters, matching the manifest's $O(L^2+F)$ time summary.

Intermediate matched rows, grouping, and deduplication may require $O(L^2)$ space in a worst-case broad plan. Actual database cost depends strongly on indexes for `(day, song_id, user_id)` and optimizer join strategies.

Duplicate listen records can multiply join rows substantially even though the distinct aggregate later corrects semantics.

## Alternatives and edge cases

- **Pre-deduplicate listens:** Selecting distinct user, song, and day before the self join can greatly reduce duplicate multiplication while preserving results.
- **Join through friendship first:** That solves the similar-friends problem, not recommendations; here existing friends must be excluded.
- **Count without `DISTINCT`:** Incorrect when `Listens` contains duplicate rows.
- **Three songs across different days:** Separate groups never combine, so the pair does not qualify.
- **Qualifies on several days:** Outer `DISTINCT` returns each direction once.
- **Directional output:** The self join emits both user orders. Returning only smaller-first pairs would violate the contract.
- **Self recommendation:** Explicit user inequality prevents it.
- **No friendship rows:** `T` is empty, so every qualifying distinct-user pair is eligible.
- **Any output order:** Absence of `ORDER BY` is intentional.
- **Exactly two common songs:** The group exists but fails `HAVING`; only three or more distinct song IDs qualify.
- **Same songs but shifted dates:** Equality is row-by-row on `day`, so matching song sets on different dates provide no evidence.
