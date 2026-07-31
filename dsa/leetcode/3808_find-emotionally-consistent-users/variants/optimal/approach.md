## General

Build one grouped relation keyed by (`user_id`, `reaction`). Each row in it gives the count of one reaction type for one user. Build a second grouped relation keyed only by `user_id`; it gives that user's total number of reactions and discards users with fewer than five distinct `content_id` values.

Join the two relations on `user_id`. For a joined reaction-type row, the consistency condition is

$$
5C_{u,t} \ge 3R_u.
$$

This integer comparison is exactly equivalent to $C_{u,t}/R_u \ge 0.60$, but it cannot drift below the boundary through floating-point approximation. It is also sufficient to identify the dominant type: two different types cannot each occupy at least 60% of the same user's rows because their combined share would exceed 100%.

Every emitted row therefore belongs to a user with at least five content reactions and names the unique type meeting the required share. Conversely, each emotionally consistent user has exactly such a grouped type row, so the join and threshold test retain it. Compute the displayed ratio from the retained counts, round it to two decimal places, and apply the two required sort keys.

## Complexity detail

Let $R$ be the number of rows in `reactions` and $U$ the number of distinct users. Under a general sort-based plan, the grouped passes cost $O(R\log R)$ time and ordering the qualifying users costs $O(U\log U)$, for $O(R\log R+U\log U)$ total time. The grouped relations and sort can use $O(R+U)$ working space. A database may choose hash aggregation or exploit indexes, but correctness does not depend on either optimization.

The benchmark defines size as $R$ and gives every user five reaction rows. The accepted query performs two whole-table grouped passes; the slower control uses correlated counts that repeatedly rescan the same table for user/type combinations.

## Alternatives and edge cases

- **Window functions:** Per-user and per-type window counts can express the same logic, but the intermediate result still contains one row per original reaction and needs deduplication before output.
- **Correlated counts:** Counting totals and type frequencies separately for every candidate row is correct, but repeated table scans can grow quadratically.
- **Rank the most frequent type:** Ranking reaction counts within each user also works, but the 60% threshold already guarantees that at most one type can pass, so ranking is unnecessary.
- **Exactly five content items:** Five is inclusive; a user with exactly five rows remains eligible for the ratio test.
- **Exactly 60%:** A split such as three matching reactions out of five qualifies. Compare unrounded integer counts so the boundary is exact.
- **No qualifying type:** A user may have enough content items yet be absent because every reaction type remains below 60%.
- **Rounded ordering ties:** `reaction_ratio` is the returned rounded value. Equal ratios use ascending `user_id` as the secondary key.
