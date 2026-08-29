## General

**Begin with actual friendship pairs.** The output must preserve `user1_id < user2_id` exactly as stored. The query starts from `Friendship AS f`, so every candidate is already a real friend pair in canonical order. Unlike recommendation queries, no reversed copy is needed.

**Attach listen histories for both endpoints.** The first join connects `user1_id` to `l1.user_id`; the second connects `user2_id` to `l2.user_id`. Conceptually this forms combinations of listen rows for the two friends. The `WHERE` clause retains combinations with the same `song_id` and the same `day`, which represent one song both users heard on one date.

Although both joins are written `LEFT JOIN`, the equality predicates in `WHERE` reject rows where either listen side is null. They therefore behave like inner joins for result membership. Writing explicit inner joins would communicate this more directly.

**Keep days separate during aggregation.** `GROUP BY 1, 2, l1.day` groups by the selected friendship columns and shared listen day. A pair must share three songs on one same day; songs heard together across different dates cannot be combined. Positional keys one and two refer to `user1_id` and `user2_id`.

**Count distinct songs, not listen rows.** `Listens` may contain duplicates. Joining duplicate rows from both users can multiply one common song many times. `COUNT(DISTINCT l1.song_id)` collapses those copies and measures the number of different shared songs. `HAVING ... >= 3` retains only qualifying pair-day groups.

**Deduplicate pairs that qualify on several days.** Grouping by day may produce several rows for one friendship. The requested result lists a pair once, so outer `SELECT DISTINCT user1_id, user2_id` removes repeated qualifying days while retaining original smaller-first ordering.

**Trace the example.** Friendship `(1,2)` has matching rows for songs 10, 11, and 12 on March 15, so its group reaches three and survives. Pair `(2,4)` shares only songs 10 and 11 that day, so it fails. Pair `(2,5)` heard similar songs on different dates; equal-day predicates prevent them from entering one group.

**Why nonfriends cannot appear.** Every result originates from one `Friendship` row. Listen joins can only decorate that row; they cannot invent another pair. This is the central difference from the preceding recommendations problem, which begins from all user pairs sharing listens and removes friendships.

**Why every similar friendship appears.** If stored friends share at least three distinct songs on one day, their listen rows match through both equality predicates. The group for that friendship and day contains those distinct song IDs, satisfies `HAVING`, and produces the stored pair. `DISTINCT` never removes the only copy; it only merges duplicate days.

**Understand duplicate multiplication.** If user one has two identical rows for a song and user two has three, the two listen joins can produce six matched combinations for that one song. The distinct aggregate collapses all six to one song ID before applying the threshold. This is why counting rows, even after grouping by day, would be semantically wrong.

**Why canonical pair orientation is preserved automatically.** The query never swaps friendship endpoints. `l1` is always attached to stored `user1_id` and `l2` to stored `user2_id`. Since the table guarantees the first is smaller, every selected row already meets the required orientation, including after `DISTINCT` combines multiple days.

**Day-specific qualification precedes pair-level deduplication.** A friendship sharing two songs on Monday and two different songs on Tuesday must fail: neither day group reaches three. Deduplicating the pair before the `HAVING` stage would incorrectly allow evidence from different days to mix.

**Output order is unrestricted.** No `ORDER BY` is needed. Canonical user ordering refers to columns within each row, not ordering among rows.

## Complexity detail

Let $L$ be listen-row count and $F$ friendship count. A broad plan may create up to quadratic combinations of listen rows while matching friend endpoints, giving the manifest's $O(L^2+F)$ time summary. Suitable indexes on user, day, and song can reduce actual matching substantially.

Intermediate joined rows and grouped state can grow toward $O(L^2)$ in a broad worst-case plan, especially because duplicate listens multiply before the distinct aggregate. The manifest reports this bound. Physical memory and disk spill depend on the SQL optimizer.

Starting from friendships can also be viewed as processing listen combinations only for $F$ known pairs, so data distribution materially affects real cost.

## Alternatives and edge cases

- **Pre-deduplicate `Listens`:** A distinct user/song/day CTE prevents duplicate join multiplication and preserves semantics.
- **Use explicit inner joins:** Produces the same qualifying rows and makes the effective null-rejecting behavior clearer.
- **Start from all listener pairs:** Then friendship must be joined afterward; beginning with `Friendship` naturally preserves canonical pair order.
- **Duplicate listen records:** `COUNT(DISTINCT song_id)` ensures one song counts once.
- **Three songs on different days:** Grouping by day keeps them separate and rejects the pair.
- **Qualifies on multiple days:** Final `DISTINCT` returns one friendship row.
- **Nonfriends with matching songs:** They never enter because `Friendship` is the driving table.
- **Already canonical ordering:** The query returns stored columns and never reverses them.
- **Any output order:** Absence of `ORDER BY` is valid.
- **Exactly three distinct matches:** The inclusive `>= 3` threshold accepts the pair.
- **Friend with no listen rows:** Null-extended join rows fail equality predicates, so the pair produces no qualifying group.
