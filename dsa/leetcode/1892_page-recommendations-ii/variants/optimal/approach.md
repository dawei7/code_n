## General

**Treat friendship as bidirectional.** Each stored row names two friends, but either user may need recommendations based on the other. CTE `S` creates a directed view of the relationship. The first query keeps `user1_id -> user2_id`, and the second reverses every row to `user2_id -> user1_id`. `UNION` removes duplicate directed pairs if the input happens to represent the same friendship in both directions. Afterward, `S.user1_id` is consistently the recommendation recipient and `S.user2_id` is one of that user's friends.

**Expand each friend into pages they like.** `S AS s LEFT JOIN Likes AS l ON s.user2_id = l.user_id` associates a directed user-friend pair with every liked page belonging to that friend. For an ordinary matched row, `l.page_id` is a candidate page for `s.user1_id`. If several friends like the same page, the join produces one row for each friend-page match, which is exactly the multiplicity needed for `friends_likes`.

**Remove pages already liked by the recipient.** The correlated `NOT EXISTS` subquery searches `Likes AS l2` for a row where `l2.user_id` equals the recipient and `l2.page_id` equals the candidate page. If such a row exists, the candidate is excluded. If none exists, the candidate has not been liked by the recipient and remains recommendable. Using `NOT EXISTS` avoids adding recipient-like columns to the outer grouping.

The references `user1_id = l2.user_id` and `l.page_id = l2.page_id` reach the outer query. Qualifying `user1_id` as `s.user1_id` would be clearer, but only `S` supplies that name in this scope, so the intended correlation is unambiguous in the exact query.

**Group identical recommendations and count supporting friends.** `GROUP BY user1_id, page_id` collapses all candidate rows for one recipient-page combination. `COUNT(1)` counts the rows in that group. Because `S` contains unique directed friendships and the `Likes` primary key contains at most one row for a user-page pair, one friend contributes at most one row to a particular page group. The count is therefore the number of distinct friends who like that page, without requiring `COUNT(DISTINCT ...)`.

**Trace user one from the example.** Directed view `S` includes friends two, three, four, and six for user one, including the reverse of stored row `(6, 1)`. Joining their likes produces pages 23 and 77 from user two, 24 and 77 from user three, 56 from user four, and 33 and 88 from user six. The anti-membership test removes page 88 because user one already likes it. Grouping counts two rows for page 77 and one for each other page.

**Why the relational stages match the intended algorithm.** Symmetrization enumerates every recipient-friend relationship exactly once. Joining to likes enumerates every friend endorsement. The anti-query removes exactly recipient-owned pages. Grouping then produces one recommendation row and counts its endorsements. Under the condition that candidate page IDs are non-null, these stages prove that every returned page is liked by at least one friend and not by the recipient, while every such page is returned.

**A material exact-query caveat.** The source uses `LEFT JOIN` rather than an inner `JOIN`. If a friend has no rows in `Likes`, the left join preserves a row with `l.page_id = NULL`. The correlated equality against `NULL` never finds a match, so `NOT EXISTS` is true; grouping can then emit a row whose `page_id` is `NULL`, and `COUNT(1)` counts it. A null page is not a valid recommendation. The general table description does not guarantee every friend likes at least one page, so the exact query is fully correct only under that additional data condition. Replacing `LEFT JOIN` with `JOIN`, or adding `l.page_id IS NOT NULL`, fixes the general case. This approach documents rather than conceals that executed behavior.

**Any result order is allowed.** There is no `ORDER BY` because the contract accepts any order. Group output order is an implementation detail and should not be relied upon.

## Complexity detail

Let $F$ be the number of friendship rows, $L$ the number of likes, and $C$ the number of friend-like candidate rows created by the join. Building the symmetric relation processes $O(F)$ rows and `UNION` may sort or hash up to $2F$ rows. With useful indexes or hashes, the joins and anti-lookups process the relations plus candidates, while grouping $C$ rows can cost $O(C)$ expected with hashing or $O(C\log C)$ with sorting.

The manifest's $O((F+L+C)\log C)$ time is a conservative plan-independent summary of deduplication, matching, and grouping work. Exact database cost depends on indexes, cardinalities, and optimizer choices. The intermediate symmetric relation, joined candidates, grouping state, and inputs lead to the stated $O(F+L+C)$ scale of working storage, with possible disk spill.

The output size is at most the number of distinct recipient-page groups and can itself be large. Primary-key indexes on `Likes(user_id, page_id)` directly support the correlated ownership test.

## Alternatives and edge cases

- **Inner join to `Likes`:** This is the appropriate general solution because a friend with no likes contributes no candidate. It prevents the exact source's possible null-page recommendation.
- **Add `l.page_id IS NOT NULL`:** Keeping the left join but filtering null candidate pages also restores correctness, though an inner join communicates the requirement more directly.
- **`UNION ALL` instead of `UNION`:** It is faster only if the input guarantees each undirected friendship is stored exactly once and never in both directions. Otherwise duplicate directed relationships inflate `friends_likes`.
- **Self anti-join:** Left join recipient likes on user and page, then require the recipient match to be null. This is equivalent to `NOT EXISTS` when written carefully.
- **Several friends like one page:** Grouping produces one recommendation and `COUNT(1)` reports every supporting friend.
- **Recipient already likes the page:** The correlated subquery finds the primary-key row and excludes the entire candidate before grouping.
- **Friend with no liked pages:** Under the exact `LEFT JOIN` this can create a null group, which is a correctness defect under the unrestricted schema; inner joining avoids it.
- **User with no friends:** The user has no row in `S` and therefore no recommendations, as intended.
- **No explicit ordering:** Any output order is valid. Adding `ORDER BY` would affect presentation and cost, not recommendation membership.
