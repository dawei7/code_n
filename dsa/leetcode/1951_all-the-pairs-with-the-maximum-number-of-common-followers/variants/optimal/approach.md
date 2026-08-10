## General

**Turn each shared follower into evidence for a user pair**

`Relations` stores one row per user-follower relationship. The query joins the table to itself on equal `follower_id`. A joined row means that the same follower follows both `r1.user_id` and `r2.user_id`.

The additional condition `r1.user_id < r2.user_id` has two purposes. It prevents pairing a user with itself, and it chooses one canonical orientation for each unordered pair. Without it, a shared follower would generate both $(x,y)$ and $(y,x)$.

Because `(user_id, follower_id)` is a primary key, a follower contributes at most one joined row to a fixed user pair. Therefore `COUNT(1)` after grouping is exactly the number of distinct common followers; an explicit `COUNT(DISTINCT follower_id)` is unnecessary.

**Count common followers per pair**

The join output is grouped by `r1.user_id, r2.user_id`. Every group represents one user pair that shares at least one follower, and its count is that pair's common-follower total.

For the sample, follower three generates evidence for pairs $(1,2)$, $(1,7)$, and $(2,7)$. Follower four generates the same three. Follower five adds evidence for $(1,7)$ only, making its grouped count the largest.

**Rank grouped counts and keep every maximum**

Within the CTE, `RANK() OVER (ORDER BY COUNT(1) DESC)` orders pair groups from the greatest count to the least. Every pair tied for the greatest count receives rank one. `RANK` rather than `ROW_NUMBER` is essential because the problem asks for all maximum pairs, not an arbitrary single winner.

The outer query selects the two IDs from rank-one rows. The ordering is already canonical from the join predicate. No `ORDER BY` is needed because any output order is accepted.

**SQL evaluation levels**

The grouped `COUNT(1)` is computed per user pair. The window function then ranks those group results, and the outer CTE consumer filters the window value. Keeping the rank filter outside the CTE avoids trying to use a window result in the same query level's WHERE clause, where it is not yet available.

**Why the query is correct**

Every grouped row corresponds to one canonical pair and counts exactly its shared followers. Ranking descending assigns rank one exactly to groups whose count equals the global maximum among generated pairs. Therefore every returned pair has the maximum common-follower count.

Conversely, any pair with a positive maximum common-follower count produces one joined row per such follower, forms a group with that maximum count, receives rank one, and is returned. Ties all share rank one.

The exact query generates only pairs that share at least one follower. If a data model required returning zero-common-follower pairs when no shared follower exists anywhere, it would need a separate universe of users and pair generation. The supplied query and intended task operate on the meaningful positive shared-follower groups produced by `Relations`.

## Complexity detail

Let $R$ be the number of relation rows and $J$ the number of joined shared-follower witness rows.

With an index or hash organization on `follower_id`, reading relations and generating the join is proportional to $R+J$. Grouping and ranking the resulting pair groups may require sorting, summarized by the manifest as $O(R+J\log J)$ time. Hash aggregation can change constants or expected bounds.

Materializing join/group state and window ordering can use $O(J)$ working space. Actual SQL complexity depends on the optimizer, indexes, follower-degree distribution, and whether intermediate results spill to disk. A follower who follows many users can generate quadratically many user pairs, so $J$ may greatly exceed $R$.

## Alternatives and edge cases

- **Dense rank:** `DENSE_RANK` would also assign one to all maximum groups. Differences in later rank gaps do not matter when filtering only rank one.
- **Maximum subquery:** Compute counts in one CTE, compute their maximum in another, and join or filter for equality. It is more verbose but expresses the same logic.
- **Row number:** `ROW_NUMBER` is incorrect because it selects only one row among tied maximum pairs.
- **Missing order predicate:** Without `r1.user_id < r2.user_id`, self-pairs and reversed duplicates appear.
- **One shared follower:** Such a pair forms a group; it wins if no pair has a larger count.
- **Tied maxima:** Every tied group receives `rk = 1` and is returned.
- **Unique maximum:** Exactly one grouped pair receives rank one, so the outer query returns one row.
- **Primary-key guarantee:** It prevents one follower from being counted twice for the same user.
- **Followers as users:** A `follower_id` need not have rows as a followed user; only their role as a shared follower matters.
- **High-degree follower:** One follower following $d$ users generates $d(d-1)/2$ canonical pair witnesses.
- **Any output order:** The outer query deliberately omits ordering.
- **Positive-group scope:** The self-join cannot materialize pairs with zero common followers; a separate user universe would be required for that different interpretation.
- **Why `COUNT(1)` is sufficient:** The relation key makes each joined witness a distinct common follower for that canonical user pair, so counting joined rows equals counting common followers.
