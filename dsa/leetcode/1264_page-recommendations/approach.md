## General

**The recommendation rule has three separate jobs**

A page belongs in the result only if at least one friend of user `1` likes it, user `1` does not already like it, and it appears only once even when several friends like it. The query mirrors these three jobs: construct the friend set, join those friends to their likes, and filter plus deduplicate the resulting pages.

The challenge in the first job is that friendship is undirected in meaning but stored in two directed-looking columns. User `1` may appear as `user1_id` or as `user2_id`. Looking at only one column would silently miss valid friends.

**Constructing a one-column friend relation**

The common table expression named `T` normalizes both orientations:

`SELECT user1_id AS user_id FROM Friendship WHERE user2_id = 1`

selects the opposite endpoint when user `1` is stored on the right. The second branch

`SELECT user2_id AS user_id FROM Friendship WHERE user1_id = 1`

selects the opposite endpoint when user `1` is stored on the left. Both branches name their result `user_id`, so the rest of the query can treat them as one ordinary table of friends without remembering how each friendship row was oriented.

The branches are combined with `UNION` rather than `UNION ALL`. `UNION` removes duplicate friend identifiers. The composite primary key prevents the exact same ordered pair from appearing twice, but the normalized result could still conceptually receive the same person from multiple orientations if both ordered representations were present. Deduplicating here ensures each friend is joined to `Likes` once. Correctness would still be protected later by the outer `DISTINCT`, but the early normalization can avoid redundant join rows.

For the example, rows containing user `1` produce friend identifiers `2`, `3`, `4`, and `6`. Friendship rows such as `(2, 3)` do not involve user `1` and appear in neither branch.

**Finding pages liked by those friends**

The main query joins `T` with `Likes` using `JOIN Likes USING (user_id)`. The `USING` clause means that the equally named `user_id` columns must match. Consequently, every joined row represents a page liked by a known friend of user `1`.

This is an inner join, which is appropriate. A friend with no like rows contributes no recommendable page and need not appear in an intermediate result. Likewise, likes from users outside `T` cannot join and are ignored.

After the join, the query needs only `page_id`. It aliases that column as `recommended_page` to satisfy the required output schema.

**Excluding pages user one already likes**

The subquery `SELECT page_id FROM Likes WHERE user_id = 1` produces user `1`'s existing likes. The condition

`page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)`

removes any candidate whose page identifier is in that set. It does not matter whether one friend or many friends like an already-liked page; all joined rows for that page fail the condition.

In the sample, friend `6` likes page `88`, but user `1` also likes page `88`, so it is excluded. Page `77` is liked by both users `2` and `3` and passes the exclusion because user `1` does not like it.

SQL's `NOT IN` requires care when its subquery can return `NULL`, because three-valued logic can make every comparison unknown. Here `page_id` participates in the `Likes` primary key, so the schema guarantees a non-null identifier. The usual `NULL` trap does not apply under this contract.

**Removing duplicate recommendations**

The main projection uses `SELECT DISTINCT page_id AS recommended_page`. Joining likes can produce several rows for one page when several friends like it. A recommendation is a page, not a friend-page event, so those rows must collapse into one output. `DISTINCT` performs that final set conversion.

Every returned page is correct: it came from a `Likes` row joined to a friend in `T`, passed the test that user `1` does not like it, and is emitted once. Conversely, take any page that should be recommended. At least one friendship row places its liking user in one branch of `T`, the friend's like row survives the join, and absence from user `1`'s likes makes the `NOT IN` condition true. The page therefore reaches the projection. This proves both soundness and completeness.

The query has no `ORDER BY` because the problem explicitly permits any result order. Adding an order would do unnecessary work and impose a promise the interface does not request.

## Complexity detail

Let $F$ be the number of `Friendship` rows, $L$ the number of `Likes` rows, and $R=F+L$. In the standard relational-algorithm model, the two filtered friendship scans take $O(F)$ without relying on indexes. Building the normalized friend set and joining it with likes can be performed with hashing in expected $O(F+L)$ time. The anti-membership set for user `1`'s likes and final duplicate elimination can likewise be implemented in expected linear time in their input sizes. This yields expected $O(R)$ time, plus the unavoidable cost of writing the result.

Actual SQL execution is chosen by the MySQL optimizer. Appropriate indexes on primary-key columns may avoid full scans, while sorting-based implementations of `UNION` or `DISTINCT` can introduce $O(R\log R)$ work in a pessimistic plan. The manifest's $O(R)$ bound describes an efficient hash/index execution rather than a guaranteed physical plan for every database configuration.

Intermediate friend identifiers, joined candidate rows, the anti-set, and duplicate-elimination state can occupy $O(R)$ space in the worst case. The database may spill those structures to disk, but their logical size remains linear. The returned distinct pages additionally require space proportional to the output, which is also at most $O(R)$.

## Alternatives and edge cases

- **Correlated `EXISTS` and `NOT EXISTS`:** Existence predicates can express “some friend likes this page” and “user one does not.” They avoid the `NULL` semantics of `NOT IN` and may optimize well, but the current schema already makes `page_id` non-null.
- **`LEFT JOIN` anti-join:** Candidate pages can be left-joined to user `1`'s likes and filtered with `IS NULL`. This is a common equivalent anti-join formulation but requires careful aliases because `Likes` appears twice.
- **`UNION ALL` instead of `UNION`:** It could preserve duplicate friend rows and rely on final `DISTINCT` for correct output. That may create unnecessary join work and makes the normalized friend relation less clean.
- **Friend stored in either column:** The two CTE branches are both necessary; omitting either one misses friendships in the opposite orientation.
- **Several friends like one page:** `DISTINCT` returns that page exactly once.
- **Friend likes a page user one likes:** The `NOT IN` filter removes it regardless of how many friends like it.
- **Friend with no likes:** The inner join produces no row for that friend, which is correct.
- **User one has no friends:** `T` is empty, so the join and result are empty.
- **User one has no likes:** The anti-subquery is empty, so every distinct page liked by a friend is eligible.
- **No ordering requirement:** Without `ORDER BY`, MySQL may return valid recommendations in any physical order.
- **Primary-key nullability:** The safety of `NOT IN` depends on `page_id` being non-null, which follows from its participation in the declared primary key.
